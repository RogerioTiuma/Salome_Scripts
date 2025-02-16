#!/usr/bin/env python

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'd:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/01_VIGA/')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("C", 6)
notebook.set("h", 0.5)
notebook.set("esp", 0.25)
notebook.set("E", 210)
notebook.set("v", 0.25)

###
### GEOM component
###
import math
import SALOMEDS
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New()
gg = salome.ImportComponentGUI("GEOM")

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

geompy.addToStudy(O,"O")
geompy.addToStudy(OX,"OX")
geompy.addToStudy(OY,"OY")
geompy.addToStudy(OZ,"OZ")


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()