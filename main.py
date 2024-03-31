from front_end import input_var, pie_chart, bar_graph
from backend import Add_to_excel, Extract_value, get_CurrentMonth, monthly_expenses


lstypes, user_input_descr, user_input_cost, expense_type, button_state = input_var()
current_Month = get_CurrentMonth()

if button_state:
    Add_to_excel(expense_type, user_input_descr, user_input_cost, current_Month)
    print("clicked")
else:
    print("fail")
    
food_amt, transport_amt, phonebill_amt, shopping_amt, investment_amt, others_amt, list_month_Amt = Extract_value()
current_month_food, current_month_transport, current_month_phonebill, current_month_shopping, current_month_investment, current_month_others = monthly_expenses(current_Month)

pie_chart(lstypes, current_month_food, current_month_transport, current_month_phonebill, current_month_shopping, current_month_investment, current_month_others)

total_Amt = food_amt + transport_amt + phonebill_amt + shopping_amt + investment_amt
bar_graph(list_month_Amt, current_Month)