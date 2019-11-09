import math

Bloodstain_Width = float(input("Input the width of the bloodstain: "))
Bloodstain_Length = float(input("Input the length of the bloodstain: "))
Bloodstain_Angle_Of_Impact = math.asin(Bloodstain_Width/Bloodstain_Length)*57.29578
print(Bloodstain_Angle_Of_Impact, "Degrees")


