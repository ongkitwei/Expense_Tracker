import pandas as pd
from datetime import date

def Add_to_excel(type, description, amount, month):
    df = pd.read_csv("info.csv" )
    print(df)
    row_to_add = int(len(df)) + 1
    
    df.loc[row_to_add, "TYPE"] = type
    df.loc[row_to_add, "DESCRIPTION"] = description
    df.loc[row_to_add, "AMOUNT"] = amount
    df.loc[row_to_add, "DATE"] = month

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

    #others amount
    others_amount_array = df[df['TYPE'] == 'Others']['AMOUNT']
    others_amount_total = sum(others_amount_array)
    # Consolidate Amount for each month
    
    # JAN
    jan_Amt = sum([x for x in df[df["DATE"] == "January"]["AMOUNT"]])
    
    # FEB
    feb_Amt = sum([x for x in df[df["DATE"] == "February"]["AMOUNT"]])

    # MAR
    mar_Amt = sum([x for x in df[df["DATE"] == "March"]["AMOUNT"]])

    # APR
    apr_Amt = sum([x for x in df[df["DATE"] == "April"]["AMOUNT"]])

    # May
    may_Amt = sum([x for x in df[df["DATE"] == "May"]["AMOUNT"]])

    # JUN
    jun_Amt = sum([x for x in df[df["DATE"] == "June"]["AMOUNT"]])

    # JUL
    jul_Amt = sum([x for x in df[df["DATE"] == "July"]["AMOUNT"]])

    # AUG
    aug_Amt = sum([x for x in df[df["DATE"] == "August"]["AMOUNT"]])

    # SEP
    sep_Amt = sum([x for x in df[df["DATE"] == "September"]["AMOUNT"]])

    # OCT
    oct_Amt = sum([x for x in df[df["DATE"] == "October"]["AMOUNT"]])

    # NOV
    nov_Amt = sum([x for x in df[df["DATE"] == "November"]["AMOUNT"]])

    # DEC
    dec_Amt = sum([x for x in df[df["DATE"] == "December"]["AMOUNT"]])

    list_month_Amt = [jan_Amt, feb_Amt, mar_Amt, apr_Amt, may_Amt, jun_Amt, jul_Amt, aug_Amt, sep_Amt, oct_Amt, nov_Amt, dec_Amt]

    return food_amount_total, transport_amount_total, phonebill_amount_total, shopping_amount_total, investment_amount_total, others_amount_total, list_month_Amt

def monthly_expenses(current_month):
    df = pd.read_csv("info.csv" )

    # food 
    current_month_food = sum(df[(df["DATE"] == current_month) & (df["TYPE"] == "Food")]["AMOUNT"])

    # transport
    current_month_transport = sum(df[(df["DATE"] == current_month) & (df["TYPE"] == "Transport")]["AMOUNT"])

    # phone bill amount
    current_month_phonebill = sum(df[(df["DATE"] == current_month) & (df["TYPE"] == "Phone Bill")]["AMOUNT"])

    # shopping amount
    current_month_shopping = sum(df[(df["DATE"] == current_month) & (df["TYPE"] == "Shopping")]["AMOUNT"])

    # investment amount
    current_month_investment = sum(df[(df["DATE"] == current_month) & (df["TYPE"] == "Investment")]["AMOUNT"])

    # others amount
    current_month_others = sum(df[(df["DATE"] == current_month) & (df["TYPE"] == "Others")]["AMOUNT"])

    return current_month_food, current_month_transport, current_month_phonebill, current_month_shopping, current_month_investment, current_month_others

def get_CurrentMonth():
    today = date.today()
    current_month = today.strftime("%B")
    return current_month