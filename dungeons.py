# print("hello")
import pandas as pd
from random import randrange

# def inputMatching(inp):
#     match inp:
#         case 1:
#             return "Settlements"
#         case 2:
#             return "Ruins"
#         case 3:
#             return "Long Rambly Name"
#         case _:
#             return "Error"

excel_file_path = 'Dungeon Creation.xlsx'

excel_data = pd.ExcelFile(excel_file_path)
sheet_dataframes = {}
for sheet_name in excel_data.sheet_names:
    sheet_dataframes[sheet_name] = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=None)

current_df = sheet_dataframes[0]
print(current_df)

# keepGoing = True
# # print(len(sheet_dataframes))

# while keepGoing:
#     introText = "\nWhat table do you want to roll?" #\n(1) Settlements\n(2) Ruins\n Input:"
#     for j in range(1, len(sheet_dataframes)+1):
#         # print(j)
#         introText = introText + f"\n{j} {inputMatching(j)}"

#     introText = introText + "\n Input: "
#     choice = input(introText)
#     if (choice == "exit") or (choice == "quit") or (choice == "q"):
#         exit()
#     sheet = inputMatching(int(choice))
#     if sheet == "Error":
#         print("Try again")
#         continue

#     current_df = sheet_dataframes[sheet]
#     diceMax = len(current_df)
#     roll = randrange(1, diceMax+1)
#     print("###\n\t Rolled", roll, "on the", sheet,"table\n\t", current_df.iloc[roll-1].loc[1])
#     if len(current_df.columns) == 3:
#         initialDice = current_df.iloc[roll-1].loc[2]
#         numberOfDice, diceNumber = initialDice.split("d")

#         # diceNumber = int(initialDice[1].split("d"))
#         if "+" in initialDice:
#             diceNumber, addition = diceNumber.split("+")
#         else:
#             addition = 0
#         # print(initialDice)
#         # print(numberOfDice)
#         # print(addition)
#         total = 0
#         for i in range(0, int(numberOfDice)):
#             total = total + randrange(1, int(diceNumber))

#         total = total+int(addition)
#         print("\t",initialDice, "gives", total)
#         print("###")
