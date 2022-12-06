# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# -- Libraries -- #
import random

# -- Variables -- #
building_generation_counter = 1 # Sets The Amount Of Buildings Generated In

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# -- Land Types -- #
land_type = [ "Residential" , "Commercial" , "Industrial" , "Agricultural" , "Government" ]
l_t = random.choice( land_type ) # Selects A Random Land Type

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# [ DEBUG ] - Sets Land Type to Commercial ( Use This If You Want Just Commercial Buildings Generating )
l_t = "Commercial"

if l_t == "Commercial":
    for x in range(building_generation_counter):

#   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---  #

        # -- Commercial Buildings -- #
        commercial_building = [ "Store" ] # Commercial Buildings
        c_b = random.choice( commercial_building ) # Selects A Random Commercial Building

#   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---  #

        # -- Main Store Names -- #
        store_name = [ "Franklin's" , "Michael's" , "Trevor's" ] # Store's 1st Name
        s_n = random.choice( store_name ) # Selects A Random 1st Store Name

#   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---  #

        # -- Main Store Types -- #
        store_type = [ "Convenience" , "Gun" , "Clothing" ] # Store Types
        s_t = random.choice( store_type ) # Selects A Random Store Type
        s_t = "Clothing"

#   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---   ---  #

        # -- Clothing Store -- #
        store_name_clothing = [ "Urban" , "Retro" , "Business" , "Sports" , "Classic" , "Economy" , "2nd Hand" ] # Store's 2nd Name
        s_n_c = random.choice( store_name_clothing ) # Selects A Random 2nd Store Name

        clothing_store_size_small_room_count = random.randint(3,4) # Sets Amount Of Rooms In A Small Store
        c_s_s_s_r_c = clothing_store_size_small_room_count
        clothing_store_size_medium_room_count = random.randint(4,6) # Sets Amount Of Rooms In A Medium Store
        c_s_s_m_r_c = clothing_store_size_medium_room_count
        clothing_store_size_large_room_count = random.randint(6,8) # Sets Amount Of Rooms In A Large Store
        c_s_s_l_r_c = clothing_store_size_large_room_count

        clothing_Store_default_room_01 = "Main Area"
        clothing_Store_default_room_02 = "Staff Room"
        clothing_Store_default_room_03 = "Restroom"

        clothing_store_room = [ "Storage Room" , "Side Room" , "Office" ]
        c_s_r = random.choice(clothing_store_room)
        
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

        # -- Building Settings -- #
        main_building_condition_int = random.randint( 1 , 100 ) # Sets Main Building Condition 0% - 100%
        main_building_condition_str = "" # Sets Main Building Condition name
        main_building_destroyed = False # Sets If Main Building Is Destroyed Or Not
        main_building_size = [ "Small" , "Medium" , "Large" ] # Main Building Sizes
        m_b_s = random.choice(main_building_size)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

        #main_building_condition_int = 0

        if main_building_condition_int > 80: # If Main Building Condition is 80% - 100%
            main_building_destroyed = False # Sets Main Building To Not Destroyed
            main_building_condition_str = "Excellent" # Sets Main Building Condition Name To Excellent
            print("MAIN_BUILD_CONDITION_DEBUG_01")
        elif main_building_condition_int  > 60 < 80: # If Main Building Condition is 60% - 80%
            main_building_destroyed = False # Sets Main Building To Not Destroyed
            main_building_condition_str = "Good" # Sets Main Building Condition Name To Good
            print("MAIN_BUILD_CONDITION_DEBUG_02")
        elif main_building_condition_int  > 40 < 60: # If Main Building Condition is 40% - 60%
            main_building_destroyed = False # Sets Main Building To Not Destroyed
            main_building_condition_str = "Okay" # Sets Main Building Condition Name To Okay
            print("MAIN_BUILD_CONDITION_DEBUG_03")
        elif main_building_condition_int  > 20 < 40: # If Main Building Condition is 20% - 40%
            main_building_destroyed = False # Sets Main Building To Not Destroyed
            main_building_condition_str = "Poor" # Sets Main Building Condition Name To Poor
            print("MAIN_BUILD_CONDITION_DEBUG_04")
        elif main_building_condition_int  > 0 < 20: # If Main Building Condition is 0% - 20%
            main_building_destroyed = True # Sets Main Building To Not Destroyed
            main_building_condition_str = "Destroyed" # Sets Main Building Condition Name To Destroyed
            print("MAIN_BUILD_CONDITION_DEBUG_05")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
        
        if main_building_destroyed == True: # If Main Building Condition is Destroyed
            print( "| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
            print( "[" , s_t , c_b , "]" )
            print( "[ Building Condition :" , main_building_condition_str , "]" )
            print( "\n| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |" )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
            
        else:
            if c_b == "Store":
                
                if s_t == "Convenience":
                        print( "[" ,  s_n , s_t , c_b , "]" )
                        print( "[ Building Condition :" , main_building_condition_str , "]" )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

                elif s_t == "Gun":
                    print( "[" , s_n , s_t , c_b , "]" )
                    print( "[ Building Condition :" , main_building_condition_str , "]" )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

                elif s_t == "Clothing":
                    
                    if m_b_s == "Small":
                        print( "| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        print( "[" , s_n , s_n_c , s_t , c_b , "]" )
                        print( "[ Building Condition :" , main_building_condition_str , "(" + str(main_building_condition_int) + "%)" , "]" )
                        print( "[ Building Size :" , m_b_s , "]" )
                        print( "[ Room Count :" , int( c_s_s_s_r_c ) + 3 , "]" )
                        print( "\n| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        print( "[ Room List ]\n")
                        print( "[" , clothing_Store_default_room_01 , "]" )
                        print( "[" , clothing_Store_default_room_02 , "]" )
                        print( "[" , clothing_Store_default_room_03 , "]" )
                        for x in range( c_s_s_s_r_c ):
                            c_s_r = random.choice(clothing_store_room)
                            print( "[" , c_s_r , "]" )
                        print( "\n| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        
                        
                    elif m_b_s == "Medium":
                        print( "| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        print( "[" , s_n , s_n_c , s_t , c_b , "]" )
                        print( "[ Building Condition :" , main_building_condition_str , "(" + str(main_building_condition_int) + "%)" , "]" )
                        print( "[ Building Size :" , m_b_s , "]" )
                        print( "[ Room Count :" , int( c_s_s_m_r_c ) + 3 , "]" )
                        print( "\n| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        print( "[ Room List ]\n")
                        print( "[" , clothing_Store_default_room_01 , "]" )
                        print( "[" , clothing_Store_default_room_02 , "]" )
                        print( "[" , clothing_Store_default_room_03 , "]" )
                        for x in range( c_s_s_m_r_c ):
                            c_s_r = random.choice(clothing_store_room)
                            print( "[" , c_s_r , "]" )
                        print( "\n| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        
                    elif m_b_s == "Large":
                        print( "| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        print( "[" , s_n , s_n_c , s_t , c_b , "]" )
                        print( "[ Building Condition :" , main_building_condition_str , "(" + str(main_building_condition_int) + "%)" , "]" )
                        print( "[ Building Size :" , m_b_s , "]" )
                        print( "[ Room Count :" , int( c_s_s_l_r_c ) + 3 , "]" )
                        print( "\n| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                        print( "[ Room List ]\n")
                        print( "[" , clothing_Store_default_room_01 , "]" )
                        print( "[" , clothing_Store_default_room_02 , "]" )
                        print( "[" , clothing_Store_default_room_03 , "]" )
                        for x in range( c_s_s_l_r_c ):
                            c_s_r = random.choice(clothing_store_room)
                            print( "[" , c_s_r , "]" )
                        print( "\n| ---   ---   ---   ---   ---   ---   ---   ---   ---   --- |\n" )
                    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


