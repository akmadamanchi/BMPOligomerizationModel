from __future__ import print_function
from pysb import *
_pysb_doctest_suppress_modelexistswarning = True

Model()

Monomer('ALK3')
Monomer('ALK8')
Monomer('RII')
Monomer('BMP2_ALK3')
Monomer('BMP2_ALK8')
Monomer('BMP2_RII')
Monomer('BMP2_ALK3_ALK3')
Monomer('BMP2_ALK3_ALK8')
Monomer('BMP2_ALK3_RII')
Monomer('BMP2_ALK8_ALK8')
Monomer('BMP2_ALK8_RII')
Monomer('BMP2_RII_RII')
Monomer('BMP2_ALK3_ALK3_RII')
Monomer('BMP2_ALK3_ALK8_RII')
Monomer('BMP2_ALK3_RII_RII')
Monomer('BMP2_ALK8_ALK8_RII')
Monomer('BMP2_ALK8_RII_RII')
Monomer('BMP2_ALK3_ALK3_RII_RII')
Monomer('BMP2_ALK3_ALK8_RII_RII')
Monomer('BMP2_ALK8_ALK8_RII_RII')

Monomer('BMP7_ALK3')
Monomer('BMP7_ALK8')
Monomer('BMP7_RII')
Monomer('BMP7_ALK3_ALK3')
Monomer('BMP7_ALK3_ALK8')
Monomer('BMP7_ALK3_RII')
Monomer('BMP7_ALK8_ALK8')
Monomer('BMP7_ALK8_RII')
Monomer('BMP7_RII_RII')
Monomer('BMP7_ALK3_ALK3_RII')
Monomer('BMP7_ALK3_ALK8_RII')
Monomer('BMP7_ALK3_RII_RII')
Monomer('BMP7_ALK8_ALK8_RII')
Monomer('BMP7_ALK8_RII_RII')
Monomer('BMP7_ALK3_ALK3_RII_RII')
Monomer('BMP7_ALK3_ALK8_RII_RII')
Monomer('BMP7_ALK8_ALK8_RII_RII')

Monomer('BMP27_ALK3')
Monomer('BMP27_ALK8')
Monomer('BMP27_RII')
Monomer('BMP27_ALK3_ALK3')
Monomer('BMP27_ALK3_ALK8')
Monomer('BMP27_ALK3_RII')
Monomer('BMP27_ALK8_ALK8')
Monomer('BMP27_ALK8_RII')
Monomer('BMP27_RII_RII')
Monomer('BMP27_ALK3_ALK3_RII')
Monomer('BMP27_ALK3_ALK8_RII')
Monomer('BMP27_ALK3_RII_RII')
Monomer('BMP27_ALK8_ALK8_RII')
Monomer('BMP27_ALK8_RII_RII')
Monomer('BMP27_ALK3_ALK3_RII_RII')
Monomer('BMP27_ALK3_ALK8_RII_RII')
Monomer('BMP27_ALK8_ALK8_RII_RII')



#RXN 1
Parameter('k1f', .0005*1*Z)
Parameter('k1r', .0004)
#       ALk3 <-> BMP2_ALK3         0.0005
Rule('ALK3_to_BMP2_ALK3', ALK3() <> BMP2_ALK3(), k1f, k1r)


#RXN 2
Parameter('k2f', 0.0000011694*1*Z)
Parameter('k2r', 0.001197)
#       ALk8 -> BMP2_ALK8         0.0000011694
Rule('ALK8_to_BMP2_ALK8', ALK8() <> BMP2_ALK8(), k2f, k2r)


#RXN 3
Parameter('k3f', .0015*1*Z)
Parameter('k3r', .07)
#       RII -> BMP2_RII
Rule('RII_to_BMP2_RII', RII() <> BMP2_RII(), k3f, k3r)

#RXN 4
Parameter('k4f', 0.0005*1*50)
Parameter('k4r', 0.0004)
#       ALK3 + BMP2_ALK3 -> BMP2_ALK3_ALK3
Rule('BMP2_ALK3_plusALK3_to_BMP2_ALK3_ALK3', ALK3() + BMP2_ALK3() <> BMP2_ALK3_ALK3(), k4f, k4r)

#RXN 5
Parameter('k5f', 0.0000011694*1*50)
Parameter('k5r', 0.001197)
#       ALK8 + BMP2_ALK3 -> BMP2_ALK3_ALK8
Rule('BMP2_ALK3_plusALK8_to_BMP2_ALK3_ALK8', ALK8() + BMP2_ALK3() <> BMP2_ALK3_ALK8(), k5f, k5r)


#RXN 6
Parameter('k6f', 0.0015*1*50)
Parameter('k6r', 0.07)
#       RII + BMP2_ALK3 -> BMP2_ALK3_RII
Rule('BMP2_ALK3_plusRII_to_BMP2_ALK3_RII', RII() + BMP2_ALK3() <> BMP2_ALK3_RII(), k6f, k6r)


#RXN 7
Parameter('k7f', 0.0005*1*50)
Parameter('k7r', 0.0004)
#       ALK3 + BMP2_ALK8 -> BMP2_ALK3_ALK8
Rule('BMP2_ALK8_plusALK3_to_BMP2_ALK3_ALK8', ALK3() + BMP2_ALK8() <> BMP2_ALK3_ALK8(), k7f, k7r)

#RXN 8 
Parameter('k8f', 0.0000011694*1*50)
Parameter('k8r', 0.001197)
#       BMP2_Alk8 * Alk8 -> BMP2_ALK8_ALK8
Rule('BMP2_ALK8_plusAlk8_to_BMP2_ALK8_ALK8', ALK8() + BMP2_ALK8() <> BMP2_ALK8_ALK8(), k8f, k8r)

#RXN 9
Parameter('k9f', 0.0015*1*50 )
Parameter('k9r', .07)
#       BMP2_ALK8 * RII -> BMP2_ALK8_RII
Rule('BMP2_ALK8_plusRII_to_BMP2_ALK8_RII', RII() + BMP2_ALK8() <> BMP2_ALK8_RII(), k9f, k9r)

#RXN 10 BMP2_RII * ALK3 -> BMP2_ALK3_RII
Parameter ('k10f', 0.0005 * 50 * 1)
Parameter ('k10r', 0.0004)
Rule('BMP2_RII_plusALK3_to_BMP2_ALK3_RII', ALK3() + BMP2_RII() <> BMP2_ALK3_RII(), k10f, k10r)

#RXN 11 BMP2_RII * ALK8 -> BMP2_ALK8_RII
Parameter ('k11f', 0.0000011694*1*50)
Parameter ('k11r', 0.001197)
Rule ('BMP2_RII_plusALK8_to_BMP2_ALK8_RII', ALK8() + BMP2_RII() <> BMP2_ALK8_RII(), k11f, k11r)

#RXN 12 BMP2_RII * RII -> BMP2_RII_RII  
Parameter ('k12f', 0.0015 * 1 * 50)
Parameter ('k12r', 0.07)
Rule ('BMP2_RII_plusRII_to_BMP2_RII_RII', RII() + BMP2_RII() <> BMP2_RII_RII(), k12f,  k12r)

#RXN 13 BMP2_Alk8_Alk8 * RII -> BMP2_Alk8_Alk8_RII
Parameter ('k13f', 0.0015 * 1 * 50)
Parameter ('k13r', 0.07)
Rule ('BMP2_ALK8_ALK8_plusRII_to_BMP2_ALK8_ALK8_RII', RII() + BMP2_ALK8_ALK8() <> BMP2_ALK8_ALK8_RII(), k13f, k13r)

#RXN 14 BMP2_RII_RII * Alk3 -> BMP2_Alk3_RII_RII
Parameter ('k14f', 0.0005 * 50 * 1)
Parameter ('k14r', 0.0004)
Rule('BMP2_RII_RIIplusALK3_to_BMP2_ALK3_RII_RII', ALK3() + BMP2_RII_RII() <> BMP2_ALK3_RII_RII(), k14f, k14r)

