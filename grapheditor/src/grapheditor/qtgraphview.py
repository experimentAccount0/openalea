# -*- python -*-
#
#       OpenAlea.Visualea: OpenAlea graphical user interface
#
#       Copyright 2006-2009 INRIA - CIRAD - INRA
#
#       File author(s): Daniel Barbeau <daniel.barbeau@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################
"""Generic Graph Widget"""

__license__ = "Cecill-C"
__revision__ = " $Id$ "

from weakref    import ref as WEAKREFRef
from types      import MethodType as TYPESMethodType
from gc         import collect as GCcollect
from exceptions import DeprecationWarning as EXDeprecationWarning
from warnings   import warn as WAWarn
from PyQt4 import QtGui, QtCore
from openalea.core.settings import Settings

import baselisteners, interfaces
import edgefactory

from math import sqrt

#__Application_Integration_Keys__
__AIK__ = [
    "mouseMoveEvent",
    "mouseReleaseEvent",
    "mousePressEvent",
    "mouseDoubleClickEvent",
    "keyReleaseEvent",
    "keyPressEvent",
    "contextMenuEvent"
    ]

__AIK_GDict__ = dict(zip(__AIK__,[None]*len(__AIK__)))


class ClientCustomisableWidget(object):
    ####################################
    # ----Class members come first---- #
    ####################################

    @classmethod
    def set_event_handler(cls, key, handler, graphType):
        """Let handler take care of the event named by key.

        :Parameters:
            - key (str) - The name of the event.
            - handler (callable) - The handler to register with key.


         The key can be any of
           * \"mouseMoveEvent\"
           * \"mouseReleaseEvent\"
           * \"mousePressEvent\"
           * \"mouseDoubleClickEvent\"
           * \"keyReleaseEvent\"
           * \"keyPressEvent\"
           * \"contextMenuEvent\"

        See the Qt documentation of those to know the expected signature
        of the handler (usually : handlerName(QObject, event)).

        """
        if cls in [Vertex, Edge] :
            raise Exception(str(cls)+".set_event_handler.\n" + \
                                     "Don't use this on classes from qtgraphview " + \
                                     "except qtgraphview.View")
            return

        if not hasattr(cls, "__application_integration__"):
            cls.__application_integration__ = {}
            cls.__originals__ = {}
        if key in cls.__application_integration__.setdefault(graphType, __AIK_GDict__.copy()):
            cls.__application_integration__[graphType][key]=handler
            try : cls.__originals__[key] = getattr(cls, key)
            except : pass

    @classmethod
    def static_init_handlers(cls, graphType):
        """we bind application overloads if they exist
        once and for all. As this happens after the
        class is constructed, it overrides any method
        called "name" with an application-specific method
        to handle events."""
        if (not hasattr(cls, "__application_integration__") or not
            graphType in cls.__application_integration__): return
        for name, hand in cls.__application_integration__[graphType].iteritems():
            if "Event" in name and hand:
                setattr(cls, name, TYPESMethodType(hand, None, cls))

    @classmethod
    def reset_event_handlers(cls):
        if hasattr(cls, "__originals__"):
            for name, hand in cls.__originals__.iteritems():
                setattr(cls, name, TYPESMethodType(hand, None, cls))

#------*************************************************------#
class Element(baselisteners.GraphElementListenerBase, ClientCustomisableWidget):
    """Base class for elements in a qtgraphview.View.

    Implements basic listeners calls for elements of a graph.
    A listener call is the method that is called after the main
    listening method (self.notify) dispatches the events. They
    are specified by interfaces.IGraphViewElement.

    The class also implements a mecanism to easily override user
    events from the client application. What does this mean? In this
    framework, the graph editor starts as a simple graph listener. The
    current module extends those listeners to be able to react to the
    events and produce a QGraphicsView of the graph with graph-specific
    interactions. The dataflowview module extends the current module
    to handle dataflows. However these extensions are not client-specific.
    There is nothing related for example specifically to Visualea.
    by using Vertex.set_event_handler(key, handler), or even on
    specialised elements like
    dataflowview.vertex.GraphicalVertex.set_event_handler(key, handler),
    one can bind a specific behaviour to the event named by \"key\". The
    handler will be specific to the class set_event_handler was called on
    (hopefully).

    :Listener calls:
        * position_changed(self,  (posx, posy))
        * add_to_view(self, view)
        * remove_from_view(self, view)

    """

    ####################################
    # ----Instance members follow----  #
    ####################################
    def __init__(self, observed=None, graph=None):
        """
        :Parameters:
             - observed (openalea.core.observer.Observed) - The item to
             observe.
             - graph (ducktype) - The graph owning the item.

        """
        baselisteners.GraphElementListenerBase.__init__(self,
                                                        observed,
                                                        graph)

    #################################
    # IGraphViewElement realisation #
    #################################
    def get_view(self):
        return self.scene()

    def add_to_view(self, view):
        """An element adds itself to the given view"""
        view.addItem(self)

    def remove_from_view(self, view):
        """An element removes itself from the given view"""
        view.removeItem(self)

    def position_changed(self, *args):
        """Updates the item's **graphical** position from
        model notifications. """
        point = QtCore.QPointF(args[0], args[1])
        self.setPos(point)

    def lock_position(self, val=True):
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, not val)


