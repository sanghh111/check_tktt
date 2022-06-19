from cgitb import reset
import random
from unittest import result
from constant.stk import ARR_SAME_LOC_PHAT, INSERT_TYPE, TEMP_COPARE_MIRROR
from tools import  check_mirror

from tools import delete_item_list


def rand_special_number(arr: list, len_n, limit):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    for i in range(len_n):
        [temp_arr.remove(j) for j in range(6, 10)] if limit == 0 else None
        temp_arr.remove(temp_int) if temp_int != None and temp_int in temp_arr else None
        value = random.randint(0, len(temp_arr) - 1)
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)
        limit = limit - 1 if temp_int >= 6 and temp_int <= 9 else limit
    return limit, result


def random_end_spe(arr: list, len_n, limit):
    result = []
    temp_arr = arr.copy()
    for i in range(len_n):
        if i == len_n -1:
            temp_arr.remove(8) if result == ARR_SAME_LOC_PHAT else None
        value = random.randint(0, len(temp_arr) - 1)
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)
    return limit, result

def rand_list(arr: list):
    value = random.randint(0, len(arr) - 1)
    return arr[value]


def rand_dict(arr: list):
    value = random.randint(1, len(arr)) if len(arr) > 1 else 1
    return arr[value]


def random_option(arr: list, spe_num: list, len_n, limit, option=None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    index_spe_num = 0
    for i in range(len_n):
        [temp_arr.remove(j) for j in range(6, 10)] if limit == 0 else None
        if option == "HEAD":
            if i == len_n - 1 and len_n > 2:
                delete_item_list(temp_arr, result[i - 1]) if result[i - 1] == result[i - 2] else None
        if option == "END":
            if i == 2:
                delete_item_list(temp_arr, result[1]) if result[0] == result[1] else None
        if option == "BETWEEN":
            delete_item_list(temp_arr, spe_num[0]) if i == 0  else None
            delete_item_list(temp_arr, spe_num[-1]) if i == len_n - 1 else None
        if option == "BETWEEN_HEAD":
            delete_item_list(temp_arr, spe_num[index_spe_num]) if index_spe_num < len(spe_num) else None
            delete_item_list(temp_arr, spe_num[index_spe_num - 1]) if index_spe_num != 0 and index_spe_num < len(
                spe_num) else None
        if option == "BETWEEN_END":
            delete_item_list(temp_arr, spe_num[index_spe_num]) if index_spe_num < len(spe_num) else None
            delete_item_list(temp_arr, spe_num[-1]) if i == len_n - 1 else None
        if i >= 2 :
            delete_item_list(temp_arr,result[i-1]) if result[i-1] == result[i-2] else None
        index_spe_num += 1
        value = random.randint(0, len(temp_arr) - 1)
        limit = limit - 1 if temp_arr[value] >= 6 and temp_arr[value] <= 9 else limit
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)
    return limit, result


def rand_mirror(arr: list, spe_num: list, len_n, limit, option=None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    for i in range(len_n):
        [temp_arr.remove(j) for j in range(6, 10)] if limit == 0 else None
        if option == 8 and len_n == 4 and i == len_n - 1:
            temp_arr_spe == TEMP_COPARE_MIRROR[1].format(A=spe_num[0], B=spe_num[1])
        delete_item_list(temp_arr, spe_num[0]) if temp_arr_spe[:3] == result else None
        if option == 12 and len_n == 6 and i == len_n - 1:
            temp_arr_spe = TEMP_COPARE_MIRROR[1].format(A=spe_num[0], B=spe_num[1], C=spe_num[2])
            delete_item_list(temp_arr, spe_num[0]) if spe_num[:5] == result else None
        value = random.randint(0, len(temp_arr) - 1)
        limit = limit - 1 if temp_arr[value] >= 6 and temp_arr[value] <= 9 else limit
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)
    return limit, result


def rand_repeat(arr: list, spe_num: list, len_n, limit, option=None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    for i in range(len_n):
        [temp_arr.remove(j) for j in range(6, 10)] if limit == 0 else None
        if i == len_n - 1:
            delete_item_list(temp_arr, 8) if result == ARR_SAME_LOC_PHAT and option == INSERT_TYPE[1] else None
            # if len(spe_num) == 2 :
            temp_spe_arr = []
            len_spe_num = len(spe_num)
            for j in range(0, i):
                temp_spe_arr.append(spe_num[j % len_spe_num])
            delete_item_list(temp_arr, spe_num[1]) if temp_spe_arr == result else None
            if len_spe_num == 2 and len_n == 2:
                delete_item_list(temp_arr,spe_num[0]) if temp_int == spe_num[-1] else None
            else :
                delete_item_list(temp_arr,result[0]) if check_mirror(result) else None
        value = random.randint(0, len(temp_arr) - 1)
        limit = limit - 1 if temp_arr[value] >= 6 and temp_arr[value] <= 9 else limit
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)
    return limit, result

def random_loc_phat(arr: list, spe_num: list, len_n, limit, option=None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    index_spe_num = 0
    for i in range(len_n):
        [temp_arr.remove(j) for j in range(6, 10)] if limit == 0 else None
        index_spe_num += 1
        if i>=2  :
            delete_item_list(temp_arr,result[i-1]) if result[i-1] == result[i-2] else None
        value = random.randint(0, len(temp_arr) - 1)
        limit = limit - 1 if temp_arr[value] >= 6 and temp_arr[value] <= 9 else limit
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)
    return limit, result

def random_end_nor(arr: list, spe_num: list, len_n, limit, option=None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    
    for i in range(len_n):
        if i >= 2:
            delete_item_list(temp_arr, result[i - 1]) if result[i - 1] == result[i - 2] else None
            for j in range(0,len_n-3):
                for k in range(3+j,len_n,2):   
                    delete_item_list(temp_arr, result[j]) if check_mirror(result) else None
        value = random.randint(0, len(temp_arr) - 1)
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)
    return limit, result

def rand_no_option(arr: list, spe_num: list, len_n, limit, option=None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    
    for i in range(len_n):
        value = rand_list(temp_arr)
        result.append(value)
    return limit, result

