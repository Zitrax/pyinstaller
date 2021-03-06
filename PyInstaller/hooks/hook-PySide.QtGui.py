#-----------------------------------------------------------------------------
# Copyright (c) 2005-2015, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


from PyInstaller.utils.hooks.hookutils import qt4_plugins_binaries

hiddenimports = ['PySide.QtCore']

binaries = []
for plug in ('accessible', 'iconengines', 'imageformats', 'inputmethods', 'graphicssystems'):
    binaries.extend(qt4_plugins_binaries(plug, ns='PySide'))