#------*************************************************------#
def defaultPaint(owner, painter, paintOptions, widget):
    rect = owner.rect()
    painter.drawEllipse(rect)

class Vertex(Element):
    """An abstract graphic item that represents a graph vertex.

    The actual implementation is done in the derived class. What this
    intermediate implementation does is that it provides the basics
    for handling edge creation from one node to the other.
    It also provides a state based pluggable painting system,
    meant to customize the painting from the application side.
    Of course, if it doesn't match your needs you
    can override it completely in your subclass."""

    ####################################
    # ----Instance members follow----  #
    ####################################
    def __init__(self, vertex, graph):
        """
        :Parameters:
            - vertex - the vertex to observe.
            - graph - the owner of the vertex

        """
        Element.__init__(self, vertex, graph)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.__paintStrategy = defaultPaint

    vertex = baselisteners.GraphElementListenerBase.get_observed

    def get_scene_center(self):
        """retrieve the center of the widget on the scene"""
        center = self.rect().center()
        center = self.mapToScene(center)
        return [center.x(), center.y()]

    def set_highlighted(self, value):
        pass

    def set_painting_strategy(self, strat):
        self.__paintStrategy = strat

    #####################
    # ----Qt World----  #
    #####################
    def itemChange(self, change, value):
        if change == QtGui.QGraphicsItem.ItemPositionChange:
            self.deaf(True)
            point = value.toPointF()
            cPos = point + self.boundingRect().center()
            self.store_view_data('position', [point.x(), point.y()])
            self.deaf(False)
            return value

    def paint(self, painter, option, widget):
        """Qt-specific call to paint things."""
        if self.__paintStrategy is None:
            self.__paintStrategy = defaultPaint
        self.__paintStrategy(self, painter, option, widget)


    def mousePressEvent(self, event):
        """Qt-specific call to handle mouse clicks on the vertex.
        Default implementation initiates the creation of an edge from
        the vertex."""
        scene = self.scene()
        if (scene and event.buttons() & QtCore.Qt.LeftButton and
            event.modifiers() & QtCore.Qt.ControlModifier):
            pos = [event.scenePos().x(), event.scenePos().y()]
            scene.new_edge_start(pos, source=self)
            return


