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

### Create Point
Point_2 = model.addPoint(Part_1_doc, 1, 0, 0)

### Create Point
Point_3 = model.addPoint(Part_1_doc, 0.999829, 2.5e-05, 0)

### Create Point
Point_4 = model.addPoint(Part_1_doc, 0.999315, 9.899999999999999e-05, 0)

### Create Point
Point_5 = model.addPoint(Part_1_doc, 0.998459, 0.000224, 0)

### Create Point
Point_6 = model.addPoint(Part_1_doc, 0.997261, 0.000397, 0)

### Create Point
Point_7 = model.addPoint(Part_1_doc, 0.995722, 0.00062, 0)

### Create Point
Point_8 = model.addPoint(Part_1_doc, 0.9938439999999999, 0.000891, 0)

### Create Point
Point_9 = model.addPoint(Part_1_doc, 0.991627, 0.00121, 0)

### Create Point
Point_10 = model.addPoint(Part_1_doc, 0.989074, 0.001577, 0)

### Create Point
Point_11 = model.addPoint(Part_1_doc, 0.986185, 0.00199, 0)

### Create Point
Point_12 = model.addPoint(Part_1_doc, 0.982963, 0.002449, 0)

### Create Point
Point_13 = model.addPoint(Part_1_doc, 0.97941, 0.002953, 0)

### Create Point
Point_14 = model.addPoint(Part_1_doc, 0.975528, 0.003501, 0)

### Create Point
Point_15 = model.addPoint(Part_1_doc, 0.971321, 0.004092, 0)

### Create Point
Point_16 = model.addPoint(Part_1_doc, 0.96679, 0.004725, 0)

### Create Point
Point_17 = model.addPoint(Part_1_doc, 0.96194, 0.005399, 0)

### Create Point
Point_18 = model.addPoint(Part_1_doc, 0.956773, 0.006112, 0)

### Create Point
Point_19 = model.addPoint(Part_1_doc, 0.9512930000000001, 0.006863, 0)

### Create Point
Point_20 = model.addPoint(Part_1_doc, 0.945503, 0.007651, 0)

### Create Point
Point_21 = model.addPoint(Part_1_doc, 0.939409, 0.008474000000000001, 0)

### Create Point
Point_22 = model.addPoint(Part_1_doc, 0.933013, 0.009332, 0)

### Create Point
Point_23 = model.addPoint(Part_1_doc, 0.92632, 0.010221, 0)

### Create Point
Point_24 = model.addPoint(Part_1_doc, 0.919335, 0.011142, 0)

### Create Point
Point_25 = model.addPoint(Part_1_doc, 0.912063, 0.012093, 0)

### Create Point
Point_26 = model.addPoint(Part_1_doc, 0.904508, 0.013071, 0)

### Create Point
Point_27 = model.addPoint(Part_1_doc, 0.8966769999999999, 0.014076, 0)

### Create Point
Point_28 = model.addPoint(Part_1_doc, 0.8885729999999999, 0.015105, 0)

### Create Point
Point_29 = model.addPoint(Part_1_doc, 0.880203, 0.016158, 0)

### Create Point
Point_30 = model.addPoint(Part_1_doc, 0.871572, 0.017232, 0)

### Create Point
Point_31 = model.addPoint(Part_1_doc, 0.862687, 0.018326, 0)

### Create Point
Point_32 = model.addPoint(Part_1_doc, 0.853553, 0.019438, 0)

### Create Point
Point_33 = model.addPoint(Part_1_doc, 0.844177, 0.020568, 0)

### Create Point
Point_34 = model.addPoint(Part_1_doc, 0.834565, 0.021712, 0)

### Create Point
Point_35 = model.addPoint(Part_1_doc, 0.824724, 0.022869, 0)

### Create Point
Point_36 = model.addPoint(Part_1_doc, 0.8146600000000001, 0.024038, 0)

### Create Point
Point_37 = model.addPoint(Part_1_doc, 0.804381, 0.025217, 0)

### Create Point
Point_38 = model.addPoint(Part_1_doc, 0.793893, 0.026405, 0)

### Create Point
Point_39 = model.addPoint(Part_1_doc, 0.783203, 0.027599, 0)

### Create Point
Point_40 = model.addPoint(Part_1_doc, 0.77232, 0.028798, 0)

### Create Point
Point_41 = model.addPoint(Part_1_doc, 0.761249, 0.03, 0)

### Create Point
Point_42 = model.addPoint(Part_1_doc, 0.75, 0.031204, 0)

### Create Point
Point_43 = model.addPoint(Part_1_doc, 0.738579, 0.032408, 0)

### Create Point
Point_44 = model.addPoint(Part_1_doc, 0.7269949999999999, 0.03361, 0)

### Create Point
Point_45 = model.addPoint(Part_1_doc, 0.715256, 0.034809, 0)

### Create Point
Point_46 = model.addPoint(Part_1_doc, 0.703368, 0.036002, 0)

### Create Point
Point_47 = model.addPoint(Part_1_doc, 0.691342, 0.037188, 0)

### Create Point
Point_48 = model.addPoint(Part_1_doc, 0.679184, 0.038366, 0)

### Create Point
Point_49 = model.addPoint(Part_1_doc, 0.666903, 0.039532, 0)

### Create Point
Point_50 = model.addPoint(Part_1_doc, 0.654508, 0.040686, 0)

### Create Point
Point_51 = model.addPoint(Part_1_doc, 0.642008, 0.041826, 0)

### Create Point
Point_52 = model.addPoint(Part_1_doc, 0.62941, 0.042949, 0)

### Create Point
Point_53 = model.addPoint(Part_1_doc, 0.616723, 0.044055, 0)

### Create Point
Point_54 = model.addPoint(Part_1_doc, 0.603956, 0.04514, 0)

### Create Point
Point_55 = model.addPoint(Part_1_doc, 0.591118, 0.046203, 0)

### Create Point
Point_56 = model.addPoint(Part_1_doc, 0.578217, 0.047242, 0)

### Create Point
Point_57 = model.addPoint(Part_1_doc, 0.565263, 0.048255, 0)

### Create Point
Point_58 = model.addPoint(Part_1_doc, 0.552264, 0.049241, 0)

### Create Point
Point_59 = model.addPoint(Part_1_doc, 0.53923, 0.050196, 0)

### Create Point
Point_60 = model.addPoint(Part_1_doc, 0.526168, 0.051119, 0)

### Create Point
Point_61 = model.addPoint(Part_1_doc, 0.513088, 0.052008, 0)

### Create Point
Point_62 = model.addPoint(Part_1_doc, 0.5, 0.052862, 0)

### Create Point
Point_63 = model.addPoint(Part_1_doc, 0.486912, 0.053676, 0)

### Create Point
Point_64 = model.addPoint(Part_1_doc, 0.473832, 0.054451, 0)

### Create Point
Point_65 = model.addPoint(Part_1_doc, 0.46077, 0.055184, 0)

### Create Point
Point_66 = model.addPoint(Part_1_doc, 0.447736, 0.055872, 0)

### Create Point
Point_67 = model.addPoint(Part_1_doc, 0.434737, 0.056514, 0)

### Create Point
Point_68 = model.addPoint(Part_1_doc, 0.421783, 0.057108, 0)

### Create Point
Point_69 = model.addPoint(Part_1_doc, 0.408882, 0.057652, 0)

### Create Point
Point_70 = model.addPoint(Part_1_doc, 0.396044, 0.058144, 0)

### Create Point
Point_71 = model.addPoint(Part_1_doc, 0.383277, 0.058582, 0)

### Create Point
Point_72 = model.addPoint(Part_1_doc, 0.37059, 0.058965, 0)

### Create Point
Point_73 = model.addPoint(Part_1_doc, 0.357992, 0.05929, 0)

### Create Point
Point_74 = model.addPoint(Part_1_doc, 0.345492, 0.059557, 0)

### Create Point
Point_75 = model.addPoint(Part_1_doc, 0.333097, 0.059763, 0)

### Create Point
Point_76 = model.addPoint(Part_1_doc, 0.320816, 0.059907, 0)

### Create Point
Point_77 = model.addPoint(Part_1_doc, 0.308658, 0.059988, 0)

### Create Point
Point_78 = model.addPoint(Part_1_doc, 0.296632, 0.060005, 0)

### Create Point
Point_79 = model.addPoint(Part_1_doc, 0.284744, 0.059956, 0)

### Create Point
Point_80 = model.addPoint(Part_1_doc, 0.273005, 0.059841, 0)

### Create Point
Point_81 = model.addPoint(Part_1_doc, 0.261421, 0.059658, 0)

### Create Point
Point_82 = model.addPoint(Part_1_doc, 0.25, 0.059407, 0)

