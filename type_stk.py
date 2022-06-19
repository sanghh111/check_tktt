import random
from constant.stk import BUSINESS_TYPE, TYPE_FOUR_FOUR_10,INSERT_TYPE
from random_number import rand_mirror, rand_repeat, rand_special_number , rand_list,rand_dict, random_end_nor, rand_no_option, random_option,random_loc_phat, random_end_spe
from tools import format_number, format_number1, get_cost_arr,get_data, format_spe, get_data_4_4, get_mirror_type, get_nor_spe, get_num_nor, get_number, get_repeat_type, merge_num_spe



def same_number(stk_type, size,is_vip,business_type=None,option=None):
    limit = stk_type['limit'] if not is_vip else -1
    arr = [1,2,3,4,5,6,7,8,9] if not is_vip else [6,7,8,9]
    account_struct = stk_type[str(size)]
    limt, arr_spe_n = rand_special_number(arr,1,limit)
    account_str, flag = format_spe(account_struct['struct'],arr_spe_n)
    return account_str, account_struct['cost']

def continous(stk_type, size,is_vip,business_type=None,option=None):
    if stk_type ==  None :
        raise KeyError 
    try:
        struct = stk_type[str(size)] 
        account_str = rand_list(struct['struct'])
        return account_str, struct['cost']
    except:
        raise KeyError

def three_thee(stk_type, size,is_vip,business_type=None,option=None):
    try:
        account_struct = stk_type[str(size)]
        arr,limit , num_spe, num_nor,cost = get_data(account_struct,is_vip)
        
        limit, arr_spe_n = rand_special_number(arr,num_spe,limit)
        account_struct = rand_dict(account_struct['format'])
        
        limit, arr_nor_n = random_option(arr,arr_spe_n,num_nor,limit,account_struct['insert_type'])

        spe, flag = format_spe(account_struct['struct'],arr_spe_n)
        if flag :
            return spe,cost
        number = format_number(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number)

    except:
        raise KeyError
    return account_str, cost


def four_four(stk_type, size,is_vip,business_type=None,option=None):
    try:
        type_option = get_data_4_4(size,business_type,option)

        account_struct = stk_type[str(size)] if type_option == None else stk_type[str(size)][type_option]
        arr,limit , num_spe, num_nor,cost = get_data(account_struct,is_vip)
        
        limit, arr_spe_n = rand_special_number(arr,num_spe,limit)
        account_struct = rand_dict(account_struct['format'])
        
        limit, arr_nor_n = random_option(arr,arr_spe_n,num_nor,limit,account_struct['insert_type'])

        spe, flag = format_spe(account_struct['struct'],arr_spe_n)
        if flag :
            return spe,cost
        number = format_number(arr_nor_n) if  type_option != TYPE_FOUR_FOUR_10[0]  else format_number1(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number)

    except:
        raise KeyError
    return account_str, cost


def five_five(stk_type, size,is_vip,business_type=None,option=None):
    try:
        account_struct = stk_type[str(size)]
        arr,limit , num_spe, num_nor,cost = get_data(account_struct,is_vip)
        
        limit, arr_spe_n = rand_special_number(arr,num_spe,limit)
        account_struct = rand_dict(account_struct['format'])
        
        limit, arr_nor_n = random_option(arr,arr_spe_n,num_nor,limit,account_struct['insert_type'])

        spe, flag = format_spe(account_struct['struct'],arr_spe_n)
        if flag :
            return spe,cost
        number = format_number1(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number)

    except:
        raise KeyError 
    return account_str, cost

def six_six(stk_type, size,is_vip,business_type=None,option=None):
    try:
        account_struct = stk_type[str(size)]
        arr,limit , num_spe, num_nor,cost = get_data(account_struct,is_vip)
        
        limit, arr_spe_n = rand_special_number(arr,num_spe,limit)
        account_struct = rand_dict(account_struct['format'])
        
        limit, arr_nor_n = random_option(arr,arr_spe_n,num_nor,limit,account_struct['insert_type'])

        spe, flag = format_spe(account_struct['struct'],arr_spe_n)
        if flag :
            return spe,cost
        number = format_number1(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number)

    except:
        raise KeyError 
    return account_str, cost

def three_four(stk_type, size,is_vip,business_type=None,option=None):
    try:
        account_struct = stk_type[str(size)]
        arr,limit , num_spe, num_nor,cost = get_data(account_struct,is_vip)
        account_struct = rand_dict(account_struct['format'])
        limit, arr_spe_n = rand_special_number(arr,num_spe,limit)
        
        limit, arr_nor_n = random_option(arr,arr_spe_n,num_nor,limit,account_struct['insert_type'])

        spe, flag = format_spe(account_struct['struct'],arr_spe_n)
        if flag :
            return spe,cost
        number = format_number(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number)

    except:
        raise KeyError 
    return account_str, cost

