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
xx = geompy.CreateGroup(Box_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(xx, [31])
[dads, xx] = geompy.GetExistingSubObjects(Box_1, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudyInFather( Box_1, dads, 'dads' )
geompy.addToStudyInFather( Box_1, xx, 'xx' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Number_of_Segments_1 = smesh.CreateHypothesis('NumberOfSegments')
Number_of_Segments_1.SetNumberOfSegments( 10 )
Regular_1D = smesh.CreateHypothesis('Regular_1D')
Quadrangle_2D = smesh.CreateHypothesis('Quadrangle_2D')
Hexa_3D = smesh.CreateHypothesis('Hexa_3D')

Quadrangle_Parameters_1 = smesh.CreateHypothesis('QuadrangleParams')
Number_of_Segments_2 = smesh.CreateHypothesis('NumberOfSegments')
Number_of_Segments_2.SetNumberOfSegments( 20 )
Quadrangle_Parameters_1.SetQuadType( smeshBuilder.QUAD_STANDARD )
Quadrangle_Parameters_1.SetTriaVertex( -1 )
Quadrangle_Parameters_1.SetEnforcedNodes( [], [] )

Quadrangle_Parameters_2 = smesh.CreateHypothesis('QuadrangleParams')
Quadrangle_Parameters_2.SetQuadType( smeshBuilder.QUAD_TRIANGLE_PREF )
Quadrangle_Parameters_2.SetTriaVertex( -1 )
Quadrangle_Parameters_2.SetEnforcedNodes( [], [] )

Number_of_Segments_3 = smesh.CreateHypothesis('NumberOfSegments')
Number_of_Segments_3.SetNumberOfSegments( 10 )
Quadrangle_Parameters_3 = smesh.CreateHypothesis('QuadrangleParams')
Quadrangle_Parameters_3.SetQuadType( smeshBuilder.QUAD_TRIANGLE_PREF )
Quadrangle_Parameters_3.SetTriaVertex( -1 )
Quadrangle_Parameters_3.SetEnforcedNodes( [], [] )

Mesh_1 = smesh.Mesh(Box_1,'Mesh_1')
status = Mesh_1.AddHypothesis(Number_of_Segments_3)
status = Mesh_1.AddHypothesis(Regular_1D)
status = Mesh_1.AddHypothesis(Quadrangle_Parameters_3)
status = Mesh_1.AddHypothesis(Quadrangle_2D)
status = Mesh_1.AddHypothesis(Hexa_3D)

dads_1 = Mesh_1.GroupOnGeom(dads,'dads',SMESH.FACE)
xx_1 = Mesh_1.GroupOnGeom(xx,'xx',SMESH.FACE)

Number_of_Segments_4 = smesh.CreateHypothesis('NumberOfSegments')
Number_of_Segments_4.SetNumberOfSegments( 20 )

status = Mesh_1.AddHypothesis(Regular_1D,dads)


status = Mesh_1.AddHypothesis(Number_of_Segments_4,dads)
[ dads_1, xx_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ dads_1, xx_1 ] = Mesh_1.GetGroups()
Sub_mesh_1 = Mesh_1.GetSubMesh( dads, 'Sub-mesh_1' )


## Set names of Mesh objects
smesh.SetName(Regular_1D, 'Regular_1D')
smesh.SetName(Hexa_3D, 'Hexa_3D')
smesh.SetName(Quadrangle_2D, 'Quadrangle_2D')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(Quadrangle_Parameters_3, 'Quadrangle Parameters_3')
smesh.SetName(Quadrangle_Parameters_2, 'Quadrangle Parameters_2')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(xx_1, 'xx')
smesh.SetName(dads_1, 'dads')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
