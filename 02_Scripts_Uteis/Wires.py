#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/00_MODELOS/GITHUB/Salome_Scripts/Scripts_Uteis')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
Face_1 = geompy.MakeFaceHW(100, 100, 1)
[Edge_1,Edge_2,Edge_3,Edge_4] = geompy.ExtractShapes(Face_1, geompy.ShapeType["EDGE"], True)
Face_2 = geompy.MakeFaceHW(200, 200, 1)
[Edge_5,Edge_6,Edge_7,Edge_8] = geompy.ExtractShapes(Face_2, geompy.ShapeType["EDGE"], True)
Face_3 = geompy.MakeFaceHW(200, 200, 1)
Face_1_vertex_7 = geompy.GetSubShape(Face_1, [7])
Face_2_vertex_7 = geompy.GetSubShape(Face_2, [7])
Line_1 = geompy.MakeLineTwoPnt(Face_1_vertex_7, Face_2_vertex_7)
Face_1_vertex_4 = geompy.GetSubShape(Face_1, [4])
Face_2_vertex_4 = geompy.GetSubShape(Face_2, [4])
Line_2 = geompy.MakeLineTwoPnt(Face_1_vertex_4, Face_2_vertex_4)
Face_4 = geompy.MakeFaceWires([Line_1, Line_2, Edge_2, Edge_6], 1)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Face_3, 'Face_3' )
geompy.addToStudyInFather( Face_1, Face_1_vertex_7, 'Face_1:vertex_7' )
geompy.addToStudyInFather( Face_2, Face_2_vertex_7, 'Face_2:vertex_7' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudyInFather( Face_1, Face_1_vertex_4, 'Face_1:vertex_4' )
geompy.addToStudyInFather( Face_2, Face_2_vertex_4, 'Face_2:vertex_4' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudyInFather( Face_1, Edge_1, 'Edge_1' )
geompy.addToStudyInFather( Face_1, Edge_2, 'Edge_2' )
geompy.addToStudyInFather( Face_1, Edge_3, 'Edge_3' )
geompy.addToStudyInFather( Face_1, Edge_4, 'Edge_4' )
geompy.addToStudyInFather( Face_2, Edge_5, 'Edge_5' )
geompy.addToStudyInFather( Face_2, Edge_6, 'Edge_6' )
geompy.addToStudyInFather( Face_2, Edge_7, 'Edge_7' )
geompy.addToStudyInFather( Face_2, Edge_8, 'Edge_8' )
geompy.addToStudy( Face_4, 'Face_4' )


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