def mirror(stk_type, size,is_vip,business_type=None,option=None):
    try:
        if size == 10 and is_vip :
            raise ValueError

        if business_type == BUSINESS_TYPE[1]:
            option = True

        mirror_type = get_mirror_type(option)
        # print('stk_type: ', stk_type)
        try:
            account_struct = stk_type[mirror_type][str(size)]
        except:
            account_struct = stk_type[mirror_type][size]
        cost, arr  = get_cost_arr(account_struct,is_vip)
        account_struct = rand_dict(account_struct['format'])
        num_spe,num_nor,limit = get_number(account_struct)
        
        limit, arr_spe_n = rand_special_number(arr,num_spe,limit)
        limit, arr_nor_n = rand_mirror(arr,arr_spe_n,num_nor,limit,size)

        spe, flag = format_spe(account_struct['struct'],arr_spe_n)
        if flag :
            return spe,cost
        number = format_number(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number)

    except:
        raise KeyError
    return account_str, cost


def repeat(stk_type, size,is_vip,business_type=None,option=None):
    try:

        repeat_type = get_repeat_type(option)
        print('stk_type: ', stk_type)
        try:
            account_struct = stk_type[repeat_type][str(size)]
        except:
            account_struct = stk_type[repeat_type][size]
        cost, arr  = get_cost_arr(account_struct,is_vip)
        account_struct = rand_dict(account_struct['format'])
        num_spe,num_nor,limit = get_number(account_struct)
        
        limit, arr_spe_n = rand_special_number(arr,num_spe,limit)
        limit, arr_nor_n = rand_repeat(arr,arr_spe_n,num_nor,limit,account_struct['insert_type'])

        spe, flag = format_spe(account_struct['struct'],arr_spe_n)
        if flag :
            return spe,cost
        number = format_number(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number)

    except:
        raise KeyError 
    return account_str, cost


def loc_phat(stk_type, size,is_vip,business_type=None,option=None):
    try:
        if not is_vip :
            raise ValueError
        try:
            account_struct = stk_type[str(size)]
        except:
            account_struct = stk_type[size]
        arr, limit, num_spe, num_nor, cost = get_data(account_struct, is_vip)


        limit, arr_nor_n = random_option(arr, None, num_nor, limit, INSERT_TYPE[0])

        number = format_number(arr_nor_n)
        account_str = account_struct['struct'].format(number = number)

    except:
        raise KeyError
    return account_str, cost

def end_spe(stk_type, size,is_vip,business_type=None,option=None):
    try:
        if is_vip :
            raise ValueError
        try:
            account_struct = stk_type[str(size)]
        except:
            account_struct = stk_type[size]
        
        arr, limit, num_spe, num_nor, cost = get_data(account_struct, is_vip)
        arr_spe = [i for i in range(6,10)]
        limit = 20
        limit, arr_spe_n = random_end_spe(arr_spe, num_spe, limit)

        limit, arr_nor_n = random_end_nor(arr, arr_spe_n, num_nor, limit)

        spe, flag = format_spe(account_struct['struct'], arr_spe_n)
        if flag:
            return spe, cost

        limit, arr_nor_n = random_loc_phat(arr, None, num_nor, limit)

        number = format_number(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number = number)

    except:
        raise KeyError
    return account_str, cost


def end_same_number(stk_type, size,is_vip,business_type=None,option=None):
    try:
        try:
            account_struct = stk_type[str(size)]
        except:
            account_struct = stk_type[size]
        
        cost , arr = get_cost_arr(account_struct, is_vip)
        limit = 20

        account_struct = rand_dict(account_struct['format'])

        num_nor,num_spe = get_nor_spe(account_struct)

        limit, arr_spe_n = random_end_spe(arr, num_spe, limit)

        limit, arr_nor_n = rand_no_option(arr, arr_spe_n, num_nor, limit)

        spe, flag = format_spe(account_struct['struct'], arr_spe_n)
        if flag:
            return spe, cost

        limit, arr_nor_n = random_loc_phat(arr, None, num_nor, limit)

        number = format_number(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number = number)

    except:
        raise KeyError
    return account_str, cost

def end_special_number(stk_type, size,is_vip,business_type=None,option=None):
    try:
        try:
            account_struct = stk_type[str(size)]
        except:
            account_struct = stk_type[size]
        
        arr, limit, num_spe, num_nor, cost = get_data(account_struct, is_vip)
        limit = 20

        account_struct = rand_dict(account_struct['format'])

        num_nor,num_spe = get_nor_spe(account_struct)

        limit, arr_spe_n = random_end_spe(arr, num_spe, limit)

        limit, arr_nor_n = rand_no_option(arr, arr_spe_n, num_nor, limit)

        spe, flag = format_spe(account_struct['struct'], arr_spe_n)
        if flag:
            return spe, cost

        limit, arr_nor_n = random_loc_phat(arr, None, num_nor, limit)

        number = format_number(arr_nor_n)
        account_str = merge_num_spe(account_struct['struct'],spe,number = number)

    except:
        raise KeyError
    return account_str, cost