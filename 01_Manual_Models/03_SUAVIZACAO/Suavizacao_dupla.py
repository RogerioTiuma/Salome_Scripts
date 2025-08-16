import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/03_SUAVIZACAO')

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS

a = 80.
b = 120.
c = 160.
e = 40.

n = int(4)
nn = int(2)
nnn = int(1)

####################################################
##       Begin of NoteBook variables section      ##
####################################################
notebook.set("a", a)
notebook.set("b", b)
notebook.set("c", c)
notebook.set("e", e)
#notebook.set("n", n)
#notebook.set("nn", nn)
#notebook.set("nnn", nnn)

####################################################
##        End of NoteBook variables section       ##
####################################################
###
### GEOM component
###

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

import SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()

# Cria uma Malha
Mesh_1 = smesh.Mesh(Partition_1,'Malha_1')
Algo_1D = Mesh_1.Segment()

# Cria um algoritmo 2D para as faces
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hypo_2D_QUAD_TRIANG = Quadrangle_2D.QuadrangleParameters( smeshBuilder.QUAD_TRIANGLE_PREF )

# Cria um algoritmo 3D para o volume
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)

######################### ESPESSURA ##################
# 1D - Cria um algoritmo para a submalha de espessura
esp_1D = Mesh_1.Segment(geom=esp)
Hypo_1D_esp = esp_1D.NumberOfSegments(2)

######################## ÁREA 1 #####################
# 1D - Cria divisões n_1
n1_1D = Mesh_1.Segment(geom=n1)
Hypo_1D_n1 = n1_1D.NumberOfSegments( n )

######################## ÁREA 2 #####################
# 1D - Cria divisões n_2
n2_1D = Mesh_1.Segment(geom=n2)
Hypo_1D_n2 = n2_1D.NumberOfSegments( nn )

######################## ÁREA 3 #####################
# 1D - Cria divisões n_3
n3_1D =  Mesh_1.Segment(geom=n3)
Hypo_1D_n3 = n3_1D.NumberOfSegments( nnn )

# Computa a malha

esp = esp_1D.GetSubMesh()
N1 = n1_1D.GetSubMesh()
N2 = n2_1D.GetSubMesh()
N3 = n3_1D.GetSubMesh()

isDone = Mesh_1.SetMeshOrder([[N1, N2]])
isDone = Mesh_1.Compute()



## Set names of Mesh objects
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Algo_1D.GetAlgorithm(), 'Algo_1D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')

smesh.SetName(Quadrangle_2D, 'Quadrangle_2D')
smesh.SetName(Hypo_2D_QUAD_TRIANG, 'Hypo_2D_QUAD_TRIANG')

smesh.SetName(Hypo_1D_esp, 'Algo_1D_esp')
smesh.SetName(Hypo_1D_n1, 'Hypo_1D_N1')
smesh.SetName(Hypo_1D_n2, 'Hypo_1D_N2')
smesh.SetName(Hypo_1D_n3, 'Hypo_1D_N3')

smesh.SetName(esp, 'Sub_mesh_Esp')
smesh.SetName(N1, 'Sub_mesh_N1')
smesh.SetName(N2, 'Sub_mesh_N2')
smesh.SetName(N3, 'Sub_mesh_N3')

############################# MALHA 2 #############################
# Cria uma Malha
Mesh_2 = smesh.Mesh(Partition_1,'Malha_2')

Algo_1D_2 = Mesh_2.Segment()
#Hypo_1D_2 = Algo_1D_2.NumberOfSegments(8)

# Cria um algoritmo 2D para as faces
Quadrangle_2D_2 = Mesh_2.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Quadrangle_2D_2.QuadrangleParameters( smeshBuilder.QUAD_QUADRANGLE_PREF )
Quadrangle_2D_2.SetTriaVertex( -1 )
Quadrangle_2D_2.SetEnforcedNodes( [], [] )

# Cria um algoritmo 3D para o volume
Hexa_3D_2 = Mesh_2.Hexahedron(algo=smeshBuilder.Hexa)

######################### ESPESSURA ##################
# 1D - Cria um algoritmo para a submalha de espessura

esp_1D_2 = Mesh_2.Segment(geom=esp)
Hypo_1D_esp_2 = esp_1D_2.NumberOfSegments(4)

######################## ÁREA 1 #####################
# 1D - Cria divisões n_1
n1_1D_2 = Mesh_2.Segment(geom=n1)
# n1_1D_2.RemoveHypothesis()
Hypo_1D_n1_2 = n1_1D_2.NumberOfSegments( int(4*n) )

######################## ÁREA 2 #####################
# 1D - Cria divisões n_2
n2_1D_2 = Mesh_2.Segment(geom=n2)
#n2_1D_2.RemoveHypothesis()
Hypo_1D_n2_2 = n2_1D_2.NumberOfSegments( int(4*nn) )

######################## ÁREA 3 #####################
# 1D - Cria divisões n_3
n3_1D_2 =  Mesh_2.Segment(geom=n3)
#n3_1D_2.RemoveHypothesis()
Hypo_1D_n3_2 = n3_1D_2.NumberOfSegments( int(4*nnn) )

# Computa a malha

esp_2 = esp_1D_2.GetSubMesh()
N1_2 = n1_1D_2.GetSubMesh()
N2_2 = n2_1D_2.GetSubMesh()
N3_2 = n3_1D_2.GetSubMesh()

isDone = Mesh_2.SetMeshOrder([[N1_2, N2_2]])
isDone = Mesh_2.Compute()



## Set names of Mesh objects
smesh.SetName(Mesh_2.GetMesh(), 'Mesh_2')
smesh.SetName(Algo_1D_2.GetAlgorithm(), 'Algo_1D_2')
smesh.SetName(Quadrangle_2D_2.GetAlgorithm(), 'Quadrangle_2D_2')
smesh.SetName(Hexa_3D_2.GetAlgorithm(), 'Hexa_3D_2')

smesh.SetName(Quadrangle_2D_2, 'Quadrangle_2D_2')
#smesh.SetName(Hypo_2D_QUAD, 'Hypo_2D_QUAD')

smesh.SetName(Hypo_1D_esp_2, 'Algo_1D_esp_2')
smesh.SetName(Hypo_1D_n1_2, 'Hypo_1D_N1_2')
smesh.SetName(Hypo_1D_n2_2, 'Hypo_1D_N2_2')
smesh.SetName(Hypo_1D_n3_2, 'Hypo_1D_N3')

smesh.SetName(esp_2, 'Sub_mesh_Esp_2')
smesh.SetName(N1_2, 'Sub_mesh_N1_2')
smesh.SetName(N2_2, 'Sub_mesh_N2_2')
smesh.SetName(N3_2, 'Sub_mesh_N3_2')



if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
