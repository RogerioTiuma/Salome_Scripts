#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/00_MODELOS/GITHUB/Salome_Scripts')

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
Box_1 = geompy.MakeBoxDXDYDZ(100, 200, 5)
Box_2 = geompy.MakeBoxDXDYDZ(50, 100, 5)
Box_3 = geompy.MakeBoxDXDYDZ(100, 100, 5)
Partition_1 = geompy.MakePartition([Box_1], [Box_2, Box_3], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
sd = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(sd, [82, 34, 76, 32])
n2 = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(n2, [57])
[sd, n2] = geompy.GetExistingSubObjects(Partition_1, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Box_3, 'Box_3' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, sd, 'sd' )
geompy.addToStudyInFather( Partition_1, n2, 'n2' )

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
Number_of_Segments_1 = Regular_1D.NumberOfSegments(10)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
sd_1 = Mesh_1.GroupOnGeom(sd,'sd',SMESH.FACE)
n2_1 = Mesh_1.GroupOnGeom(n2,'n2',SMESH.FACE)


#hyp_6.SetLength( 22.3663 ) ### not created Object
Regular_1D_1 = Mesh_1.Segment(geom=sd)
bora = Regular_1D_1.NumberOfSegments(15)
Quadrangle_2D_1 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=sd)
Quadrangle_Parameters_1 = Quadrangle_2D_1.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ sd_1, n2_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ sd_1, n2_1 ] = Mesh_1.GetGroups()
ciboula = Regular_1D_1.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')

smesh.SetName(bora, 'bora')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(sd_1, 'sd')
smesh.SetName(n2_1, 'n2')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(ciboula, 'ciboula')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