### Create Point
Point_83 = model.addPoint(Part_1_doc, 0.238751, 0.059088, 0)

### Create Point
Point_84 = model.addPoint(Part_1_doc, 0.22768, 0.058699, 0)

### Create Point
Point_85 = model.addPoint(Part_1_doc, 0.216797, 0.05824, 0)

### Create Point
Point_86 = model.addPoint(Part_1_doc, 0.206107, 0.057712, 0)

### Create Point
Point_87 = model.addPoint(Part_1_doc, 0.195619, 0.057114, 0)

### Create Point
Point_88 = model.addPoint(Part_1_doc, 0.18534, 0.056446, 0)

### Create Point
Point_89 = model.addPoint(Part_1_doc, 0.175276, 0.055708, 0)

### Create Point
Point_90 = model.addPoint(Part_1_doc, 0.165435, 0.054901, 0)

### Create Point
Point_91 = model.addPoint(Part_1_doc, 0.155823, 0.054026, 0)

### Create Point
Point_92 = model.addPoint(Part_1_doc, 0.146447, 0.053083, 0)

### Create Point
Point_93 = model.addPoint(Part_1_doc, 0.137313, 0.052072, 0)

### Create Point
Point_94 = model.addPoint(Part_1_doc, 0.128428, 0.050995, 0)

### Create Point
Point_95 = model.addPoint(Part_1_doc, 0.119797, 0.049854, 0)

### Create Point
Point_96 = model.addPoint(Part_1_doc, 0.111427, 0.048648, 0)

### Create Point
Point_97 = model.addPoint(Part_1_doc, 0.103323, 0.047379, 0)

### Create Point
Point_98 = model.addPoint(Part_1_doc, 0.09549199999999999, 0.046049, 0)

### Create Point
Point_99 = model.addPoint(Part_1_doc, 0.087937, 0.044659, 0)

### Create Point
Point_100 = model.addPoint(Part_1_doc, 0.080665, 0.04321, 0)

### Create Point
Point_101 = model.addPoint(Part_1_doc, 0.07368, 0.041705, 0)

### Create Point
Point_102 = model.addPoint(Part_1_doc, 0.066987, 0.040145, 0)

### Create Point
Point_103 = model.addPoint(Part_1_doc, 0.060591, 0.038532, 0)

### Create Point
Point_104 = model.addPoint(Part_1_doc, 0.054497, 0.036867, 0)

### Create Point
Point_105 = model.addPoint(Part_1_doc, 0.048707, 0.035152, 0)

### Create Point
Point_106 = model.addPoint(Part_1_doc, 0.043227, 0.033389, 0)

### Create Point
Point_107 = model.addPoint(Part_1_doc, 0.03806, 0.03158, 0)

### Create Point
Point_108 = model.addPoint(Part_1_doc, 0.03321, 0.029726, 0)

### Create Point
Point_109 = model.addPoint(Part_1_doc, 0.028679, 0.02783, 0)

### Create Point
Point_110 = model.addPoint(Part_1_doc, 0.024472, 0.025893, 0)

### Create Point
Point_111 = model.addPoint(Part_1_doc, 0.02059, 0.023917, 0)

### Create Point
Point_112 = model.addPoint(Part_1_doc, 0.017037, 0.021904, 0)

### Create Point
Point_113 = model.addPoint(Part_1_doc, 0.013815, 0.019854, 0)

### Create Point
Point_114 = model.addPoint(Part_1_doc, 0.010926, 0.01777, 0)

### Create Point
Point_115 = model.addPoint(Part_1_doc, 0.008373, 0.015652, 0)

### Create Point
Point_116 = model.addPoint(Part_1_doc, 0.006156, 0.013503, 0)

### Create Point
Point_117 = model.addPoint(Part_1_doc, 0.004278, 0.011324, 0)

### Create Point
Point_118 = model.addPoint(Part_1_doc, 0.002739, 0.009114000000000001, 0)

### Create Point
Point_119 = model.addPoint(Part_1_doc, 0.001541, 0.006877, 0)

### Create Point
Point_120 = model.addPoint(Part_1_doc, 0.000685, 0.004611, 0)

### Create Point
Point_121 = model.addPoint(Part_1_doc, 0.000171, 0.002319, 0)

### Create Point
Point_122 = model.addPoint(Part_1_doc, 0, 0, 0)

### Create Point
Point_123 = model.addPoint(Part_1_doc, 0.000171, -0.002319, 0)

### Create Point
Point_124 = model.addPoint(Part_1_doc, 0.000685, -0.004611, 0)

### Create Point
Point_125 = model.addPoint(Part_1_doc, 0.001541, -0.006877, 0)

### Create Point
Point_126 = model.addPoint(Part_1_doc, 0.002739, -0.009114000000000001, 0)

### Create Point
Point_127 = model.addPoint(Part_1_doc, 0.004278, -0.011324, 0)

### Create Point
Point_128 = model.addPoint(Part_1_doc, 0.006156, -0.013503, 0)

### Create Point
Point_129 = model.addPoint(Part_1_doc, 0.008373, -0.015652, 0)

### Create Point
Point_130 = model.addPoint(Part_1_doc, 0.010926, -0.01777, 0)

### Create Point
Point_131 = model.addPoint(Part_1_doc, 0.013815, -0.019854, 0)

### Create Point
Point_132 = model.addPoint(Part_1_doc, 0.017037, -0.021904, 0)

### Create Point
Point_133 = model.addPoint(Part_1_doc, 0.02059, -0.023917, 0)

### Create Point
Point_134 = model.addPoint(Part_1_doc, 0.024472, -0.025893, 0)

### Create Point
Point_135 = model.addPoint(Part_1_doc, 0.028679, -0.02783, 0)

### Create Point
Point_136 = model.addPoint(Part_1_doc, 0.03321, -0.029726, 0)

### Create Point
Point_137 = model.addPoint(Part_1_doc, 0.03806, -0.03158, 0)

### Create Point
Point_138 = model.addPoint(Part_1_doc, 0.043227, -0.033389, 0)

### Create Point
Point_139 = model.addPoint(Part_1_doc, 0.048707, -0.035152, 0)

### Create Point
Point_140 = model.addPoint(Part_1_doc, 0.054497, -0.036867, 0)

### Create Point
Point_141 = model.addPoint(Part_1_doc, 0.060591, -0.038532, 0)

### Create Point
Point_142 = model.addPoint(Part_1_doc, 0.066987, -0.040145, 0)

### Create Point
Point_143 = model.addPoint(Part_1_doc, 0.07368, -0.041705, 0)

### Create Point
Point_144 = model.addPoint(Part_1_doc, 0.080665, -0.04321, 0)

### Create Point
Point_145 = model.addPoint(Part_1_doc, 0.087937, -0.044659, 0)

### Create Point
Point_146 = model.addPoint(Part_1_doc, 0.09549199999999999, -0.046049, 0)

### Create Point
Point_147 = model.addPoint(Part_1_doc, 0.103323, -0.047379, 0)

### Create Point
Point_148 = model.addPoint(Part_1_doc, 0.111427, -0.048648, 0)

### Create Point
Point_149 = model.addPoint(Part_1_doc, 0.119797, -0.049854, 0)

### Create Point
Point_150 = model.addPoint(Part_1_doc, 0.128428, -0.050995, 0)

### Create Point
Point_151 = model.addPoint(Part_1_doc, 0.137313, -0.052072, 0)

### Create Point
Point_152 = model.addPoint(Part_1_doc, 0.146447, -0.053083, 0)

### Create Point
Point_153 = model.addPoint(Part_1_doc, 0.155823, -0.054026, 0)

### Create Point
Point_154 = model.addPoint(Part_1_doc, 0.165435, -0.054901, 0)

### Create Point
Point_155 = model.addPoint(Part_1_doc, 0.175276, -0.055708, 0)

### Create Point
Point_156 = model.addPoint(Part_1_doc, 0.18534, -0.056446, 0)

### Create Point
Point_157 = model.addPoint(Part_1_doc, 0.195619, -0.057114, 0)

### Create Point
Point_158 = model.addPoint(Part_1_doc, 0.206107, -0.057712, 0)

### Create Point
Point_159 = model.addPoint(Part_1_doc, 0.216797, -0.05824, 0)

### Create Point
Point_160 = model.addPoint(Part_1_doc, 0.22768, -0.058699, 0)

### Create Point
Point_161 = model.addPoint(Part_1_doc, 0.238751, -0.059088, 0)

### Create Point
Point_162 = model.addPoint(Part_1_doc, 0.25, -0.059407, 0)

### Create Point
Point_163 = model.addPoint(Part_1_doc, 0.261421, -0.059658, 0)

