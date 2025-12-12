from def_function import *

print("====== FINAL PROJECT COMPILER ======\n")

user_profile = input("Greetings! Please enter your name --> ")
print(f"Hello {user_profile}! Welcome to my Final Project Compiler.\n")

program_active = True

while program_active == True:

    print("\n================ MAIN MENU ================")
    print("Select an option below:")
    print("A - Activities Section")
    print("B - Code Challenges Section")
    print("X - Exit Program")
    print("============================================")

    main_input = input("Your choice --> ").lower()
    print("")

    # EXIT PROGRAM
    if main_input == "x":
        print("System shutting down... Goodbye!")
        break

    # ACTIVITIES SECTION
    elif main_input == "a":
        print("===== ACTIVITIES MENU =====")
        print("Choose from the following groups:")
        print("G1 - Activities 1 to 5")
        print("G2 - Activities 6 to 10")
        print("G3 - Activities 11 to 15")
        print("G4 - Activities 16 to 20")
        print("G5 - Activities 21 to 24_1")
        print("G6 - Activities 26 to 28")
        print("Q  - Quit Activities Menu")
        print("=============================")

        act_group = input("Select group: ").lower()

        # GROUP 1
        if act_group == "g1":
            print("\nYou've selected Group 1 (Activities 1–5)")
            print("Choose one activity: ")
            print("A1 - Activity 1")
            print("A2 - Activity 2")
            print("A3 - Activity 3")
            print("A4 - Activity 4")
            print("A5 - Activity 5")

            sub_act = input("Pick activity: ").lower()

            if sub_act == "a1":
                print("Launching Activity 1...")
                activity1()
                continue

            elif sub_act == "a2":
                print("Launching Activity 2...")
                activity2()
                continue

            elif sub_act == "a3":
                print("Launching Activity 3...")
                activity3()
                continue

            elif sub_act == "a4":
                print("Launching Activity 4...")
                activity4()
                continue

            elif sub_act == "a5":
                print("Launching Activity 5...")
                activity5()
                continue

            else:
                print("Invalid option! Returning to menu.")
                continue

        # GROUP 2
        elif act_group == "g2":
            print("\nYou've selected Group 2 (Activities 6–10)")
            print("Choose one activity: ")
            print("A6  - Activity 6")
            print("A7  - Activity 7")
            print("A8  - Activity 8")
            print("A9  - Activity 9")
            print("A10 - Activity 10")

            sub_act = input("Pick activity: ").lower()

            if sub_act == "a6":
                print("Launching Activity 6...")
                activity6()
                continue

            elif sub_act == "a7":
                print("Launching Activity 7...")
                activity7()
                continue

            elif sub_act == "a8":
                print("Launching Activity 8...")
                activity8()
                continue

            elif sub_act == "a9":
                print("Launching Activity 9...")
                activity9()
                continue

            elif sub_act == "a10":
                print("Launching Activity 10...")
                activity10()
                continue

            else:
                print("Invalid option! Returning to menu.")
                continue

        # GROUP 3
        elif act_group == "g3":
            print("\nYou've selected Group 3 (Activities 11–15)")
            print("Choose one activity: ")
            print("A11 - Activity 11")
            print("A12 - Activity 12")
            print("A13 - Activity 13")
            print("A14 - Activity 14")
            print("A15 - Activity 15")

            sub_act = input("Pick activity: ").lower()

            if sub_act == "a11":
                print("Launching Activity 11...")
                activity11()
                continue

            elif sub_act == "a12":
                print("Launching Activity 12...")
                activity12()
                continue

            elif sub_act == "a13":
                print("Launching Activity 13...")
                activity13()
                continue

            elif sub_act == "a14":
                print("Launching Activity 14...")
                activity14()
                continue

            elif sub_act == "a15":
                print("Launching Activity 15...")
                activity15()
                continue

            else:
                print("Invalid option! Returning to menu.")
                continue

        # GROUP 4
        elif act_group == "g4":
            print("\nYou've selected Group 4 (Activities 16–20)")
            print("Choose one activity: ")
            print("A16 - Activity 16")
            print("A17 - Activity 17")
            print("A18 - Activity 18")
            print("A19 - Activity 19")
            print("A20 - Activity 20")

            sub_act = input("Pick activity: ").lower()

            if sub_act == "a16":
                print("Launching Activity 16...")
                activity16()
                continue

            elif sub_act == "a17":
                print("Launching Activity 17...")
                activity17()
                continue

            elif sub_act == "a18":
                print("Launching Activity 18...")
                activity18()
                continue

            elif sub_act == "a19":
                print("Launching Activity 19...")
                activity19()
                continue

            elif sub_act == "a20":
                print("Launching Activity 20...")
                activity20()
                continue

            else:
                print("Invalid option! Returning to menu.")
                continue

        # GROUP 5
        elif act_group == "g5":
            print("\nYou've selected Group 5 (Activities 21–24_1)")
            print("Choose one activity: ")
            print("A21     - Activity 21")
            print("A22     - Activity 22")
            print("A23     - Activity 23")
            print("A24     - Activity 24")
            print("A24_1   - Activity 24_1")

            sub_act = input("Pick activity: ").lower()

            if sub_act == "a21":
                print("Launching Activity 21...")
                activity21()
                continue

            elif sub_act == "a22":
                print("Launching Activity 22...")
                activity22()
                continue

            elif sub_act == "a23":
                print("Launching Activity 23...")
                activity23()
                continue

            elif sub_act == "a24":
                print("Launching Activity 24...")
                activity24()
                continue

            elif sub_act == "a24_1":
                print("Launching Activity 24_1...")
                activity25()
                continue

            else:
                print("Invalid option! Returning to menu.")
                continue

        # GROUP 6
        elif act_group == "g6":
            print("\nYou've selected Group 6 (Activities 26–28)")
            print("Pick one activity:")
            print("A26 - Activity 26")
            print("A27 - Activity 27")
            print("A28 - Activity 28")

            sub_act = input("Pick activity: ").lower()

            if sub_act == "a26":
                print("Launching Activity 26...")
                activity26()
                continue
            elif sub_act == "a27":
                print("Launching Activity 27...")
                activity27()
                continue
            elif sub_act == "a28":
                print("Launching Activity 28...")
                activity28()
                continue
            else:
                print("Invalid input!")
                continue

        elif act_group == "q":
            print("Exiting Activities Menu...")
            continue

        else:
            print("Invalid group selection!")
            continue


    # CODE CHALLENGES SECTION
    elif main_input == "b":

        print("===== CODE CHALLENGES MENU =====")
        print("Z1 - Challenges 1 to 5")
        print("Z2 - Challenges 6 to 10")
        print("Z3 - Challenges 11 to 15")
        print("Z4 - Challenge 16")
        print("ZQ - Quit Code Challenges")
        print("================================")

        chal_group = input("Choose a group: ").lower()

        # CHALLENGE GROUP 1
        if chal_group == "z1":
            print("\nYou've chosen Challenges 1 to 5")
            print("Select:")
            print("C1 - Challenge 1")
            print("C2 - Challenge 2")
            print("C3 - Challenge 3")
            print("C4 - Challenge 4")
            print("C5 - Challenge 5")

            task = input("Pick challenge: ").lower()

            if task == "c1":
                code_challenge1()
                continue
            elif task == "c2":
                code_challenge2()
                continue
            elif task == "c3":
                code_challenge3()
                continue
            elif task == "c4":
                code_challenge4()
                continue
            elif task == "c5":
                code_challenge5()
                continue
            else:
                print("Invalid input!")
                continue

        # CHALLENGE GROUP 2
        elif chal_group == "z2":
            print("\nYou've chosen Challenges 6 to 10")
            print("Select:")
            print("C6  - Challenge 6")
            print("C7  - Challenge 7")
            print("C8  - Challenge 8")
            print("C9  - Challenge 9")
            print("C10 - Challenge 10")

            task = input("Pick challenge: ").lower()

            if task == "c6":
                code_challenge6()
                continue
            elif task == "c7":
                code_challenge7()
                continue
            elif task == "c8":
                code_challenge8()
                continue
            elif task == "c9":
                code_challenge9()
                continue
            elif task == "c10":
                code_challenge10()
                continue
            else:
                print("Invalid input!")
                continue

        # CHALLENGE GROUP 3
        elif chal_group == "z3":
            print("\nYou've chosen Challenges 11 to 15")
            print("Select:")
            print("C11 - Challenge 11")
            print("C12 - Challenge 12")
            print("C13 - Challenge 13")
            print("C14 - Challenge 14")
            print("C15 - Challenge 15")

            task = input("Pick challenge: ").lower()

            if task == "c11":
                code_challenge11()
                continue
            elif task == "c12":
                code_challenge12()
                continue
            elif task == "c13":
                code_challenge13()
                continue
            elif task == "c14":
                code_challenge14()
                continue
            elif task == "c15":
                code_challenge15()
                continue
            else:
                print("Invalid input!")
                continue

        # CHALLENGE GROUP 4
        elif chal_group == "z4":
            print("You selected Challenge 16")
            print("To continue, type: C16")
            task = input("Select challenge: ").lower()

            if task == "c16":
                code_challenge16()
                continue
            else:
                print("Invalid input!")
                continue

        elif chal_group == "zq":
            print("Exiting Code Challenges...")
            continue

        else:
            print("Invalid group selection!")
            continue


    # INVALID MAIN INPUT
    else:
        print("Invalid menu choice! Please choose a valid option.")
        continue
