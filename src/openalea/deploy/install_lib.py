################################################################################
# -*- python -*-
#
#       OpenAlea.Deploy : OpenAlea setuptools extension
#
#       Copyright 2006-2007 INRIA - CIRAD - INRA  
#
#       File author(s): Samuel Dufour-Kowalski <samuel.dufour@sophia.inria.fr>
#                       Christophe Pradal <christophe.prada@cirad.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
################################################################################

__license__ = "Cecill-C"
__revision__ =" $Id: environ_var.py 847 2007-10-04 11:53:07Z dufourko $"

__doc__ = """ Install dynamic library """


import os
import sys
import shutil
import glob
from os.path import join

egg_marker_extension = ".egm"

from openalea.deploy.util import get_all_lib_dirs, get_base_dir
from distutils.dir_util import mkpath
from distutils.sysconfig import get_python_lib


def get_default_dyn_lib():
    """ Return the default path for dynamic library """
    
    if("posix" in os.name):
        return "/usr/local/lib"
    elif("win" in sys.platform.lower()):
        basedir = get_python_lib()
        return os.path.join(basedir, "shared_libs")


def get_dyn_lib_dir():
    """ Return the shared lib directory """
    bdir = get_base_dir("openalea.deploy")
    dir = os.path.abspath(join(bdir, os.path.pardir))

    try:
        f = open(join(dir, "shared-lib.pth"), 'r')
        lib_dir = f.read()
        f.close()
    except Exception, e:
        lib_dir = get_default_dyn_lib()
        
    return lib_dir



def set_dyn_lib_dir(path):
    """ Set the shared lib directory """
    bdir = get_base_dir("openalea.deploy")
    dir = os.path.abspath(join(bdir, os.path.pardir))
    dst = join(dir, "shared-lib.pth")
    try:
        f = open(dst, 'w')
        f.write(path)
        print "Write ", dst
        f.close()
    except Exception, e:
        print e

def is_lib(filename):
    """ Return true if filename is a library """

    for pat in (".dll", ".so", ".a", ".lib"):
        if filename.endswith(pat):
            return True

    return False


def link_lib(src, dst):
    
    """ Create a symlink/copy library if necessary
    And create a marker file if it is absent
    """

    mark_file = dst + egg_marker_extension

    # test if there is a marker

    try:
        f = open(mark_file, 'r')
        mark = f.read()
        f.close()

        # file is identical : return
        if(mark == src):
            return False

    except Exception, e:
        pass
    
    # copy
    print "Installing %s -> %s"%(src, dst)
    if(os.path.exists(dst)):
        os.unlink(dst)

    if(hasattr(os, 'symlink')):
        os.symlink(src, dst)
    else:
        shutil.copy2(src, dst)

    # create a mark file
    print "Installing ", mark_file
    f = open(mark_file, 'w')
    f.write(src)
    f.close()

    return True


    
def clean_lib(lib_dir, clean_all=False):
    """ Remove lib if source has been removed
    If clean_all is True, remove all library with egm
    """

    for egm in glob.iglob(join(lib_dir, "*" + egg_marker_extension)):
        f = open(egm, 'r')
        srcfile = f.read()
        f.close()

        if(not os.path.exists(srcfile) or clean_all):
            libfile = egm[:- len(egg_marker_extension)]
            print "Removing ", libfile
            os.remove(libfile)
            print "Removing ", egm
            os.remove(egm)



def install_lib(lib_dir):
    """
    Install dynamic library in lib_dir
    if None, use previous dir or default
    Return real lib_dir
    """
    if(not lib_dir):
        lib_dir = get_dyn_lib_dir()

    # Create directory
    if(not os.path.exists(lib_dir)):
        mkpath(lib_dir)

    old_lib_dir = get_dyn_lib_dir()
    changed = (old_lib_dir != lib_dir)
    # remove unused lib
    clean_lib(old_lib_dir, changed)

    if(changed):
        set_dyn_lib_dir(lib_dir)
    
    # get all lib_dir
    egglibdirs = set(get_all_lib_dirs())

    # install lib
    for d in egglibdirs:

        src_dir = os.path.abspath(d)
        dst_dir = os.path.abspath(lib_dir)
    
        for f in os.listdir(src_dir):

            if( is_lib(f) ):
                src = join(src_dir, f)
                dst = join(dst_dir, f)
                link_lib(src, dst)


    return lib_dir
                




    


