money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
in_spend = 6000
month = 3

Trata = salary - spend
ost_month = money_capital + Trata
prose = (6000 / 100 * 5) + spend
print(Trata)
print(ost_month)
print(prose)
if ost_month <= 0:
    print( "1 месяц")
else:
    Trata1= salary - prose
    ost_month1 = ost_month + Trata1
    prose1= (prose/100 * 5) + prose

if ost_month1 <= 0:
    print("2 месяц")
else:
    Trata2 = salary - prose1
    ost_month2 = ost_month1 + Trata2
    prose2 = (prose1 / 100 * 5) + prose1

    print(Trata2)
    print(ost_month2)
    print(prose2)
    if ost_month2 <= 0:
        print("3 месяц")
    else:

        Trata3 = salary - prose2
        ost_month3 = ost_month2 + Trata3
        prose3 = (prose2 / 100 * 5) + prose2
        print(Trata3)
        print(ost_month3)
        print(prose3)
        if ost_month3 <= 0:
            print("4 месяц")
        else:
            Trata4 = salary - prose3
            ost_month4 = ost_month3 + Trata4
            prose4 = (prose3 / 100 * 5) + prose3
            print(Trata4)
            print(ost_month4)
            print(prose4)
        if ost_month4 <= 0:
            print("5 месяц")
        else:
            Trata5 = salary - prose4
            ost_month5 = ost_month4 + Trata5
            prose5 = (prose4 / 100 * 5) + prose4
            print(Trata5)
            print(ost_month5)
            print(prose5)
            if ost_month5 <= 0:
                print("6 месяц")
            else:
                Trata6 = salary - prose5
                ost_month6 = ost_month5 + Trata6
                prose6 = (prose5 / 100 * 5) + prose5
                print(Trata6)
                print(ost_month6)
                print(prose6)
                if ost_month6 <= 0:
                    print("7 месяц")
                else:

                    Trata7 = salary - prose6
                    ost_month7 = ost_month6 + Trata7
                    prose7 = (prose6 / 100 * 5) + prose6

