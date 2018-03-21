"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['source/main.py']
DATA_FILES = []
PACKAGES = [
	'sip', 
	'PyQt4._qt', 
	're', 
	'os', 
	'itertools', 
	'ete3', 
	'copy', 
	'subprocess', 
	'collections', 
	'scipy', 
	'natsort', 
	'functools', 
	'webbrowser', 
	'os', 
	'matplotlib', 
	'cStringIO', 
	'numpy', 
	'math', 
	'random', 
	'shutil', 
	'dendropy', 
	'PIL', 
	'reportlab',
    'reportlab.lib',
    'reportlab.lib.colors',
    'reportlab.platypus',
    'biopython'
 ]
OPTIONS = {
	'iconfile': '/Users/Peter/PycharmProjects/ALPHA/browser.icns', 
	'argv_emulation': True, 
	'includes': PACKAGES
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
