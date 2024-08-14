# print("hello")
import pandas as pd

from random import randrange

# excel_data = pd.ExcelFile('testSheet.xlsx')
# print(df)
# df1 = pd.read_excel(df, 'Settlements')
# print(df1)
def inputMatching(inp):
    match inp:
        case 1:
            return "Settlements"
        case 2:
            return "Ruins"
        case _:
            return "Error"

excel_file_path = 'testSheet.xlsx'

excel_data = pd.ExcelFile(excel_file_path)
sheet_dataframes = {}
for sheet_name in excel_data.sheet_names:
    sheet_dataframes[sheet_name] = pd.read_excel(excel_file_path, sheet_name=sheet_name, header=None)

keepGoing = True

while keepGoing:

    introText = "\nWhat table do you want to roll?\n(1) Settlements\n(2) Ruins\n Input:"
    choice = input(introText)
    if (choice == "exit") or (choice == "quit") or (choice == "q"):
        exit()
    sheet = inputMatching(int(choice))
    if sheet == "Error":
        print("Try again")
        continue

    current_df = sheet_dataframes[sheet]
    # print(current_df)
    # print(current_df.head())
    diceMax = len(current_df)
    # print("\n")
    # print(diceMax)
    roll = randrange(1, diceMax+1)
    print("###\n\t ``Rolled", roll, "on the", sheet,"table\n\t", current_df.iloc[roll-1].loc[1])
    if len(current_df.columns) == 3:
        initialDice = current_df.iloc[roll-1].loc[2]
        numberOfDice, diceNumber = initialDice.split("d")

        # diceNumber = int(initialDice[1].split("d"))
        if "+" in initialDice:
            diceNumber, addition = diceNumber.split("+")
        else:
            addition = 0
        # print(initialDice)
        # print(numberOfDice)   
        # print(addition)
        total = 0
        for i in range(0, int(numberOfDice)):
            total = total + randrange(1, int(diceNumber))
        
        total = total+int(addition)
        print("\t",initialDice, "gives", total)
        print("\n###")
