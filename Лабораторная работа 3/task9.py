salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

months_ = salary - spend
rost = (6000/100 * 3)+spend
need_money11 = ()
print(months_ ,"начало")


months_1=salary - rost
rost1 = (rost/100 * 3)+rost
nado = (months_1 + months_)*(-1)
print(nado,"оп, оп..живём-живём 1 ме")


months_2=salary - rost1
rost2 = (rost1/100 * 3)+rost1
nado1 = (nado - months_2 - months_1)*(1)
print(round(nado1),"оп, оп..живём-живём 2 ме")


months_3=salary - rost2
rost3 = (rost2/100 * 3)+rost2
nado2 = (nado1 - months_3 - months_2)*(1)
print(round(nado2),'оп, оп..живём-живём 3 ме')



months_4=salary - rost3
rost4 = (rost3/100 * 3)+rost3
nado3= (nado2 - months_4 - months_3)*(1)
print(round(nado3),'оп, оп..живём-живём 4 ме')


months_5=salary - rost4
rost5 = (rost4/100 * 3)+rost4
nado4= (nado3 - months_5 - months_4)*(1)
print(round(nado4), 'оп, оп..живём-живём 5 ме')

months_6=salary - rost5
rost6 = (rost5/100 * 3)+rost5
nado5= (nado4 - months_5 - months_4)*(1)
print(round(nado5), 'оп, оп..живём-живём 6 м')


months_7=salary - rost6
rost7 = (rost6 /100 * 3)+rost6
nado6= (nado4 - months_6 - months_5)*(1)
print(round(nado6), 'оп, оп..живём-живём 7 мес')



months_8=salary - rost7
rost8 = (rost7 /100 * 3)+rost7
nado7= (nado5 - months_7 - months_6)*(1)
print(round(nado7), 'оп, оп..живём-живём 8 мес')


months_9=salary - rost7
rost9 = (rost8 /100 * 3)+rost8
nado8= (nado6 - months_8 - months_6)*(1)
print(round(nado8), 'оп, оп..живём-живём 9 мес')


months_10=salary - rost8
rost10 = (rost9 /100 * 3)+rost9
nado9= (nado7 - months_9 - months_7)*(1)
print(round(nado9), 'оп, оп..живём-живём 10 мес')


months_11=salary - rost8
rost11 = (rost10 /100 * 3)+rost10
nado10= (nado9 - months_9 - months_8)*(1)

print(round(nado10) ,"нужно для 11-ого месяцa")
