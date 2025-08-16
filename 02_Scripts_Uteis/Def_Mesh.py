import salome
salome.salome_init()

from salome.geom import geomBuilder
from salome.smesh import smeshBuilder

# Iniciar o construtor de geometria
geom_builder = geomBuilder.New()

# Iniciar o construtor de malha
smesh_builder = smeshBuilder.New()

# Criar uma caixa
box = geom_builder.MakeBoxDXDYDZ(10., 10., 10.)
geom_builder.addToStudy(box, "Box")

# Criar uma malha hexagonal na caixa
hexa = smesh_builder.Mesh(box, "Box : hexahedral mesh")

# Criar um algoritmo 1D para as arestas
algo1D = hexa.Segment()

# Criar um algoritmo 2D para as faces
algo2D = hexa.Quadrangle()

# Criar um algoritmo 3D para os sólidos
algo3D = hexa.Hexahedron()

# Definir hipóteses
algo1D.Arithmetic1D(1, 4)

# Calcular a malha
if not hexa.Compute(): 
    raise Exception("Erro ao calcular a malha")

# Criar uma malha tetraédrica na caixa
tetra = smesh_builder.Mesh(box, "Box : tetrahedrical mesh")

# Criar um algoritmo 1D para as arestas
algo1D = tetra.Segment()

# Criar um algoritmo 2D para as faces
algo2D = tetra.Triangle()

# Criar um algoritmo 3D para os sólidos
algo3D = tetra.Tetrahedron()

# Definir hipóteses
algo1D.Arithmetic1D(1, 4)
algo2D.LengthFromEdges()

# Calcular a malha
if not tetra.Compute(): 
    raise Exception("Erro ao calcular a malha")

# Forçar a atualização do navegador de objetos
if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
