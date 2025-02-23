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
geomObj_1 = geompy.MakeVertex(0, 0, 0)
geomObj_2 = geompy.MakeVectorDXDYDZ(1, 0, 0)
geomObj_3 = geompy.MakeVectorDXDYDZ(0, 1, 0)
geomObj_4 = geompy.MakeVectorDXDYDZ(0, 0, 1)
Box_1 = geompy.MakeBoxDXDYDZ(100, 100, 10)
Box_2 = geompy.MakeBoxDXDYDZ(75, 75, 10)
Partition_1 = geompy.MakePartition([Box_1], [Box_2], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
Partition_1_vertex_20 = geompy.GetSubShape(Partition_1, [20])
Partition_1_vertex_48 = geompy.GetSubShape(Partition_1, [48])
Line_1 = geompy.MakeLineTwoPnt(Partition_1_vertex_20, Partition_1_vertex_48)
Partition_1_vertex_22 = geompy.GetSubShape(Partition_1, [22])
Partition_1_vertex_55 = geompy.GetSubShape(Partition_1, [55])
Line_2 = geompy.MakeLineTwoPnt(Partition_1_vertex_22, Partition_1_vertex_55)
Quadrangle_Face_1 = geompy.MakeQuad2Edges(Line_1, Line_2)
diag = geompy.MakePartition([Partition_1], [Quadrangle_Face_1], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
Menores = geompy.CreateGroup(diag, geompy.ShapeType["FACE"])
geompy.UnionIDs(Menores, [69, 45, 55, 72])
Maiores = geompy.CreateGroup(diag, geompy.ShapeType["FACE"])
geompy.UnionIDs(Maiores, [34, 32])
[Menores, Maiores] = geompy.GetExistingSubObjects(diag, False)
Partition_1_edge_19 = geompy.GetSubShape(Partition_1, [19])
Plane_1 = geompy.MakePlane(Partition_1_vertex_20, Partition_1_edge_19, 2000)
Partition_1_vertex_17 = geompy.GetSubShape(Partition_1, [17])
Partition_1_edge_51 = geompy.GetSubShape(Partition_1, [51])
Plane_2 = geompy.MakePlane(Partition_1_vertex_17, Partition_1_edge_51, 2000)
Partition_3 = geompy.MakePartition([Partition_1], [Plane_1, Plane_2], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
n20 = geompy.CreateGroup(Partition_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(n20, [34, 32])
n10 = geompy.CreateGroup(Partition_3, geompy.ShapeType["FACE"])
geompy.UnionIDs(n10, [79, 55, 96, 86, 45, 69])
[n20, n10] = geompy.GetExistingSubObjects(Partition_3, False)
linhas1 = geompy.CreateGroup(Partition_3, geompy.ShapeType["EDGE"])
geompy.UnionIDs(linhas1, [68, 57, 98, 44, 78, 49, 71, 88, 40])
geompy.DifferenceIDs(linhas1, [68, 57, 98, 44, 78, 49, 71, 88, 40])
geompy.UnionIDs(linhas1, [68, 57, 98, 44, 78, 49, 71, 88, 40, 95, 90, 64])
geompy.DifferenceIDs(linhas1, [68, 57, 98, 44, 78, 49, 71, 88, 40, 95, 90, 64])
geompy.UnionIDs(linhas1, [68, 57, 98, 44, 78, 49, 71, 88, 40, 95, 90, 64])
[n20, n10, linhas1] = geompy.GetExistingSubObjects(Partition_3, False)
lin_1 = geompy.CreateGroup(diag, geompy.ShapeType["EDGE"])
geompy.UnionIDs(lin_1, [49, 64, 44, 57, 40, 68])
[Menores, Maiores, lin_1] = geompy.GetExistingSubObjects(diag, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Box_2, 'Box_2' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, Partition_1_vertex_20, 'Partition_1:vertex_20' )
geompy.addToStudyInFather( Partition_1, Partition_1_vertex_48, 'Partition_1:vertex_48' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudyInFather( Partition_1, Partition_1_vertex_22, 'Partition_1:vertex_22' )
geompy.addToStudyInFather( Partition_1, Partition_1_vertex_55, 'Partition_1:vertex_55' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Quadrangle_Face_1, 'Quadrangle Face_1' )
geompy.addToStudy( diag, 'diag' )
geompy.addToStudyInFather( diag, Menores, 'Menores' )
geompy.addToStudyInFather( diag, Maiores, 'Maiores' )
geompy.addToStudyInFather( Partition_1, Partition_1_edge_19, 'Partition_1:edge_19' )
geompy.addToStudy( Plane_1, 'Plane_1' )
geompy.addToStudyInFather( Partition_1, Partition_1_edge_51, 'Partition_1:edge_51' )
geompy.addToStudyInFather( Partition_1, Partition_1_vertex_17, 'Partition_1:vertex_17' )
geompy.addToStudy( Plane_2, 'Plane_2' )
geompy.addToStudy( Partition_3, 'Partition_3' )
geompy.addToStudyInFather( Partition_3, n20, 'n20' )
geompy.addToStudyInFather( Partition_3, n10, 'n10' )
geompy.addToStudyInFather( Partition_3, linhas1, 'linhas1' )
geompy.addToStudyInFather( diag, lin_1, 'lin_1' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Reducao_diag = smesh.Mesh(diag,'Reducao_diag')
Regular_1D = Reducao_diag.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(20)
Quadrangle_2D = Reducao_diag.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Reducao_diag.Hexahedron(algo=smeshBuilder.Hexa)
Menores_1 = Reducao_diag.GroupOnGeom(Menores,'Menores',SMESH.FACE)
Maiores_1 = Reducao_diag.GroupOnGeom(Maiores,'Maiores',SMESH.FACE)
isDone = Reducao_diag.Compute()


[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_Parameters_1 = Quadrangle_2D.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF_REVERSED,-1,[],[])
isDone = Reducao_diag.Compute()

[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Number_of_Segments_1.SetNumberOfSegments( 10 )
isDone = Reducao_diag.Compute()
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Regular_1D_1 = Reducao_diag.Segment(geom=Menores)
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(5)
Quadrangle_2D_1 = Reducao_diag.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=Menores)
Quadrangle_Parameters_2 = Quadrangle_2D_1.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF_REVERSED,-1,[],[])
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_Parameters_2.SetQuadType( smeshBuilder.QUAD_QUADRANGLE_PREF )
Quadrangle_Parameters_2.SetTriaVertex( -1 )
Quadrangle_Parameters_2.SetEnforcedNodes( [], [] )
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
#Reducao_diag.GetMesh().RemoveSubMesh( smeshObj_1 ) ### smeshObj_1 has not been yet created
Number_of_Segments_1.SetNumberOfSegments( 5 )
isDone = Reducao_diag.Compute()
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Regular_1D_2 = Reducao_diag.Segment(geom=Maiores)
Number_of_Segments_3 = Regular_1D_2.NumberOfSegments(10)
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_2D_2 = Reducao_diag.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=Maiores)
Quadrangle_Parameters_3 = Quadrangle_2D_2.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_Parameters_3.SetQuadType( smeshBuilder.QUAD_QUADRANGLE_PREF )
Quadrangle_Parameters_3.SetTriaVertex( -1 )
Quadrangle_Parameters_3.SetEnforcedNodes( [], [] )
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
status = Reducao_diag.RemoveHypothesis(Quadrangle_Parameters_3,Maiores)
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_Parameters_4 = Quadrangle_2D_2.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Number_of_Segments_1.SetNumberOfSegments( 4 )
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
quad_1 = smesh.Mesh(Partition_3,'quad_1')
Regular_1D_3 = quad_1.Segment()
Number_of_Segments_4 = Regular_1D_3.NumberOfSegments(4)
Quadrangle_2D_3 = quad_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D_1 = quad_1.Hexahedron(algo=smeshBuilder.Hexa)
n20_1 = quad_1.GroupOnGeom(n20,'n20',SMESH.FACE)
n10_1 = quad_1.GroupOnGeom(n10,'n10',SMESH.FACE)
isDone = quad_1.Compute()
[ n20_1, n10_1 ] = quad_1.GetGroups()
Regular_1D_4 = quad_1.Segment(geom=n20)
Number_of_Segments_5 = Regular_1D_4.NumberOfSegments(20)
[ n20_1, n10_1 ] = quad_1.GetGroups()
Quadrangle_Parameters_5 = Quadrangle_2D_3.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF_REVERSED,-1,[],[])
[ n20_1, n10_1 ] = quad_1.GetGroups()
Quadrangle_2D_4 = quad_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=n20)
Quadrangle_Parameters_6 = Quadrangle_2D_4.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ n20_1, n10_1 ] = quad_1.GetGroups()
Quadrangle_Parameters_5.SetQuadType( smeshBuilder.QUAD_QUADRANGLE_PREF )
Quadrangle_Parameters_5.SetTriaVertex( -1 )
Quadrangle_Parameters_5.SetEnforcedNodes( [], [] )
[ n20_1, n10_1 ] = quad_1.GetGroups()
Viscous_Layers_2D_1 = Quadrangle_2D_4.ViscousLayers2D(3,1,1,[],1)
[ n20_1, n10_1 ] = quad_1.GetGroups()
Viscous_Layers_2D_1.SetGroupName( 'Viscous Layers' )
[ n20_1, n10_1 ] = quad_1.GetGroups()
Viscous_Layers_2D_1.SetTotalThickness( 1 )
Viscous_Layers_2D_1.SetNumberLayers( 3 )
Viscous_Layers_2D_1.SetStretchFactor( 1 )
Viscous_Layers_2D_1.SetEdges( [], 0 )
[ n20_1, n10_1 ] = quad_1.GetGroups()
Quadratic_Mesh_1 = Regular_1D_4.QuadraticMesh()
status = quad_1.RemoveHypothesis(Viscous_Layers_2D_1,n20)
[ n20_1, n10_1 ] = quad_1.GetGroups()
status = quad_1.RemoveHypothesis(Quadratic_Mesh_1,n20)
Propagation_of_Node = Regular_1D_4.PropagationOfDistribution()
[ n20_1, n10_1 ] = quad_1.GetGroups()
status = quad_1.RemoveHypothesis(Propagation_of_Node,n20)
Propagation_of_1D_Hyp = Regular_1D_4.Propagation()
[ n20_1, n10_1 ] = quad_1.GetGroups()
Number_of_Segments_5.SetScaleFactor( 4 )
Number_of_Segments_5.SetReversedEdges( [] )
status = quad_1.RemoveHypothesis(Propagation_of_1D_Hyp,n20)
[ n20_1, n10_1 ] = quad_1.GetGroups()
Number_of_Segments_5.SetDistrType( 0 )
Number_of_Segments_5.SetNumberOfSegments( 16 )
[ n20_1, n10_1 ] = quad_1.GetGroups()
Quadrangle_Parameters_6.SetQuadType( smeshBuilder.QUAD_STANDARD )
Quadrangle_Parameters_6.SetTriaVertex( -1 )
Quadrangle_Parameters_6.SetEnforcedNodes( [], [] )
[ n20_1, n10_1 ] = quad_1.GetGroups()
status = quad_1.RemoveHypothesis(Quadrangle_Parameters_5)
[ n20_1, n10_1 ] = quad_1.GetGroups()
Number_of_Segments_4.SetNumberOfSegments( 8 )
[ n20_1, n10_1 ] = quad_1.GetGroups()
Quadrangle_Parameters_7 = Quadrangle_2D_3.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ n20_1, n10_1 ] = quad_1.GetGroups()
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_Parameters_4.SetQuadType( smeshBuilder.QUAD_STANDARD )
Quadrangle_Parameters_4.SetTriaVertex( -1 )
Quadrangle_Parameters_4.SetEnforcedNodes( [], [] )
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_Parameters_1.SetQuadType( smeshBuilder.QUAD_QUADRANGLE_PREF )
Quadrangle_Parameters_1.SetTriaVertex( -1 )
Quadrangle_Parameters_1.SetEnforcedNodes( [], [] )
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Number_of_Segments_3.SetNumberOfSegments( 8 )
isDone = Reducao_diag.Compute()
[ Menores_1, Maiores_1 ] = Reducao_diag.GetGroups()
Quadrangle_Parameters_7.SetQuadType( smeshBuilder.QUAD_TRIANGLE_PREF )
Quadrangle_Parameters_7.SetTriaVertex( -1 )
Quadrangle_Parameters_7.SetEnforcedNodes( [], [] )
isDone = quad_1.Compute()
[ n20_1, n10_1 ] = quad_1.GetGroups()