#RXN 15 BMP2_RII_RII * Alk8 -> BMP2_Alk8_RII_RII
Parameter ('k15f', 0.0000011694*1*50)
Parameter ('k15r', 0.001197)
Rule ('BMP2_RII_RIIplusALK8_to_BMP2_ALK8_RII_RII', ALK8() + BMP2_RII_RII() <> BMP2_ALK8_RII_RII(), k15f, k15r)

#RXN 16 BMP2_Alk3_Alk3 * RII -> BMP2_Alk3_Alk3_RII 
Parameter ('k16f', 0.0015 * 1 * 50)
Parameter ('k16r', 0.07)
Rule ('BMP2_ALK3_ALK3_plusRII_to_BMP2_ALK3_ALK3_RII', RII() + BMP2_ALK3_ALK3() <> BMP2_ALK3_ALK3_RII(), k16f, k16r)

#RXN 17 BMP2_ALK3_ALK8 * RII -> BMP2_ALK3_ALK8_RII
Parameter ('k17f', 0.0015 * 1 * 50)
Parameter ('k17r', 0.07)
Rule ('BMP2_ALK3_ALK8_plusRII_to_BMP2_ALK3_ALK8_RII', RII() + BMP2_ALK3_ALK8() <> BMP2_ALK3_ALK8_RII(), k17f, k17r)

#RXN 18 BMP2_Alk3_RII * Alk3 -> BMP2_Alk3_Alk3_RII
Parameter ('k18f', 0.0005 * 1 * 50)
Parameter ('k18r', 0.0004)
Rule ('BMP2_ALK3_RII_plusALK3_to_BMP2_ALK3_ALK3_RII', ALK3() + BMP2_ALK3_RII() <> BMP2_ALK3_ALK3_RII(), k18f, k18r)

#RXN 19 BMP2_Alk3_RII * Alk8 -> BMP2_Alk3_Alk8_RII
Parameter ('k19f', 0.0000011694 * 1 *50)
Parameter ('k19r', 0.001197)
Rule ('BMP2_ALK3_RIIplusALK8_to_BMP2_ALK3_ALK8_RII', ALK8() + BMP2_ALK3_RII() <> BMP2_ALK3_ALK8_RII(), k19f, k19r)

#RXN 20 BMP2_Alk3_RII * RII -> BMP2_Alk3_RII_RII
Parameter ('k20f', 0.0015 * 1 * 50)
Parameter ('k20r', 0.07)
Rule ('BMP2_ALK3_RII_plusRII_to_BMP2_ALK3_RII_RII', RII() + BMP2_ALK3_RII() <> BMP2_ALK3_RII_RII(), k20f, k20r)


#RXN 21 BMP2_Alk8_RII * Alk3 -> BMP2_Alk3_Alk8_RII
Parameter ('k21f', 0.0005 * 1 * 50)
Parameter ('k21r', 0.0004)
Rule ('BMP2_ALK8_RII_plusALK3_to_BMP2_ALK3_ALK8_RII', ALK3() + BMP2_ALK8_RII() <> BMP2_ALK3_ALK8_RII(), k21f, k21r)

#RXN 22 BMP2_Alk8_RII * Alk8 -> BMP2_Alk8_Alk8_RII
Parameter ('k22f', 0.0000011694 * 1 *50)
Parameter ('k22r', 0.001197)
Rule ('BMP2_ALK8_RIIplusALK8_to_BMP2_ALK8_ALK8_RII', ALK8() + BMP2_ALK8_RII() <> BMP2_ALK8_ALK8_RII(), k22f, k22r)



#RXN 23 BMP2_Alk8_RII * RII -> BMP2_Alk8_RII_RII
Parameter ('k23f', 0.0015 * 1 * 50)
Parameter ('k23r', 0.07)
Rule ('BMP2_ALK8_RII_plusRII_to_BMP2_ALK8_RII_RII', RII() + BMP2_ALK8_RII() <> BMP2_ALK8_RII_RII(), k23f, k23r)

#RXN 24 BMP2_Alk3_Alk3_RII * RII -> BMP2_Alk3_Alk3_RII_RII
Parameter ('k24f', 0.0015 * 1 * 50)
Parameter ('k24r', 0.07)
Rule ('BMP2_ALK3_ALK3_RII_plusRII_to_BMP2_ALK3_ALK3_RII_RII', RII() + BMP2_ALK3_ALK3_RII() <> BMP2_ALK3_ALK3_RII_RII(), k24f, k24r)

#RXN 25 BMP2_Alk3_Alk8_RII * RII -> BMP2_Alk3_Alk8_RII_RII1
Parameter ('k25f', 0.0015 * 1 * 50)
Parameter ('k25r', 0.07)
Rule ('BMP2_ALK3_ALK8_RII_plusRII_to_BMP2_ALK3_ALK8_RII_RII', RII() + BMP2_ALK3_ALK8_RII() <> BMP2_ALK3_ALK8_RII_RII(), k25f, k25r)

#RXN 26 BMP2_Alk3_RII_RII * Alk3 -> BMP2_Alk3_Alk3_RII_RII
Parameter ('k26f', 0.0005 * 1 * 50)
Parameter ('k26r', 0.0004)
Rule ('BMP2_ALK3_RII_RII_plusALK3_to_BMP2_ALK3_ALK3_RII_RII', ALK3() + BMP2_ALK3_RII_RII() <> BMP2_ALK3_ALK3_RII_RII(), k26f, k26r)

#RXN 27 BMP2_Alk3_RII_RII * Alk8 -> BMP2_Alk3_Alk8_RII_RII
Parameter ('k27f', 0.0000011694 * 1 * 50)
Parameter ('k27r', 0.001197)
Rule ('BMP2_ALK3_RII_RIIplusALK8_to_BMP2_ALK3_ALK8_RII_RII', ALK8() + BMP2_ALK3_RII_RII() <> BMP2_ALK3_ALK8_RII_RII(), k27f, k27r)

#RXN 28 BMP2_Alk8_Alk8_RII * RII -> BMP2_Alk8_Alk8_RII_RII
Parameter ('k28f', 0.0015 * 1 * 50)
Parameter ('k28r', 0.07)
Rule ('BMP2_ALK8_ALK8_RII_plusRII_to_BMP2_ALK8_ALK8_RII_RII', RII() + BMP2_ALK8_ALK8_RII() <> BMP2_ALK8_ALK8_RII_RII(), k28f, k28r)

#RXN 29 BMP2_Alk8_RII_RII * Alk3 -> BMP2_Alk3_Alk8_RII_RII
Parameter ('k29f', 0.0005 * 1 * 50)
Parameter ('k29r', 0.0004)
Rule ('BMP2_ALK8_RII_RII_plusALK3_to_BMP2_ALK3_ALK8_RII_RII', ALK3() + BMP2_ALK8_RII_RII() <> BMP2_ALK3_ALK8_RII_RII(), k29f, k29r)

#RXN 30 BMP2_Alk8_RII_RII * Alk8 -> BMP2_Alk8_Alk8_RII_RII
Parameter ('k30f', 0.0000011694 * 1 * 50)
Parameter ('k30r', 0.001197)
Rule ('BMP2_ALK8_RII_RIIplusALK8_to_BMP2_ALK8_ALK8_RII_RII', ALK8() + BMP2_ALK8_RII_RII() <> BMP2_ALK8_ALK8_RII_RII(), k30f, k30r)


#RXN 1
Parameter('k31f', 0.00014 * 1 *Z)
Parameter('k31r', 0.0079)
#       ALk3 <-> BMP7_ALK3         0.0005
Rule('ALK3_to_BMP7_ALK3', ALK3() <> BMP7_ALK3(), k31f, k31r)


#RXN 2
Parameter('k32f', 0.000002338*1*Z)
Parameter('k32r', 0.001197)
#       ALk8 -> BMP7_ALK8         0.0000011694
Rule('ALK8_to_BMP7_ALK8', ALK8() <> BMP7_ALK8(), k32f, k32r)


