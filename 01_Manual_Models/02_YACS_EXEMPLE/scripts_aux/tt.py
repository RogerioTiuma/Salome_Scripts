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
plateresrmed.FieldsStatus = ['TS0/00000001/ComSup0/reslin__SIEF_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELNO@@][@@GSSNE', 'TS0/00000001/ComSup0/reslin__DEPL@@][@@P1', 'TS0/00000001/ComSup0/reslin__SIEQ_NOEU@@][@@P1']
plateresrmed.VectorsProperty = 0
plateresrmed.TimeModeProperty = 0
plateresrmed.TimesFlagsStatus = ['0000']
plateresrmed.GhostCellGeneratorCallForPara = 1

# Properties modified on plateresrmed
plateresrmed.FieldsStatus = ['TS0/00000001/ComSup0/reslin__DEPL@@][@@P1', 'TS0/00000001/ComSup0/reslin__SIEF_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELGA@@][@@GAUSS', 'TS0/00000001/ComSup0/reslin__SIEQ_ELNO@@][@@GSSNE', 'TS0/00000001/ComSup0/reslin__SIEQ_NOEU@@][@@P1']

UpdatePipeline(time=0.0, proxy=plateresrmed)
Render()
Show(plateresrmed)
SaveScreenshot('D:/00_MODELOS/GITHUB/Salome_Scripts/Manual_Models/02_YACS_EXEMPLE/picture.png')