quad_2 = smesh.Mesh(Partition_3,'quad_2')
Regular_1D_5 = quad_2.Segment()
Number_of_Segments_6 = Regular_1D_5.NumberOfSegments(4)
Quadrangle_2D_5 = quad_2.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D_2 = quad_2.Hexahedron(algo=smeshBuilder.Hexa)
n20_2 = quad_2.GroupOnGeom(n20,'n20',SMESH.FACE)
n10_2 = quad_2.GroupOnGeom(n10,'n10',SMESH.FACE)
linhas1_1 = quad_2.GroupOnGeom(linhas1,'linhas1',SMESH.EDGE)

[ n20_2, n10_2, linhas1_1 ] = quad_2.GetGroups()
Regular_1D_6 = quad_2.Segment(geom=n20)
Number_of_Segments_7 = Regular_1D_6.NumberOfSegments(8)
[ n20_2, n10_2, linhas1_1 ] = quad_2.GetGroups()
Quadrangle_2D_6 = quad_2.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=n20)
Quadrangle_Parameters_8 = Quadrangle_2D_6.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ n20_2, n10_2, linhas1_1 ] = quad_2.GetGroups()
Quadrangle_Parameters_8.SetQuadType( smeshBuilder.QUAD_QUADRANGLE_PREF )
Quadrangle_Parameters_8.SetTriaVertex( -1 )
Quadrangle_Parameters_8.SetEnforcedNodes( [], [] )
Quadrangle_Parameters_9 = Quadrangle_2D_5.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ n20_2, n10_2, linhas1_1 ] = quad_2.GetGroups()
Regular_1D_7 = quad_2.Segment(geom=linhas1)
Number_of_Segments_8 = Regular_1D_7.NumberOfSegments(1)
[ n20_2, n10_2, linhas1_1 ] = quad_2.GetGroups()
Number_of_Segments_8.SetNumberOfSegments( 1 )
[ n20_2, n10_2, linhas1_1 ] = quad_2.GetGroups()