#RXN 3
Parameter('k33f', 0.0014*1*Z)
Parameter('k33r', 0.009)
#       RII -> BMP7_RII
Rule('RII_to_BMP7_RII', RII() <> BMP7_RII(), k33f, k33r)

#RXN 4
Parameter('k34f', 0.00014*1*50)
Parameter('k34r', 0.0079)
#       ALK3 + BMP7_ALK3 -> BMP7_ALK3_ALK3
Rule('BMP7_ALK3_plusALK3_to_BMP7_ALK3_ALK3', ALK3() + BMP7_ALK3() <> BMP7_ALK3_ALK3(), k34f, k34r)

#RXN 5
Parameter('k35f', 0.000002338*1*50)
Parameter('k35r', 0.001197)
#       ALK8 + BMP7_ALK3 -> BMP7_ALK3_ALK8
Rule('BMP7_ALK3_plusALK8_to_BMP7_ALK3_ALK8', ALK8() + BMP7_ALK3() <> BMP7_ALK3_ALK8(), k35f, k35r)


#RXN 6
Parameter('k36f', 0.0014*1*50)
Parameter('k36r', 0.009)
#       RII + BMP7_ALK3 -> BMP7_ALK3_RII
Rule('BMP7_ALK3_plusRII_to_BMP7_ALK3_RII', RII() + BMP7_ALK3() <> BMP7_ALK3_RII(), k36f, k36r)


#RXN 7
Parameter('k37f', 0.00014*1*50)
Parameter('k37r', 0.0079)
#       ALK3 + BMP7_ALK8 -> BMP7_ALK3_ALK8
Rule('BMP7_ALK8_plusALK3_to_BMP7_ALK3_ALK8', ALK3() + BMP7_ALK8() <> BMP7_ALK3_ALK8(), k37f, k37r)

#RXN 8 
Parameter('k38f', 0.000002338*1*50)
Parameter('k38r', 0.001197)
#       BMP7_Alk8 * Alk8 -> BMP7_ALK8_ALK8
Rule('BMP7_ALK8_plusAlk8_to_BMP7_ALK8_ALK8', ALK8() + BMP7_ALK8() <> BMP7_ALK8_ALK8(), k38f, k38r)

#RXN 9
Parameter('k39f', 0.0014*1*50 )
Parameter('k39r', 0.009)
#       BMP7_ALK8 * RII -> BMP7_ALK8_RII
Rule('BMP7_ALK8_plusRII_to_BMP7_ALK8_RII', RII() + BMP7_ALK8() <> BMP7_ALK8_RII(), k39f, k39r)

#RXN 10 BMP7_RII * ALK3 -> BMP7_ALK3_RII
Parameter ('k40f', 0.00014 * 50 * 1)
Parameter ('k40r', 0.0079)
Rule('BMP7_RII_plusALK3_to_BMP7_ALK3_RII', ALK3() + BMP7_RII() <> BMP7_ALK3_RII(), k40f, k40r)

#RXN 11 BMP7_RII * ALK8 -> BMP7_ALK8_RII
Parameter ('k41f', 0.000002338 * 1 * 50)
Parameter ('k41r', 0.001197)
Rule ('BMP7_RII_plusALK8_to_BMP7_ALK8_RII', ALK8() + BMP7_RII() <> BMP7_ALK8_RII(), k41f, k41r)

#RXN 12 BMP7_RII * RII -> BMP7_RII_RII  
Parameter ('k42f', 0.0014 * 1 * 50)
Parameter ('k42r', 0.009)
Rule ('BMP7_RII_plusRII_to_BMP7_RII_RII', RII() + BMP7_RII() <> BMP7_RII_RII(), k42f,  k42r)

#RXN 13 BMP7_Alk8_Alk8 * RII -> BMP7_Alk8_Alk8_RII
Parameter ('k43f', 0.0014 * 1 * 50)
Parameter ('k43r', 0.009)
Rule ('BMP7_ALK8_ALK8_plusRII_to_BMP7_ALK8_ALK8_RII', RII() + BMP7_ALK8_ALK8() <> BMP7_ALK8_ALK8_RII(), k43f, k43r)

#RXN 14 BMP7_RII_RII * Alk3 -> BMP7_Alk3_RII_RII
Parameter ('k44f', 0.00014 * 50 * 1)
Parameter ('k44r', 0.0079)
Rule('BMP7_RII_RIIplusALK3_to_BMP7_ALK3_RII_RII', ALK3() + BMP7_RII_RII() <> BMP7_ALK3_RII_RII(), k44f, k44r)

#RXN 15 BMP7_RII_RII * Alk8 -> BMP7_Alk8_RII_RII
Parameter ('k45f', 0.000002338 * 1 * 50)
Parameter ('k45r', 0.001197)
Rule ('BMP7_RII_RIIplusALK8_to_BMP7_ALK8_RII_RII', ALK8() + BMP7_RII_RII() <> BMP7_ALK8_RII_RII(), k45f, k45r)

#RXN 16 BMP7_Alk3_Alk3 * RII -> BMP7_Alk3_Alk3_RII 
Parameter ('k46f', 0.0014 * 1 * 50)
Parameter ('k46r', 0.009)
Rule ('BMP7_ALK3_ALK3_plusRII_to_BMP7_ALK3_ALK3_RII', RII() + BMP7_ALK3_ALK3() <> BMP7_ALK3_ALK3_RII(), k46f, k46r)

#RXN 17 BMP7_ALK3_ALK8 * RII -> BMP7_ALK3_ALK8_RII
Parameter ('k47f', 0.0014 * 1 * 50)
Parameter ('k47r', 0.009)
Rule ('BMP7_ALK3_ALK8_plusRII_to_BMP7_ALK3_ALK8_RII', RII() + BMP7_ALK3_ALK8() <> BMP7_ALK3_ALK8_RII(), k47f, k47r)

#RXN 18 BMP7_Alk3_RII * Alk3 -> BMP7_Alk3_Alk3_RII
Parameter ('k48f', 0.00014 * 1 * 50)
Parameter ('k48r', 0.0079)
Rule ('BMP7_ALK3_RII_plusALK3_to_BMP7_ALK3_ALK3_RII', ALK3() + BMP7_ALK3_RII() <> BMP7_ALK3_ALK3_RII(), k48f, k48r)

#RXN 19 BMP7_Alk3_RII * Alk8 -> BMP7_Alk3_Alk8_RII
Parameter ('k49f', 0.000002338 * 1 *50)
Parameter ('k49r', 0.001197)
Rule ('BMP7_ALK3_RIIplusALK8_to_BMP7_ALK3_ALK8_RII', ALK8() + BMP7_ALK3_RII() <> BMP7_ALK3_ALK8_RII(), k49f, k49r)

#RXN 20 BMP7_Alk3_RII * RII -> BMP7_Alk3_RII_RII
Parameter ('k50f', 0.0014 * 1 * 50)
Parameter ('k50r', 0.009)
Rule ('BMP7_ALK3_RII_plusRII_to_BMP7_ALK3_RII_RII', RII() + BMP7_ALK3_RII() <> BMP7_ALK3_RII_RII(), k50f, k50r)


#RXN 21 BMP7_Alk8_RII * Alk3 -> BMP7_Alk3_Alk8_RII
Parameter ('k51f', 0.00014 * 1 * 50)
Parameter ('k51r', 0.0079)
Rule ('BMP7_ALK8_RII_plusALK3_to_BMP7_ALK3_ALK8_RII', ALK3() + BMP7_ALK8_RII() <> BMP7_ALK3_ALK8_RII(), k51f, k51r)

#RXN 22 BMP7_Alk8_RII * Alk8 -> BMP7_Alk8_Alk8_RII
Parameter ('k52f', 0.000002338 * 1 *50)
Parameter ('k52r', 0.001197)
Rule ('BMP7_ALK8_RIIplusALK8_to_BMP7_ALK8_ALK8_RII', ALK8() + BMP7_ALK8_RII() <> BMP7_ALK8_ALK8_RII(), k52f, k52r)



