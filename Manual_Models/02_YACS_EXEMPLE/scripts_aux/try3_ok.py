#!/usr/bin/env python

import sys
sys.path.append("D:/SALOME-9.10.0/W64/ParaView/bin/Lib/site-packages")
import paraview.simple as pvs

# Desativar reset automático da câmera
pvs._DisableFirstRenderCameraReset()

# Caminho do arquivo MED
med_file_path = "D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/plate-res.rmed"

# Criar um novo leitor MED
plateresrmed = pvs.MEDReader(registrationName='plate-res.rmed', FileNames=[med_file_path])

# Definir campos a serem lidos
plateresrmed.FieldsStatus = [
    'TS0/00000001/ComSup0/reslin__DEPL@@][@@P1',
    'TS0/00000001/ComSup0/reslin__SIEF_ELGA@@][@@GAUSS',
    'TS0/00000001/ComSup0/reslin__SIEQ_ELGA@@][@@GAUSS',
    'TS0/00000001/ComSup0/reslin__SIEQ_ELNO@@][@@GSSNE',
    'TS0/00000001/ComSup0/reslin__SIEQ_NOEU@@][@@P1'
]

# Limpar as visualizações anteriores, se existirem
def cleanup():
    for view in pvs.GetViews():
        pvs.Delete(view)
        
cleanup()  # Chama a função para garantir que as visualizações anteriores sejam removidas

# Criar visualização
renderView1 = pvs.CreateView('RenderView')
plateresrmedDisplay = pvs.Show(plateresrmed, renderView1)

# Criar segunda visualização
renderView2 = pvs.CreateView('RenderView')
plateresrmedDisplay2 = pvs.Show(plateresrmed, renderView2)

# Ajustar visualização
renderView1.ResetCamera(False)
renderView1.Update()

# Definir coloração inicial para SIEQ_NOEU (stress)
pvs.ColorBy(plateresrmedDisplay, ('POINTS', 'reslin__SIEQ_NOEU', 'Magnitude'))
plateresrmedDisplay.RescaleTransferFunctionToDataRange(True, False)
plateresrmedDisplay.SetScalarBarVisibility(renderView1, True)

# Configurar barra de cores para SIEQ_NOEU
scalarBar = pvs.GetScalarBar(plateresrmedDisplay.LookupTable, renderView1)
scalarBar.TitleFontSize = 10
scalarBar.LabelFontSize = 8

# Definir posição da câmera
renderView1.CameraPosition = [-838.295, 510.063, 789.928]
renderView1.CameraFocalPoint = [250.0, 250.0, 6.0]
renderView1.CameraViewUp = [0.5909, 0.0445, 0.8055]
renderView1.CameraParallelScale = 353.604

# Salvar captura de tela para stress
screenshot_path = "D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/stress1.png"
pvs.SaveScreenshot(screenshot_path, renderView1, ImageResolution=[1508, 649])

# Alterar representação e salvar nova imagem
plateresrmedDisplay.SetRepresentationType('Surface With Edges')
screenshot_path2 = "D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/stress2.png"
pvs.SaveScreenshot(screenshot_path2, renderView1, ImageResolution=[1508, 649])

# Ocultar barra de cores SIEQ_NOEU antes de imagens DEPL
pvs.HideScalarBarIfNotNeeded(plateresrmedDisplay.LookupTable, renderView1)

##############################################################################################

# Alterar coloração para DEPL
pvs.ColorBy(plateresrmedDisplay2, ('POINTS', 'reslin__DEPL', 'Magnitude'))
plateresrmedDisplay2.RescaleTransferFunctionToDataRange(True, False)
plateresrmedDisplay2.SetScalarBarVisibility(renderView2, True)  # Exibir a barra de cores correta para DEPL

# Configurar barra de cores para DEPL
scalarBar2 = pvs.GetScalarBar(plateresrmedDisplay2.LookupTable, renderView2)
scalarBar2.TitleFontSize = 10
scalarBar2.LabelFontSize = 8

# Definir posição da câmera
renderView2.CameraPosition = [-838.295, 510.063, 789.928]
renderView2.CameraFocalPoint = [250.0, 250.0, 6.0]
renderView2.CameraViewUp = [0.5909, 0.0445, 0.8055]
renderView2.CameraParallelScale = 353.604

# Salvar capturas de tela para deslocamento (DEPL)
screenshot_path3 = "D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/DEPL1.png"
pvs.SaveScreenshot(screenshot_path3, renderView2, ImageResolution=[1508, 649])

plateresrmedDisplay2.SetRepresentationType('Surface With Edges')
screenshot_path4 = "D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/DEPL2.png"
pvs.SaveScreenshot(screenshot_path4, renderView2, ImageResolution=[1508, 649])

# Atualizar pipeline
pvs.UpdatePipeline(time=0.0, proxy=plateresrmed)
pvs.Render()
