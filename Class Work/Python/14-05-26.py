# #Guess the number between 1 to 50

# import random

# lucky = random.randint(1, 50)
# chance = 1

# while True:
#     if chance < 4:
#         print("Chance ", chance)
#         choice = int(input("Enter Number"))

#         if choice > 50:
#             print("Invalid choice")
#             break

#         elif choice == lucky:
#             print("You Win")
#             break

#         elif choice < lucky:
#             print("Original number is greater")
#             chance += 1
#         else:
#             print("Original number is lower")
#             chance += 1
#     else:
#         print("You Lost")
#         break
#======================================================================================================

# import random
# l = ["rock", "paper", "scissor"]


# while True:
#     comp = random.choice(l)
#     choicess ="Choose between rock, paper and scissor"
#     print(choicess)
#     choice = input("Your Choice : ")

#     if choice == "rock" and comp == "rock":
#         print("Computer choose : " ,comp)
#         print("Draw")
#     elif choice == "paper" and comp == "paper":
#         print("Computer choose : " ,comp)
#         print("Draw")
#     elif choice == "scissor" and comp == "scissor":
#         print("Computer choose : " ,comp)
#         print("Draw")
#     elif choice == "rock" and comp == "scissor":
#         print("Computer choose : " ,comp)
#         print("You Win")
#     elif choice == "paper" and comp == "rock":
#         print("Computer choose : " ,comp)
#         print("You Win")
#     elif choice == "scissor" and comp == "paper":
#         print("Computer choose : " ,comp)
#         print("You Win")
#     else:
#         print("Computer choose : " ,comp)
#         print("You Lost")
        


