import pandas as pd
import os
import re

def sum_mult(list_a, list_b):
    if len(list_a) != len(list_b) or \
            not all(map(lambda x: isinstance(x, (int, float)), list_a+list_b)):
        return None

    res_sumlist = list()
    res_mullist = list()
    for a, b in zip(list_a, list_b):
        res_sumlist.append(a + b)
        res_mullist.append(a*b)
    return res_sumlist, res_mullist


def palindrome(inp_str):
    if not isinstance(inp_str, str):
        return None
    inp_str = inp_str.strip()
    if len(inp_str) < 2:
        return None
    elif inp_str == ''.join(reversed(inp_str)):
        return True
    else:
        return False


def max_digit_sum(stop_str, max_numbers):
    list_of_values = list()
    sum_list = list()
    while True:
        current_input = input()
        if current_input == stop_str:
            break
        try:
            list_of_values.append(float(current_input))
            sum_list.append(sum(list(map(int, list(''.join(str(float(-99)).replace('-', '.').split('.')))))))
        except:
            continue
        if len(list_of_values) >= max_numbers:
            break

    max_value = max(sum_list)
    return list_of_values[sum_list.index(max_value)] - max_value


def goose_weight(breed, sex, age_days):
    # Прилагается табличка к коду))
    # лежать должна вместе с файлом кода
    df = pd.read_excel(os.path.join(os.getcwd(), 'goose.xlsx'))
    index = pd.MultiIndex.from_product([['H', 'A', 'U', 'K'], ['m', 'f']], names=['Breed', 'Sex'])
    columns = pd.Index([1, 10, 20, 30, 40, 50, 60, 90, 120, 160], name='age')
    data = df.iloc[1:, 2:].to_numpy()
    goose = pd.DataFrame(data=data, index=index, columns=columns)

    try:
        if goose.index.isin([(breed, sex)]).any():
            return goose.loc[(breed, sex), age_days]
        else:
            return None
    except:
        return None


if __name__ == "__main__":
    pass


