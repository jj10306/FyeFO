from piQ.data_init import data_dict, hash_city
from pprint import pprint

def get_user_info(gtid):
    try:
        hashed = hash_city(gtid)
        user_dict = data_dict[hashed]
        return user_dict
    except KeyError: #if the person is not on the roster
        return
