import random

### RESIDENTIAL ###

rbt = ["House","Flat","Apartment","Bungalow","Shack"]
rbs = ["Small","Medium","Large"]
rbe = ["Garage","Shed"]


rs1 = random.choice(rbt) # Selects the buidling type
rs2 = random.choice(rbs) # Selects the size
rs3 = random.randint(2,3) # Selects the amount of floors
rs4 = random.choice(rbe) # Selects any extras
rs5 = random.randint(1,100) # Selects the condition of rs1
rs6 = random.randint(1,100) # Selects the condition of rs4

multiple_stories = True
extras_enabled = True

if rs1 == "House":
    multiple_stories = True
    extras_enabled = True
elif rs1 == "Flat":
    multiple_stories = False
    extras_enabled = False
elif rs1 == "Apartment":
    multiple_stories = False
    extras_enabled = False
elif rs1 == "Bungalow":
    multiple_stories = False
    extras_enabled = True
elif rs1 == "Shack":
    multiple_stories = False
    extras_enabled = True

def building_info():
    
    if multiple_stories == True:
        print(rs3,"Story",rs1,str(rs5)+"% with a",rs4,str(rs6)+"%")
    else:
        if extras_enabled == True:
            print(rs2,rs1,str(rs5)+"% with a",rs4,str(rs6)+"%")
        else:
            print(rs2,rs1,str(rs5)+"%")
        

building_info()
