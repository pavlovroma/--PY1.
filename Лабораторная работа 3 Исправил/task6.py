list_ = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


for i, ind_ in enumerate(list_):
    chis = max(list_)
    if ind_ == chis:
        print(chis, "максимальное число/", i, "индекс макc числа")
        list_[ i ], list_[ -1 ] = list_[ -1 ], list_[ i ]
        print(list_)