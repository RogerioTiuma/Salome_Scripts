#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/Lenovo/00_MODELOS/00_TREINO_SOFTWARE/00_CURSO_WIKKI/01_CURSO_SALOME/SALOME_SCRIPTS')

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
Vertex_1 = geompy.MakeVertex(0, 0, 0)
Vertex_2 = geompy.MakeVertex(0, 0, 80)
Translation_1 = geompy.MakeTranslation(Vertex_1, 0, 0, 80)
Translation_2 = geompy.MakeTranslation(Vertex_1, 0, 80, 80)
Translation_3 = geompy.MakeTranslation(Vertex_1, 0, 100, 60)
Translation_4 = geompy.MakeTranslation(Vertex_1, 0, 100, 20)
Translation_5 = geompy.MakeTranslation(Vertex_1, 0, 80, 0)
Translation_6 = geompy.MakeTranslation(O, 0, 20, 60)
Line_1 = geompy.MakeLineTwoPnt(O, Translation_1)
Line_2 = geompy.MakeLineTwoPnt(Translation_1, Translation_2)
Line_3 = geompy.MakeLineTwoPnt(Translation_2, Translation_3)
Line_4 = geompy.MakeLineTwoPnt(Translation_3, Translation_4)
Line_1_vertex_2 = geompy.GetSubShape(Line_1, [2])
Line_5 = geompy.MakeLineTwoPnt(Line_1_vertex_2, Translation_5)
Circle_1 = geompy.MakeCircle(Translation_6, OX, 10)
Translation_7 = geompy.MakeTranslation(O, 0, 80, 20)
Line_4_vertex_3 = geompy.GetSubShape(Line_4, [3])
Line_5_vertex_3 = geompy.GetSubShape(Line_5, [3])
Arc_1 = geompy.MakeArcCenter(Translation_7, Line_4_vertex_3, Line_5_vertex_3,False)
Wire_1 = geompy.MakeWire([Line_1, Line_2, Line_3, Line_4, Line_5, Arc_1], 1e-07)
Face_1 = geompy.MakeFaceWires([Circle_1, Wire_1], 1)
Face_2 = geompy.MakeFaceHW(100, 100, 2)
geompy.TranslateDXDYDZ(Face_2, 0, 50, 50)
Fillet_2D_1 = geompy.MakeFillet2D(Face_2, 20, [4])
Fillet_2D_1_vertex_11 = geompy.GetSubShape(Fillet_2D_1, [11])
Circle_2 = geompy.MakeCircle(Fillet_2D_1_vertex_11, OX, 10)
Translation_8 = geompy.MakeTranslation(Circle_2, 0, 20, -20)
Face_3 = geompy.MakeFaceWires([Translation_8], 1)
Cut_1 = geompy.MakeCutList(Fillet_2D_1, [Face_3], True)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Translation_2, 'Translation_2' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Translation_4, 'Translation_4' )
geompy.addToStudy( Translation_3, 'Translation_3' )
geompy.addToStudy( Translation_5, 'Translation_5' )
geompy.addToStudy( Translation_6, 'Translation_6' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Line_3, 'Line_3' )
geompy.addToStudy( Line_4, 'Line_4' )
geompy.addToStudyInFather( Line_1, Line_1_vertex_2, 'Line_1:vertex_2' )
geompy.addToStudy( Line_5, 'Line_5' )
geompy.addToStudy( Circle_1, 'Circle_1' )
geompy.addToStudyInFather( Line_4, Line_4_vertex_3, 'Line_4:vertex_3' )
geompy.addToStudy( Translation_7, 'Translation_7' )
geompy.addToStudyInFather( Line_5, Line_5_vertex_3, 'Line_5:vertex_3' )
geompy.addToStudy( Arc_1, 'Arc_1' )
geompy.addToStudy( Wire_1, 'Wire_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Fillet_2D_1, 'Fillet 2D_1' )
geompy.addToStudyInFather( Fillet_2D_1, Fillet_2D_1_vertex_11, 'Fillet 2D_1:vertex_11' )
geompy.addToStudy( Circle_2, 'Circle_2' )
geompy.addToStudy( Translation_8, 'Translation_8' )
geompy.addToStudy( Face_3, 'Face_3' )
geompy.addToStudy( Cut_1, 'Cut_1' )

### Folders and it's content
Exemplo_1 = geompy.NewFolder('Exemplo_1')
geompy.PutToFolder(Vertex_1, Exemplo_1)
geompy.PutToFolder(Vertex_2, Exemplo_1)
geompy.PutToFolder(Translation_1, Exemplo_1)
geompy.PutToFolder(Translation_2, Exemplo_1)
geompy.PutToFolder(Translation_3, Exemplo_1)
geompy.PutToFolder(Translation_4, Exemplo_1)
geompy.PutToFolder(Translation_5, Exemplo_1)
geompy.PutToFolder(Translation_6, Exemplo_1)
geompy.PutToFolder(Line_1, Exemplo_1)
geompy.PutToFolder(Line_2, Exemplo_1)
geompy.PutToFolder(Line_3, Exemplo_1)
geompy.PutToFolder(Line_4, Exemplo_1)
geompy.PutToFolder(Line_5, Exemplo_1)
geompy.PutToFolder(Circle_1, Exemplo_1)
geompy.PutToFolder(Translation_7, Exemplo_1)
geompy.PutToFolder(Arc_1, Exemplo_1)
geompy.PutToFolder(Wire_1, Exemplo_1)
geompy.PutToFolder(Face_1, Exemplo_1)
Exemplo_2 = geompy.NewFolder('Exemplo_2')
geompy.PutToFolder(Face_2, Exemplo_2)
geompy.PutToFolder(Fillet_2D_1, Exemplo_2)
geompy.PutToFolder(Circle_2, Exemplo_2)
geompy.PutToFolder(Translation_8, Exemplo_2)
geompy.PutToFolder(Face_3, Exemplo_2)
geompy.PutToFolder(Cut_1, Exemplo_2)


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