### Create Point
Point_164 = model.addPoint(Part_1_doc, 0.273005, -0.059841, 0)

### Create Point
Point_165 = model.addPoint(Part_1_doc, 0.284744, -0.059956, 0)

### Create Point
Point_166 = model.addPoint(Part_1_doc, 0.296632, -0.060005, 0)

### Create Point
Point_167 = model.addPoint(Part_1_doc, 0.308658, -0.059988, 0)

### Create Point
Point_168 = model.addPoint(Part_1_doc, 0.320816, -0.059907, 0)

### Create Point
Point_169 = model.addPoint(Part_1_doc, 0.333097, -0.059763, 0)

### Create Point
Point_170 = model.addPoint(Part_1_doc, 0.345492, -0.059557, 0)

### Create Point
Point_171 = model.addPoint(Part_1_doc, 0.357992, -0.05929, 0)

### Create Point
Point_172 = model.addPoint(Part_1_doc, 0.37059, -0.058965, 0)

### Create Point
Point_173 = model.addPoint(Part_1_doc, 0.383277, -0.058582, 0)

### Create Point
Point_174 = model.addPoint(Part_1_doc, 0.396044, -0.058144, 0)

### Create Point
Point_175 = model.addPoint(Part_1_doc, 0.408882, -0.057652, 0)

### Create Point
Point_176 = model.addPoint(Part_1_doc, 0.421783, -0.057108, 0)

### Create Point
Point_177 = model.addPoint(Part_1_doc, 0.434737, -0.056514, 0)

### Create Point
Point_178 = model.addPoint(Part_1_doc, 0.447736, -0.055872, 0)

### Create Point
Point_179 = model.addPoint(Part_1_doc, 0.46077, -0.055184, 0)

### Create Point
Point_180 = model.addPoint(Part_1_doc, 0.473832, -0.054451, 0)

### Create Point
Point_181 = model.addPoint(Part_1_doc, 0.486912, -0.053676, 0)

### Create Point
Point_182 = model.addPoint(Part_1_doc, 0.5, -0.052862, 0)

### Create Point
Point_183 = model.addPoint(Part_1_doc, 0.513088, -0.052008, 0)

### Create Point
Point_184 = model.addPoint(Part_1_doc, 0.526168, -0.051119, 0)

### Create Point
Point_185 = model.addPoint(Part_1_doc, 0.53923, -0.050196, 0)

### Create Point
Point_186 = model.addPoint(Part_1_doc, 0.552264, -0.049241, 0)

### Create Point
Point_187 = model.addPoint(Part_1_doc, 0.565263, -0.048255, 0)

### Create Point
Point_188 = model.addPoint(Part_1_doc, 0.578217, -0.047242, 0)

### Create Point
Point_189 = model.addPoint(Part_1_doc, 0.591118, -0.046203, 0)

### Create Point
Point_190 = model.addPoint(Part_1_doc, 0.603956, -0.04514, 0)

### Create Point
Point_191 = model.addPoint(Part_1_doc, 0.616723, -0.044055, 0)

### Create Point
Point_192 = model.addPoint(Part_1_doc, 0.62941, -0.042949, 0)

### Create Point
Point_193 = model.addPoint(Part_1_doc, 0.642008, -0.041826, 0)

### Create Point
Point_194 = model.addPoint(Part_1_doc, 0.654508, -0.040686, 0)

### Create Point
Point_195 = model.addPoint(Part_1_doc, 0.666903, -0.039532, 0)

### Create Point
Point_196 = model.addPoint(Part_1_doc, 0.679184, -0.038366, 0)

### Create Point
Point_197 = model.addPoint(Part_1_doc, 0.691342, -0.037188, 0)

### Create Point
Point_198 = model.addPoint(Part_1_doc, 0.703368, -0.036002, 0)

### Create Point
Point_199 = model.addPoint(Part_1_doc, 0.715256, -0.034809, 0)

### Create Point
Point_200 = model.addPoint(Part_1_doc, 0.7269949999999999, -0.03361, 0)

### Create Point
Point_201 = model.addPoint(Part_1_doc, 0.738579, -0.032408, 0)

### Create Point
Point_202 = model.addPoint(Part_1_doc, 0.75, -0.031204, 0)

### Create Point
Point_203 = model.addPoint(Part_1_doc, 0.761249, -0.03, 0)

### Create Point
Point_204 = model.addPoint(Part_1_doc, 0.77232, -0.028798, 0)

### Create Point
Point_205 = model.addPoint(Part_1_doc, 0.783203, -0.027599, 0)

### Create Point
Point_206 = model.addPoint(Part_1_doc, 0.793893, -0.026405, 0)

### Create Point
Point_207 = model.addPoint(Part_1_doc, 0.804381, -0.025217, 0)

### Create Point
Point_208 = model.addPoint(Part_1_doc, 0.8146600000000001, -0.024038, 0)

### Create Point
Point_209 = model.addPoint(Part_1_doc, 0.824724, -0.022869, 0)

### Create Point
Point_210 = model.addPoint(Part_1_doc, 0.834565, -0.021712, 0)

### Create Point
Point_211 = model.addPoint(Part_1_doc, 0.844177, -0.020568, 0)

### Create Point
Point_212 = model.addPoint(Part_1_doc, 0.853553, -0.019438, 0)

### Create Point
Point_213 = model.addPoint(Part_1_doc, 0.862687, -0.018326, 0)

### Create Point
Point_214 = model.addPoint(Part_1_doc, 0.871572, -0.017232, 0)

### Create Point
Point_215 = model.addPoint(Part_1_doc, 0.880203, -0.016158, 0)

### Create Point
Point_216 = model.addPoint(Part_1_doc, 0.8885729999999999, -0.015105, 0)

### Create Point
Point_217 = model.addPoint(Part_1_doc, 0.8966769999999999, -0.014076, 0)

### Create Point
Point_218 = model.addPoint(Part_1_doc, 0.904508, -0.013071, 0)

### Create Point
Point_219 = model.addPoint(Part_1_doc, 0.912063, -0.012093, 0)

### Create Point
Point_220 = model.addPoint(Part_1_doc, 0.919335, -0.011142, 0)

### Create Point
Point_221 = model.addPoint(Part_1_doc, 0.92632, -0.010221, 0)

### Create Point
Point_222 = model.addPoint(Part_1_doc, 0.933013, -0.009332, 0)

### Create Point
Point_223 = model.addPoint(Part_1_doc, 0.939409, -0.008474000000000001, 0)

### Create Point
Point_224 = model.addPoint(Part_1_doc, 0.945503, -0.007651, 0)

### Create Point
Point_225 = model.addPoint(Part_1_doc, 0.9512930000000001, -0.006863, 0)

### Create Point
Point_226 = model.addPoint(Part_1_doc, 0.956773, -0.006112, 0)

### Create Point
Point_227 = model.addPoint(Part_1_doc, 0.96194, -0.005399, 0)

### Create Point
Point_228 = model.addPoint(Part_1_doc, 0.96679, -0.004725, 0)

### Create Point
Point_229 = model.addPoint(Part_1_doc, 0.971321, -0.004092, 0)

### Create Point
Point_230 = model.addPoint(Part_1_doc, 0.975528, -0.003501, 0)

### Create Point
Point_231 = model.addPoint(Part_1_doc, 0.97941, -0.002953, 0)

### Create Point
Point_232 = model.addPoint(Part_1_doc, 0.982963, -0.002449, 0)

### Create Point
Point_233 = model.addPoint(Part_1_doc, 0.986185, -0.00199, 0)

### Create Point
Point_234 = model.addPoint(Part_1_doc, 0.989074, -0.001577, 0)

### Create Point
Point_235 = model.addPoint(Part_1_doc, 0.991627, -0.00121, 0)

### Create Point
Point_236 = model.addPoint(Part_1_doc, 0.9938439999999999, -0.000891, 0)

### Create Point
Point_237 = model.addPoint(Part_1_doc, 0.995722, -0.00062, 0)

### Create Point
Point_238 = model.addPoint(Part_1_doc, 0.997261, -0.000397, 0)

### Create Point
Point_239 = model.addPoint(Part_1_doc, 0.998459, -0.000224, 0)

### Create Point
Point_240 = model.addPoint(Part_1_doc, 0.999315, -9.899999999999999e-05, 0)

### Create Point
Point_241 = model.addPoint(Part_1_doc, 0.999829, -2.5e-05, 0)

