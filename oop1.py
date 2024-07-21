#oops concept in python
#it is combinatons of attributes (variables) & methods (functions)
from oop2 import ECE

ECE_A=ECE(25,45,12,2024)
ECE_B=ECE(32,38,13,2024)
ECE_C=ECE(45,22,11,2024)

print("A_girls- ",ECE_A.girls,"; ","A_boys- ",ECE_A.boys,"; ","A_teachers- ",ECE_A.teachers ,"; ","A_year- ",ECE_A.year ,"; ")
ECE_A.academics()
ECE_A.sports()
ECE_B.sports()
ECE_C.academics()