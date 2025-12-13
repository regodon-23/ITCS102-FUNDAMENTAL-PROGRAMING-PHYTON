from def_function import *

print("====== FINAL PROJECT HUB ======\n")

student_name = input("Hello! Kindly enter your name --> ")
print(f"Welcome {student_name}! You are now inside the Project Hub.\n")

system_on = True

while system_on:

    print("\n================ HOME MENU ================")
    print("Choose an option:")
    print("A - Activity Module")
    print("B - Coding Challenges")
    print("X - Close Program")
    print("==========================================")

    main_choice = input("Your selection --> ").lower()
    print("")

    # EXIT SYSTEM
    if main_choice == "x":
        print("Closing system... See you next time!")
        break

    # ACTIVITY MODULE
    elif main_choice == "a":
        print("===== ACTIVITY GROUPS =====")
        print("G1 - Activities 1 to 5")
        print("G2 - Activities 6 to 10")
        print("G3 - Activities 11 to 15")
        print("G4 - Activities 16 to 20")
        print("G5 - Activities 21 to 24_1")
        print("G6 - Activities 26 to 28")
        print("Q  - Back to Main Menu")
        print("============================")

        group_pick = input("Select group --> ").lower()

        # GROUP 1
        if group_pick == "g1":
            print("\nGroup 1 Selected (Activities 1–5)")
            print("G1 - Activity 01")
            print("G2 - Activity 2")
            print("G3 - Activity 3")
            print("G4 - Activity 4")
            print("G5 - Activity 5")

            act_pick = input("Choose activity --> ").lower()

            if act_pick == "g1":
                activity1()
            elif act_pick == "g2":
                activity2()
            elif act_pick == "g3":
                activity3()
            elif act_pick == "g4":
                activity4()
            elif act_pick == "g5":
                activity5()
            else:
                print("Invalid activity!")
            continue

        # GROUP 2
        elif group_pick == "g2":
            print("\nGroup 2 Selected (Activities 6–10)")
            print("g6  - Activity 6")
            print("g7  - Activity 7")
            print("g8  - Activity 8")
            print("g9  - Activity 9")
            print("g10 - Activity 10")

            act_pick = input("Choose activity --> ").lower()

            if act_pick == "g6":
                activity6()
            elif act_pick == "g7":
                activity7()
            elif act_pick == "g8":
                activity8()
            elif act_pick == "g9":
                activity9()
            elif act_pick == "g10":
                activity10()
            else:
                print("Invalid activity!")
            continue

        # GROUP 3
        elif group_pick == "g3":
            print("\nGroup 3 Selected (Activities 11–15)")
            print("G11 - Activity 11")
            print("G12 - Activity 12")
            print("G13 - Activity 13")
            print("G14 - Activity 14")
            print("G15 - Activity 15")

            act_pick = input("Choose activity --> ").lower()

            if act_pick == "g11":
                activity11()
            elif act_pick == "g12":
                activity12()
            elif act_pick == "g13":
                activity13()
            elif act_pick == "g14":
                activity14()
            elif act_pick == "g15":
                activity15()
            else:
                print("Invalid activity!")
            continue

        # GROUP 4
        elif group_pick == "g4":
            print("\nGroup 4 Selected (Activities 16–20)")
            print("G16 - Activity 16")
            print("G17 - Activity 17")
            print("G18 - Activity 18")
            print("G19 - Activity 19")
            print("G20 - Activity 20")

            act_pick = input("Choose activity --> ").lower()

            if act_pick == "g16":
                activity16()
            elif act_pick == "g17":
                activity17()
            elif act_pick == "g18":
                activity18()
            elif act_pick == "g19":
                activity19()
            elif act_pick == "g20":
                activity20()
            else:
                print("Invalid activity!")
            continue

        # GROUP 5
        elif group_pick == "g5":
            print("\nGroup 5 Selected (Activities 21–24_1)")
            print("G21   - Activity 21")
            print("G22   - Activity 22")
            print("G23   - Activity 23")
            print("G24   - Activity 24")
            print("G24_1 - Activity 24_1")

            act_pick = input("Choose activity --> ").lower()

            if act_pick == "g21":
                activity21()
            elif act_pick =="g22":
                activity22()
            elif act_pick == "g23":
                activity23()
            elif act_pick == "g24":
                activity24()
            elif act_pick == "g24_1":
                activity25()
            else:
                print("Invalid activity!")
            continue

        # GROUP 6
        elif group_pick == "g6":
            print("\nGroup 6 Selected (Activities 26–28)")
            print("G26 - Activity 26")
            print("G27 - Activity 27")
            print("G28 - Activity 28")

            act_pick = input("Choose activity --> ").lower()

            if act_pick == "g26":
                activity26()
            elif act_pick == "g27":
                activity27()
            elif act_pick == "g28":
                activity28()
            else:
                print("Invalid activity!")
            continue

        elif group_pick == "q":
            print("Returning to Main Menu...")
            continue

        else:
            print("Invalid group!")
            continue

    # CODING CHALLENGES
    elif main_choice == "b":
        print("===== CODING CHALLENGES =====")
        print("Z1 - Challenges 1 to 5")
        print("Z2 - Challenges 6 to 10")
        print("Z3 - Challenges 11 to 15")
        print("Z4 - Challenge 16")
        print("ZQ - Back to Main Menu")
        print("============================")

        challenge_set = input("Choose set --> ").lower()

        if challenge_set == "z1":
            task_pick = input("Select C1–C5 --> ").lower()
            if task_pick == "c1": code_challenge1()
            elif task_pick == "c2": code_challenge2()
            elif task_pick == "c3": code_challenge3()
            elif task_pick == "c4": code_challenge4()
            elif task_pick == "c5": code_challenge5()
            else: print("Invalid challenge!")
            continue

        elif challenge_set == "z2":
            task_pick = input("Select C6–C10 --> ").lower()
            if task_pick == "c6": code_challenge6()
            elif task_pick == "c7": code_challenge7()
            elif task_pick == "c8": code_challenge8()
            elif task_pick == "c9": code_challenge9()
            elif task_pick == "c10": code_challenge10()
            else: print("Invalid challenge!")
            continue

        elif challenge_set == "z3":
            task_pick = input("Select C11–C15 --> ").lower()
            if task_pick == "c11": code_challenge11()
            elif task_pick == "c12": code_challenge12()
            elif task_pick == "c13": code_challenge13()
            elif task_pick == "c14": code_challenge14()
            elif task_pick == "c15": code_challenge15()
            else: print("Invalid challenge!")
            continue

        elif challenge_set == "z4":
            task_pick = input("Type C16 to continue --> ").lower()
            if task_pick == "c16": code_challenge16()
            else: print("Invalid challenge!")
            continue

        elif challenge_set == "zq":
            print("Returning to Main Menu...")
            continue

        else:
            print("Invalid selection!")
            continue

    else:
        print("Invalid main option!")
        continue