### Create Compound
Compound_1_objects = [model.selection("VERTEX", "Point_1"),
                      model.selection("VERTEX", "Point_2"),
                      model.selection("VERTEX", "Point_3"),
                      model.selection("VERTEX", "Point_4"),
                      model.selection("VERTEX", "Point_5"),
                      model.selection("VERTEX", "Point_6"),
                      model.selection("VERTEX", "Point_7"),
                      model.selection("VERTEX", "Point_8"),
                      model.selection("VERTEX", "Point_9"),
                      model.selection("VERTEX", "Point_10"),
                      model.selection("VERTEX", "Point_11"),
                      model.selection("VERTEX", "Point_12"),
                      model.selection("VERTEX", "Point_13"),
                      model.selection("VERTEX", "Point_14"),
                      model.selection("VERTEX", "Point_15"),
                      model.selection("VERTEX", "Point_16"),
                      model.selection("VERTEX", "Point_17"),
                      model.selection("VERTEX", "Point_18"),
                      model.selection("VERTEX", "Point_19"),
                      model.selection("VERTEX", "Point_20"),
                      model.selection("VERTEX", "Point_21"),
                      model.selection("VERTEX", "Point_22"),
                      model.selection("VERTEX", "Point_23"),
                      model.selection("VERTEX", "Point_24"),
                      model.selection("VERTEX", "Point_25"),
                      model.selection("VERTEX", "Point_26"),
                      model.selection("VERTEX", "Point_27"),
                      model.selection("VERTEX", "Point_28"),
                      model.selection("VERTEX", "Point_29"),
                      model.selection("VERTEX", "Point_30"),
                      model.selection("VERTEX", "Point_31"),
                      model.selection("VERTEX", "Point_32"),
                      model.selection("VERTEX", "Point_33"),
                      model.selection("VERTEX", "Point_34"),
                      model.selection("VERTEX", "Point_35"),
                      model.selection("VERTEX", "Point_36"),
                      model.selection("VERTEX", "Point_37"),
                      model.selection("VERTEX", "Point_38"),
                      model.selection("VERTEX", "Point_39"),
                      model.selection("VERTEX", "Point_40"),
                      model.selection("VERTEX", "Point_41"),
                      model.selection("VERTEX", "Point_42"),
                      model.selection("VERTEX", "Point_43"),
                      model.selection("VERTEX", "Point_44"),
                      model.selection("VERTEX", "Point_45"),
                      model.selection("VERTEX", "Point_46"),
                      model.selection("VERTEX", "Point_47"),
                      model.selection("VERTEX", "Point_48"),
                      model.selection("VERTEX", "Point_49"),
                      model.selection("VERTEX", "Point_50"),
                      model.selection("VERTEX", "Point_51"),
                      model.selection("VERTEX", "Point_52"),
                      model.selection("VERTEX", "Point_53"),
                      model.selection("VERTEX", "Point_54"),
                      model.selection("VERTEX", "Point_55"),
                      model.selection("VERTEX", "Point_56"),
                      model.selection("VERTEX", "Point_57"),
                      model.selection("VERTEX", "Point_58"),
                      model.selection("VERTEX", "Point_59"),
                      model.selection("VERTEX", "Point_60"),
                      model.selection("VERTEX", "Point_61"),
                      model.selection("VERTEX", "Point_62"),
                      model.selection("VERTEX", "Point_63"),
                      model.selection("VERTEX", "Point_64"),
                      model.selection("VERTEX", "Point_65"),
                      model.selection("VERTEX", "Point_66"),
                      model.selection("VERTEX", "Point_67"),
                      model.selection("VERTEX", "Point_68"),
                      model.selection("VERTEX", "Point_69"),
                      model.selection("VERTEX", "Point_70"),
                      model.selection("VERTEX", "Point_71"),
                      model.selection("VERTEX", "Point_72"),
                      model.selection("VERTEX", "Point_73"),
                      model.selection("VERTEX", "Point_74"),
                      model.selection("VERTEX", "Point_75"),
                      model.selection("VERTEX", "Point_76"),
                      model.selection("VERTEX", "Point_77"),
                      model.selection("VERTEX", "Point_78"),
                      model.selection("VERTEX", "Point_79"),
                      model.selection("VERTEX", "Point_80"),
                      model.selection("VERTEX", "Point_81"),
                      model.selection("VERTEX", "Point_82"),
                      model.selection("VERTEX", "Point_83"),
                      model.selection("VERTEX", "Point_84"),
                      model.selection("VERTEX", "Point_85"),
                      model.selection("VERTEX", "Point_86"),
                      model.selection("VERTEX", "Point_87"),
                      model.selection("VERTEX", "Point_88"),
                      model.selection("VERTEX", "Point_89"),
                      model.selection("VERTEX", "Point_90"),
                      model.selection("VERTEX", "Point_91"),
                      model.selection("VERTEX", "Point_92"),
                      model.selection("VERTEX", "Point_93"),
                      model.selection("VERTEX", "Point_94"),
                      model.selection("VERTEX", "Point_95"),
                      model.selection("VERTEX", "Point_96"),
                      model.selection("VERTEX", "Point_97"),
                      model.selection("VERTEX", "Point_98"),
                      model.selection("VERTEX", "Point_99"),
                      model.selection("VERTEX", "Point_100"),
                      model.selection("VERTEX", "Point_101"),
                      model.selection("VERTEX", "Point_102"),
                      model.selection("VERTEX", "Point_103"),
                      model.selection("VERTEX", "Point_104"),
                      model.selection("VERTEX", "Point_105"),
                      model.selection("VERTEX", "Point_106"),
                      model.selection("VERTEX", "Point_107"),
                      model.selection("VERTEX", "Point_108"),
                      model.selection("VERTEX", "Point_109"),
                      model.selection("VERTEX", "Point_110"),
                      model.selection("VERTEX", "Point_111"),
                      model.selection("VERTEX", "Point_112"),
                      model.selection("VERTEX", "Point_113"),
                      model.selection("VERTEX", "Point_114"),
                      model.selection("VERTEX", "Point_115"),
                      model.selection("VERTEX", "Point_116"),
                      model.selection("VERTEX", "Point_117"),
                      model.selection("VERTEX", "Point_118"),
                      model.selection("VERTEX", "Point_119"),
                      model.selection("VERTEX", "Point_120"),
                      model.selection("VERTEX", "Point_121"),
                      model.selection("VERTEX", "Point_122"),
                      model.selection("VERTEX", "Point_123"),
                      model.selection("VERTEX", "Point_124"),
                      model.selection("VERTEX", "Point_125"),
                      model.selection("VERTEX", "Point_126"),
                      model.selection("VERTEX", "Point_127"),
                      model.selection("VERTEX", "Point_128"),
                      model.selection("VERTEX", "Point_129"),
                      model.selection("VERTEX", "Point_130"),
                      model.selection("VERTEX", "Point_131"),
                      model.selection("VERTEX", "Point_132"),
                      model.selection("VERTEX", "Point_133"),
                      model.selection("VERTEX", "Point_134"),
                      model.selection("VERTEX", "Point_135"),
                      model.selection("VERTEX", "Point_136"),
                      model.selection("VERTEX", "Point_137"),
                      model.selection("VERTEX", "Point_138"),
                      model.selection("VERTEX", "Point_139"),
                      model.selection("VERTEX", "Point_140"),
                      model.selection("VERTEX", "Point_141"),
                      model.selection("VERTEX", "Point_142"),
                      model.selection("VERTEX", "Point_143"),
                      model.selection("VERTEX", "Point_144"),
                      model.selection("VERTEX", "Point_145"),
                      model.selection("VERTEX", "Point_146"),
                      model.selection("VERTEX", "Point_147"),
                      model.selection("VERTEX", "Point_148"),
                      model.selection("VERTEX", "Point_149"),
                      model.selection("VERTEX", "Point_150"),
                      model.selection("VERTEX", "Point_151"),
                      model.selection("VERTEX", "Point_152"),
                      model.selection("VERTEX", "Point_153"),
                      model.selection("VERTEX", "Point_154"),
                      model.selection("VERTEX", "Point_155"),
                      model.selection("VERTEX", "Point_156"),
                      model.selection("VERTEX", "Point_157"),
                      model.selection("VERTEX", "Point_158"),
                      model.selection("VERTEX", "Point_159"),
                      model.selection("VERTEX", "Point_160"),
                      model.selection("VERTEX", "Point_161"),
                      model.selection("VERTEX", "Point_162"),
                      model.selection("VERTEX", "Point_163"),
                      model.selection("VERTEX", "Point_164"),
                      model.selection("VERTEX", "Point_165"),
                      model.selection("VERTEX", "Point_166"),
                      model.selection("VERTEX", "Point_167"),
                      model.selection("VERTEX", "Point_168"),
                      model.selection("VERTEX", "Point_169"),
                      model.selection("VERTEX", "Point_170"),
                      model.selection("VERTEX", "Point_171"),
                      model.selection("VERTEX", "Point_172"),
                      model.selection("VERTEX", "Point_173"),
                      model.selection("VERTEX", "Point_174"),
                      model.selection("VERTEX", "Point_175"),
                      model.selection("VERTEX", "Point_176"),
                      model.selection("VERTEX", "Point_177"),
                      model.selection("VERTEX", "Point_178"),
                      model.selection("VERTEX", "Point_179"),
                      model.selection("VERTEX", "Point_180"),
                      model.selection("VERTEX", "Point_181"),
                      model.selection("VERTEX", "Point_182"),
                      model.selection("VERTEX", "Point_183"),
                      model.selection("VERTEX", "Point_184"),
                      model.selection("VERTEX", "Point_185"),
                      model.selection("VERTEX", "Point_186"),
                      model.selection("VERTEX", "Point_187"),
                      model.selection("VERTEX", "Point_188"),
                      model.selection("VERTEX", "Point_189"),
                      model.selection("VERTEX", "Point_190"),
                      model.selection("VERTEX", "Point_191"),
                      model.selection("VERTEX", "Point_192"),
                      model.selection("VERTEX", "Point_193"),
                      model.selection("VERTEX", "Point_194"),
                      model.selection("VERTEX", "Point_195"),
                      model.selection("VERTEX", "Point_196"),
                      model.selection("VERTEX", "Point_197"),
                      model.selection("VERTEX", "Point_198"),
                      model.selection("VERTEX", "Point_199"),
                      model.selection("VERTEX", "Point_200"),
                      model.selection("VERTEX", "Point_201"),
                      model.selection("VERTEX", "Point_202"),
                      model.selection("VERTEX", "Point_203"),
                      model.selection("VERTEX", "Point_204"),
                      model.selection("VERTEX", "Point_205"),
                      model.selection("VERTEX", "Point_206"),
                      model.selection("VERTEX", "Point_207"),
                      model.selection("VERTEX", "Point_208"),
                      model.selection("VERTEX", "Point_209"),
                      model.selection("VERTEX", "Point_210"),
                      model.selection("VERTEX", "Point_211"),
                      model.selection("VERTEX", "Point_212"),
                      model.selection("VERTEX", "Point_213"),
                      model.selection("VERTEX", "Point_214"),
                      model.selection("VERTEX", "Point_215"),
                      model.selection("VERTEX", "Point_216"),
                      model.selection("VERTEX", "Point_217"),
                      model.selection("VERTEX", "Point_218"),
                      model.selection("VERTEX", "Point_219"),
                      model.selection("VERTEX", "Point_220"),
                      model.selection("VERTEX", "Point_221"),
                      model.selection("VERTEX", "Point_222"),
                      model.selection("VERTEX", "Point_223"),
                      model.selection("VERTEX", "Point_224"),
                      model.selection("VERTEX", "Point_225"),
                      model.selection("VERTEX", "Point_226"),
                      model.selection("VERTEX", "Point_227"),
                      model.selection("VERTEX", "Point_228"),
                      model.selection("VERTEX", "Point_229"),
                      model.selection("VERTEX", "Point_230"),
                      model.selection("VERTEX", "Point_231"),
                      model.selection("VERTEX", "Point_232"),
                      model.selection("VERTEX", "Point_233"),
                      model.selection("VERTEX", "Point_234"),
                      model.selection("VERTEX", "Point_235"),
                      model.selection("VERTEX", "Point_236"),
                      model.selection("VERTEX", "Point_237"),
                      model.selection("VERTEX", "Point_238"),
                      model.selection("VERTEX", "Point_239"),
                      model.selection("VERTEX", "Point_240")]
