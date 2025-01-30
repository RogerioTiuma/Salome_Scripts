#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Lenovo/00_MODELOS/00_TREINO_SOFTWARE/00_CURSO_WIKKI/01_CURSO_SALOME/02_MIXURE_TEE')

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("C", 950)
notebook.set("C05", "C/2")
notebook.set("Dex", 219)
notebook.set("Rex", "Dex/2")
notebook.set("t", 6)
notebook.set("Rin", "Rex-t")
notebook.set("Cd", 133)
notebook.set("Cd05", "Cd/2")
notebook.set("r1", 15)
notebook.set("r2", 3)
notebook.set("d", 3.6)
notebook.set("DL", "Dex+2*tL")
notebook.set("RL", "DL/2")
notebook.set("LL", 230)
notebook.set("LL05", "LL/2")
notebook.set("tL", 4)
notebook.set("Pi", 3.14)
notebook.set("Ld", 102)
notebook.set("Ld05", "Ld/2")
notebook.set("tetha", "Ld05/Rex")
notebook.set("SL1", "Cd05+t-d")
notebook.set("e", "t-d")
notebook.set("e1", "d+tL")
notebook.set("SL2", "Cd05-r1")
notebook.set("tetha1", "(Ld05+t-d)/Rex")
notebook.set("n", 8)
notebook.set("n3", "7*n")
####################################################
##        End of NoteBook variables section       ##
####################################################
###
### SHAPER component
###

from salome.shaper import model

model.begin()
partSet = model.moduleDocument()

### Create Part
Part_1 = model.addPart(partSet)
Part_1_doc = Part_1.document()

model.end()