Mesh_1 = smesh.Mesh(diag,'Mesh_1')
Regular_1D_8 = Mesh_1.Segment()
Number_of_Segments_9 = Regular_1D_8.NumberOfSegments(4)
Quadrangle_2D_7 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D_3 = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
Menores_2 = Mesh_1.GroupOnGeom(Menores,'Menores',SMESH.FACE)
Maiores_2 = Mesh_1.GroupOnGeom(Maiores,'Maiores',SMESH.FACE)
lin_1_1 = Mesh_1.GroupOnGeom(lin_1,'lin_1',SMESH.EDGE)
isDone = Mesh_1.Compute()


[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Regular_1D_9 = Mesh_1.Segment(geom=Maiores)
Number_of_Segments_10 = Regular_1D_9.NumberOfSegments(8)
Quadrangle_2D_8 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=Maiores)
Quadrangle_Parameters_10 = Quadrangle_2D_8.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Regular_1D_10 = Mesh_1.Segment(geom=lin_1)
Number_of_Segments_11 = Regular_1D_10.NumberOfSegments(1)
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Number_of_Segments_10.SetNumberOfSegments( 15 )
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Quadrangle_Parameters_11 = Quadrangle_2D_7.QuadrangleParameters(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Quadrangle_Parameters_10.SetQuadType( smeshBuilder.QUAD_STANDARD )
Quadrangle_Parameters_10.SetTriaVertex( -1 )
Quadrangle_Parameters_10.SetEnforcedNodes( [], [] )
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Number_of_Segments_9.SetNumberOfSegments( 5 )
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Number_of_Segments_7.SetNumberOfSegments( 16 )
isDone = quad_2.Compute()
[ n20_2, n10_2, linhas1_1 ] = quad_2.GetGroups()
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Quadrangle_Parameters_11.SetQuadType( smeshBuilder.QUAD_QUADRANGLE_PREF )
Quadrangle_Parameters_11.SetTriaVertex( -1 )
Quadrangle_Parameters_11.SetEnforcedNodes( [], [] )
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Number_of_Segments_11.SetNumberOfSegments( 1 )
isDone = Mesh_1.Compute()
[ Menores_2, Maiores_2, lin_1_1 ] = Mesh_1.GetGroups()
Sub_mesh_1 = Regular_1D_2.GetSubMesh()
Sub_mesh_2 = Regular_1D_4.GetSubMesh()
Sub_mesh_3 = quad_2.GetSubMesh( n20, 'Sub-mesh_3' )
Sub_mesh_4 = Regular_1D_7.GetSubMesh()
Sub_mesh_5 = Regular_1D_9.GetSubMesh()
Sub_mesh_6 = Regular_1D_10.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Menores_2, 'Menores')
smesh.SetName(Maiores_2, 'Maiores')
smesh.SetName(n10_1, 'n10')
smesh.SetName(n20_1, 'n20')
smesh.SetName(n10_2, 'n10')
smesh.SetName(n20_2, 'n20')
smesh.SetName(Quadrangle_Parameters_6, 'Quadrangle Parameters_6')
smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')
smesh.SetName(Number_of_Segments_5, 'Number of Segments_5')
smesh.SetName(Quadrangle_Parameters_5, 'Quadrangle Parameters_5')
smesh.SetName(Propagation_of_1D_Hyp, 'Propagation of 1D Hyp. on Opposite Edges_1')
smesh.SetName(linhas1_1, 'linhas1')
smesh.SetName(Quadrangle_Parameters_7, 'Quadrangle Parameters_7')
smesh.SetName(Quadratic_Mesh_1, 'Quadratic Mesh_1')
smesh.SetName(Propagation_of_Node, 'Propagation of Node Distribution on Opposite Edges_1')
smesh.SetName(Number_of_Segments_6, 'Number of Segments_6')
smesh.SetName(Number_of_Segments_7, 'Number of Segments_7')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Sub_mesh_6, 'Sub-mesh_6')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Sub_mesh_5, 'Sub-mesh_5')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(Menores_1, 'Menores')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(Maiores_1, 'Maiores')
smesh.SetName(Sub_mesh_4, 'Sub-mesh_4')
smesh.SetName(Quadrangle_Parameters_9, 'Quadrangle Parameters_9')
smesh.SetName(Quadrangle_Parameters_8, 'Quadrangle Parameters_8')
smesh.SetName(Number_of_Segments_9, 'Number of Segments_9')
smesh.SetName(Number_of_Segments_8, 'Number of Segments_8')
smesh.SetName(Number_of_Segments_10, 'Number of Segments_10')
smesh.SetName(Quadrangle_Parameters_10, 'Quadrangle Parameters_10')
smesh.SetName(Quadrangle_Parameters_11, 'Quadrangle Parameters_11')
smesh.SetName(Number_of_Segments_11, 'Number of Segments_11')
smesh.SetName(Reducao_diag.GetMesh(), 'Reducao_diag')
smesh.SetName(quad_1.GetMesh(), 'quad_1')
smesh.SetName(quad_2.GetMesh(), 'quad_2')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(lin_1_1, 'lin_1')
smesh.SetName(Quadrangle_Parameters_2, 'Quadrangle Parameters_2')
smesh.SetName(Quadrangle_Parameters_1, 'Quadrangle Parameters_1')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Quadrangle_Parameters_4, 'Quadrangle Parameters_4')
smesh.SetName(Quadrangle_Parameters_3, 'Quadrangle Parameters_3')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
