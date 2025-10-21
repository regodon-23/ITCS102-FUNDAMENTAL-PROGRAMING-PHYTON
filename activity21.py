isDirty = True
while isDirty == True:
    confirm = input(" Do you wish to continue washing(yes/no)")

    if confirm == 'yes' :
        print("continuing the cycle")
        continue
    elif confirm == 'no' :
            print("cycle stops")
            break
    else:
        print("Invalid choice")
        continue