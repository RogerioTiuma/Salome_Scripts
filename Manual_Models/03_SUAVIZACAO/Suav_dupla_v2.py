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


############################ PARÂMETROS ##################
a = 100
b = 150
c = 225
e = 10

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("a", a)
notebook.set("b", b)
notebook.set("c", c)
notebook.set("e", e)
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
O_1 = geompy.MakeVertex(0, 0, 0)
OX_1 = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY_1 = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ_1 = geompy.MakeVectorDXDYDZ(0, 0, 1)
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
geompy.addToStudy( O_1, 'O' )
geompy.addToStudy( OX_1, 'OX' )
geompy.addToStudy( OY_1, 'OY' )
geompy.addToStudy( OZ_1, 'OZ' )
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
Number_of_Segments_1 = Regular_1D.NumberOfSegments(20,None,[])
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
esp_1 = Mesh_1.GroupOnGeom(esp,'esp',SMESH.EDGE)
n1_1 = Mesh_1.GroupOnGeom(n1,'n1',SMESH.FACE)
n2_1 = Mesh_1.GroupOnGeom(n2,'n2',SMESH.FACE)
n3_1 = Mesh_1.GroupOnGeom(n3,'n3',SMESH.FACE)
Regular_1D_1 = Mesh_1.Segment(geom=esp)
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(3,None,[])


[ esp_1, n1_1, n2_1, n3_1 ] = Mesh_1.GetGroups()
Quadrangle_Parameters_1 = Quadrangle_2D.QuadrangleParameters(smeshBuilder.QUAD_TRIANGLE_PREF,None,[],[])
Regular_1D_2 = Mesh_1.Segment(geom=n2)
Number_of_Segments_3 = Regular_1D_2.NumberOfSegments(10,None,[])
Sub_mesh_2 = Regular_1D_2.GetSubMesh()
Quadrangle_2D_1 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=n2)
Regular_1D_3 = Mesh_1.Segment(geom=n3)
Number_of_Segments_4 = Regular_1D_3.NumberOfSegments(5,None,[])
Sub_mesh_3 = Regular_1D_3.GetSubMesh()
Quadrangle_2D_2 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=n3)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_3, Sub_mesh_2 ] ])

[ esp_1, n1_1, n2_1, n3_1 ] = Mesh_1.GetGroups()
Quadrangle_Parameters_2 = Quadrangle_2D_1.QuadrangleParameters(smeshBuilder.QUAD_TRIANGLE_PREF,None,[],[])
[ esp_1, n1_1, n2_1, n3_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_2, Sub_mesh_3 ] ])
[ esp_1, n1_1, n2_1, n3_1 ] = Mesh_1.GetGroups()
Regular_1D_4 = Mesh_1.Segment(geom=n1)

Number_of_Segments_5 = Regular_1D_4.NumberOfSegments(20,None,[])
Sub_mesh_4 = Regular_1D_4.GetSubMesh()
Quadrangle_2D_3 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=n1)
status = Mesh_1.AddHypothesis(Quadrangle_Parameters_1,n1)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_4, Sub_mesh_2, Sub_mesh_3 ] ])

isDone = Mesh_1.Compute()
[ esp_1, n1_1, n2_1, n3_1 ] = Mesh_1.GetGroups()
Sub_mesh_1 = Regular_1D_1.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Sub_mesh_4, 'Sub-mesh_4')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(n1_1, 'n1')
smesh.SetName(n3_1, 'n3')
smesh.SetName(n2_1, 'n2')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(esp_1, 'esp')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Number_of_Segments_5, 'Number of Segments_5')
smesh.SetName(Quadrangle_Parameters_2, 'Quadrangle Parameters_2')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
