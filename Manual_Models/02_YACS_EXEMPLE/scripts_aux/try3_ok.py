#!/usr/bin/env python

import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
plateresrmed = MEDReader(registrationName='plate-res.rmed', FileNames=['D:\\00_MODELOS\\GITHUB\\Salome_Scripts\\Manual_Models\\02_YACS_EXEMPLE\\plate-res.rmed'])

# Properties modified on plateresrmed
plateresrmed.FieldsStatus = ['TS0/00000001/ComSup0/reslin__DEPL@@][@@P1', 'TS0/00000001/ComSup0/reslin__SIEF_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELNO@@][@@GSSNE', 'TS0/00000001/ComSup0/reslin__SIEQ_NOEU@@][@@P1']

# get active source.
plateresrmed = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
plateresrmedDisplay = GetDisplayProperties(plateresrmed, view=renderView1)

# reset view to fit data
renderView1.ResetCamera(False)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(plateresrmed)

# set scalar coloring
ColorBy(plateresrmedDisplay, ('POINTS', 'reslin__SIEQ_NOEU', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
plateresrmedDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
plateresrmedDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEULUT = GetColorTransferFunction('reslin__SIEQ_NOEU')

# get opacity transfer function/opacity map for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEUPWF = GetOpacityTransferFunction('reslin__SIEQ_NOEU')

# get 2D transfer function for 'reslin__SIEQ_NOEU'
reslin__SIEQ_NOEUTF2D = GetTransferFunction2D('reslin__SIEQ_NOEU')

# get layout
# layout = GetLayout()

# layout/tab size in pixels
#layout.SetSize(1508, 649)

# current camera placement for renderView1
renderView1.CameraPosition = [-838.2954601598269, 510.0627204941391, 789.9280527608555]
renderView1.CameraFocalPoint = [250.0, 250.0, 6.0]
renderView1.CameraViewUp = [0.5908781622391416, 0.04448910644042894, 0.80553318789298]
renderView1.CameraParallelScale = 353.6042986164054

UpdatePipeline(time=0.0, proxy=plateresrmed)
Render()
Show(plateresrmed)

# save screenshot
SaveScreenshot('D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/stress1.png', renderView1, ImageResolution=[1508, 649])

# change representation type
plateresrmedDisplay.SetRepresentationType('Surface With Edges')

# layout/tab size in pixels
# layout1.SetSize(1508, 649)

# current camera placement for renderView1
renderView1.CameraPosition = [-838.2954601598269, 510.0627204941391, 789.9280527608555]
renderView1.CameraFocalPoint = [250.0, 250.0, 6.0]
renderView1.CameraViewUp = [0.5908781622391416, 0.04448910644042894, 0.80553318789298]
renderView1.CameraParallelScale = 353.6042986164054

# save screenshot
SaveScreenshot('D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/stress2.png', renderView1, ImageResolution=[1508, 649])

# set scalar coloring
ColorBy(plateresrmedDisplay, ('POINTS', 'reslin__DEPL', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(reslin__SIEQ_NOEULUT, renderView1)

# rescale color and/or opacity maps used to include current data range
plateresrmedDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
plateresrmedDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'reslin__DEPL'
reslin__DEPLLUT = GetColorTransferFunction('reslin__DEPL')

# get opacity transfer function/opacity map for 'reslin__DEPL'
reslin__DEPLPWF = GetOpacityTransferFunction('reslin__DEPL')

# get 2D transfer function for 'reslin__DEPL'
reslin__DEPLTF2D = GetTransferFunction2D('reslin__DEPL')

# layout/tab size in pixels
# layout1.SetSize(1508, 649)

# current camera placement for renderView1
renderView1.CameraPosition = [-838.2954601598269, 510.0627204941391, 789.9280527608555]
renderView1.CameraFocalPoint = [250.0, 250.0, 6.0]
renderView1.CameraViewUp = [0.5908781622391416, 0.04448910644042894, 0.80553318789298]
renderView1.CameraParallelScale = 353.6042986164054

# save screenshot
SaveScreenshot('D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/DEPL1.png', renderView1, ImageResolution=[1508, 649])

# change representation type
plateresrmedDisplay.SetRepresentationType('Surface')

# layout/tab size in pixels
# layout1.SetSize(1508, 649)

# current camera placement for renderView1
renderView1.CameraPosition = [-838.2954601598269, 510.0627204941391, 789.9280527608555]
renderView1.CameraFocalPoint = [250.0, 250.0, 6.0]
renderView1.CameraViewUp = [0.5908781622391416, 0.04448910644042894, 0.80553318789298]
renderView1.CameraParallelScale = 353.6042986164054

# save screenshot
SaveScreenshot('D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/DEPL2.png', renderView1, ImageResolution=[1508, 649])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-838.2954601598269, 510.0627204941391, 789.9280527608555]
renderView1.CameraFocalPoint = [250.0, 250.0, 6.0]
renderView1.CameraViewUp = [0.5908781622391416, 0.04448910644042894, 0.80553318789298]
renderView1.CameraParallelScale = 353.6042986164054
