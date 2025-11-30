print("Adding data to a dictionary")
print("--------------------------------")

tuloy = True 
empty_dict = {}
def print_anime():
    for a,b in empty_dict.items():
        print(f"Code - {a} : Anime - {b}")
def pangsearch():
    print(f"results shows {empty_dict[key].upper()} on our database.")
while tuloy == True:
    keys = input("enter anime code: ")
    values = input("enter anime name: ")
    empty_dict[keys] = values
    choice = input("would you like to continiue?\ny - yes\nn - no\np - print\ns - search\nansewer: ").lower()

    if choice == 'y':
        print("continuing...")
        continue
    elif choice == 'n':
        print("program ended.")
        break
    elif choice == 'p':
        print_anime()
        continue
    elif choice == 's':
        key = input("enter anime code to search: ")
        if key in empty_dict:
            pangsearch()
        else:
            print("anime code not found in database.")
        continue
    else:
        print("invalid input.")
        continue
        