#RXN 23 BMP7_Alk8_RII * RII -> BMP7_Alk8_RII_RII
Parameter ('k53f', 0.0014 * 1 * 50)
Parameter ('k53r', 0.009)
Rule ('BMP7_ALK8_RII_plusRII_to_BMP7_ALK8_RII_RII', RII() + BMP7_ALK8_RII() <> BMP7_ALK8_RII_RII(), k53f, k53r)

#RXN 24 BMP7_Alk3_Alk3_RII * RII -> BMP7_Alk3_Alk3_RII_RII
Parameter ('k54f', 0.0014 * 1 * 50)
Parameter ('k54r', 0.009)
Rule ('BMP7_ALK3_ALK3_RII_plusRII_to_BMP7_ALK3_ALK3_RII_RII', RII() + BMP7_ALK3_ALK3_RII() <> BMP7_ALK3_ALK3_RII_RII(), k54f, k54r)

#RXN 25 BMP7_Alk3_Alk8_RII * RII -> BMP7_Alk3_Alk8_RII_RII1
Parameter ('k55f', 0.0014 * 1 * 50)
Parameter ('k55r', 0.009)
Rule ('BMP7_ALK3_ALK8_RII_plusRII_to_BMP7_ALK3_ALK8_RII_RII', RII() + BMP7_ALK3_ALK8_RII() <> BMP7_ALK3_ALK8_RII_RII(), k55f, k55r)

#RXN 26 BMP7_Alk3_RII_RII * Alk3 -> BMP7_Alk3_Alk3_RII_RII
Parameter ('k56f', 0.00014 * 1 * 50)
Parameter ('k56r', 0.0079)
Rule ('BMP7_ALK3_RII_RII_plusALK3_to_BMP7_ALK3_ALK3_RII_RII', ALK3() + BMP7_ALK3_RII_RII() <> BMP7_ALK3_ALK3_RII_RII(), k56f, k56r)

#RXN 27 BMP7_Alk3_RII_RII * Alk8 -> BMP7_Alk3_Alk8_RII_RII
Parameter ('k57f', 0.000002338 * 1 * 50)
Parameter ('k57r', 0.001197)
Rule ('BMP7_ALK3_RII_RIIplusALK8_to_BMP7_ALK3_ALK8_RII_RII', ALK8() + BMP7_ALK3_RII_RII() <> BMP7_ALK3_ALK8_RII_RII(), k57f, k57r)

#RXN 28 BMP7_Alk8_Alk8_RII * RII -> BMP7_Alk8_Alk8_RII_RII
Parameter ('k58f', 0.0014 * 1 * 50)
Parameter ('k58r', 0.009)
Rule ('BMP7_ALK8_ALK8_RII_plusRII_to_BMP7_ALK8_ALK8_RII_RII', RII() + BMP7_ALK8_ALK8_RII() <> BMP7_ALK8_ALK8_RII_RII(), k58f, k58r)

#RXN 29 BMP7_Alk8_RII_RII * Alk3 -> BMP7_Alk3_Alk8_RII_RII
Parameter ('k59f', 0.00014 * 1 * 50)
Parameter ('k59r', 0.0079)
Rule ('BMP7_ALK8_RII_RII_plusALK3_to_BMP7_ALK3_ALK8_RII_RII', ALK3() + BMP7_ALK8_RII_RII() <> BMP7_ALK3_ALK8_RII_RII(), k59f, k59r)

#RXN 30 BMP7_Alk8_RII_RII * Alk8 -> BMP7_Alk8_Alk8_RII_RII
Parameter ('k60f', 0.000002338 * 1 * 50)
Parameter ('k60r', 0.001197)
Rule ('BMP7_ALK8_RII_RIIplusALK8_to_BMP7_ALK8_ALK8_RII_RII', ALK8() + BMP7_ALK8_RII_RII() <> BMP7_ALK8_ALK8_RII_RII(), k60f, k60r)

#RXN 61
Parameter('k61f', 0.0005 * 1 *Z)
Parameter('k61r', 0.0004)
#       ALk3 <-> BMP27_ALK3         0.0005
Rule('ALK3_to_BMP27_ALK3', ALK3() <> BMP27_ALK3(), k61f, k61r)


#RXN 62
Parameter('k62f', 0.000002338*1*Z)
Parameter('k62r', 0.001197)
#       ALk8 -> BMP27_ALK8         0.0000011694
Rule('ALK8_to_BMP27_ALK8', ALK8() <> BMP27_ALK8(), k62f, k62r)


#RXN 63
Parameter('k63f', 0.0014*1*Z)
Parameter('k63r', 0.009)
#       RII -> BMP27_RII
Rule('RII_to_BMP27_RII', RII() <> BMP27_RII(), k63f, k63r)

#RXN 64
Parameter('k64f', 0.00014*1*50)
Parameter('k64r', 0.0079)
#       ALK3 + BMP27_ALK3 -> BMP27_ALK3_ALK3
Rule('BMP27_ALK3_plusALK3_to_BMP27_ALK3_ALK3', ALK3() + BMP27_ALK3() <> BMP27_ALK3_ALK3(), k64f, k64r)

#RXN 65
Parameter('k65f', 0.000002338*1*50)
Parameter('k65r', 0.001197)
#       ALK8 + BMP27_ALK3 -> BMP27_ALK3_ALK8
Rule('BMP27_ALK3_plusALK8_to_BMP27_ALK3_ALK8', ALK8() + BMP27_ALK3() <> BMP27_ALK3_ALK8(), k65f, k65r)


#RXN 66
Parameter('k66f', 0.0014*1*50)
Parameter('k66r', 0.009)
#       RII + BMP27_ALK3 -> BMP27_ALK3_RII
Rule('BMP27_ALK3_plusRII_to_BMP27_ALK3_RII', RII() + BMP27_ALK3() <> BMP27_ALK3_RII(), k66f, k66r)


#RXN 67
Parameter('k67f', 0.0005*1*50)
Parameter('k67r', 0.0004)
#       ALK3 + BMP27_ALK8 -> BMP27_ALK3_ALK8
Rule('BMP27_ALK8_plusALK3_to_BMP27_ALK3_ALK8', ALK3() + BMP27_ALK8() <> BMP27_ALK3_ALK8(), k67f, k67r)

#RXN 68 
Parameter('k68f', 0.0000011694*1*50)
Parameter('k68r', 0.001197)
#       BMP27_Alk8 * Alk8 -> BMP27_ALK8_ALK8
Rule('BMP27_ALK8_plusAlk8_to_BMP27_ALK8_ALK8', ALK8() + BMP27_ALK8() <> BMP27_ALK8_ALK8(), k68f, k68r)

#RXN 69
Parameter('k69f', 0.0014*1*50 )
Parameter('k69r', 0.009)
#       BMP27_ALK8 * RII -> BMP27_ALK8_RII
Rule('BMP27_ALK8_plusRII_to_BMP27_ALK8_RII', RII() + BMP27_ALK8() <> BMP27_ALK8_RII(), k69f, k69r)

#RXN 70 BMP27_RII * ALK3 -> BMP27_ALK3_RII
Parameter ('k70f', 0.0005 * 50 * 1)
Parameter ('k70r', 0.0004)
Rule('BMP27_RII_plusALK3_to_BMP27_ALK3_RII', ALK3() + BMP27_RII() <> BMP27_ALK3_RII(), k70f, k70r)

#RXN 71 BMP27_RII * ALK8 -> BMP27_ALK8_RII
Parameter ('k71f', 0.000002338 * 1 * 50)
Parameter ('k71r', 0.001197)
Rule ('BMP27_RII_plusALK8_to_BMP27_ALK8_RII', ALK8() + BMP27_RII() <> BMP27_ALK8_RII(), k71f, k71r)

