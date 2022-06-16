from constant.struct_stk import STRUCT_STK
import json

def create_stk(account_type=None,size=None,is_vip=False,business_type=True,option=None):
    
    #LOAD DATA
    stk_type = STRUCT_STK[account_type]
    func = stk_type['func']
    try:
        stk_type = stk_type[business_type] 
    except:
        pass
    return func(stk_type,size,is_vip,business_type,option)

