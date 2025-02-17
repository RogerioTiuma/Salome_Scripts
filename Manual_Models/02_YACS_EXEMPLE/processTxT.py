import os, sys, re
import pandas as pd

pathToRes = r"D:\00_MODELOS\GITHUB\Salome_Scripts\Manual_Models\02_YACS_EXEMPLE\plate-res.txt"  
pathToCsv = r"D:\00_MODELOS\GITHUB\Salome_Scripts\Manual_Models\02_YACS_EXEMPLE\mydata2.csv"

myfile = open(pathToRes, 'r')
content = myfile.read()

dispRegex = re.compile(r'LA VALEUR (MAX|MIN)IMALE DE (DX|DY|DZ) {2,}EST {1,}(-?\d.\d{14}E-?\+?\d\d) ')
mo = dispRegex.findall(content)

print(mo)

mydata = pd.DataFrame(mo, columns=["MIN/MAX", "Component", "Value"])

mydata.to_csv(pathToCsv, index=False)
