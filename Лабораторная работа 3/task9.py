salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
current_spend = spend

for current_deng in range(1, months + 1 ):
        current_deng = (current_spend - salary)
        current_spend = (increase + 1) * current_spend
        need_money += current_deng
print(round(need_money),"рублей")