###
### SHAPERSTUDY component
###

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
Vertex_1 = geompy.MakeVertex(0.05, 0.25, 0)
Vertex_2 = geompy.MakeVertexWithRef(Vertex_1, 1.9, 0, 0)
Line_1 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_2)
Vertex_3 = geompy.MakeVertexWithRef(Vertex_2, 0, 0.2, 0)
Vertex_4 = geompy.MakeVertexWithRef(Vertex_2, -3, 0.2, 0)
Vertex_5 = geompy.MakeVertexWithRef(Vertex_2, -3, 0, 0)
Line_1_vertex_3 = geompy.GetSubShape(Line_1, [3])
Line_2 = geompy.MakeLineTwoPnt(Line_1_vertex_3, Vertex_3)
Line_3 = geompy.MakeLineTwoPnt(Vertex_3, Vertex_4)
Line_4 = geompy.MakeLineTwoPnt(Vertex_4, Vertex_5)
Line_1_vertex_2 = geompy.GetSubShape(Line_1, [2])
Line_5 = geompy.MakeLineTwoPnt(Vertex_5, Line_1_vertex_2)
Face_1 = geompy.MakeFaceWires([Line_1, Line_2, Line_3, Line_4, Line_5], 1)
Face_2 = geompy.MakeFaceHW(0.1, 0.5, 1)
Fuse_1 = geompy.MakeFuseList([Face_1, Face_2], True, True)
Fuse_1_vertex_14 = geompy.GetSubShape(Fuse_1, [14])
Fuse_1_edge_13 = geompy.GetSubShape(Fuse_1, [13])
Plane_1 = geompy.MakePlane(Fuse_1_vertex_14, Fuse_1_edge_13, 1)
Fuse_1_vertex_5 = geompy.GetSubShape(Fuse_1, [5])
Fuse_1_edge_4 = geompy.GetSubShape(Fuse_1, [4])
Plane_2 = geompy.MakePlane(Fuse_1_vertex_5, Fuse_1_edge_4, 1)
Plane_2_edge_8 = geompy.GetSubShape(Plane_2, [8])
Plane_3 = geompy.MakePlane(Fuse_1_vertex_5, Plane_2_edge_8, 1)
Partition_1 = geompy.MakePartition([Fuse_1], [Plane_1, Plane_2, Plane_3], [], [], geompy.ShapeType["SHELL"], 0, [], 0)
NoExtraEdges_1 = geompy.RemoveExtraEdges(Partition_1, False)
horz_esq = geompy.CreateGroup(NoExtraEdges_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(horz_esq, [28, 30])
horz_direita = geompy.CreateGroup(NoExtraEdges_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(horz_direita, [4, 9])
horz_central = geompy.CreateGroup(NoExtraEdges_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(horz_central, [14, 18])
vert_cima = geompy.CreateGroup(NoExtraEdges_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(vert_cima, [11, 32, 7, 16])
vert_baixo = geompy.CreateGroup(NoExtraEdges_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(vert_baixo, [25, 21])
[horz_esq, horz_direita, horz_central, vert_cima, vert_baixo] = geompy.GetExistingSubObjects(NoExtraEdges_1, False)
geompy.DifferenceIDs(horz_central, [14, 18])
geompy.UnionIDs(horz_central, [14, 18, 23])
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudyInFather( Line_1, Line_1_vertex_3, 'Line_1:vertex_3' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Line_3, 'Line_3' )
geompy.addToStudy( Line_4, 'Line_4' )
geompy.addToStudyInFather( Line_1, Line_1_vertex_2, 'Line_1:vertex_2' )
geompy.addToStudy( Line_5, 'Line_5' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Fuse_1, 'Fuse_1' )
geompy.addToStudyInFather( Fuse_1, Fuse_1_edge_13, 'Fuse_1:edge_13' )
geompy.addToStudyInFather( Fuse_1, Fuse_1_vertex_14, 'Fuse_1:vertex_14' )
geompy.addToStudy( Plane_1, 'Plane_1' )
geompy.addToStudyInFather( Fuse_1, Fuse_1_vertex_5, 'Fuse_1:vertex_5' )
geompy.addToStudyInFather( Fuse_1, Fuse_1_edge_4, 'Fuse_1:edge_4' )
geompy.addToStudy( Plane_2, 'Plane_2' )
geompy.addToStudyInFather( Plane_2, Plane_2_edge_8, 'Plane_2:edge_8' )
geompy.addToStudy( Plane_3, 'Plane_3' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudy( NoExtraEdges_1, 'NoExtraEdges_1' )
geompy.addToStudyInFather( NoExtraEdges_1, horz_esq, 'horz_esq' )
geompy.addToStudyInFather( NoExtraEdges_1, horz_direita, 'horz_direita' )
geompy.addToStudyInFather( NoExtraEdges_1, horz_central, 'horz_central' )
geompy.addToStudyInFather( NoExtraEdges_1, vert_cima, 'vert_cima' )
geompy.addToStudyInFather( NoExtraEdges_1, vert_baixo, 'vert_baixo' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Fuse_1,'Mesh_1')
Regular_1D = Mesh_1.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(15)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
isDone = Mesh_1.Compute()
Mesh_2 = smesh.Mesh(NoExtraEdges_1,'Mesh_2')
Regular_1D_1 = Mesh_2.Segment()
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(15)
Quadrangle_2D_1 = Mesh_2.Quadrangle(algo=smeshBuilder.QUADRANGLE)
horz_esq_1 = Mesh_2.GroupOnGeom(horz_esq,'horz_esq',SMESH.EDGE)
horz_direita_1 = Mesh_2.GroupOnGeom(horz_direita,'horz_direita',SMESH.EDGE)
horz_central_1 = Mesh_2.GroupOnGeom(horz_central,'horz_central',SMESH.EDGE)
vert_cima_1 = Mesh_2.GroupOnGeom(vert_cima,'vert_cima',SMESH.EDGE)
vert_baixo_1 = Mesh_2.GroupOnGeom(vert_baixo,'vert_baixo',SMESH.EDGE)
isDone = Mesh_2.Compute()
[ horz_esq_1, horz_direita_1, horz_central_1, vert_cima_1, vert_baixo_1 ] = Mesh_2.GetGroups()
Regular_1D_2 = Mesh_2.Segment(geom=vert_cima)
Number_of_Segments_3 = Regular_1D_2.NumberOfSegments(5)
isDone = Mesh_2.Compute()
[ horz_esq_1, horz_direita_1, horz_central_1, vert_cima_1, vert_baixo_1 ] = Mesh_2.GetGroups()
Number_of_Segments_4 = smesh.CreateHypothesis('NumberOfSegments')
Number_of_Segments_4.SetNumberOfSegments( 5 )
Regular_1D_3 = Mesh_2.Segment(geom=horz_central)
status = Mesh_2.AddHypothesis(Number_of_Segments_4,horz_central)
status = Mesh_2.RemoveHypothesis(Number_of_Segments_4,horz_central)
Number_of_Segments_5 = Regular_1D_3.NumberOfSegments(3)
isDone = Mesh_2.Compute()
[ horz_esq_1, horz_direita_1, horz_central_1, vert_cima_1, vert_baixo_1 ] = Mesh_2.GetGroups()
Sub_mesh_1 = Regular_1D_2.GetSubMesh()
Sub_mesh_2 = Regular_1D_3.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Mesh_2.GetMesh(), 'Mesh_2')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(horz_esq_1, 'horz_esq')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(horz_direita_1, 'horz_direita')
smesh.SetName(Number_of_Segments_5, 'Number of Segments_5')
smesh.SetName(horz_central_1, 'horz_central')
smesh.SetName(vert_cima_1, 'vert_cima')
smesh.SetName(vert_baixo_1, 'vert_baixo')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
