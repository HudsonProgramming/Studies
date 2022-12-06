import random

########## AREA TYPE ##########

area_type_selection = random.randint(1,4)
area_type = ""

if area_type_selection == 1:
    area_type = "R"
elif area_type_selection == 2:
    area_type = "C"
elif area_type_selection == 3:
    area_type = "I"
elif area_type_selection == 4:
    area_type = "A"
    
########## AREA WEALTH ##########

area_wealth_selection = random.randint(1,100)
area_wealth = ""

if area_wealth_selection > 98:
    #print("Military: 2%")
    area_wealth = "Military"
elif area_wealth_selection > 90 < 98:
    #print("High Value: 8%")
    area_wealth = "H"
elif area_wealth_selection > 80 < 90:
    #print("Medium-High Value: 10%")
    area_wealth = "MH"
elif area_wealth_selection > 53 < 80:
    #print("Medium Value: 20%")
    area_wealth = "M"
elif area_wealth_selection > 28 < 53:
    #print("Low Medium Value: 25%")
    area_wealth = "LM"
elif area_wealth_selection > 0 < 28:
    #print("Low Value: 35%")
    area_wealth = "L"

print("Area Type Code:",area_type)
print("Area Wealth Code:",area_wealth)

##################################

residential_building_type = ["House"]
residential_building_size = ["One Story","Two Story","Three Story"]
residential_building_extra = ["Garage","Shed"]
residential_building_condition = random.randint(1,100)

residential_selection_one = random.choice(residential_building_type)
residential_selection_two = random.choice(residential_building_size)
residential_selection_three = random.choice(residential_building_extra)

if residential_selection_one == "Flat":
    residential_selection_two == "One Story"

building_info = residential_selection_two + " " + residential_selection_one + " with a " + residential_selection_three
print(building_info)

