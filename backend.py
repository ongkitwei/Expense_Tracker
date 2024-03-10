import pandas as pd

def Add_to_excel(type, description, amount):
    df = pd.read_csv("info.csv" )
    print(df)
    row_to_add = int(len(df)) + 1
    
    df.loc[row_to_add, "TYPE"] = type
    df.loc[row_to_add, "DESCRIPTION"] = description
    df.loc[row_to_add, "AMOUNT"] = amount

    df.iloc[:, 2] = ''

    df.to_csv("info.csv", index=False) 
    print(df)

def Extract_value():
    df = pd.read_csv("info.csv" )

    #food amount 
    food_amount_array = df[df['TYPE'] == 'Food']['AMOUNT']
    food_amount_total = sum(food_amount_array)

    #transport amount
    transport_amount_array = df[df['TYPE'] == 'Transport']['AMOUNT']
    transport_amount_total = sum(transport_amount_array)

    #phone bill amount
    phonebill_amount_array = df[df['TYPE'] == 'Phone Bill']['AMOUNT']
    phonebill_amount_total = sum(phonebill_amount_array)

    #shopping amount
    shopping_amount_array = df[df['TYPE'] == 'Shopping']['AMOUNT']
    shopping_amount_total = sum(shopping_amount_array)

    #investment amount
    investment_amount_array = df[df['TYPE'] == 'Investment']['AMOUNT']
    investment_amount_total = sum(investment_amount_array)

    fa = 5
    pba =65
    sa =44
    ia =34
    return food_amount_total, transport_amount_total, phonebill_amount_total, shopping_amount_total, investment_amount_total