#RXN 72 BMP27_RII * RII -> BMP27_RII_RII  
Parameter ('k72f', 0.0015 * 1 * 50)
Parameter ('k72r', 0.07)
Rule ('BMP27_RII_plusRII_to_BMP27_RII_RII', RII() + BMP27_RII() <> BMP27_RII_RII(), k72f,  k12r)

#RXN 73 BMP27_Alk8_Alk8 * RII -> BMP27_Alk8_Alk8_RII
Parameter ('k73f', 0.0014 * 1 * 50)
Parameter ('k73r', 0.009)
Rule ('BMP27_ALK8_ALK8_plusRII_to_BMP27_ALK8_ALK8_RII', RII() + BMP27_ALK8_ALK8() <> BMP27_ALK8_ALK8_RII(), k73f, k73r)

#RXN 74 BMP27_RII_RII * Alk3 -> BMP27_Alk3_RII_RII
Parameter ('k74f', 0.0005 * 50 * 1)
Parameter ('k74r', 0.0004)
Rule('BMP27_RII_RIIplusALK3_to_BMP27_ALK3_RII_RII', ALK3() + BMP27_RII_RII() <> BMP27_ALK3_RII_RII(), k74f, k74r)

#RXN 75 BMP27_RII_RII * Alk8 -> BMP27_Alk8_RII_RII
Parameter ('k75f', 0.000002338 * 1 * 50)
Parameter ('k75r', 0.001197)
Rule ('BMP27_RII_RIIplusALK8_to_BMP27_ALK8_RII_RII', ALK8() + BMP27_RII_RII() <> BMP27_ALK8_RII_RII(), k75f, k75r)

#RXN 76 BMP27_Alk3_Alk3 * RII -> BMP27_Alk3_Alk3_RII 
Parameter ('k76f', 0.0014 * 1 * 50)
Parameter ('k76r', 0.009)
Rule ('BMP27_ALK3_ALK3_plusRII_to_BMP27_ALK3_ALK3_RII', RII() + BMP27_ALK3_ALK3() <> BMP27_ALK3_ALK3_RII(), k76f, k76r)

#RXN 77 BMP27_ALK3_ALK8 * RII -> BMP27_ALK3_ALK8_RII
Parameter ('k77f', 0.0014 * 1 * 50)
Parameter ('k77r', 0.009)
Rule ('BMP27_ALK3_ALK8_plusRII_to_BMP27_ALK3_ALK8_RII', RII() + BMP27_ALK3_ALK8() <> BMP27_ALK3_ALK8_RII(), k77f, k77r)

#RXN 78 BMP27_Alk3_RII * Alk3 -> BMP27_Alk3_Alk3_RII
Parameter ('k78f', 0.00014 * 1 * 50)
Parameter ('k78r', 0.0079)
Rule ('BMP27_ALK3_RII_plusALK3_to_BMP27_ALK3_ALK3_RII', ALK3() + BMP27_ALK3_RII() <> BMP27_ALK3_ALK3_RII(), k78f, k78r)

#RXN 79 BMP27_Alk3_RII * Alk8 -> BMP27_Alk3_Alk8_RII
Parameter ('k79f', 0.000002338 * 1 *50)
Parameter ('k79r', 0.001197)
Rule ('BMP27_ALK3_RIIplusALK8_to_BMP27_ALK3_ALK8_RII', ALK8() + BMP27_ALK3_RII() <> BMP27_ALK3_ALK8_RII(), k79f, k79r)

#RXN 80 BMP27_Alk3_RII * RII -> BMP27_Alk3_RII_RII
Parameter ('k80f', 0.0015 * 1 * 50)
Parameter ('k80r', 0.07)
Rule ('BMP27_ALK3_RII_plusRII_to_BMP27_ALK3_RII_RII', RII() + BMP27_ALK3_RII() <> BMP27_ALK3_RII_RII(), k80f, k80r)


#RXN 81 BMP27_Alk8_RII * Alk3 -> BMP27_Alk3_Alk8_RII
Parameter ('k81f', 0.0005 * 1 * 50)
Parameter ('k81r', 0.0004)
Rule ('BMP27_ALK8_RII_plusALK3_to_BMP27_ALK3_ALK8_RII', ALK3() + BMP27_ALK8_RII() <> BMP27_ALK3_ALK8_RII(), k81f, k81r)

#RXN 82 BMP27_Alk8_RII * Alk8 -> BMP27_Alk8_Alk8_RII
Parameter ('k82f', 0.0000011694 * 1 *50)
Parameter ('k82r', 0.001197)
Rule ('BMP27_ALK8_RIIplusALK8_to_BMP27_ALK8_ALK8_RII', ALK8() + BMP27_ALK8_RII() <> BMP27_ALK8_ALK8_RII(), k82f, k82r)



#RXN 83 BMP27_Alk8_RII * RII -> BMP27_Alk8_RII_RII
Parameter ('k83f', 0.0015 * 1 * 50)
Parameter ('k83r', 0.07)
Rule ('BMP27_ALK8_RII_plusRII_to_BMP27_ALK8_RII_RII', RII() + BMP27_ALK8_RII() <> BMP27_ALK8_RII_RII(), k83f, k83r)

#RXN 84 BMP27_Alk3_Alk3_RII * RII -> BMP27_Alk3_Alk3_RII_RII
Parameter ('k84f', 0.0015 * 1 * 50)
Parameter ('k84r', 0.07)
Rule ('BMP27_ALK3_ALK3_RII_plusRII_to_BMP27_ALK3_ALK3_RII_RII', RII() + BMP27_ALK3_ALK3_RII() <> BMP27_ALK3_ALK3_RII_RII(), k84f, k84r)

#RXN 85 BMP27_Alk3_Alk8_RII * RII -> BMP27_Alk3_Alk8_RII_RII1
Parameter ('k85f', 0.0015 * 1 * 50)
Parameter ('k85r', 0.07)
Rule ('BMP27_ALK3_ALK8_RII_plusRII_to_BMP27_ALK3_ALK8_RII_RII', RII() + BMP27_ALK3_ALK8_RII() <> BMP27_ALK3_ALK8_RII_RII(), k85f, k85r)

#RXN 86 BMP27_Alk3_RII_RII * Alk3 -> BMP27_Alk3_Alk3_RII_RII
Parameter ('k86f', 0.00014 * 1 * 50)
Parameter ('k86r', 0.0079)
Rule ('BMP27_ALK3_RII_RII_plusALK3_to_BMP27_ALK3_ALK3_RII_RII', ALK3() + BMP27_ALK3_RII_RII() <> BMP27_ALK3_ALK3_RII_RII(), k86f, k86r)

#RXN 87 BMP27_Alk3_RII_RII * Alk8 -> BMP27_Alk3_Alk8_RII_RII
Parameter ('k87f', 0.000002338 * 1 * 50)
Parameter ('k87r', 0.001197)
Rule ('BMP27_ALK3_RII_RIIplusALK8_to_BMP27_ALK3_ALK8_RII_RII', ALK8() + BMP27_ALK3_RII_RII() <> BMP27_ALK3_ALK8_RII_RII(), k87f, k87r)

#RXN 88 BMP27_Alk8_Alk8_RII * RII -> BMP27_Alk8_Alk8_RII_RII
Parameter ('k88f', 0.0015 * 1 * 50)
Parameter ('k88r', 0.07)
Rule ('BMP27_ALK8_ALK8_RII_plusRII_to_BMP27_ALK8_ALK8_RII_RII', RII() + BMP27_ALK8_ALK8_RII() <> BMP27_ALK8_ALK8_RII_RII(), k88f, k88r)

#RXN 89 BMP27_Alk8_RII_RII * Alk3 -> BMP27_Alk3_Alk8_RII_RII
Parameter ('k89f', 0.0005 * 1 * 50)
Parameter ('k89r', 0.0004)
Rule ('BMP27_ALK8_RII_RII_plusALK3_to_BMP27_ALK3_ALK8_RII_RII', ALK3() + BMP27_ALK8_RII_RII() <> BMP27_ALK3_ALK8_RII_RII(), k89f, k89r)

