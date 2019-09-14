import json
import math
from datetime import datetime
import locale

today_ = datetime.today()
today_str_ = str(today_.day) + '/' + str(today_.month) + '/' + str(today_.year)

def today_str():
    '''Returns today's date in string format'''
    return today_str_

def date_format(date_str_):
    format_list_ = ["%d/%m/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y-%m-%d", "%d%m%Y", "%Y%m%d"]
    locale.

    # for x in format_list_:
    #     try:
    #         out = x if datetime.strptime(date_str_, format_list_[x]) else False
    #     except:
    #         return x
        
    #     return out

date_format("01/01/2019")

# def format(x):
#     try:
#         datetime.strptime(date_str_, format_list_[x])
#         fmt = format_list_[x]
#     except:
#         format(x = x + 1)
#         fmt = False
#     return fmt if fmt else 0



def calc_age(birth_date_):
    return 1

def parse_date(date_str_, format_ = "%d/%m/%Y"):
    return datetime.strptime(date_str_, format_)


def eval_include(include_, value_, list_=list):
    '''Returns True if value is included or excluded from a list'''
    if include_ is not None and value_ is not None and list_ is not None:
        if include_=='S' and value_ in list_:
            return True
        elif include_=='N' and value_ not in list_:
            return True
    else:
        return False

def eval_date(value_, list_=[]):
    if value_ is not None and list_ is not None:
        return True if value_ in list_ else False
        


def json_out(result_, out_file_="results.json"):
    json.dump(result_, open(out_file_, "w"), indent=4)