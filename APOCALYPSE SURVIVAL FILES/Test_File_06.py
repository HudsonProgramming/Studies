import random

store_type = ["Shop","Cafe"]
store_type_select = random.choice(store_type)
store_size = ["Small","Medium","Large"]
store_size_select = random.choice(store_size)

# ////////////////////////////////////////////////////////////////////////////////////// #

shop_room_list_default = ["Main Display Room","Restroom","Staff Room"]
shop_room_list_addon = ["Side Display Room","Storage Room","Staff Room"]
shop_room_addon_select = random.choice(shop_room_list_addon)

if store_size_select == "Small":
    store_room_count = random.randint(1,2)
if store_size_select == "Medium":
    store_room_count = random.randint(2,3)
if store_size_select == "Large":
    store_room_count = random.randint(3,5)

if store_type_select == "Shop":
    for x in range(store_room_count):
        print("You discover...",store_type_select)
        userinput = input("Enter: Y/N")
        userinput = userinput.lower()
        if userinput == "y":
            print("YES")
        elif userinput == "n":
            print("NO")
        else:
            print("Invalid Input")
        
        

'''
print("[ Store Type:",store_type_select,"]")
print("[ Store Size:",store_size_select,"]")
'''
