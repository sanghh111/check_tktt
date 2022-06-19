from constant.stk import INSERT_TYPE, MIRROR_TYPE, NAME_STK, BUSINESS_TYPE, REPEAT_TYPE,TYPE_FOUR_FOUR_10
from type_stk import *

STRUCT_STK ={
    NAME_STK[0] : {
        "func" : same_number,
        "limit" : 0,
        '8' : {
            'struct' : '{A}'*8,
            'cost' : 30
            },
        '10': {
            'struct' :'{A}'*10,
            'cost' : 20
            },
        '12': {
            'struct': '{A}'*12,
            'cost' : 10
            }
    },
    NAME_STK[1] : {
        "func" : continous,
        BUSINESS_TYPE[0] : None,
        BUSINESS_TYPE[1]: {
            'limit' : None,
            '8' : {
                'struct' :['01234567','12345678','23456789'],
                'cost': 30
                },
            '10': {
                'struct':['123456879'],
                'cost': 20
                }
        }
    },
    NAME_STK[2]: {
        "func" : three_thee,
        BUSINESS_TYPE[0] : {
            '8' :{
                'format': {
                    1: {
                        'struct': "{A}"*3+"{B}"*3+"{number}",
                        'insert_type' : INSERT_TYPE[1],
                    },
                    2 : {
                        'struct':"{number}"+"{A}"*3+"{B}"*3,
                        'insert_type': INSERT_TYPE[0],
                        },
                },
                'limit' :  2,
                'cost' : 8,
                'num_spe' : 2,
                'num_nor':  2,
                },
            '10' :{
                'format':{
                    1: {
                        'struct' :"{A}"*3+"{B}"*3+"{number}",
                        'insert_type': INSERT_TYPE[1]
                        },
                    2 : {
                        'struct' : "{number}"+"{A}"*3+"{B}"*3,
                        'insert_type': INSERT_TYPE[0]
                        },
                    },
                'limit' : 5,
                'cost' : 5,
                'num_spe' : 2,
                'num_nor':  4,
                },
            '12' :{
                'format' :{
                1: {
                    'struct' : "{A}"*3+"{B}"*3+"{number}",
                    'insert_type': None,
                    },
                2 :{
                    'struct': "{number}"+"{A}"*3+"{B}"*3,
                    'insert_type': None
                    }
                },
                'limit' : 7,
                'cost' : 3,
                'num_spe' : 2,
                'num_nor':  6,
                },
        },
        BUSINESS_TYPE[1]: {
            '12' : {
                'format' : {
                    1: {
                        'struct': "{A}"*4+"{B}"*4+"{C}"*4+"{D}"*4,
                        'insert_type': None
                    }
                },
                'limit' : 3,
                'cost' : 8,
                'num_spe' : 4,
                'num_nor': 0
            },
        },
    },
    NAME_STK[3]: {
        "func" : four_four,
        BUSINESS_TYPE[0]:
        { 
            '8' : {
                    'limit': 1,
                    'cost' : 20,
                    'format': {
                        1:  {
                            'struct' :"{A}"*4+"{B}"*4,
                            'insert_type': None
                            },
                        },
                    'num_spe' : 2,
                    'num_nor':  0,
                },
            '10' : {
                    'limit': 2,
                    'cost' : 20,
                    'format': {
                        1: {
                           'struct': "{A}"*4+"{B}"*4+"{number}",
                           'insert_type' : INSERT_TYPE[1]
                           },
                        2: {
                            'struct': "{number}"+"{A}"*4+"{B}"*4,
                            'insert_type' : INSERT_TYPE[0]
                            }
                        },
                    'num_spe' : 2,
                    'num_nor':  2,
                    },
            '12' : {
                    'limit': 1,
                    'cost' : 20,
                    'format': {
                        1: {
                            'struct': "{A}"*4+"{B}"*4+"{number}",
                            'insert_type': INSERT_TYPE[1]
                            },
                        2: {
                            'struct': "{number}"+"{A}"*4+"{B}"*4,
                            'insert_type': INSERT_TYPE[0]
                            }
                    },
                    'num_spe' : 2,
                    'num_nor':  4, 
                },
            },
        BUSINESS_TYPE[1]:{
            '8' : {
                'limit': 1,
                'cost' : 30,
                'format': {
                    1: {
                        'struct' : "{A}"*4+"{B}"*4,
                        'insert_type' : None
                        }
                },
                'num_spe' : 2,
                'num_nor':  0, 
                },
            '10': {
                TYPE_FOUR_FOUR_10[1] : {
                    'format' : {
                        1  : {
                            'struct':"{number}"+"{A}"*4+"{B}"*4,
                            'insert_type' : INSERT_TYPE[0]
                            },
                        1  : {
                            'struct':"{A}"*4+"{B}"*4+"{number}",
                            'insert_type' : INSERT_TYPE[1]
                            }   
                    },
                    'num_spe' : 2,
                    'num_nor':  2,
                    'limit' : 3,
                    'cost': 20,
                },
                TYPE_FOUR_FOUR_10[0] : {
                    'num_spe' : 2,
                    'num_nor':  2,
                    'limit' : 3,
                    'cost': 15,
                    'format' : {
                        1 : {
                            'struct' : "{a}"+"{A}"*4+"{b}"+"{B}"*4,
                            'insert_type' : INSERT_TYPE[3]
                        },
                        2 : {
                            'struct' : "{A}"*4+"{a}"+"{B}"*4+"{b}",
                            'insert_type' : INSERT_TYPE[4]
                        },
                        3 : {
                            'struct' : "{A}"*4+"{a}"+"{b}"+"{B}"*4,
                            'insert_type' : INSERT_TYPE[2]
                        },
                    }
                }
            },
            '12': {
                'num_spe' : 3,
                'num_nor':  0,
                'limit' : 2,
                'cost': 20,
                'format' : {
                    1 : {
                        'struct' : "{A}"*4+"{B}"*4+"{C}"*4,
                        'insert_type' : None
                    }
                }
            }
        },
    },
    NAME_STK[4] : {
        'func' : five_five,
        BUSINESS_TYPE[0]: None,
        BUSINESS_TYPE[1]: {
            '10' : {
            'format':{ 
                1: {
                    'struct' : "{A}"*5+"{B}"*5,
                    'insert_type' : None
                    },
                },
            'num_spe' : 2,
            'num_nor':  0,
            'limit' : 1,
            'cost': 20,
            },
            '12' : {
            'format':{ 
                        1 : {
                            'struct' : "{a}"+"{A}"*5+"{b}"+"{B}"*5,
                            'insert_type' : INSERT_TYPE[3]
                        },
                        2 : {
                            'struct' : "{A}"*5+"{a}"+"{B}"*5+"{b}",
                            'insert_type' : INSERT_TYPE[4]
                        },
                        3 : {
                            'struct' : "{A}"*5+"{a}"+"{b}"+"{B}"*5,
                            'insert_type' : INSERT_TYPE[2]
                        },
                },
                'num_spe' : 2,
                'num_nor':  2,
                'limit' : 2,
                'cost': 15,
            }
        }
    },
    NAME_STK[5]: {
            'func' : six_six,
            BUSINESS_TYPE[0] : None,
            BUSINESS_TYPE[1]: {
                '12' :    {    
                    'num_spe' : 2,
                    'num_nor':  0,
                    'limit' : 1,
                    'cost': 20,
                    'format':  {
                        1 : {
                            'struct' : "{A}"*6+"{B}"*6,
                            'insert_type' : None
                        }
                    }
                }                
            }    
    },
    NAME_STK[6] : {
       'func' : three_four,
       BUSINESS_TYPE[0] : {
            '8' : {
                'num_spe' : 2,
                'num_nor':  1,
                'limit' : 1,
                'cost': 10,
                'format':  {
                    1 : {
                        'struct' : "{number}"+"{A}"*3+"{B}"*4,
                        'insert_type' : INSERT_TYPE[0]
                    },
                    2 : {
                        'struct' : "{number}"+"{A}"*4+"{B}"*3,
                        'insert_type' : INSERT_TYPE[0]
                    },
                    3 : {
                        'struct' : "{A}"*3+"{B}"*4+"{number}",
                        'insert_type' : INSERT_TYPE[1]
                    },
                    4 : {
                        'struct' : "{A}"*4+"{B}"*3+"{number}",
                        'insert_type' : INSERT_TYPE[1]
                    },
                }
            },
            '10' : {
                'num_spe' : 2,
                'num_nor':  3,
                'limit' : 4,
                'cost': 8,
                'format':  {
                    1 : {
                        'struct' : "{number}"+"{A}"*3+"{B}"*4,
                        'insert_type' : INSERT_TYPE[0]
                    },
                    2 : {
                        'struct' : "{number}"+"{A}"*4+"{B}"*3,
                        'insert_type' : INSERT_TYPE[0]
                    },
                    3 : {
                        'struct' : "{A}"*3+"{B}"*4+"{number}",
                        'insert_type' : INSERT_TYPE[1]
                    },
                    4 : {
                        'struct' : "{A}"*4+"{B}"*3+"{number}",
                        'insert_type' : INSERT_TYPE[1]
                    },
                }
            },
            '12' : {
                'num_spe' : 2,
                'num_nor':  5,
                'limit' : 6,
                'cost': 5,
                'format':  {
                    1 : {
                        'struct' : "{number}"+"{A}"*3+"{B}"*4,
                        'insert_type' : INSERT_TYPE[0]
                    },
                    2 : {
                        'struct' : "{number}"+"{A}"*4+"{B}"*3,
                        'insert_type' : INSERT_TYPE[0]
                    },
                    3 : {
                        'struct' : "{A}"*3+"{B}"*4+"{number}",
                        'insert_type' : INSERT_TYPE[1]
                    },
                    4 : {
                        'struct' : "{A}"*4+"{B}"*3+"{number}",
                        'insert_type' : INSERT_TYPE[1]
                    },
                }
            },
        },
        BUSINESS_TYPE[1] : {
            '10' : {
                'num_spe' : 3,
                'num_nor':  0,
                'limit' : 2,
                'cost': 8,
                'format':  {
                    1 : {
                        'struct' : "{A}"*3+"{B}"*3+"{C}"*4,
                        'insert_type' : None
                    },
                    2 : {
                        'struct' : "{A}"*3+"{B}"*4+"{C}"*3,
                        'insert_type' : None
                    },
                    3 : {
                        'struct' : "{A}"*4+"{B}"*3+"{C}"*3,
                        'insert_type' : None
                    },
                }
            },
            '12' : {
                'num_spe' : 3,
                'num_nor': None,
                'limit' : 3,
                'cost': 5,
                'format':  {
                    1 : {
                        'struct' : "{number}"+"{A}"*3+"{B}"*3+"{C}"*4,
                        'insert_type' : INSERT_TYPE[0],
                        'num_nor':  2,

                    },
                    2 : {
                        'struct' : "{number}"+"{A}"*3+"{B}"*4+"{C}"*3,
                        'insert_type' : INSERT_TYPE[0],
                        'num_nor':  2,
                    },
                    3 : {
                        'struct' : "{number}"+"{A}"*4+"{B}"*3+"{C}"*3,
                        'insert_type' : INSERT_TYPE[0],
                        'num_nor':  2,
                    },
                    4 : {
                        'struct' : "{number}"+"{A}"*3+"{B}"*4+"{C}"*4,
                        'insert_type' : INSERT_TYPE[0],
                        'num_nor':  1,
                    },
                    5 : {
                        'struct' : "{number}"+"{A}"*4+"{B}"*3+"{C}"*4,
                        'insert_type' : INSERT_TYPE[0],
                        'num_nor':  1,
                    },
                    6 : {
                        'struct' : "{number}"+"{A}"*4+"{B}"*4+"{C}"*3,
                        'insert_type' : INSERT_TYPE[0],
                        'num_nor':  2,
                    },
                }
            },
        }
    },
    NAME_STK[7]: {
        "func": mirror,
        BUSINESS_TYPE[0]:{
            MIRROR_TYPE[0] : {
                8: {
                    'cost': 15,
                    'format' : {
                        1: {
                            'struct' :  "{A}{B}{B}{A}{A}{B}{B}{A}",
                            'limit' : 2,
                            'num_spe' : 2 ,
                            'num_nor' : 0,
                            'insert_type' : None 
                        },
                        2: {
                            'struct' :  "{A}{B}{B}{A}{C}{D}{D}{C}",
                            'limit'  :  3,
                            'num_spe' : 4 ,
                            'num_nor' : 0,
                            'insert_type' : None 
                        },
                        3: {
                            'struct' :  "{A}{B}{C}{D}{D}{C}{B}{A}",
                            'limit'  :  3 ,
                            'num_spe' : 2 ,
                            'num_nor' : 0,
                            'insert_type' : None 
                        }
                    } 
                },
                10: {
                    'cost': 15,
                    'format' : {
                        1: {
                            'struct' :  "{A}{B}{C}{D}{E}{E}{D}{C}{B}{A}",
                            'limit' : 4,
                            'num_spe' : 5 ,
                            'num_nor' : 0,
                            'insert_type' : None 
                        },
                    } 
                },
                12: {
                    'cost': 8,
                    'format' : {
                        1: {
                            'struct' :  "{A}{B}{B}{A}{C}{D}{D}{C}{E}{F}{F}{E}",
                            'limit' : 5,
                            'num_spe' : 6 ,
                            'num_nor' : 0,
                            'insert_type' : None 
                        },
                        2: {
                            'struct' :  "{A}{B}{C}{D}{E}{F}{F}{E}{D}{C}{B}{A}",
                            'limit' : 5,
                            'num_spe' : 6 ,
                            'num_nor' : 0,
                            'insert_type' : None 
                        },
                        3: {
                            'struct' :  "{A}{B}{B}{A}{A}{B}{B}{A}{A}{B}{B}{A}",
                            'limit' : 1,
                            'num_spe' : 2 ,
                            'num_nor' : 0,
                            'insert_type' : None 
                        },
                    }
                },
            },
            MIRROR_TYPE[1] : {
                8 : {
                    'cost' : 5,
                    'format' : {
                        1: {
                            'struct' : "{A}{B}{B}{A}{number}",
                            'limit' : 5 ,
                            'num_spe' : 2,
                            'num_nor' : 4,
                            'insert_type' : INSERT_TYPE[1]
                        },
                        2: {
                            'struct': "{A}{B}{C}{C}{B}{A}{number}",
                            'limit' : 4,
                            'num_spe' : 3,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                        },
                        3: {
                            'struct': "{number}{A}{B}{C}{C}{B}{A}",
                            'limit' : 4,
                            'num_spe' : 3,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0],
                        },
                        4: {
                            'struct': "{number}{A}{B}{B}{A}",
                            'limit' : 4,
                            'num_spe' : 2,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0],
                        },
                    },   
                },
                10: {
                    'cost' : 3,
                    'format': { 
                        1: {
                            'struct' : "{A}{B}{B}{A}{number}",
                            'limit' : 7 ,
                            'num_spe' : 2,
                            'num_nor' : 6,
                            'insert_type' : INSERT_TYPE[1]
                        },
                        2: {
                            'struct': "{A}{B}{C}{C}{B}{A}{number}",
                            'limit' : 6,
                            'num_spe' : 3,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[1]
                        },
                        3: {
                            'struct' : "{A}{B}{C}{D}{D}{C}{B}{A}{number}",
                            'limit' : 5 ,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type' : INSERT_TYPE[1]
                        },
                        4: {
                            'struct': "{A}{B}{B}{A}{C}{D}{D}{C}{number}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                        },
                        5: {
                            'struct' : "{number}{A}{B}{B}{A}",
                            'limit' : 7 ,
                            'num_spe' : 2,
                            'num_nor' : 6,
                            'insert_type' : INSERT_TYPE[0]
                        },
                        6: {
                            'struct': "{number}{A}{B}{C}{C}{B}{A}",
                            'limit' : 6,
                            'num_spe' : 3,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                        },
                        7: {
                            'struct' : "{number}{A}{B}{C}{D}{D}{C}{B}{A}",
                            'limit' : 5 ,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type' : INSERT_TYPE[0]
                        },
                        8: {
                            'struct': "{number}{A}{B}{B}{A}{C}{D}{D}{C}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                        },
                    },
                },
                12 : {
                    'cost' : 1,
                    'format': { 
                        1: {
                            'struct' : "{A}{B}{C}{C}{B}{A}{number}",
                            'limit' : 8 ,
                            'num_spe' : 3,
                            'num_nor' : 6,
                            'insert_type' : INSERT_TYPE[1]
                        },
                        2: {
                            'struct': "{A}{B}{C}{D}{D}{C}{B}{A}{number}",
                            'limit' : 7,
                            'num_spe' : 4,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[1]
                        },
                        3: {
                            'struct' : "{A}{B}{C}{D}{E}{E}{D}{C}{B}{A}{number}",
                            'limit' : 6 ,
                            'num_spe' : 5,
                            'num_nor' : 2,
                            'insert_type' : INSERT_TYPE[1]
                        },
                        4: {
                            'struct': "{A}{B}{B}{A}{C}{D}{D}{C}{number}",
                            'limit' : 7,
                            'num_spe' : 4,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[1]
                        },
                        5: {
                            'struct' : "{number}{A}{B}{C}{C}{B}{A}",
                            'limit' : 8 ,
                            'num_spe' : 3,
                            'num_nor' : 6,
                            'insert_type' : INSERT_TYPE[0]
                        },
                        6: {
                            'struct': "{number}{A}{B}{C}{D}{D}{C}{B}{A}",
                            'limit' : 7,
                            'num_spe' : 4,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                        },
                        7: {
                            'struct' : "{number}{A}{B}{C}{D}{E}{E}{D}{C}{B}{A}",
                            'limit' : 6 ,
                            'num_spe' : 5,
                            'num_nor' : 2,
                            'insert_type' : INSERT_TYPE[0]
                        },
                        8: {
                            'struct': "{number}{A}{B}{B}{A}{C}{D}{D}{C}",
                            'limit' : 7,
                            'num_spe' : 4,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                        },
                    } 
                }
            },
        },
        BUSINESS_TYPE[1]:{
            MIRROR_TYPE[0] : 
            {8 : {
                'cost' : 10,
                'format' : {
                    1 : {
                        'struct': "{A}{B}{B}{A}{A}{B}{B}{A}",
                        'limit' : 1,
                        'num_spe' : 2,
                        'num_nor' : 0,
                        'insert_type': None
                    },
                    2 : {
                        'struct': "{A}{B}{B}{A}{C}{D}{D}{C}",
                        'limit' : 3,
                        'num_spe' : 4,
                        'num_nor' : 0,
                        'insert_type': None
                    },
                }
            },
            10 : {
                'cost' : 10,
                'format' : {
                    1 : {
                        'struct': "{A}{B}{C}{D}{E}{E}{D}{C}{B}{A}",
                        'limit' : 4,
                        'num_spe' : 5,
                        'num_nor' : 0,
                        'insert_type': None
                    },
                }
            },
            12 : {
                'cost' : 10,
                'format' : {
                    1 : {
                        'struct': "{A}{B}{B}{A}{A}{B}{B}{A}{A}{B}{B}{A}",
                        'limit' : 1,
                        'num_spe' : 2,
                        'num_nor' : 0,
                        'insert_type': None
                    },
                    2: {
                        'struct': "{A}{B}{B}{A}{C}{D}{D}{C}{E}{F}{F}{E}",
                        'limit' : 5,
                        'num_spe': 6,
                        'num_nor': 0,
                        'insert_type': None
                    },
                    3: {
                        'struct': "{A}{B}{C}{D}{E}{F}{F}{E}{D}{C}{B}{A}",
                        'limit' : 5,
                        'num_spe': 6,
                        'num_nor': 0,
                        'insert_type': None
                    }
                }
            }
            },MIRROR_TYPE[1]:None
    }
    },
    NAME_STK[8]: {
        'func' : repeat,
        BUSINESS_TYPE[0]:{
            REPEAT_TYPE[0] : {
                8: {
                    'cost' : 15,
                    'format' : {
                        1 : {
                            'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}",
                            'limit' : 1,
                            'num_spe' : 2,
                            'num_nor' : 0,
                            'insert_type': None
                        },
                        2 : {
                            'struct': "{A}{B}{C}{D}{A}{B}{C}{D}",
                            'limit' : 3,
                            'num_spe' : 4,
                            'num_nor' : 0,
                            'insert_type': None
                        }
                    },
                },
                10: {
                    'cost' : 10,
                    'format' : {
                        1 : {
                            'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}",
                            'limit' : 1,
                            'num_spe' : 2,
                            'num_nor' : 0,
                            'insert_type': None
                        },
                    }
                },
                12: {
                    'cost' : 8,
                    'format' : {
                        1 : {
                            'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}",
                            'limit' : 1,
                            'num_spe' : 2,
                            'num_nor' : 0,
                            'insert_type': None
                        },
                    }
                }
            },
            REPEAT_TYPE[1]:{
                8 : {
                    'cost' : 5,
                    'format' :{
                        1: {
                        'struct':   "{A}{B}{A}{B}{number}",
                        'limit' : 5,
                        'num_spe' : 2,
                        'num_nor' : 4,
                        'insert_type': INSERT_TYPE[1]
                        },
                        2: {
                        'struct':   "{A}{B}{A}{B}{A}{B}{number}",
                        'limit' : 3,
                        'num_spe' : 2,
                        'num_nor' : 2,
                        'insert_type': INSERT_TYPE[1]
                        },
                        3: {
                        'struct':   "{number}{A}{B}{A}{B}",
                        'limit' : 5,
                        'num_spe' : 2,
                        'num_nor' : 4,
                        'insert_type': INSERT_TYPE[0]
                        },
                        4: {
                        'struct':   "{number}{A}{B}{A}{B}{A}{B}",
                        'limit' : 3,
                        'num_spe' : 2,
                        'num_nor' : 2,
                        'insert_type': INSERT_TYPE[0]
                        },
                        5: {
                        'struct':   "{A}{B}{C}{A}{B}{C}{number}",
                        'limit' : 5,
                        'num_spe' : 2,
                        'num_nor' : 4,
                        'insert_type': INSERT_TYPE[1]
                        },
                        6: {
                        'struct':   "{number}{A}{B}{C}{A}{B}{C}",
                        'limit' : 3,
                        'num_spe' : 2,
                        'num_nor' : 2,
                        'insert_type': INSERT_TYPE[1]
                        },
                    }
                },
                10 :{
                    'cost' : 3,
                    'format' :{
                        1: {
                            'struct':   "{A}{B}{A}{B}{number}",
                            'limit' : 7,
                            'num_spe' : 2,
                            'num_nor' : 6,
                            'insert_type': INSERT_TYPE[1]
                            },
                        2: {
                            'struct':   "{A}{B}{A}{B}{A}{B}{number}",
                            'limit' : 5,
                            'num_spe' : 2,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[1]
                            },
                        3: {
                        'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}{number}",
                            'limit' : 3,
                            'num_spe' : 2,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                            },
                        4: {
                            'struct':   "{A}{B}{A}{B}{C}{D}{C}{D}{number}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                            },
                        5: {
                            'struct':   "{number}{A}{B}{A}{B}",
                            'limit' : 7,
                            'num_spe' : 2,
                            'num_nor' : 6,
                            'insert_type': INSERT_TYPE[0]
                            },
                        6: {
                            'struct':   "{number}{A}{B}{A}{B}{A}{B}",
                            'limit' : 5,
                            'num_spe' : 2,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                            },
                        7: {
                            'struct':   "{number}{A}{B}{A}{B}{A}{B}{A}{B}",
                            'limit' : 3,
                            'num_spe' : 2,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                            },
                        8: {
                            'struct':   "{number}{A}{B}{A}{B}{C}{D}{C}{D}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                            },
                        9: {
                            'struct':   "{number}{A}{B}{C}{A}{B}{C}",
                            'limit' : 6,
                            'num_spe' : 3,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                            },
                        10: {
                            'struct':   "{number}{A}{B}{A}{B}{C}{D}{C}{D}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                            },
                        11: {
                            'struct':   "{number}{A}{B}{C}{D}{A}{B}{C}{D}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                            },
                        12: {
                            'struct':   "{A}{B}{C}{D}{A}{B}{C}{D}{number}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                            },
                        }
                    },
                12 :{
                    'cost' : 3,
                    'format' :{
                        1: {
                            'struct':   "{A}{B}{A}{B}{C}{D}{C}{D}{number}",
                            'limit' : 7,
                            'num_spe' : 4,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[1]
                            },
                        2: {
                            'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}{number}",
                            'limit' : 5,
                            'num_spe' : 2,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[1]
                            },
                        3: {
                            'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{number}",
                            'limit' : 3,
                            'num_spe' : 2,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                            },
                        4: {
                            'struct':   "{A}{B}{A}{B}{A}{B}{C}{D}{C}{D}{number}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                            },
                        5: {
                            'struct':   "{A}{B}{A}{B}{C}{D}{C}{D}{C}{D}{number}",
                            'limit' : 2,
                            'num_spe' : 2,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[1]
                            },
                        6: {
                            'struct':   "{number}{A}{B}{A}{B}{C}{D}{C}{D}",
                            'limit' : 5,
                            'num_spe' : 2,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                            },
                        7: {
                            'struct':   "{number}{A}{B}{A}{B}{A}{B}{A}{B}",
                            'limit' : 5,
                            'num_spe' : 2,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                            },
                        8: {
                            'struct':   "{number}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}",
                            'limit' : 2,
                            'num_spe' : 2,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                            },
                        9: {
                            'struct':   "{number}{A}{B}{A}{B}{A}{B}{C}{D}{C}{D}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                            },
                        10: {
                            'struct':   "{number}{A}{B}{A}{B}{C}{D}{C}{D}{C}{D}",
                            'limit' : 5,
                            'num_spe' : 4,
                            'num_nor' : 2,
                            'insert_type': INSERT_TYPE[0]
                            },
                        11: {
                            'struct':   "{number}{A}{B}{C}{D}{A}{B}{C}{D}",
                            'limit' : 7,
                            'num_spe' : 4,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[0]
                            },
                        12: {
                            'struct':   "{A}{B}{C}{D}{A}{B}{C}{D}{number}",
                            'limit' : 7,
                            'num_spe' : 4,
                            'num_nor' : 4,
                            'insert_type': INSERT_TYPE[1]
                            },
                        }
                    },
                }
        },
        BUSINESS_TYPE[1] : {
            8 : {
                    'cost' : 10,
                    'format' : {
                    1:{ 
                        'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}",
                        'limit' : 1,
                        'num_spe' : 2,
                        'num_nor' : 0,
                        'insert_type': None
                        },
                    2:{ 
                        'struct':   "{A}{B}{C}{D}{A}{B}{C}{D}",
                        'limit' : 3,
                        'num_spe' : 4,
                        'num_nor' : 0,
                        'insert_type': None
                        }
                    } 
            },
            10 : {
                'cost' : 10,
                    'format' : {
                    1:{ 
                        'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}",
                        'limit' : 1,
                        'num_spe' : 2,
                        'num_nor' : 0,
                        'insert_type': None
                        },
                    2:{ 
                        'struct':   "{A}{B}{C}{D}{E}{A}{B}{C}{D}{E}",
                        'limit' : 3,
                        'num_spe' : 5,
                        'num_nor' : 0,
                        'insert_type': None
                        }
                    } 
            },
            12 :{
                    'cost' : 10,
                    'format' : {
                    1:{ 
                        'struct':   "{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}{A}{B}",
                        'limit' : 1,
                        'num_spe' : 2,
                        'num_nor' : 0,
                        'insert_type': None
                        },
                    2:{ 
                        'struct':   "{A}{B}{C}{D}{E}{F}{A}{B}{C}{D}{E}{F}",
                        'limit' : 3,
                        'num_spe' : 4,
                        'num_nor' : 0,
                        'insert_type': None
                        }
                    } 
            }
        },
    },
    NAME_STK[9]: {
        'func' : loc_phat,
        BUSINESS_TYPE[0]:{
            8 : {
                'cost' : 0.5,
                'limit' : None,
                'struct': "{number}6868",
                'num_spe' : 0,
                'num_nor' : 4,
                'insert_type' : None
            },
            10 : {
                'cost' : 0.5,
                'limit' : None,
                'struct': "{number}6868",
                'num_spe' : 0,
                'num_nor' : 6,
                'insert_type': None
            },
            12 : {
                'cost' : 0.5,
                'limit' : None,
                'struct': "{number}6868",
                'num_spe' : 0,
                'num_nor' : 8,
                'insert_type': None
            },
        },
        BUSINESS_TYPE[1]: None,
    },
    NAME_STK[10]: {
        'func': end_spe,
        BUSINESS_TYPE[1] : None,
        BUSINESS_TYPE[0]: {
            8 : {
                'cost' : 0.1,
                'limit' : 20,
                'struct': "{number}{A}{B}{C}{D}",
                'num_spe' : 4,
                'num_nor' : 4,
                'insert_type' : INSERT_TYPE[5]
            },
            10 : {
                'cost' : 0.1,
                'limit' : 20,
                'struct': "{number}{A}{B}{C}{D}",
                'num_spe' : 4,
                'num_nor' : 6,
                'insert_type': INSERT_TYPE[5]
            },
            12 : {
                'cost' : 0.1,
                'limit' : 20,
                'struct': "{number}{A}{B}{C}{D}",
                'num_spe' : 4,
                'num_nor' : 8,
                'insert_type': INSERT_TYPE[5]
            },
        }
    },
    NAME_STK[11]: {
        'func': end_same_number,
        BUSINESS_TYPE[0] : None,
        BUSINESS_TYPE[1]: {
            8 : {
                'cost' : 8,
                'format' : {
                    1: {
                        'struct': "{number}"+"{A}"*7,
                        'limit' : 1,
                        'num_spe' : 1,
                        'num_nor' : 1,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    2: {
                        'struct': "{number}"+"{A}"*6,
                        'limit' : 2,
                        'num_spe' : 1,
                        'num_nor' : 2,
                        'insert_type' : INSERT_TYPE[0]
                        },
                }
            },
            10 : {
                'cost' : 8,
                'format' : {
                    1: {
                        'struct': "{number}"+"{A}"*9,
                        'limit' : 1,
                        'num_spe' : 1,
                        'num_nor' : 1,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    2: {
                        'struct': "{number}"+"{A}"*8,
                        'limit' : 2,
                        'num_spe' : 1,
                        'num_nor' : 2,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    3: {
                        'struct': "{number}"+"{A}"*7,
                        'limit' : 3,
                        'num_spe' : 1,
                        'num_nor' : 3,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    4: {
                        'struct': "{number}"+"{A}"*6,
                        'limit' : 4,
                        'num_spe' : 1,
                        'num_nor' : 4,
                        'insert_type' : INSERT_TYPE[0]
                        },
                }
            },
            12 : {
                'cost' : 8,
                'format' : {
                    1: {
                        'struct': "{number}"+"{A}"*1,
                        'limit' : 1,
                        'num_spe' : 1,
                        'num_nor' : 1,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    2: {
                        'struct': "{number}"+"{A}"*1,
                        'limit' : 2,
                        'num_spe' : 1,
                        'num_nor' : 2,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    3: {
                        'struct': "{number}"+"{A}"*9,
                        'limit' : 3,
                        'num_spe' : 1,
                        'num_nor' : 3,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    4: {
                        'struct': "{number}"+"{A}"*8,
                        'limit' : 4,
                        'num_spe' : 1,
                        'num_nor' : 4,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    5: {
                        'struct': "{number}"+"{A}"*7,
                        'limit' : 5,
                        'num_spe' : 1,
                        'num_nor' : 5,
                        'insert_type' : INSERT_TYPE[0]
                        },
                    6: {
                        'struct': "{number}"+"{A}"*6,
                        'limit' : 6,
                        'num_spe' : 1,
                        'num_nor' : 6,
                        'insert_type' : INSERT_TYPE[0]
                        },
                }
            },
        }
    },
    NAME_STK[12]: {
        BUSINESS_TYPE[0] : None,
        BUSINESS_TYPE[1]: {
            8 : {
                'cost' : 8,
                'limit' : None,
                'struct': "{number}{A}{B}{C}",
                'num_spe' : 3,
                'num_nor' : 2,
                'insert_type' : INSERT_TYPE[5]
            },
            10 : {
                'cost' : 8,
                'limit' : None,
                'struct': "{number}{A}{B}{C}",
                'num_spe' : 3,
                'num_nor' : 4,
                'insert_type': INSERT_TYPE[5]
            },
            12 : {
                'cost' : 8,
                'limit' : None,
                'struct': "{number}{A}{B}{C}",
                'num_spe' : 3,
                'num_nor' : 6,
                'insert_type': INSERT_TYPE[5]
            },
        }
    },
}
