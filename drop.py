import pandas as pd

df = pd.read_csv("info.csv" )
# amount = df.iloc[:,3]

# amount_list = [x for x in amount]
# # total = amount_list.sum()

# print(amount_list)
# print(sum(amount_list))


# transport_df = df[df['TYPE'] == 'Transport']
transport_amount = df[df['TYPE'] == 'Transport']['AMOUNT']
print(sum(transport_amount))