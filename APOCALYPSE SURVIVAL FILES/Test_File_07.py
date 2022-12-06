################################################
################## LIBRARIES ###################

import random

################## LIBRARIES ###################
################################################
################### OPTIONS ###################

##### LAND TYPE #####
land_type = ["Residential","Commercial","Industrial","Agricultural","Government"]

##### RESIDENTIAL #####
residential_building_choice = ["House","Flat","Apartment","Bungalow","Shack"]
residential_building_extra = ["Garage","Shed"]

##### COMMERCIAL #####
commercial_building_choice = ["Store","Supermarket","Shopping Centre","Office","Warehouse","Hotel","Pub","Resturant","Cafe","Gym","Medical Centre","Hospital","Nursing Home","Hair Salon","Theme Park","Bank","Stall","Kennel","Vehicle Repair Garage","Florist"]
store_type = ["Hardware","Clothing","Drug","Grocery","Charity","Electronic","DIY","2nd Hand","Book","Gardening","Jewelery","Music","Game","Bicycle","Sports"]
commercial_building_extra = ["Parking Lot"]

##### INDUSTRIAL #####
industrial_building_choice = ["Manufacturing Factory","Warehouse","Power Station","Construction Site","Brewery","Nuclear Power Plant"]
factory_type = ["Petroleum","Chemical","Plastic","Food","Clothing","Textile","Metal","Electronic","Vehicle","Wood","Paper","Cardboard","Ceramic","Glass"]
industrial_building_extra = ["Warehouse"]

##### AGRICULTURAL #####
agricultural_building_choice = ["Farm","Forestry"]
industrial_building_extra = ["Barn"]

##### GOVERNMENT #####
government_building_choice = ["Post Office","Police Station","School","Airport","Military Base"]
government_building_extra = ["Parking Lot"]

##### SIZE #####
building_size = ["Small","Medium","Large"]

################### OPTIONS ###################
################################################
################## VARIABLES ###################

while True:

    bc = random.randint(0,100) # Generates building Condition 0% - 100%
    ec = random.randint(0,100) # Generates extra Condition 0% - 100%
    lt = random.choice(land_type) # Generates Land Type
    bss = 2 # Small buildings capped at 2 floors
    bsm = random.randint(2,4) # Generates floors for medium buildings
    bsl = random.randint(3,5) # Generates floors for large buildings
    multiple_stories = True # Multiple floors?
    extras_enabled = True # Extras?
    extra_true_or_false = random.randint(1,4)

    ################## VARIABLES ###################
    ################################################
    ################ FUNCTIONALITY ################

    # BUILDING CONDITION / SIZE FUNCTIONALITY
    if bc <= 25:
        bs = "Destroyed"
    else:
        bs = random.choice(building_size)

    if ec <= 25:
        ec = "Destroyed"
    else:
        ec = ec

    if extra_true_or_false == 1:
        extras_enabled = True
    else:
        extras_enabled = False

        
    #lt = "Residential"

    if lt == "Residential":
        rbc = random.choice(residential_building_choice)

########################################################################################
########################################################################################
########################################################################################
########################################################################################
        # HOUSE OPTION
    
        if rbc == "House":
            
    ########################################################################################
    ########################################################################################
            #EXTRAS ENABLED
            
            if extras_enabled == True:
                 rbe = random.choice(residential_building_extra)
                 
    ########################################################################################
            #HOUSE DESTROYED
                 
                 if bs == "Destroyed":
                     
    ########################################################################################
             #HOUSE DESTROYED AND BUILDING EXTRA DESTROYED
                     
                    if ec == "Destroyed": 
                         print(bs,rbc,"with a",ec,rbe)

    ########################################################################################
             #HOUSE DESTROYED BUT BUILDING EXTRA NOT DESTROYED

                    else:
                        print(bs,rbc,"with a",rbe,"("+str(ec)+"%)")

    ########################################################################################
             #HOUSE NOT DESTROYED
                        
                 else:

    ########################################################################################
             #HOUSE NOT DESTROYED BUT BUILDING EXTRA DESTROYED
                     
                     if ec == "Destroyed":

    ########################################################################################
             #HOUSE WITH MULTIPLE FLOORS NOT DESTROYED BUT BUILDING EXTRA DESTROYED
                         
                         if multiple_stories == True:
                            if bs == "Small":
                                print(bs,bss,"Story",rbc,"("+str(bc)+"%) with a",ec,rbe)
                            elif bs == "Medium":
                                print(bs,bsm,"Story",rbc,"("+str(bc)+"%) with a",ec,rbe)
                            elif bs == "Large":
                                print(bs,bsl,"Story",rbc,"("+str(bc)+"%) with a",ec,rbe)                
                         elif multiple_stories == False:
                            print(bs,rbc,"("+str(bc)+"%) with a",ec,rbe)

    ########################################################################################
             #HOUSE WITH 1 FLOOR NOT DESTROYED BUT BUILDING EXTRA DESTROYED

                     else:
                            if multiple_stories == True:
                                if bs == "Small":
                                    print(bs,bss,"Story",rbc,"("+str(bc)+"%) with a",rbe,"("+str(ec)+"%)")
                                elif bs == "Medium":
                                    print(bs,bsm,"Story",rbc,"("+str(bc)+"%) with a",rbe,"("+str(ec)+"%)")
                                elif bs == "Large":
                                    print(bs,bsl,"Story",rbc,"("+str(bc)+"%) with a",rbe,"("+str(ec)+"%)")                
                            elif multiple_stories == False:
                                print(bs,rbc,"("+str(bc)+"%) with a",rbe,"("+str(ec)+"%)")
                                
    ########################################################################################
    ########################################################################################
            #EXTRAS NOT ENABLED
                                
            else:

    ########################################################################################
            #HOUSE DESTROYED
                
                if bs == "Destroyed":
                    print(bs,rbc)

    ########################################################################################
            #HOUSE NOT DESTROYED

                else:

    ########################################################################################
            #HOUSE WITH MULTIPLE FLOORS NOT DESTROYED
                    
                    if multiple_stories == True:
                        if bs == "Small":
                            print(bs,bss,"Story",rbc,"("+str(bc)+"%)")
                        elif bs == "Medium":
                            print(bs,bsm,"Story",rbc,"("+str(bc)+"%)")
                        elif bs == "Large":
                            print(bs,bsl,"Story",rbc,"("+str(bc)+"%)")

    ########################################################################################
            #HOUSE WITH 1 FLOOR NOT DESTROYED

                    elif multiple_stories == False:
                        print(bs,rbc,"("+str(bc)+"%)")

########################################################################################
########################################################################################
########################################################################################
########################################################################################
            #BUILDING WITH 1 FLOOR NOT DESTROYED

        else:
            print(bs,rbc,str(bc)+"%")

    ########################################################################################   

    elif lt == "Commercial":
        rbc = random.choice(commercial_building_choice)
        print(bs,rbc,str(bc)+"%")

    elif lt == "Industrial":
        rbc = random.choice(industrial_building_choice)
        print(bs,rbc,str(bc)+"%")

    elif lt == "Agricultural":
        rbc = random.choice(agricultural_building_choice)
        print(bs,rbc,str(bc)+"%")

    elif lt == "Government":
        rbc = random.choice(government_building_choice)
        print(bs,rbc,str(bc)+"%")

            

            