#------*************************************************------#
class Edge(Element):
    """Base class for Qt based edges."""

    def __init__(self, edge=None, graph=None, src=None, dest=None):
        Element.__init__(self, edge, graph)

        self.setFlag(QtGui.QGraphicsItem.GraphicsItemFlag(
            QtGui.QGraphicsItem.ItemIsSelectable))

        self.srcBBox = baselisteners.ObservedBlackBox(self, src)
        self.dstBBox = baselisteners.ObservedBlackBox(self, dest)

        self.sourcePoint = QtCore.QPointF()
        self.destPoint = QtCore.QPointF()

        self.__edge_path = None
        self.set_edge_path(edgefactory.EdgeFactory())
        self.setPen(QtGui.QPen(QtCore.Qt.black, 3,
                               QtCore.Qt.SolidLine,
                               QtCore.Qt.RoundCap,
                               QtCore.Qt.RoundJoin))

    edge = baselisteners.GraphElementListenerBase.get_observed

    def change_observed(self, old, new):
        if old == self.srcBBox():
            self.set_observed_source(new)
        elif old == self.dstBBox():
            self.set_observed_destination(new)
        else:
            Element.change_observed(self, old, new)
        return

    def set_observed_source(self, src):
        """todo evaluate this for inclusion into the interfaces"""
        self.srcBBox.clear_observed()
        self.srcBBox(src)

    def set_observed_destination(self, dest):
        """todo evaluate this for inclusion into the interfaces"""
        self.dstBBox.clear_observed()
        self.dstBBox(dest)

    def clear_observed(self, *args):
        self.srcBBox.clear_observed()
        self.dstBBox.clear_observed()
        Element.clear_observed(self, *args)

    def set_edge_path(self, path):
        self.__edge_path = path
        path = self.__edge_path.get_path(self.sourcePoint, self.destPoint)
        self.setPath(path)

    def update_line_source(self, *pos):
        self.sourcePoint = QtCore.QPointF(*pos)
        self.__update_line()

    def update_line_destination(self, *pos):
        self.destPoint = QtCore.QPointF(*pos)
        self.__update_line()

    def __update_line(self):
        path = self.__edge_path.get_path(self.sourcePoint, self.destPoint)
        self.setPath(path)

    def notify(self, sender, event):
        if(event[0] == "metadata_changed"):
            if(event[1]=="connectorPosition"):
                pos = event[2]
                if(sender==self.srcBBox()):
                    self.update_line_source(*pos)
                elif(sender==self.dstBBox()):
                    self.update_line_destination(*pos)
            elif(event[1]=="hide" and (sender==self.dstBBox() or sender==self.srcBBox())):
                if event[2]:
                    self.setVisible(False)
                else:
                    self.setVisible(True)

    def remove(self):
        self.graph().remove_edge(self.srcBBox(), self.dstBBox())


    ############
    # Qt World #
    ############
    def shape(self):
        path = self.__edge_path.shape()
        if not path:
            return QtGui.QGraphicsPathItem.shape(self)
        else:
            return path

    def itemChange(self, change, value):
        """ Callback when item has been modified (move...) """

        if (change == QtGui.QGraphicsItem.ItemSelectedChange):
            if(value.toBool()):
                color = QtCore.Qt.blue
            else:
                color = QtCore.Qt.black

            self.setPen(QtGui.QPen(color, 3,
                                   QtCore.Qt.SolidLine,
                                   QtCore.Qt.RoundCap,
                                   QtCore.Qt.RoundJoin))

        return QtGui.QGraphicsItem.itemChange(self, change, value)



class FloatingEdge( Edge ):

    def __init__(self, srcPoint, graph):
        Edge.__init__(self, None, graph, None, None)
        self.sourcePoint = QtCore.QPointF(*srcPoint)
        self.destPoint = QtCore.QPointF(self.sourcePoint)

    def notify(self, sender, event):
        return

    def consolidate(self, graph):
        try:
            srcVertex, dstVertex = self.get_connections()
            if(srcVertex == None or dstVertex == None):
                return
            graph.add_edge(srcVertex, dstVertex)
        except Exception, e:
            # pass
            print "consolidation failed :", type(e), e,\
            ". Are you sure you plugged the right ports?"
        return

    def get_connections(self):
        #find the vertex items that were activated

        srcVertexItem = self.scene().find_closest_connectable(self.sourcePoint, boxsize = 2)
        dstVertexItem = self.scene().find_closest_connectable(self.destPoint, boxsize = 2)

        scene = self.scene()

        if( type(srcVertexItem) not in scene.connector_types or
            type(dstVertexItem) not in scene.connector_types):
            raise Exception( "Non connectable types for : " + str(srcVertexItem) + " : " + \
                                str(dstVertexItem) )
            return None, None

        #if the input and the output are on the same vertex...
        if(srcVertexItem == dstVertexItem):
            raise Exception("Nonsense connection : plugging self to self.")

        return srcVertexItem.vertex(), dstVertexItem.vertex()


