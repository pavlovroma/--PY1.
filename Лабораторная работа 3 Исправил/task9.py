salary = 5000
spend = 6000
months = 10
increase = 0.03

need_money = 0


for sum_ in range(1, months + 1):
    sum_ = (spend - salary)

    spend *= (0.03 + 1)
    need_money += sum_

    print(round(need_money), "руб")