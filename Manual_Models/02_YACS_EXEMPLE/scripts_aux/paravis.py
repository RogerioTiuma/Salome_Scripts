#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE')

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
O = O
OX = OX
OY = OY
OZ = OZ
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(__NOT__Published__Object__,'Mesh_1')
Regular_1D = Mesh_1.Segment()
Local_Length_1 = Regular_1D.LocalLength(4,None,1e-07)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE)
Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa)
volume = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'volume',SMESH.VOLUME)
zmax = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'zmax',SMESH.FACE)
zmin = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'zmin',SMESH.FACE)
xmax = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'xmax',SMESH.FACE)
xmin = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'xmin',SMESH.FACE)
ymin = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'ymin',SMESH.FACE)
ymax = Mesh_1.GroupOnGeom(__NOT__Published__Object__,'ymax',SMESH.FACE)
isDone = Mesh_1.Compute()
[ volume, zmax, zmin, xmax, xmin, ymin, ymax ] = Mesh_1.GetGroups()
smesh.SetName(Mesh_1, 'Mesh_1')
try:
  Mesh_1.ExportMED( r'D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/Plate.med', 0, 41, 1, Mesh_1, 1, [], '',-1, 1 )
  pass
except:
  print('ExportPartToMED() failed. Invalid file name?')


## Set names of Mesh objects
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
smesh.SetName(zmax, 'zmax')
smesh.SetName(xmax, 'xmax')
smesh.SetName(volume, 'volume')
smesh.SetName(zmin, 'zmin')
smesh.SetName(ymin, 'ymin')
smesh.SetName(xmin, 'xmin')
smesh.SetName(ymax, 'ymax')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Local_Length_1, 'Local Length_1')

###
### YACS component
###

###
### PARAVIS component
###

import pvsimple
pvsimple.ShowParaviewView()
# trace generated using paraview version 5.11.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 11

#### import the simple module from the paraview
from pvsimple import *
#### disable automatic camera reset on 'Show'
pvsimple._DisableFirstRenderCameraReset()

# create a new 'MED Reader'
plateresrmed = MEDReader(registrationName='plate-res.rmed', FileNames=['D:\\00_MODELOS\\GITHUB\\Salome_Scripts\\Manual_Models\\02_YACS_EXEMPLE\\plate-res.rmed'])

# Properties modified on plateresrmed
plateresrmed.FieldsStatus = ['TS0/00000001/ComSup0/reslin__DEPL@@][@@P1', 'TS0/00000001/ComSup0/reslin__SIEF_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELNO@@][@@GSSNE', 'TS0/00000001/ComSup0/reslin__SIEQ_NOEU@@][@@P1']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
plateresrmedDisplay = Show(plateresrmed, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
plateresrmedDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

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

# rescale color and/or opacity maps used to exactly fit the current data range
plateresrmedDisplay.RescaleTransferFunctionToDataRange(False, True)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1508, 652)

# current camera placement for renderView1
renderView1.CameraPosition = [250.00000000000003, 250.00000000000003, 1135.1091713071664]
renderView1.CameraFocalPoint = [250.00000000000003, 250.00000000000003, 6.0]
renderView1.CameraParallelScale = 353.6042986164054

# save screenshot
SaveScreenshot('D:\00_MODELOS\GITHUB\Salome_Scripts\Manual_Models\02_YACS_EXEMPLE\DELP2.png', renderView1, ImageResolution=[1508, 652])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [250.00000000000003, 250.00000000000003, 1135.1091713071664]
renderView1.CameraFocalPoint = [250.00000000000003, 250.00000000000003, 6.0]
renderView1.CameraParallelScale = 353.6042986164054

###
### ASTERSTUDY component
###


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
