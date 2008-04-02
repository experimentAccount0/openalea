# -*- python -*-
#
#       OpenAlea.Core
#
#       Copyright 2006-2008 INRIA - CIRAD - INRA  
#
#       File author(s): Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
###############################################################################


__doc__="""
Data management classes
"""

__license__= "Cecill-C"
__revision__=" $Id$ "

from openalea.core.node import AbstractFactory, Node, NodeFactory
from openalea.core.interface import IData

import os
import string



class PackageData(object):
    """ String representing a package data """

    def __init__(self, pkg, filename):
        """ 
        pkg : package name 
        name : data name
        """
        self.pkg = pkg
        self.name = filename

        from openalea.core.pkgmanager import PackageManager

        path = PackageManager()[self.pkg].path
        self.repr = os.path.join(path, self.name)
        

    def __repr__(self):
        return "PackageData(%s, %s)"%(self.pkg, self.name)

    def __str__(self):
        return self.repr



class DataFactory(AbstractFactory):
    """ Data representation as factory """
    
    #mimetype = "openalea/datafactory"

    def __init__(self,
                 name,
                 description = '',
                 **kargs):

        AbstractFactory.__init__(self, name, description, category='data', **kargs)
        self.pkgdata_cache = None

    
    def get_pkg_data(self):
        """ Return the associated PackageData object"""

        if(not self.pkgdata_cache):
            self.pkgdata_cache = PackageData(self.package.name, self.name)
            
        return self.pkgdata_cache
    
    
    def instantiate(self, call_stack=[]):
        """ Return a node instance
        @param call_stack : the list of NodeFactory id already in call stack
        (in order to avoir infinite recursion)
        """

        node =  DataNode(self.get_pkg_data())
        node.factory = self
        return node


    

    def instantiate_widget(self, node=None, parent=None, edit=False):
        """ Return the corresponding widget initialised with node """

        # Code Editor
        if(edit):
            from openalea.visualea.code_editor import get_editor
            w = get_editor()(parent)
            w.edit_file(str(self.get_pkg_data()))
            return w 

        # Node Widget
        if(node == None): node = self.instantiate()

        from openalea.visualea.node_widget import DefaultNodeWidget
        return DefaultNodeWidget(node, parent)
    
    
    def get_writer(self):
        """ Return the writer class """
 
        return PyDataFactoryWriter(self)


    def clean_files(self):
        """ Remove files depending of factory """
        
        os.remove(str(self.get_pkg_data()))



class DataNode(Node):
    """ Node representing a Data """
 
    def __init__(self, packagedata):

        # compute path
        v = packagedata

        Node.__init__(self,
                      inputs=(dict(name='data', interface=IData, value=v),),
                      outputs=(dict(name='data', interface=IData),),
                      )
        self.caption = 'Data : %s:%s'%(v.pkg, v.name)
        
    def __call__(self, args):
        return args[0],




class PyDataFactoryWriter(object):
    """ DataFactory python Writer """

    datafactory_template = """
$NAME = DataFactory(name=$PNAME, 
                    description=$DESCRIPTION, 
                    )
"""

    def __init__(self, factory):
        self.factory = factory

    def __repr__(self):
        """ Return the python string representation """
        f = self.factory
        fstr = string.Template(self.datafactory_template)
        result = fstr.safe_substitute(NAME=f.get_python_name(),
                                      PNAME=repr(f.name),
                                      DESCRIPTION=repr(f.description),
                                      )
        return result



           