Compound_1 = model.addCompound(Part_1_doc, Compound_1_objects)
Compound_1.result().setName("Points_NACA0012_2.txt")

### Create Export
Export_1 = model.exportToXAO(Part_1_doc, 'C:\\Users\\Lenovo\\AppData\\Local\\Temp\\shaper_vw0su6z0.xao', model.selection("COMPOUND", "Points_NACA0012_2.txt"), 'XAO')

### Create Polyline
Polyline_1_objects = [model.selection("VERTEX", "all-in-Point_1"),
                      model.selection("VERTEX", "all-in-Point_2"),
                      model.selection("VERTEX", "all-in-Point_3"),
                      model.selection("VERTEX", "all-in-Point_4"),
                      model.selection("VERTEX", "all-in-Point_5"),
                      model.selection("VERTEX", "all-in-Point_6"),
                      model.selection("VERTEX", "all-in-Point_7"),
                      model.selection("VERTEX", "all-in-Point_8"),
                      model.selection("VERTEX", "all-in-Point_9"),
                      model.selection("VERTEX", "all-in-Point_10"),
                      model.selection("VERTEX", "all-in-Point_11"),
                      model.selection("VERTEX", "all-in-Point_12"),
                      model.selection("VERTEX", "all-in-Point_13"),
                      model.selection("VERTEX", "all-in-Point_14"),
                      model.selection("VERTEX", "all-in-Point_15"),
                      model.selection("VERTEX", "all-in-Point_16"),
                      model.selection("VERTEX", "all-in-Point_17"),
                      model.selection("VERTEX", "all-in-Point_18"),
                      model.selection("VERTEX", "all-in-Point_19"),
                      model.selection("VERTEX", "all-in-Point_20"),
                      model.selection("VERTEX", "all-in-Point_21"),
                      model.selection("VERTEX", "all-in-Point_22"),
                      model.selection("VERTEX", "all-in-Point_23"),
                      model.selection("VERTEX", "all-in-Point_24"),
                      model.selection("VERTEX", "all-in-Point_25"),
                      model.selection("VERTEX", "all-in-Point_26"),
                      model.selection("VERTEX", "all-in-Point_27"),
                      model.selection("VERTEX", "all-in-Point_28"),
                      model.selection("VERTEX", "all-in-Point_29"),
                      model.selection("VERTEX", "all-in-Point_30"),
                      model.selection("VERTEX", "all-in-Point_31"),
                      model.selection("VERTEX", "all-in-Point_32"),
                      model.selection("VERTEX", "all-in-Point_33"),
                      model.selection("VERTEX", "all-in-Point_34"),
                      model.selection("VERTEX", "all-in-Point_35"),
                      model.selection("VERTEX", "all-in-Point_36"),
                      model.selection("VERTEX", "all-in-Point_37"),
                      model.selection("VERTEX", "all-in-Point_38"),
                      model.selection("VERTEX", "all-in-Point_39"),
                      model.selection("VERTEX", "all-in-Point_40"),
                      model.selection("VERTEX", "all-in-Point_41"),
                      model.selection("VERTEX", "all-in-Point_42"),
                      model.selection("VERTEX", "all-in-Point_43"),
                      model.selection("VERTEX", "all-in-Point_44"),
                      model.selection("VERTEX", "all-in-Point_45"),
                      model.selection("VERTEX", "all-in-Point_46"),
                      model.selection("VERTEX", "all-in-Point_47"),
                      model.selection("VERTEX", "all-in-Point_48"),
                      model.selection("VERTEX", "all-in-Point_49"),
                      model.selection("VERTEX", "all-in-Point_50"),
                      model.selection("VERTEX", "all-in-Point_51"),
                      model.selection("VERTEX", "all-in-Point_52"),
                      model.selection("VERTEX", "all-in-Point_53"),
                      model.selection("VERTEX", "all-in-Point_54"),
                      model.selection("VERTEX", "all-in-Point_55"),
                      model.selection("VERTEX", "all-in-Point_56"),
                      model.selection("VERTEX", "all-in-Point_57"),
                      model.selection("VERTEX", "all-in-Point_58"),
                      model.selection("VERTEX", "all-in-Point_59"),
                      model.selection("VERTEX", "all-in-Point_60"),
                      model.selection("VERTEX", "all-in-Point_61"),
                      model.selection("VERTEX", "all-in-Point_62"),
                      model.selection("VERTEX", "all-in-Point_63"),
                      model.selection("VERTEX", "all-in-Point_64"),
                      model.selection("VERTEX", "all-in-Point_65"),
                      model.selection("VERTEX", "all-in-Point_66"),
                      model.selection("VERTEX", "all-in-Point_67"),
                      model.selection("VERTEX", "all-in-Point_68"),
                      model.selection("VERTEX", "all-in-Point_69"),
                      model.selection("VERTEX", "all-in-Point_70"),
                      model.selection("VERTEX", "all-in-Point_71"),
                      model.selection("VERTEX", "all-in-Point_72"),
                      model.selection("VERTEX", "all-in-Point_73"),
                      model.selection("VERTEX", "all-in-Point_74"),
                      model.selection("VERTEX", "all-in-Point_75"),
                      model.selection("VERTEX", "all-in-Point_76"),
                      model.selection("VERTEX", "all-in-Point_77"),
                      model.selection("VERTEX", "all-in-Point_78"),
                      model.selection("VERTEX", "all-in-Point_79"),
                      model.selection("VERTEX", "all-in-Point_80"),
                      model.selection("VERTEX", "all-in-Point_81"),
                      model.selection("VERTEX", "all-in-Point_82"),
                      model.selection("VERTEX", "all-in-Point_83"),
                      model.selection("VERTEX", "all-in-Point_84"),
                      model.selection("VERTEX", "all-in-Point_85"),
                      model.selection("VERTEX", "all-in-Point_86"),
                      model.selection("VERTEX", "all-in-Point_87"),
                      model.selection("VERTEX", "all-in-Point_88"),
                      model.selection("VERTEX", "all-in-Point_89"),
                      model.selection("VERTEX", "all-in-Point_90"),
                      model.selection("VERTEX", "all-in-Point_91"),
                      model.selection("VERTEX", "all-in-Point_92"),
                      model.selection("VERTEX", "all-in-Point_93"),
                      model.selection("VERTEX", "all-in-Point_94"),
                      model.selection("VERTEX", "all-in-Point_95"),
                      model.selection("VERTEX", "all-in-Point_96"),
                      model.selection("VERTEX", "all-in-Point_97"),
                      model.selection("VERTEX", "all-in-Point_98"),
                      model.selection("VERTEX", "all-in-Point_99"),
                      model.selection("VERTEX", "all-in-Point_100"),
                      model.selection("VERTEX", "all-in-Point_101"),
                      model.selection("VERTEX", "all-in-Point_102"),
                      model.selection("VERTEX", "all-in-Point_103"),
                      model.selection("VERTEX", "all-in-Point_104"),
                      model.selection("VERTEX", "all-in-Point_105"),
                      model.selection("VERTEX", "all-in-Point_106"),
                      model.selection("VERTEX", "all-in-Point_107"),
                      model.selection("VERTEX", "all-in-Point_108"),
                      model.selection("VERTEX", "all-in-Point_109"),
                      model.selection("VERTEX", "all-in-Point_110"),
                      model.selection("VERTEX", "all-in-Point_111"),
                      model.selection("VERTEX", "all-in-Point_112"),
                      model.selection("VERTEX", "all-in-Point_113"),
                      model.selection("VERTEX", "all-in-Point_114"),
                      model.selection("VERTEX", "all-in-Point_115"),
                      model.selection("VERTEX", "all-in-Point_116"),
                      model.selection("VERTEX", "all-in-Point_117"),
                      model.selection("VERTEX", "all-in-Point_118"),
                      model.selection("VERTEX", "all-in-Point_119"),
                      model.selection("VERTEX", "all-in-Point_120"),
                      model.selection("VERTEX", "all-in-Point_121"),
                      model.selection("VERTEX", "all-in-Point_122"),
                      model.selection("VERTEX", "all-in-Point_123"),
                      model.selection("VERTEX", "all-in-Point_124"),
                      model.selection("VERTEX", "all-in-Point_125"),
                      model.selection("VERTEX", "all-in-Point_126"),
                      model.selection("VERTEX", "all-in-Point_127"),
                      model.selection("VERTEX", "all-in-Point_128"),
                      model.selection("VERTEX", "all-in-Point_129"),
                      model.selection("VERTEX", "all-in-Point_130"),
                      model.selection("VERTEX", "all-in-Point_131"),
                      model.selection("VERTEX", "all-in-Point_132"),
                      model.selection("VERTEX", "all-in-Point_133"),
                      model.selection("VERTEX", "all-in-Point_134"),
                      model.selection("VERTEX", "all-in-Point_135"),
                      model.selection("VERTEX", "all-in-Point_136"),
                      model.selection("VERTEX", "all-in-Point_137"),
                      model.selection("VERTEX", "all-in-Point_138"),
                      model.selection("VERTEX", "all-in-Point_139"),
                      model.selection("VERTEX", "all-in-Point_140"),
                      model.selection("VERTEX", "all-in-Point_141"),
                      model.selection("VERTEX", "all-in-Point_142"),
                      model.selection("VERTEX", "all-in-Point_143"),
                      model.selection("VERTEX", "all-in-Point_144"),
                      model.selection("VERTEX", "all-in-Point_145"),
                      model.selection("VERTEX", "all-in-Point_146"),
                      model.selection("VERTEX", "all-in-Point_147"),
                      model.selection("VERTEX", "all-in-Point_148"),
                      model.selection("VERTEX", "all-in-Point_149"),
                      model.selection("VERTEX", "all-in-Point_150"),
                      model.selection("VERTEX", "all-in-Point_151"),
                      model.selection("VERTEX", "all-in-Point_152"),
                      model.selection("VERTEX", "all-in-Point_153"),
                      model.selection("VERTEX", "all-in-Point_154"),
                      model.selection("VERTEX", "all-in-Point_155"),
                      model.selection("VERTEX", "all-in-Point_156"),
                      model.selection("VERTEX", "all-in-Point_157"),
                      model.selection("VERTEX", "all-in-Point_158"),
                      model.selection("VERTEX", "all-in-Point_159"),
                      model.selection("VERTEX", "all-in-Point_160"),
                      model.selection("VERTEX", "all-in-Point_161"),
                      model.selection("VERTEX", "all-in-Point_162"),
                      model.selection("VERTEX", "all-in-Point_163"),
                      model.selection("VERTEX", "all-in-Point_164"),
                      model.selection("VERTEX", "all-in-Point_165"),
                      model.selection("VERTEX", "all-in-Point_166"),
                      model.selection("VERTEX", "all-in-Point_167"),
                      model.selection("VERTEX", "all-in-Point_168"),
                      model.selection("VERTEX", "all-in-Point_169"),
                      model.selection("VERTEX", "all-in-Point_170"),
                      model.selection("VERTEX", "all-in-Point_171"),
                      model.selection("VERTEX", "all-in-Point_172"),
                      model.selection("VERTEX", "all-in-Point_173"),
                      model.selection("VERTEX", "all-in-Point_174"),
                      model.selection("VERTEX", "all-in-Point_175"),
                      model.selection("VERTEX", "all-in-Point_176"),
                      model.selection("VERTEX", "all-in-Point_177"),
                      model.selection("VERTEX", "all-in-Point_178"),
                      model.selection("VERTEX", "all-in-Point_179"),
                      model.selection("VERTEX", "all-in-Point_180"),
                      model.selection("VERTEX", "all-in-Point_181"),
                      model.selection("VERTEX", "all-in-Point_182"),
                      model.selection("VERTEX", "all-in-Point_183"),
                      model.selection("VERTEX", "all-in-Point_184"),
                      model.selection("VERTEX", "all-in-Point_185"),
                      model.selection("VERTEX", "all-in-Point_186"),
                      model.selection("VERTEX", "all-in-Point_187"),
                      model.selection("VERTEX", "all-in-Point_188"),
                      model.selection("VERTEX", "all-in-Point_189"),
                      model.selection("VERTEX", "all-in-Point_190"),
                      model.selection("VERTEX", "all-in-Point_191"),
                      model.selection("VERTEX", "all-in-Point_192"),
                      model.selection("VERTEX", "all-in-Point_193"),
                      model.selection("VERTEX", "all-in-Point_194"),
                      model.selection("VERTEX", "all-in-Point_195"),
                      model.selection("VERTEX", "all-in-Point_196"),
                      model.selection("VERTEX", "all-in-Point_197"),
                      model.selection("VERTEX", "all-in-Point_198"),
                      model.selection("VERTEX", "all-in-Point_199"),
                      model.selection("VERTEX", "all-in-Point_200"),
                      model.selection("VERTEX", "all-in-Point_201"),
                      model.selection("VERTEX", "all-in-Point_202"),
                      model.selection("VERTEX", "all-in-Point_203"),
                      model.selection("VERTEX", "all-in-Point_204"),
                      model.selection("VERTEX", "all-in-Point_205"),
                      model.selection("VERTEX", "all-in-Point_206"),
                      model.selection("VERTEX", "all-in-Point_207"),
                      model.selection("VERTEX", "all-in-Point_208"),
                      model.selection("VERTEX", "all-in-Point_209"),
                      model.selection("VERTEX", "all-in-Point_210"),
                      model.selection("VERTEX", "all-in-Point_211"),
                      model.selection("VERTEX", "all-in-Point_212"),
                      model.selection("VERTEX", "all-in-Point_213"),
                      model.selection("VERTEX", "all-in-Point_214"),
                      model.selection("VERTEX", "all-in-Point_215"),
                      model.selection("VERTEX", "all-in-Point_216"),
                      model.selection("VERTEX", "all-in-Point_217"),
                      model.selection("VERTEX", "all-in-Point_218"),
                      model.selection("VERTEX", "all-in-Point_219"),
                      model.selection("VERTEX", "all-in-Point_220"),
                      model.selection("VERTEX", "all-in-Point_221"),
                      model.selection("VERTEX", "all-in-Point_222"),
                      model.selection("VERTEX", "all-in-Point_223"),
                      model.selection("VERTEX", "all-in-Point_224"),
                      model.selection("VERTEX", "all-in-Point_225"),
                      model.selection("VERTEX", "all-in-Point_226"),
                      model.selection("VERTEX", "all-in-Point_227"),
                      model.selection("VERTEX", "all-in-Point_228"),
                      model.selection("VERTEX", "all-in-Point_229"),
                      model.selection("VERTEX", "all-in-Point_230"),
                      model.selection("VERTEX", "all-in-Point_231"),
                      model.selection("VERTEX", "all-in-Point_232"),
                      model.selection("VERTEX", "all-in-Point_233"),
                      model.selection("VERTEX", "all-in-Point_234"),
                      model.selection("VERTEX", "all-in-Point_235"),
                      model.selection("VERTEX", "all-in-Point_236"),
                      model.selection("VERTEX", "all-in-Point_237"),
                      model.selection("VERTEX", "all-in-Point_238"),
                      model.selection("VERTEX", "all-in-Point_239"),
                      model.selection("VERTEX", "all-in-Point_240")]
