# getting variable according the following example
#
# price - 28$
# add to it 2 dollars
# 30
# '30$'

price = '28$'
new_price = price[:2]
new_price_int = int(new_price)
update_price = new_price_int + 2
update_price_str = str(update_price) + '$'
print(update_price_str)
