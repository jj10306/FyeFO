from piQ.data_init import data_dict, hash_city


def getAvergeWait(source):

    try:
        return round(source.totalWait/source.totalHelped,2)
    except:
        return 0

def get_user_info(gtid):
    try:
        hashed = hash_city(gtid)
        user_dict = data_dict[hashed]
        return user_dict
    except KeyError: #if the person is not on the roster
        return