#RXN 90 BMP27_Alk8_RII_RII * Alk8 -> BMP27_Alk8_Alk8_RII_RII
Parameter ('k90f', 0.0000011694 * 1 * 50)
Parameter ('k90r', 0.001197)
Rule ('BMP27_ALK8_RII_RIIplusALK8_to_BMP27_ALK8_ALK8_RII_RII', ALK8() + BMP27_ALK8_RII_RII() <> BMP27_ALK8_ALK8_RII_RII(), k90f, k90r)

#RXN 1 BMP2_ALK3 Endo 
Parameter('kendo', .0005)
Rule('BMP2_ALK3_endo', BMP2_ALK3() >> ALK3(), kendo)


#RXN 2      BMP2_ALK8 endo         
Rule('BMP2_ALK8_endo', BMP2_ALK8() >> ALK8(), kendo)

#RXN 3        BMP2_RII endo
Rule('BMP2_RII_endo', BMP2_RII() >> RII(), kendo)

#RXN 4 BMP2_ALK3_ALK3 endo
Rule('BMP2_ALK3_ALK3_endo', BMP2_ALK3_ALK3() >> ALK3() + ALK3(), kendo)

#RXN 5       BMP2_ALK3_ALK8 endo
Rule('BMP2_ALK3_ALK8_endo', BMP2_ALK3_ALK8() >> ALK3() + ALK8(), kendo)


#RXN 6	BMP2_ALK3_RII endo
Rule('BMP2_ALK3_RII_endo',  BMP2_ALK3_RII() >> ALK3() + RII(), kendo)


#RXN 7  BMP2_ALK8_ALK8 endo
Rule('BMP2_ALK8_ALK8_endo', BMP2_ALK8_ALK8() >> ALK8() + ALK8(), kendo)

#RXN 8  BMP2_ALK8_RII endo
Rule('BMP2_ALK8_RII_endo',  BMP2_ALK8_RII() >> ALK8() + RII(), kendo)


#RXN 9		BMP2_RII_RII endo
Rule('BMP2_RII_RII_endo',  BMP2_RII_RII() >> RII() + RII(), kendo)


#RXN 10 BMP2_ALK3_ALK3_RII endo 
Rule ('BMP2_ALK3_ALK3_RII_endo', BMP2_ALK3_ALK3_RII() >> ALK3() + ALK3() + RII(), kendo)

#RXN 11 BMP2_ALK3_ALK8_RII endo
Rule ('BMP2_ALK3_ALK8_RII_endo', BMP2_ALK3_ALK8_RII() >> ALK3() + ALK8() + RII(), kendo)

#RXN 12 BMP2_ALK3_RII_RII endo 
Rule ('BMP2_ALK3_RII_RII_endo',  BMP2_ALK3_RII_RII() >> ALK3() + RII() + RII(), kendo)

#RXN 13 BMP2_ALK8_ALK8_RII endo  
Rule ('BMP2_ALK8_ALK8_RII_endo', BMP2_ALK8_ALK8_RII() >> ALK8() + ALK8() + RII(), kendo)

#RXN 14 BMP2_ALK8_RII_RII endo  
Rule ('BMP2_ALK8_RII_RII_endo',  BMP2_ALK8_RII_RII() >> ALK8() + RII() + RII(), kendo)

#RXN 15 BMP2_ALK3_ALK3_RII_RII endo  
Rule ('BMP2_ALK3_ALK3_RII_RII_endo', BMP2_ALK3_ALK3_RII_RII() >> ALK3() + ALK3() + RII() + RII(), kendo)

#RXN 16 BMP2_ALK3_ALK8_RII_RII endo  
Rule ('BMP2_ALK3_ALK8_RII_RII_endo', BMP2_ALK3_ALK8_RII_RII() >> ALK3() + ALK8() + RII() + RII(), kendo)

#RXN 17 BMP2_ALK8_ALK8_RII_RII endo  
Rule ('BMP2_ALK8_ALK8_RII_RII_endo', BMP2_ALK8_ALK8_RII_RII() >> ALK8() + ALK8() + RII() + RII(), kendo)

#RXN 1 BMP7_ALK3 Endo 
Rule('BMP7_ALK3_endo', BMP7_ALK3() >> ALK3(), kendo)


#RXN 2      BMP7_ALK8 endo         
Rule('BMP7_ALK8_endo', BMP7_ALK8() >> ALK8(), kendo)

#RXN 3        BMP7_RII endo
Rule('BMP7_RII_endo', BMP7_RII() >> RII(), kendo)

#RXN 4 BMP7_ALK3_ALK3 endo
Rule('BMP7_ALK3_ALK3_endo', BMP7_ALK3_ALK3() >> ALK3() + ALK3(), kendo)

#RXN 5       BMP7_ALK3_ALK8 endo
Rule('BMP7_ALK3_ALK8_endo', BMP7_ALK3_ALK8() >> ALK3() + ALK8(), kendo)


#RXN 6	BMP7_ALK3_RII endo
Rule('BMP7_ALK3_RII_endo',  BMP7_ALK3_RII() >> ALK3() + RII(), kendo)


#RXN 7  BMP7_ALK8_ALK8 endo
Rule('BMP7_ALK8_ALK8_endo', BMP7_ALK8_ALK8() >> ALK8() + ALK8(), kendo)

#RXN 8  BMP7_ALK8_RII endo
Rule('BMP7_ALK8_RII_endo',  BMP7_ALK8_RII() >> ALK8() + RII(), kendo)


#RXN 9		BMP7_RII_RII endo
Rule('BMP7_RII_RII_endo',  BMP7_RII_RII() >> RII() + RII(), kendo)


#RXN 10 BMP7_ALK3_ALK3_RII endo 
Rule ('BMP7_ALK3_ALK3_RII_endo', BMP7_ALK3_ALK3_RII() >> ALK3() + ALK3() + RII(), kendo)

#RXN 11 BMP7_ALK3_ALK8_RII endo
Rule ('BMP7_ALK3_ALK8_RII_endo', BMP7_ALK3_ALK8_RII() >> ALK3() + ALK8() + RII(), kendo)

#RXN 12 BMP7_ALK3_RII_RII endo 
Rule ('BMP7_ALK3_RII_RII_endo',  BMP7_ALK3_RII_RII() >> ALK3() + RII() + RII(), kendo)

#RXN 13 BMP7_ALK8_ALK8_RII endo  
Rule ('BMP7_ALK8_ALK8_RII_endo', BMP7_ALK8_ALK8_RII() >> ALK8() + ALK8() + RII(), kendo)

#RXN 14 BMP7_ALK8_RII_RII endo  
Rule ('BMP7_ALK8_RII_RII_endo',  BMP7_ALK8_RII_RII() >> ALK8() + RII() + RII(), kendo)

#RXN 15 BMP7_ALK3_ALK3_RII_RII endo  
Rule ('BMP7_ALK3_ALK3_RII_RII_endo', BMP7_ALK3_ALK3_RII_RII() >> ALK3() + ALK3() + RII() + RII(), kendo)

#RXN 16 BMP7_ALK3_ALK8_RII_RII endo  
Rule ('BMP7_ALK3_ALK8_RII_RII_endo', BMP7_ALK3_ALK8_RII_RII() >> ALK3() + ALK8() + RII() + RII(), kendo)

#RXN 17 BMP7_ALK8_ALK8_RII_RII endo  
Rule ('BMP7_ALK8_ALK8_RII_RII_endo', BMP7_ALK8_ALK8_RII_RII() >> ALK8() + ALK8() + RII() + RII(), kendo)

#RXN 1 BMP27_ALK3 Endo 
Rule('BMP27_ALK3_endo', BMP27_ALK3() >> ALK3(), kendo)


#RXN 2      BMP27_ALK8 endo         
Rule('BMP27_ALK8_endo', BMP27_ALK8() >> ALK8(), kendo)

