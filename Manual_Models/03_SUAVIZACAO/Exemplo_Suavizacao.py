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


############ VARIAVEIS #############
C1 = 100.
L1 = 200.

C2 = 75.
L2 = 150.

C3 = 50.
L3 = 100.

e = 10.


####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("a", 12)
notebook.set("b", 25)
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

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )



################ CRIANDO BOX PARA SIMETRIA ######################
Box_1 = geompy.MakeBoxDXDYDZ(C1, L1, e)
Box_2 = geompy.MakeBoxDXDYDZ(C2, L2, e)
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Box_2, 'Box_2' )


######################## MODELO 1 - MODELO COM DIAGONAL NA PONTA ################################
################ GERANDO PARTIÇÕES ##############################
md1 = geompy.MakePartition([Box_1], [Box_2], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
geompy.addToStudy( md1, 'Partition_1' )


############### GERANDO DIAGONAL ##################################
Partition_1_vertex_20 = geompy.GetSubShape(md1, [20])
Partition_1_vertex_48 = geompy.GetSubShape(md1, [48])
Line_1 = geompy.MakeLineTwoPnt(Partition_1_vertex_20, Partition_1_vertex_48)

geompy.addToStudyInFather( md1, Partition_1_vertex_20, 'Partition_1:vertex_20' )
geompy.addToStudyInFather( md1, Partition_1_vertex_48, 'Partition_1:vertex_48' )
geompy.addToStudy( Line_1, 'Line_1' )

Partition_1_vertex_22 = geompy.GetSubShape(md1, [22])
Partition_1_vertex_55 = geompy.GetSubShape(md1, [55])
Line_2 = geompy.MakeLineTwoPnt(Partition_1_vertex_22, Partition_1_vertex_55)

geompy.addToStudyInFather( md1, Partition_1_vertex_22, 'Partition_1:vertex_22' )
geompy.addToStudyInFather( md1, Partition_1_vertex_55, 'Partition_1:vertex_55' )
geompy.addToStudy( Line_2, 'Line_2' )

Quadrangle_Face_1 = geompy.MakeQuad2Edges(Line_1, Line_2)
geompy.addToStudy( Quadrangle_Face_1, 'Quadrangle Face_1' )

Modelo_1_Diag = geompy.MakePartition([md1], [Quadrangle_Face_1], [], [], geompy.ShapeType["SOLID"], 0, [], 0)
geompy.addToStudy( Modelo_1_Diag, 'Modelo_1_Diag' )



############### GERANDO GRUPOS #####################################
############### GRUPO DE FACES
Suavizacao = geompy.CreateGroup(Modelo_1_Diag, geompy.ShapeType["FACE"])
geompy.UnionIDs(Suavizacao, [69, 45, 55, 72])

Refinado = geompy.CreateGroup(Modelo_1_Diag, geompy.ShapeType["FACE"])
geompy.UnionIDs(Refinado, [34, 32])

geompy.addToStudyInFather( Modelo_1_Diag, Suavizacao, 'Suavizacao' )
geompy.addToStudyInFather( Modelo_1_Diag, Refinado, 'Refinado' )

############### GRUPO DE LINHAS 
lin_1 = geompy.CreateGroup(Modelo_1_Diag, geompy.ShapeType["EDGE"])
geompy.UnionIDs(lin_1, [49, 64, 44, 57, 40, 68])
geompy.addToStudyInFather( Modelo_1_Diag, lin_1, 'lin_1' )

[Suavizacao, Refinado, lin_1] = geompy.GetExistingSubObjects(Modelo_1_Diag, False)


##################################### MODELO 2 - COM QUADRADO NA PONTA ###############################################
################# GERANDO PARTIÇÃO DOS PLANOS #####################
Partition_1_edge_19 = geompy.GetSubShape(md1, [19])
Plane_1 = geompy.MakePlane(Partition_1_vertex_20, Partition_1_edge_19, 2000)

Partition_1_vertex_17 = geompy.GetSubShape(md1, [17])
Partition_1_edge_51 = geompy.GetSubShape(md1, [51])
Plane_2 = geompy.MakePlane(Partition_1_vertex_17, Partition_1_edge_51, 2000)

geompy.addToStudyInFather( md1, Partition_1_edge_19, 'Partition_1:edge_19' )
geompy.addToStudy( Plane_1, 'Plane_1' )
geompy.addToStudyInFather( md1, Partition_1_edge_51, 'Partition_1:edge_51' )
geompy.addToStudyInFather( md1, Partition_1_vertex_17, 'Partition_1:vertex_17' )
geompy.addToStudy( Plane_2, 'Plane_2' )

md2 = geompy.MakePartition([md1], [Plane_1, Plane_2], [], [], geompy.ShapeType["SOLID"], 0, [], 0)

geompy.addToStudy( md2, 'md2' )

################################### GERANDO GRUPOS DE FACES ##############################

md2_Refinado = geompy.CreateGroup(md2, geompy.ShapeType["FACE"])
geompy.UnionIDs(md2_Refinado, [34, 32])

md2_Suavizacao = geompy.CreateGroup(md2, geompy.ShapeType["FACE"])
geompy.UnionIDs(md2_Suavizacao, [79, 55, 96, 86, 45, 69])

[md2_Refinado, md2_Suavizacao] = geompy.GetExistingSubObjects(md2, False)

linhas1 = geompy.CreateGroup(md2, geompy.ShapeType["EDGE"])
geompy.UnionIDs(linhas1, [68, 57, 98, 44, 78, 49, 71, 88, 40, 95, 90, 64])
[n20, n10, linhas1] = geompy.GetExistingSubObjects(md2, False)

geompy.addToStudyInFather( md2, n20, 'n20' )
geompy.addToStudyInFather( md2, n10, 'n10' )
geompy.addToStudyInFather( md2, linhas1, 'linhas1' )


"""###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

n_e = 4
n_ref = 10
n_suav = 5

Reducao_diag = smesh.Mesh(Modelo_1_Diag,'Modelo_1_Diag')
Regular_1D = Reducao_diag.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(n_ref)
Quadrangle_2D = Reducao_diag.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Quadrangle_2D.SetQuadType( smeshBuilder.QUAD_TRIANGLE_PREF )

Hexa_3D = Reducao_diag.Hexahedron(algo=smeshBuilder.Hexa)
Suavizacao = Reducao_diag.GroupOnGeom(Suavizacao,'Suavizacao',SMESH.FACE)
Refinado = Reducao_diag.GroupOnGeom(Refinado,'Refinado',SMESH.FACE)
lin_1 = Reducao_diag.GroupOnGeom(lin_1,'Refinado',SMESH.FACE)

[Suavizacao, Refinado, lin_1] = Reducao_diag.GetGroups()
Regular_1D_9 = Reducao_diag.Segment(geom=Suavizacao)
Number_of_Segments_10 = Regular_1D_9.NumberOfSegments(n_suav)
Quadrangle_2D_8 = Reducao_diag.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=Suavizacao)
Sub_mesh_6 = Regular_1D_9.GetSubMesh()

isDone = Reducao_diag.Compute()"""



import SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()

n_e = 4
n_ref = 8
n_suav = 4

Reducao_diag = smesh.Mesh(Modelo_1_Diag, 'Modelo_1_Diag')

# 1D Mesh
Regular_1D = Reducao_diag.Segment()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(n_suav)

# 2D Mesh
Quadrangle_2D = Reducao_diag.Quadrangle(smeshBuilder.QUADRANGLE)
Quadrangle_2D.QuadranglePreference(smeshBuilder.QUAD_QUADRANGLE_PREF,-1,[],[])

# 3D Mesh
Hexa_3D = Reducao_diag.Hexahedron(algo=smeshBuilder.Hexa)

# Groups
Suavizacao = Reducao_diag.GroupOnGeom(Suavizacao, 'Suavizacao', SMESH.FACE)
Refinado = Reducao_diag.GroupOnGeom(Refinado, 'Refinado', SMESH.FACE)
lin_1 = Reducao_diag.GroupOnGeom(lin_1, 'Refinado', SMESH.FACE)

# Aplicando hipótese de suavização
Regular_1D_9 = Reducao_diag.Segment(Refinado.GetShape())
Number_of_Segments_10 = Regular_1D_9.NumberOfSegments(n_ref)
Quadrangle_2D_8 = Reducao_diag.Quadrangle(algo=smeshBuilder.QUADRANGLE, geom=Refinado.GetShape())

# Obtenção do submalha
Sub_mesh_6 = Reducao_diag.GetSubMesh(Refinado.GetShape(),'Suavizacao' )

# Computar malha
isDone = Reducao_diag.Compute()
 



if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
