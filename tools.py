import string
from constant.stk import MIRROR_TYPE, REPEAT_TYPE, TYPE_FOUR_FOUR_10, BUSINESS_TYPE

# TYPE_FOUR_FOUR_10 = ["ADJACENT","NO_ADJACENT"]s

# BUSINESS_TYPE = ["PERSONAL","BUSINESS"]

alphabet_low = string.ascii_lowercase

alphabet_up = string.ascii_uppercase


def format_spe(struct, data):
    temp_dist = {}
    for i in range(len(data)):
        temp_dist[alphabet_up[i]] = data[i]
    try:
        struct = struct.format(**temp_dist)
        return struct, True
    except:
        return temp_dist, False


def format_number(data):
    number = ''
    for i in data:
        number += str(i)
    return number


def format_number1(data):
    temp_dist = {}
    for i in range(len(data)):
        temp_dist[alphabet_low[i]] = data[i]
    return temp_dist


def merge_num_spe(struct, spe, number):
    try:
        spe.update(**number)
    except:
        spe.update(number=number) if number != '' else None
    return struct.format(**spe)


def get_data(struct, is_vip):
    limit = struct['limit'] if not is_vip else -1
    num_spe = struct['num_spe']
    num_nor = struct['num_nor']
    cost = struct['cost']
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] if not is_vip else [6, 7, 8, 9]

    return arr, limit, num_spe, num_nor, cost


def get_data_4_4(size, business_type, option):
    if not (size == 10 and business_type == BUSINESS_TYPE[1]):
        return None
    return TYPE_FOUR_FOUR_10[0] if option else TYPE_FOUR_FOUR_10[1]


def delete_item_list(arr: list, value):
    try:
        arr.remove(value)
    except:
        pass


def get_num_nor(struct):
    return struct['num_nor']


def get_cost_arr(struct, is_vip):
    arr = [i for i in range(1, 10)] if not is_vip else [i for i in range(6, 10)]
    return struct['cost'], arr


def get_mirror_type(option):
    return MIRROR_TYPE[0] if option else MIRROR_TYPE[1]


def get_repeat_type(option):
    return REPEAT_TYPE[0] if option else REPEAT_TYPE[1]


def get_number(struct):
    return struct['num_spe'], struct['num_nor'], struct['limit']
    pass

def check_mirror(arr):
    len_arr = len(arr) + 1
    half_len_arr = int((len_arr / 2 ))
    for i in range(half_len_arr-1):
        print((i))
        print(arr[half_len_arr -i -1 ])
        if arr[half_len_arr -i -1 ] != arr[half_len_arr + i] :
            return  False
    return True


arr = [1,2,2,2]
print(check_mirror(arr))