#RXN 3        BMP27_RII endo
Rule('BMP27_RII_endo', BMP27_RII() >> RII(), kendo)

#RXN 4 BMP27_ALK3_ALK3 endo
Rule('BMP27_ALK3_ALK3_endo', BMP27_ALK3_ALK3() >> ALK3() + ALK3(), kendo)

#RXN 5       BMP27_ALK3_ALK8 endo
Rule('BMP27_ALK3_ALK8_endo', BMP27_ALK3_ALK8() >> ALK3() + ALK8(), kendo)


#RXN 6	BMP27_ALK3_RII endo
Rule('BMP27_ALK3_RII_endo',  BMP27_ALK3_RII() >> ALK3() + RII(), kendo)


#RXN 7  BMP27_ALK8_ALK8 endo
Rule('BMP27_ALK8_ALK8_endo', BMP27_ALK8_ALK8() >> ALK8() + ALK8(), kendo)

#RXN 8  BMP27_ALK8_RII endo
Rule('BMP27_ALK8_RII_endo',  BMP27_ALK8_RII() >> ALK8() + RII(), kendo)


#RXN 9		BMP27_RII_RII endo
Rule('BMP27_RII_RII_endo',  BMP27_RII_RII() >> RII() + RII(), kendo)


#RXN 10 BMP27_ALK3_ALK3_RII endo 
Rule ('BMP27_ALK3_ALK3_RII_endo', BMP27_ALK3_ALK3_RII() >> ALK3() + ALK3() + RII(), kendo)

#RXN 11 BMP27_ALK3_ALK8_RII endo
Rule ('BMP27_ALK3_ALK8_RII_endo', BMP27_ALK3_ALK8_RII() >> ALK3() + ALK8() + RII(), kendo)

#RXN 12 BMP27_ALK3_RII_RII endo 
Rule ('BMP27_ALK3_RII_RII_endo',  BMP27_ALK3_RII_RII() >> ALK3() + RII() + RII(), kendo)

#RXN 13 BMP27_ALK8_ALK8_RII endo  
Rule ('BMP27_ALK8_ALK8_RII_endo', BMP27_ALK8_ALK8_RII() >> ALK8() + ALK8() + RII(), kendo)

#RXN 14 BMP27_ALK8_RII_RII endo  
Rule ('BMP27_ALK8_RII_RII_endo',  BMP27_ALK8_RII_RII() >> ALK8() + RII() + RII(), kendo)

#RXN 15 BMP27_ALK3_ALK3_RII_RII endo  
Rule ('BMP27_ALK3_ALK3_RII_RII_endo', BMP27_ALK3_ALK3_RII_RII() >> ALK3() + ALK3() + RII() + RII(), kendo)

#RXN 16 BMP27_ALK3_ALK8_RII_RII endo  
Rule ('BMP27_ALK3_ALK8_RII_RII_endo', BMP27_ALK3_ALK8_RII_RII() >> ALK3() + ALK8() + RII() + RII(), kendo)

#RXN 17 BMP27_ALK8_ALK8_RII_RII endo  
Rule ('BMP27_ALK8_ALK8_RII_RII_endo', BMP27_ALK8_ALK8_RII_RII() >> ALK8() + ALK8() + RII() + RII(), kendo)


# Initial values
Parameter('ALK3_0', 66.4)
Parameter('ALK8_0', 66.4)
Parameter('RII_0',  132.8)
Initial(ALK3(), ALK3_0)
Initial(ALK8(), ALK8_0)
Initial(RII(), RII_0)

# Observe total amount of each monomer
Observable('obsALK3', ALK3())
Observable('obsALK8', ALK8())
Observable('obsRII', RII())
Observable('BMP2_ALK3', BMP2_ALK3())
Observable('BMP2_ALK8', BMP2_ALK8())
Observable('BMP2_RII', BMP2_RII())
Observable('BMP2_ALK3_ALK3', BMP2_ALK3_ALK3())
Observable('BMP2_ALK3_ALK8', BMP2_ALK3_ALK8())
Observable('BMP2_ALK3_RII', BMP2_ALK3_RII())
Observable('BMP2_ALK8_ALK8', BMP2_ALK8_ALK8())
Observable('BMP2_ALK8_RII', BMP2_ALK8_RII())
Observable('BMP2_RII_RII', BMP2_RII_RII())
Observable('BMP2_ALK3_ALK3_RII', BMP2_ALK3_ALK3_RII())
Observable('BMP2_ALK3_ALK8_RII', BMP2_ALK3_ALK8_RII())
Observable('BMP2_ALK3_RII_RII', BMP2_ALK3_RII_RII())
Observable('BMP2_ALK8_ALK8_RII', BMP2_ALK8_ALK8_RII())
Observable('BMP2_ALK8_RII_RII', BMP2_ALK8_RII_RII())
Observable('BMP2_ALK3_ALK3_RII_RII', BMP2_ALK3_ALK3_RII_RII())
Observable('BMP2_ALK3_ALK8_RII_RII', BMP2_ALK3_ALK8_RII_RII())
Observable('BMP2_ALK8_ALK8_RII_RII', BMP2_ALK8_ALK8_RII_RII())

Observable('BMP7_ALK3', BMP7_ALK3())
Observable('BMP7_ALK8', BMP7_ALK8())
Observable('BMP7_RII', BMP7_RII())
Observable('BMP7_ALK3_ALK3', BMP7_ALK3_ALK3())
Observable('BMP7_ALK3_ALK8', BMP7_ALK3_ALK8())
Observable('BMP7_ALK3_RII', BMP7_ALK3_RII())
Observable('BMP7_ALK8_ALK8', BMP7_ALK8_ALK8())
Observable('BMP7_ALK8_RII', BMP7_ALK8_RII())
Observable('BMP7_RII_RII', BMP7_RII_RII())
Observable('BMP7_ALK3_ALK3_RII', BMP7_ALK3_ALK3_RII())
Observable('BMP7_ALK3_ALK8_RII', BMP7_ALK3_ALK8_RII())
Observable('BMP7_ALK3_RII_RII', BMP7_ALK3_RII_RII())
Observable('BMP7_ALK8_ALK8_RII', BMP7_ALK8_ALK8_RII())
Observable('BMP7_ALK8_RII_RII', BMP7_ALK8_RII_RII())
Observable('BMP7_ALK3_ALK3_RII_RII', BMP7_ALK3_ALK3_RII_RII())
Observable('BMP7_ALK3_ALK8_RII_RII', BMP7_ALK3_ALK8_RII_RII())
Observable('BMP7_ALK8_ALK8_RII_RII', BMP7_ALK8_ALK8_RII_RII())

Observable('BMP27_ALK3', BMP27_ALK3())
Observable('BMP27_ALK8', BMP27_ALK8())
Observable('BMP27_RII', BMP27_RII())
Observable('BMP27_ALK3_ALK3', BMP27_ALK3_ALK3())
Observable('BMP27_ALK3_ALK8', BMP27_ALK3_ALK8())
Observable('BMP27_ALK3_RII', BMP27_ALK3_RII())
Observable('BMP27_ALK8_ALK8', BMP27_ALK8_ALK8())
Observable('BMP27_ALK8_RII', BMP27_ALK8_RII())
Observable('BMP27_RII_RII', BMP27_RII_RII())
Observable('BMP27_ALK3_ALK3_RII', BMP27_ALK3_ALK3_RII())
Observable('BMP27_ALK3_ALK8_RII', BMP27_ALK3_ALK8_RII())
Observable('BMP27_ALK3_RII_RII', BMP27_ALK3_RII_RII())
Observable('BMP27_ALK8_ALK8_RII', BMP27_ALK8_ALK8_RII())
Observable('BMP27_ALK8_RII_RII', BMP27_ALK8_RII_RII())
Observable('BMP27_ALK3_ALK3_RII_RII', BMP27_ALK3_ALK3_RII_RII())
Observable('BMP27_ALK3_ALK8_RII_RII', BMP27_ALK3_ALK8_RII_RII())
Observable('BMP27_ALK8_ALK8_RII_RII', BMP27_ALK8_ALK8_RII_RII())

