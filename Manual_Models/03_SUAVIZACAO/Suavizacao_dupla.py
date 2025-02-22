#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/03_SUAVIZACAO')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("a", 100)
notebook.set("b", 200)
notebook.set("c", 400)
notebook.set("e", 10)
####################################################
##        End of NoteBook variables section       ##
####################################################
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
Box_1 = geompy.MakeBoxDXDYDZ("a", "a", "e")
Box_2 = geompy.MakeBoxDXDYDZ("b", "a", "e")
Box_3 = geompy.MakeBoxDXDYDZ("c", "a", "e")
Partition_1 = geompy.MakePartition([Box_3], [Box_1, Box_2], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
esp = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(esp, [16, 54, 21, 66, 42, 11, 78, 6])
n1 = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(n1, [34, 32])
n2 = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(n2, [45, 55])
n3 = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(n3, [79, 69])
[esp, n1, n2, n3] = geompy.GetExistingSubObjects(Partition_1, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Box_3, 'Box_3' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, esp, 'esp' )
geompy.addToStudyInFather( Partition_1, n1, 'n1' )
geompy.addToStudyInFather( Partition_1, n2, 'n2' )
geompy.addToStudyInFather( Partition_1, n3, 'n3' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Partition_1,'Mesh_1')
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(20)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
esp_1 = Mesh_1.GroupOnGeom(esp,'esp',SMESH.EDGE)
n1_1 = Mesh_1.GroupOnGeom(n1,'n1',SMESH.FACE)
n2_1 = Mesh_1.GroupOnGeom(n2,'n2',SMESH.FACE)
n3_1 = Mesh_1.GroupOnGeom(n3,'n3',SMESH.FACE)

Regular_1D_1 = Mesh_1.Segment(geom=esp)
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(3)
isDone = Mesh_1.Compute()
[ esp_1, n1_1, n2_1, n3_1 ] = Mesh_1.GetGroups()
Sub_mesh_1 = Regular_1D_1.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(n1_1, 'n1')
smesh.SetName(n3_1, 'n3')
smesh.SetName(n2_1, 'n2')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(esp_1, 'esp')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