#------*************************************************------#
class Scene(QtGui.QGraphicsScene, baselisteners.GraphListenerBase):
    """A Qt implementation of GraphListenerBase"""
    def __init__(self, parent, graph):
        QtGui.QGraphicsScene.__init__(self, parent)
        baselisteners.GraphListenerBase.__init__(self, graph)
        self.__selectAdditions  = False #select newly added items
        self.__views = set()
        self.initialise_from_model()

    #############################################################################
    # Functions to correctly cooperate with the View class (reference counting) #
    #############################################################################
    def register_view(self,  view):
        self.__views.add(WEAKREFRef(view))

    def unregister_view(self,  view):
        toDiscard = None
        for v in self.__views:
            if v() == view : toDiscard = v; break
        self.__views.remove(toDiscard)
        try: self.graph().unregister_listener(view)
        except : pass
        if len(self.__views)==0:
            self.clear()


    #################################
    # IGraphListener implementation #
    #################################
    def get_scene(self):
        return self

    def find_closest_connectable(self, pos, boxsize = 10.0):
        #creation of a square to find connectables inside.
        if isinstance(pos, QtCore.QPointF) : pos = pos.x(), pos.y()
        rect = QtCore.QRectF((pos[0] - boxsize/2), (pos[1] - boxsize/2), boxsize, boxsize);
        dstPortItems = self.items(rect)
        dstPortItems = [item for item in dstPortItems if self.is_connectable(item)]

        distance = float('inf')
        dstPortItem = None
        for item in dstPortItems:
            d = sqrt((item.boundingRect().center().x() - pos[0])**2 +
                        (item.boundingRect().center().y() - pos[1])**2)
            if d < distance:
                distance = d
                dstPortItem = item
        return dstPortItem

    def post_addition(self, element):
        """defining virtual bases makes the program start
        but crash during execution if the method is not implemented, where
        the interface checking system could prevent the application from
        starting, with a die-early behaviour."""
        element.setSelected(self.__selectAdditions)

    def rebuild(self):
        """ Build the scene with graphic vertex and edge"""
        self.clear()
        self.initialise_from_model()

    def clear(self):
        """ Remove all items from the scene """
        QtGui.QGraphicsScene.clear(self)
        baselisteners.GraphListenerBase.clear(self)
        GCcollect()

    ##################
    # QtWorld-Events #
    ##################
    def mouseMoveEvent(self, event):
        if(self.is_creating_edge()):
            pos = event.scenePos()
            pos = [pos.x(), pos.y()]
            self.new_edge_set_destination(*pos)
        QtGui.QGraphicsScene.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if(self.is_creating_edge()):
            self.new_edge_end()
        QtGui.QGraphicsScene.mouseReleaseEvent(self, event)

    #########################
    # Other utility methods #
    #########################
    def select_added_elements(self, val):
        WAWarn(EXDeprecationWarning(
                      "Please use self.%s instead"%("select_added_items",)),
                      stacklevel=2)
        self.select_added_items(val)

    def select_added_items(self, val):
        self.__selectAdditions=val

    def get_items(self, filterType=None, subcall=None):
        """ """
        if filterType and not isinstance(filterType, list):
            filterType = [filterType]
        return [ (item if subcall is None else subcall(item))
                 for item in self.items() if
                 (True if filterType is None else (type(item) in filterType))]

    def get_selected_items(self, filterType=None, subcall=None):
        """ """
        if filterType and not isinstance(filterType, list):
            filterType = [filterType]
        return [ (item if subcall is None else subcall(item))
                 for item in self.items() if item.isSelected() and
                 (True if filterType is None else (type(item) in filterType))]

    def get_selection_center(self, selection=None):
        """ """
        items = None
        if selection: items = selection
        else: items = self.get_selected_items()

        l = len(items)
        if(l == 0) : return QtCore.QPointF(30,30)

        sx = sum((i.pos().x() for i in items))
        sy = sum((i.pos().y() for i in items))
        return QtCore.QPointF( float(sx)/l, float(sy)/l )



#------*************************************************------#
def deprecate(methodName, newName=None):
    """create deprecation wrappers"""
    if newName is None : newName = methodName
    def deprecation_wrapper(self, *args, **kwargs):
        WAWarn(EXDeprecationWarning(
                            "Please use self.scene().%s instead"%(newName,)),
                      stacklevel=2)
        return getattr(self.scene(), newName)(*args, **kwargs)
    return deprecation_wrapper


