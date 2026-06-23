import os
import sys
import pci

if getattr(sys, 'frozen', False):
    basedir = os.path.dirname(sys.executable)
else:
    basedir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, basedir)
inter = pci.interpreter()