Polyline_1 = model.addPolyline3D(Part_1_doc, Polyline_1_objects, True)

### Create Export
Export_2 = model.exportToXAO(Part_1_doc, 'C:\\Users\\Lenovo\\AppData\\Local\\Temp\\shaper_4s09l43u.xao', model.selection("COMPOUND", "Points_NACA0012_2.txt"), 'XAO')

### Create Export
Export_3 = model.exportToXAO(Part_1_doc, 'C:\\Users\\Lenovo\\AppData\\Local\\Temp\\shaper_43yaixhr.xao', model.selection("WIRE", "Polyline_1_1"), 'XAO')
Folder_1 = model.addFolder(Part_1_doc, Point_2, Export_3)
Folder_1.setName("Points_NACA0012_2.txt")

model.end()

###
### SHAPERSTUDY component
###

model.publishToShaperStudy()
import SHAPERSTUDY
Points_NACA0012_2.txt, = SHAPERSTUDY.shape(model.featureStringId(Compound_1))
Polyline_1_1, = SHAPERSTUDY.shape(model.featureStringId(Polyline_1))
###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

(imported, geomObj_1, [], [], []) = geompy.ImportXAO("C:/Users/Lenovo/AppData/Local/Temp/shaper_vw0su6z0.xao")
(imported, Points_NACA0012_2_txt, [], [], []) = geompy.ImportXAO("C:/Users/Lenovo/AppData/Local/Temp/shaper_4s09l43u.xao")
(imported, Polyline_1_1, [], [], []) = geompy.ImportXAO("C:/Users/Lenovo/AppData/Local/Temp/shaper_43yaixhr.xao")
Face_1 = geompy.MakeFaceWires([Polyline_1_1], 1)
Face_2 = geompy.MakeFaceHW(3, 0.5, 1)
Translation_1 = geompy.MakeTranslation(Face_2, 1, 0, 0)
Cut_1 = geompy.MakeCutList(Translation_1, [Face_1], True)
Vertex_1 = geompy.MakeVertex(-0.15, 0.15, 0)
Vertex_2 = geompy.MakeVertex(-0.15, -0.15, 0)
Vertex_3 = geompy.MakeVertex(-0.15, -0.25, 0)
Vertex_4 = geompy.MakeVertex(-0.15, 0.25, 0)
Vertex_5 = geompy.MakeVertex(1.25, 0.25, 0)
Vertex_6 = geompy.MakeVertex(1.25, 0.15, 0)
Vertex_7 = geompy.MakeVertex(1.25, -0.15, 0)
Vertex_8 = geompy.MakeVertex(1.25, -0.25, 0)
Line_1 = geompy.MakeLineTwoPnt(Vertex_8, Vertex_7)
Line_2 = geompy.MakeLineTwoPnt(Vertex_7, Vertex_2)
Line_3 = geompy.MakeLineTwoPnt(Vertex_2, Vertex_3)
Line_4 = geompy.MakeLineTwoPnt(Vertex_3, Vertex_1)
Line_5 = geompy.MakeLineTwoPnt(Vertex_1, Vertex_4)
Line_4_vertex_3 = geompy.GetSubShape(Line_4, [3])
Line_6 = geompy.MakeLineTwoPnt(Vertex_6, Line_4_vertex_3)
Line_6_vertex_2 = geompy.GetSubShape(Line_6, [2])
Line_7 = geompy.MakeLineTwoPnt(Line_6_vertex_2, Vertex_5)
Line_2_vertex_2 = geompy.GetSubShape(Line_2, [2])
Line_8 = geompy.MakeLineTwoPnt(Line_6_vertex_2, Line_2_vertex_2)
Partition_1 = geompy.MakePartition([Cut_1], [Line_1, Line_2, Line_3, Line_4, Line_5, Line_6, Line_7, Line_8], [], [], geompy.ShapeType["FACE"], 0, [], 0)
Esq_Dir = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(Esq_Dir, [2, 30])
cima_baixo = geompy.CreateGroup(Partition_1, geompy.ShapeType["FACE"])
geompy.UnionIDs(cima_baixo, [23, 16])
linhas_cima_baixo = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(linhas_cima_baixo, [22, 18, 25, 29])
linhas_dir_esq = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(linhas_dir_esq, [32, 11])
[Esq_Dir, cima_baixo, linhas_cima_baixo, linhas_dir_esq] = geompy.GetExistingSubObjects(Partition_1, False)
aerofolio = geompy.CreateGroup(Partition_1, geompy.ShapeType["EDGE"])
geompy.UnionIDs(aerofolio, [232, 484, 294, 418, 314, 52, 98, 410, 452, 236, 516, 190, 300, 290, 356, 446, 104, 130, 212, 382, 310, 476, 472, 454, 204, 198, 254, 426, 58, 422, 82, 158, 490, 156, 210, 276, 414, 306, 358, 432, 72, 136, 466, 380, 260, 496, 280, 402, 458, 140, 160, 238, 372, 68, 134, 520, 262, 388, 154, 488, 218, 330, 346, 386, 440, 90, 508, 296, 428, 178, 244, 242, 370, 56, 70, 184, 150, 322, 352, 76, 152, 270, 348, 406, 96, 110, 486, 256, 362, 462, 312, 240, 106, 456, 172, 114, 298, 366, 84, 200, 384, 66, 196, 216, 332, 368, 338, 94, 438, 168, 498, 272, 138, 304, 320, 474, 430, 80, 460, 186, 164, 504, 378, 328, 374, 124, 142, 224, 318, 44, 392, 444, 308, 510, 464, 188, 230, 246, 340, 88, 434, 120, 500, 404, 220, 250, 400, 442, 174, 162, 470, 482, 326, 50, 394, 292, 41, 144, 166, 194, 274, 376, 420, 78, 126, 514, 336, 182, 228, 492, 258, 302, 398, 450, 146, 506, 494, 252, 102, 122, 268, 396, 86, 214, 208, 206, 436, 390, 64, 180, 518, 248, 416, 148, 512, 278, 266, 344, 48, 74, 128, 264, 108, 92, 116, 132, 316, 350, 412, 100, 176, 468, 234, 360, 226, 334, 288, 408, 60, 448, 192, 478, 286, 354, 54, 170, 282, 502, 342, 62, 118, 222, 202, 324, 364, 424, 46, 284, 480, 112])
geompy.addToStudy( Points_NACA0012_2_txt, 'Points_NACA0012_2.txt' )
geompy.addToStudy( Polyline_1_1, 'Polyline_1_1' )
geompy.addToStudy( Face_1, 'Face_1' )
geompy.addToStudy( Face_2, 'Face_2' )
geompy.addToStudy( Translation_1, 'Translation_1' )
geompy.addToStudy( Vertex_1, 'Vertex_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )
geompy.addToStudy( Vertex_2, 'Vertex_2' )
geompy.addToStudy( Vertex_3, 'Vertex_3' )
geompy.addToStudy( Vertex_4, 'Vertex_4' )
geompy.addToStudy( Vertex_5, 'Vertex_5' )
geompy.addToStudy( Vertex_6, 'Vertex_6' )
geompy.addToStudy( Vertex_7, 'Vertex_7' )
geompy.addToStudy( Vertex_8, 'Vertex_8' )
geompy.addToStudy( Line_1, 'Line_1' )
geompy.addToStudy( Line_2, 'Line_2' )
geompy.addToStudy( Line_3, 'Line_3' )
geompy.addToStudy( Line_4, 'Line_4' )
geompy.addToStudy( Line_5, 'Line_5' )
geompy.addToStudyInFather( Line_4, Line_4_vertex_3, 'Line_4:vertex_3' )
geompy.addToStudy( Line_6, 'Line_6' )
geompy.addToStudyInFather( Line_6, Line_6_vertex_2, 'Line_6:vertex_2' )
geompy.addToStudy( Line_7, 'Line_7' )
geompy.addToStudyInFather( Line_2, Line_2_vertex_2, 'Line_2:vertex_2' )
geompy.addToStudy( Line_8, 'Line_8' )
geompy.addToStudy( Partition_1, 'Partition_1' )
geompy.addToStudyInFather( Partition_1, Esq_Dir, 'Esq_Dir' )
geompy.addToStudyInFather( Partition_1, cima_baixo, 'cima_baixo' )
geompy.addToStudyInFather( Partition_1, linhas_cima_baixo, 'linhas_cima_baixo' )
geompy.addToStudyInFather( Partition_1, linhas_dir_esq, 'linhas_dir_esq' )
geompy.addToStudyInFather( Partition_1, aerofolio, 'aerofolio' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_1 = smesh.Mesh(Partition_1,'Mesh_1')
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 0.1 )
NETGEN_2D_Parameters_1.SetMinSize( 0.001 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 2 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 88 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 168 )
Esq_Dir_1 = Mesh_1.GroupOnGeom(Esq_Dir,'Esq_Dir',SMESH.FACE)
cima_baixo_1 = Mesh_1.GroupOnGeom(cima_baixo,'cima_baixo',SMESH.FACE)
linhas_cima_baixo_1 = Mesh_1.GroupOnGeom(linhas_cima_baixo,'linhas_cima_baixo',SMESH.EDGE)
linhas_dir_esq_1 = Mesh_1.GroupOnGeom(linhas_dir_esq,'linhas_dir_esq',SMESH.EDGE)
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()
smeshObj_1 = smesh.CreateHypothesis('QuadrangleParams')
smeshObj_2 = smesh.CreateHypothesis('NETGEN_Parameters_2D', 'NETGENEngine')
smeshObj_3 = smesh.CreateHypothesis('ProjectionSource2D')
Regular_1D = Mesh_1.Segment(geom=Esq_Dir)
Sub_mesh_1 = Regular_1D.GetSubMesh()
Number_of_Segments_1 = Regular_1D.NumberOfSegments(10)
Quadrangle_2D = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=Esq_Dir)
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()
Regular_1D_1 = Mesh_1.Segment(geom=cima_baixo)
Sub_mesh_2 = Regular_1D_1.GetSubMesh()
Number_of_Segments_2 = Regular_1D_1.NumberOfSegments(2)
Quadrangle_2D_1 = Mesh_1.Quadrangle(algo=smeshBuilder.QUADRANGLE,geom=cima_baixo)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_1, Sub_mesh_2 ] ])
Mesh_1.Clear()
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_2, Sub_mesh_1 ] ])
Mesh_1.Clear()
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()
status = Mesh_1.RemoveHypothesis(NETGEN_2D_Parameters_1)
NETGEN_2D_Parameters_2 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_2.SetMaxSize( 0.1 )
NETGEN_2D_Parameters_2.SetMinSize( 0.001 )
NETGEN_2D_Parameters_2.SetSecondOrder( 0 )
NETGEN_2D_Parameters_2.SetOptimize( 1 )
NETGEN_2D_Parameters_2.SetFineness( 3 )
NETGEN_2D_Parameters_2.SetChordalError( -1 )
NETGEN_2D_Parameters_2.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_2.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_2.SetFuseEdges( 1 )
NETGEN_2D_Parameters_2.SetWorstElemMeasure( 0 )
NETGEN_2D_Parameters_2.SetUseDelauney( 0 )
NETGEN_2D_Parameters_2.SetCheckChartBoundary( 0 )
NETGEN_2D_Parameters_2.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_2.SetWorstElemMeasure( 88 )
NETGEN_2D_Parameters_2.SetCheckChartBoundary( 168 )
Viscous_Layers_2D_1 = NETGEN_1D_2D.ViscousLayers2D(0.03,10,1.2,[ 232, 484, 294, 418, 314, 52, 98, 410, 452, 236, 516, 190, 300, 290, 356, 446, 104, 130, 212, 382, 310, 476, 472, 454, 204, 198, 254, 426, 58, 422, 82, 158, 490, 156, 210, 276, 414, 306, 358, 432, 72, 136, 466, 380, 260, 496, 280, 402, 458, 140, 160, 238, 372, 68, 134, 520, 262, 388, 154, 488, 218, 330, 346, 386, 440, 90, 508, 296, 428, 178, 244, 242, 370, 56, 70, 184, 150, 322, 352, 76, 152, 270, 348, 406, 96, 110, 486, 256, 362, 462, 312, 240, 106, 456, 172, 114, 298, 366, 84, 200, 384, 66, 196, 216, 332, 368, 338, 94, 438, 168, 498, 272, 138, 304, 320, 474, 430, 80, 460, 186, 164, 504, 378, 328, 374, 124, 142, 224, 318, 44, 392, 444, 308, 510, 464, 188, 230, 246, 340, 88, 434, 120, 500, 404, 220, 250, 400, 442, 174, 162, 470, 482, 326, 50, 394, 292, 41, 144, 166, 194, 274, 376, 420, 78, 126, 514, 336, 182, 228, 492, 258, 302, 398, 450, 146, 506, 494, 252, 102, 122, 268, 396, 86, 214, 208, 206, 436, 390, 64, 180, 518, 248, 416, 148, 512, 278, 266, 344, 48, 74, 128, 264, 108, 92, 116, 132, 316, 350, 412, 100, 176, 468, 234, 360, 226, 334, 288, 408, 60, 448, 192, 478, 286, 354, 54, 170, 282, 502, 342, 62, 118, 222, 202, 324, 364, 424, 46, 284, 480, 112 ],0)
Mesh_1.Clear()
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_1, Sub_mesh_2 ] ])
Mesh_1.Clear()
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_2, Sub_mesh_1 ] ])
Mesh_1.Clear()
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()
Regular_1D_2 = Mesh_1.Segment(geom=linhas_dir_esq)
Sub_mesh_3 = Regular_1D_2.GetSubMesh()
Number_of_Segments_3 = Regular_1D_2.NumberOfSegments(6)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_3, Sub_mesh_2, Sub_mesh_1 ] ])
Regular_1D_3 = Mesh_1.Segment(geom=linhas_cima_baixo)
Sub_mesh_4 = Regular_1D_3.GetSubMesh()
Number_of_Segments_4 = Regular_1D_3.NumberOfSegments(20)
isDone = Mesh_1.SetMeshOrder( [ [ Sub_mesh_4, Sub_mesh_3, Sub_mesh_2, Sub_mesh_1 ] ])
Mesh_1.Clear()
isDone = Mesh_1.Compute()
[ Esq_Dir_1, cima_baixo_1, linhas_cima_baixo_1, linhas_dir_esq_1 ] = Mesh_1.GetGroups()