class View(QtGui.QGraphicsView, ClientCustomisableWidget):
    """A View implementing client customisation """

    ####################################
    # ----Class members come first---- #
    ####################################
    __application_integration__= dict( zip(__AIK__,[None]*len(__AIK__)) )
    __application_integration__.update({"mimeHandlers":{}, "pressHKMap":{}, "releaseHKMap":{}})
    __defaultDropHandler = None

    @classmethod
    def set_mime_handler_map(cls, mapping):
        cls.__application_integration__["mimeHandlers"].update(mapping)

    @classmethod
    def set_keypress_handler_map(cls, mapping):
        cls.__application_integration__["pressHKMap"] = mapping

    @classmethod
    def set_keyrelease_handler_map(cls, mapping):
        cls.__application_integration__["releaseHKMap"] = mapping

    @classmethod
    def set_default_drop_handler(cls, handler):
        cls.__defaultDropHandler = handler

    #A few signals that strangely enough don't exist in QWidget
    closing = QtCore.pyqtSignal(baselisteners.GraphListenerBase, QtGui.QGraphicsScene)

    ####################################
    # ----Instance members follow----  #
    ####################################
    def __init__(self, parent, graph=None, clone=False):
        QtGui.QGraphicsView.__init__(self, parent)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        if graph is not None:
            #if the graph has already a qtgraphview.Scene GraphListener
            #reuse it:
            existingScene = None
            for listener in graph.listeners:
                if isinstance(listener(), Scene):
                    existingScene = listener()
                    break
            self.setScene(existingScene if (existingScene and not clone) else Scene(None, graph))

        # ---Qt Stuff---
        self.setCacheMode(QtGui.QGraphicsView.CacheBackground)
        self.setRenderHint(QtGui.QPainter.Antialiasing)
        self.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtGui.QGraphicsView.AnchorViewCenter)
        self.setDragMode(QtGui.QGraphicsView.RubberBandDrag)

    def setScene(self, scene):
        """ Overload of QGraphicsView.setScene to correctly handle multiple views
        of the same scene using reference counting. """
        self.__scene = scene
        if scene is not None:
            scene.register_view(self)
            self.closing.connect(scene.unregister_view)
        QtGui.QGraphicsView.setScene(self, scene)

    ##################
    # QtWorld-Events #
    ##################
    def reset_item_event_handlers(self):
        items = self.scene().get_items(Element)
        for i in items:
            i.reset_event_handlers()

    def wheelEvent(self, event):
        delta = -event.delta() / 2400.0 + 1.0
        self.scale_view(delta)

    # ----drag and drop----
    def accept_drop(self, event):
        """ Return the format of the object if a handler is registered for it.
        If not, if there is a default handler, returns True, else returns False.
        """
        for format in self.__application_integration__["mimeHandlers"].keys():
            if event.mimeData().hasFormat(format): return format
        return True if self.__defaultDropHandler else False

    def dragEnterEvent(self, event):
        """While the user hasn't released the object, this method is called
        to tell qt if the view accepts the object or not."""
        event.setAccepted(True if self.accept_drop(event) else False)

    def dragMoveEvent(self, event):
        format = self.accept_drop(event)
        if (format):
            event.setDropAction(QtCore.Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        format = self.accept_drop(event)
        handler = self.__application_integration__["mimeHandlers"].get(format)
        if(handler):
            handler(self, event)
        else:
            self.__defaultDropHandler(event)
        QtGui.QGraphicsView.dropEvent(self, event)

    # ----hotkeys----
    def keyPressEvent(self, event):
        combo = event.modifiers().__int__(), event.key()
        action = self.__application_integration__["pressHKMap"].get(combo)
        if(action):
            action(self, event)
        else:
            QtGui.QGraphicsView.keyPressEvent(self, event)

    def keyReleaseEvent(self, event):
        combo = event.modifiers().__int__(), event.key()
        action = self.__application_integration__["releaseHKMap"].get(combo)
        if(action):
            action(self, event)
        else:
            QtGui.QGraphicsView.keyReleaseEvent(self, event)

    # ----low level----
    def closeEvent(self, evt):
        """a big hack to cleanly remove items from the view
        and delete the python objects so that they stop leaking
        on some operating systems"""
        self.closing.emit(self, self.scene())
        self.setScene(None)
        return QtGui.QGraphicsView.closeEvent(self, evt)

    #########################
    # Other utility methods #
    #########################
    def scale_view(self, factor):
        self.scale(factor, factor)

    def show_entire_scene (self) :
        """Scale the scene and center it
        in order to display the entire content
        without scrolling.
        """
        sc_rect = self.scene().itemsBoundingRect()

        sc_center = sc_rect.center()
        if sc_rect.width() > 0. :
            w_ratio = self.width() / sc_rect.width() * 0.9
        else :
            w_ratio = 1.
        if sc_rect.height() > 0. :
            h_ratio = self.height() / sc_rect.height() * 0.9
        else :
            h_ratio = 1.
        sc_scale = min(w_ratio,h_ratio)

        mat = QtGui.QMatrix()
        mat.scale(sc_scale,sc_scale)
        self.setMatrix(mat)
        self.centerOn(sc_center)

    ######################
    # Deprecated methods #
    ######################
    graph = deprecate("graph")
    set_graph = deprecate("set_graph")
    rebuild_scene = deprecate("rebuild")
    clear_scene = deprecate("clear")
    get_selected_items = deprecate("get_items")
    get_selected_items = deprecate("get_selected_items")
    get_selection_center = deprecate("get_selection_center")
    select_added_elements = deprecate("select_added_elements")
    post_addition = deprecate("post_addition")
    notify = deprecate("notify")


interfaces.IGraphListener.check(Scene)

