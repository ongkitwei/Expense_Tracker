from front_end import input_var, pie_chart
from backend import Add_to_excel, Extract_value
import streamlit as st


lstypes, user_input_descr, user_input_cost, expense_type, button_state = input_var()

if button_state:
    Add_to_excel(expense_type, user_input_descr, user_input_cost)
    print("clicked")
else:
    print("fail")
    
food_amt, transport_amt, phonebill_amt, shopping_amt, investment_amt = Extract_value()
pie_chart(lstypes, food_amt, transport_amt, phonebill_amt, shopping_amt, investment_amt)

