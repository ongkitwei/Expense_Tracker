import streamlit as st
import plotly.express as px

# User's description of expense
def input_var():
    typesE = ("Food", "Transport", "Phone Bill", "Shopping", "Investment")
    col1, col3 = st.columns(2)

    with col1:
        user_input_descr = st.text_input(label="", placeholder="enter description of expense")

    with col3:
        user_input_cost = st.text_input(label="", placeholder="$")

    expense_type = st.selectbox(
                    "Select the type",
                    typesE
        )
    
    button_state = st.button(" ADD ", use_container_width=True)
    return typesE, user_input_descr, user_input_cost, expense_type, button_state

#Show numbers on pie chart
def pie_chart(ls, food_amt, transport_amt, phonebill_amt, shopping_amt, investment_amt):
    labels = [x for x in ls]
    values = [food_amt, transport_amt, phonebill_amt, shopping_amt, investment_amt] #need to change this ltr/

    fig = px.pie(names=labels, values=values, title='Pie Chart')
    st.plotly_chart(fig)