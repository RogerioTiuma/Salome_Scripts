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
Box_1 = geompy.MakeBoxDXDYDZ(200, 200, 200)
dads = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(dads, [33])
[dads] = geompy.GetExistingSubObjects(Box_1, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudyInFather( Box_1, dads, 'dads' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Box_1,'Mesh_1')
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(10)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
dads_1 = Mesh_1.GroupOnGeom(dads,'dads',SMESH.FACE)
Regular_1D_1 = Mesh_1.Segment(geom=dads)
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(20)


Quadrangle_2D_1 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=dads)
Quadrangle_Parameters_1 = Quadrangle_2D_1.QuadrangleParameters(smeshBuilder.QUAD_TRIANGLE_PREF,-1,[],[])


[ dads_1 ] = Mesh_1.GetGroups()
Quadrangle_Parameters_1.SetQuadType( smeshBuilder.QUAD_STANDARD )
Quadrangle_Parameters_1.SetTriaVertex( -1 )
Quadrangle_Parameters_1.SetEnforcedNodes( [], [] )

[ dads_1 ] = Mesh_1.GetGroups()
Quadrangle_Parameters_2 = Quadrangle_2D.QuadrangleParameters(smeshBuilder.QUAD_TRIANGLE_PREF,-1,[],[])
[ dads_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ dads_1 ] = Mesh_1.GetGroups()
Sub_mesh_1 = Regular_1D_1.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(dads_1, 'dads')
smesh.SetName(Quadrangle_Parameters_2, 'Quadrangle Parameters_2')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
