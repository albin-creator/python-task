def print_hex_pattern(rows, columns):
    hex_top = "   _ _ _     "
    hex_middle_top = " /     \\_ _ _"
    hex_middle_bottom = " \\_ _ _/     "

    for r in range(rows):
        if r == 0:
            print(hex_top * columns)
        else:
            for _ in range(2):
                print(" " + "".join([hex_middle_top for _ in range(columns)])[:-5])
                print(" " + "".join([hex_middle_bottom for _ in range(columns)])[:-5])
    
    if rows % 2 == 0:
        print(hex_top * columns)

print("Inputs :- 4  7 ")
print_hex_pattern(3,4)

def print_hex_pattern(rows,columns):
    hex_top = "   _ _ _     "
    hex_middle_top = " /     \\_ _ _"
    hex_middle_bottom = " \\_ _ _/     "

    for r in range(rows):
        if r == 0:
            print(hex_top * columns)
        else:
            for _ in range(1 if r == 1 else 2):
                print(" " + "".join([hex_middle_top for _ in range(columns)])[:-5])
                print(" " + "".join([hex_middle_bottom for _ in range(columns)])[:-5])

print("\nInputs :- 3  5 ")
print_hex_pattern(3,3)