from matplotlib.pyplot import *
from numpy import linspace, array
from pysb.simulator import ScipyOdeSimulator

# We will integrate from t=0 to t=86400
t = linspace(0, 20000, 200)
# Simulate the model
print("Simulating...")

y = ScipyOdeSimulator(model, rtol=1e-4, atol=[1e-8, 1e-14, 1e-6]).run(
tspan=t).all
'''
# Gather the observables of interest into a matrix
yobs = array([y[obs] for obs in ('BMP2_ALK3_ALK3_RII_RII', 'BMP2_ALK3_ALK8_RII_RII', 'BMP2_ALK8_ALK8_RII_RII', 'BMP7_ALK3_ALK3_RII_RII', 'BMP7_ALK3_ALK8_RII_RII', 'BMP7_ALK8_ALK8_RII_RII', 'BMP27_ALK3_ALK3_RII_RII', 'BMP27_ALK3_ALK8_RII_RII', 'BMP27_ALK8_ALK8_RII_RII')]).T
# Plot normalized trajectories
plot(t, yobs*7.525)
legend(['BMP2_ALK3_ALK3_RII_RII', 'BMP2_ALK3_ALK8_RII_RII', 'BMP2_ALK8_ALK8_RII_RII', 'BMP7_ALK3_ALK3_RII_RII', 'BMP7_ALK3_ALK8_RII_RII', 'BMP7_ALK8_ALK8_RII_RII', 'BMP27_ALK3_ALK3_RII_RII', 'BMP27_ALK3_ALK8_RII_RII', 'BMP27_ALK8_ALK8_RII_RII'], loc='lower right')
savefig('DeterministicSolution.png') 
'''
# Gather the observables of interest into a matrix
yobs = array([y[obs] for obs in ('BMP2_ALK3_ALK3_RII_RII', 'BMP27_ALK3_ALK3_RII_RII', 'BMP27_ALK3_ALK8_RII_RII')]).T
# Plot normalized trajectories
'''
plot(t, yobs)
legend(['BMP2_ALK3_ALK3_RII_RII', 'BMP27_ALK3_ALK3_RII_RII', 'BMP27_ALK3_ALK8_RII_RII'], loc='lower right')
savefig('DeterministicSolution.png') 
'''
print ('Z',Z)
print (Z*7.525)

shotobsALK3 = ((y['obsALK3'])[49])
shotobsALK8 = ((y['obsALK8'])[49])
shotobsRII = ((y['obsRII'])[49])
shotBMP2_ALK3 = ((y['BMP2_ALK3'])[49])
shotBMP2_ALK8 = ((y['BMP2_ALK8'])[49])
shotBMP2_RII = ((y['BMP2_RII'])[49])
shotBMP2_ALK3_ALK3 = ((y['BMP2_ALK3_ALK3'])[49])
shotBMP2_ALK3_ALK8 = ((y['BMP2_ALK3_ALK8'])[49])
shotBMP2_ALK3_RII = ((y['BMP2_ALK3_RII'])[49])
shotBMP2_ALK8_ALK8 = ((y['BMP2_ALK8_ALK8'])[49])
shotBMP2_ALK8_RII = ((y['BMP2_ALK8_RII'])[49])
shotBMP2_RII_RII = ((y['BMP2_RII_RII'])[49])
shotBMP2_ALK3_ALK3_RII = ((y['BMP2_ALK3_ALK3_RII'])[49])
shotBMP2_ALK3_ALK8_RII = ((y['BMP2_ALK3_ALK8_RII'])[49])
shotBMP2_ALK3_RII_RII = ((y['BMP2_ALK3_RII_RII'])[49])
shotBMP2_ALK8_ALK8_RII = ((y['BMP2_ALK8_ALK8_RII'])[49])
shotBMP2_ALK8_RII_RII = ((y['BMP2_ALK8_RII_RII'])[49])
shotBMP2_ALK3_ALK3_RII_RII = ((y['BMP2_ALK3_ALK3_RII_RII'])[49])
shotBMP2_ALK3_ALK8_RII_RII = ((y['BMP2_ALK3_ALK8_RII_RII'])[49])
shotBMP2_ALK8_ALK8_RII_RII = ((y['BMP2_ALK8_ALK8_RII_RII'])[49])
shotBMP7_ALK3 = ((y['BMP7_ALK3'])[49])
shotBMP7_ALK8 = ((y['BMP7_ALK8'])[49])
shotBMP7_RII = ((y['BMP7_RII'])[49])
shotBMP7_ALK3_ALK3 = ((y['BMP7_ALK3_ALK3'])[49])
shotBMP7_ALK3_ALK8 = ((y['BMP7_ALK3_ALK8'])[49])
shotBMP7_ALK3_RII = ((y['BMP7_ALK3_RII'])[49])
shotBMP7_ALK8_ALK8 = ((y['BMP7_ALK8_ALK8'])[49])
shotBMP7_ALK8_RII = ((y['BMP7_ALK8_RII'])[49])
shotBMP7_RII_RII = ((y['BMP7_RII_RII'])[49])
shotBMP7_ALK3_ALK3_RII = ((y['BMP7_ALK3_ALK3_RII'])[49])
shotBMP7_ALK3_ALK8_RII = ((y['BMP7_ALK3_ALK8_RII'])[49])
shotBMP7_ALK3_RII_RII = ((y['BMP7_ALK3_RII_RII'])[49])
shotBMP7_ALK8_ALK8_RII = ((y['BMP7_ALK8_ALK8_RII'])[49])
shotBMP7_ALK8_RII_RII = ((y['BMP7_ALK8_RII_RII'])[49])
shotBMP7_ALK3_ALK3_RII_RII = ((y['BMP7_ALK3_ALK3_RII_RII'])[49])
shotBMP7_ALK3_ALK8_RII_RII = ((y['BMP7_ALK3_ALK8_RII_RII'])[49])
shotBMP7_ALK8_ALK8_RII_RII = ((y['BMP7_ALK8_ALK8_RII_RII'])[49])
shotBMP27_ALK3 = ((y['BMP27_ALK3'])[49])
shotBMP27_ALK8 = ((y['BMP27_ALK8'])[49])
shotBMP27_RII = ((y['BMP27_RII'])[49])
shotBMP27_ALK3_ALK3 = ((y['BMP27_ALK3_ALK3'])[49])
shotBMP27_ALK3_ALK8 = ((y['BMP27_ALK3_ALK8'])[49])
shotBMP27_ALK3_RII = ((y['BMP27_ALK3_RII'])[49])
shotBMP27_ALK8_ALK8 = ((y['BMP27_ALK8_ALK8'])[49])
shotBMP27_ALK8_RII = ((y['BMP27_ALK8_RII'])[49])
shotBMP27_RII_RII = ((y['BMP27_RII_RII'])[49])
shotBMP27_ALK3_ALK3_RII = ((y['BMP27_ALK3_ALK3_RII'])[49])
shotBMP27_ALK3_ALK8_RII = ((y['BMP27_ALK3_ALK8_RII'])[49])
shotBMP27_ALK3_RII_RII = ((y['BMP27_ALK3_RII_RII'])[49])
shotBMP27_ALK8_ALK8_RII = ((y['BMP27_ALK8_ALK8_RII'])[49])
shotBMP27_ALK8_RII_RII = ((y['BMP27_ALK8_RII_RII'])[49])
shotBMP27_ALK3_ALK3_RII_RII = ((y['BMP27_ALK3_ALK3_RII_RII'])[49])
shotBMP27_ALK3_ALK8_RII_RII = ((y['BMP27_ALK3_ALK8_RII_RII'])[49])
shotBMP27_ALK8_ALK8_RII_RII = ((y['BMP27_ALK8_ALK8_RII_RII'])[49])

