import random
from constant.stk import INSERT_TYPE, TEMP_COPARE_MIRROR

from tools import delete_item_list

def rand_special_number(arr:list,len_n,limit):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    for i in range(len_n):
        [ temp_arr.remove(j) for j in range(6,10)] if limit == 0 else None 
        temp_arr.remove(temp_int) if temp_int != None and temp_int in temp_arr else None
        value = random.randint(0,len(temp_arr)-1)
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)      
        limit = limit - 1 if temp_int >= 6 and temp_int <= 9 else limit
    return limit , result

def rand_list(arr:list):
    value = random.randint(0,len(arr)-1)
    return arr[value]

def rand_dict(arr:list):
    
    value = random.randint(1,len(arr)) if len(arr) >1 else 1
    return arr[value]

def random_option(arr:list,spe_num:list,len_n,limit,option = None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    index_spe_num = 0
    for i in range(len_n):
        [ temp_arr.remove(j) for j in range(6,10)] if limit == 0 else None 
        if option == "HEAD":
            delete_item_list(temp_arr,spe_num[0]) if i == len_n-1 else None
            if i == len_n -1 and len_n > 2 :
                delete_item_list(temp_arr,result[i-1]) if result[i-1] == result[i-2]  else None
        if option == "END":
            delete_item_list( temp_arr,spe_num[-1]) if i == 0 else None
            if i==2 :
                delete_item_list(temp_arr,result[1]) if result[0] == result[1]  else None
        if option == "BETWEEN" :
            delete_item_list(temp_arr,spe_num[0]) if i == 0 else None
            delete_item_list(temp_arr,spe_num[-1]) if i == len_n -1 else None
        if option == "BETWEEN_HEAD":
            delete_item_list(temp_arr,spe_num[index_spe_num]) if  index_spe_num < len(spe_num)   else None
            delete_item_list(temp_arr,spe_num[index_spe_num - 1]) if  index_spe_num != 0 and index_spe_num < len(spe_num) else None
        if option == "BETWEEN_END":
            delete_item_list(temp_arr,spe_num[index_spe_num]) if index_spe_num < len(spe_num)  else None
            delete_item_list(temp_arr,spe_num[-1]) if  i == len_n-1 else None
        index_spe_num += 1
        print('temp_arr: ', temp_arr)
        value = random.randint(0,len(temp_arr)-1)
        limit = limit -1 if temp_arr[value] >=6 and temp_arr[value] <=9 else limit
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)      
    return limit , result

def rand_mirror(arr:list,spe_num:list,len_n,limit,option = None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    for i in range(len_n):
        [ temp_arr.remove(j) for j in range(6,10)] if limit == 0 else None 
        if option ==8  and len_n == 4 and i == len_n-1:
            temp_arr_spe == TEMP_COPARE_MIRROR[1].format(A=spe_num[0]
                                                        ,B=spe_num[1])
            delete_item_list(temp_arr,spe_num[0]) if  temp_arr_spe[:3] == result else None
        if option ==12  and len_n == 6 and i == len_n -1 :
            temp_arr_spe = TEMP_COPARE_MIRROR[1].format(A=spe_num[0]
                                                        ,B=spe_num[1],
                                                        C=spe_num[2])
            delete_item_list(temp_arr,spe_num[0]) if spe_num[:5] == result else None
        value = random.randint(0,len(temp_arr)-1)
        limit = limit -1 if temp_arr[value] >=6 and temp_arr[value] <=9 else limit
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)      
    return limit , result


def rand_repeat(arr:list,spe_num:list,len_n,limit,option = None):
    result = []
    temp_int = None
    temp_arr = arr.copy()
    for i in range(len_n):
        [ temp_arr.remove(j) for j in range(6,10)] if limit == 0 else None 
        if i == len_n-1:
            delete_item_list(temp_arr,8) if temp_int == 6 and option == INSERT_TYPE[1] else None
        value = random.randint(0,len(temp_arr)-1)
        limit = limit -1 if temp_arr[value] >=6 and temp_arr[value] <=9 else limit
        temp_int = temp_arr[value]
        temp_arr = arr.copy()
        result.append(temp_int)      
    return limit , result