## some objects were removed
aStudyBuilder = salome.myStudy.NewBuilder()
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_3))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_2))
if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

## Set names of Mesh objects
smesh.SetName(cima_baixo_1, 'cima_baixo')
smesh.SetName(Number_of_Segments_4, 'Number of Segments_4')
smesh.SetName(Esq_Dir_1, 'Esq_Dir')
smesh.SetName(Quadrangle_2D.GetAlgorithm(), 'Quadrangle_2D')
smesh.SetName(Regular_1D.GetAlgorithm(), 'Regular_1D')
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Number_of_Segments_1, 'Number of Segments_1')
smesh.SetName(Number_of_Segments_2, 'Number of Segments_2')
smesh.SetName(NETGEN_2D_Parameters_2, 'NETGEN 2D Parameters_2')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(linhas_dir_esq_1, 'linhas_dir_esq')
smesh.SetName(linhas_cima_baixo_1, 'linhas_cima_baixo')
smesh.SetName(Viscous_Layers_2D_1, 'Viscous Layers 2D_1')
smesh.SetName(Number_of_Segments_3, 'Number of Segments_3')
smesh.SetName(Sub_mesh_4, 'Sub-mesh_4')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')
smesh.SetName(Sub_mesh_3, 'Sub-mesh_3')
smesh.SetName(Sub_mesh_2, 'Sub-mesh_2')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
