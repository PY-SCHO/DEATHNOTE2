single_dimen_array = [1, 2, 3, 4, 5]
two_dimen_array = [ [1, 2], [3, 4], [5, 6], [7, 8], [9, 0]
                         ]

def display_single_dimen_array(ARRAY):
    print("single dimensional array elements: ")
    for element in ARRAY:
        print(element)
def display_two_dimen_array(ARRAY):
    print("two dimensional array elements: ")
    for sublist in ARRAY:
        print(sublist)



choose = input("which array you want to display? (1 for single , 2 for two dimension): ")

if choose == "1":
    display_single_dimen_array(single_dimen_array)
elif choose == "2":
    display_two_dimen_array(two_dimen_array)
else:
    print("error")        


