import random

'''
num = random.randint(1, 4)
print(num)
if num == 1:
    print("Small House")
if num == 2:
    print("Forest")
if num == 3:
    print("Hospital")
if num == 4:
    print("Large warehouse")


area_value = random.randint(1,100)
print("Area Value:",area_value)
if area_value > 75:
    print("High Value Area")
elif area_value > 50 < 75:
    print("Medium-High Value Area")
elif area_value > 25 < 50:
    print("Medium Value Area")
elif area_value > 0 < 25:
    print("Low Value Area")

MILITARY ------------------- M

HIGH VALUE --------------- H

MEDIUM-HIGH VALUE -- MH

MEDIUM VALUE ----------- M

LOW-MEDIUM VALUE --- LM

LOW VALUE ---------------- L
'''

land_type = random.randint(1,4)
#print("Land Type:",land_type)
if land_type == 1:
    print("Land Type: Residential")
    
elif land_type == 2:
    print("Land Type: Commercial")
elif land_type == 3:
    print("Land Type: Industrial")
elif land_type == 4:
    print("Land Type: Agricultural")

area = ""
area_value = random.randint(1,100)
area_value = 100
#print("Area Value:",area_value)
if area_value > 98:
    print("Military: 2%")
    area = "M"
elif area_value > 90 < 98:
    print("High Value: 8%")
    area = "H"
elif area_value > 80 < 90:
    print("Medium-High Value: 10%")
    area = "MH"
elif area_value > 53 < 80:
    print("Medium Value: 20%")
    area = "M"
elif area_value > 28 < 53:
    print("Low Medium Value: 25%")
    area = "LM"
elif area_value > 0 < 28:
    print("Low Value: 35%")
    area = "L"

#print(area)
          
