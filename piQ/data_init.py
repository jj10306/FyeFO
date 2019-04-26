import os
import hashlib
# https://pythonprogramming.net/password-hashing-flask-tutorial/

# dictionary containing {gtid: name pairs} that will be passed across modules
data_dict = dict()

def data_scrape():
    # gets the path to clean_data.csv, agnostic to directory
    # structure as long as __file__ and clean_data.csv are in sibling directories
    # fileDir = os.path.dirname(os.path.realpath('__file__'))
    # filename = os.path.join(fileDir, '../data/clean_data.csv')
    # filename = os.path.abspath(os.path.realpath(filename))

    roster = open("clean_data.csv")
    roster.readline()
    student_lines = roster.readlines()

    for line in student_lines:
        line = line.strip()
        name, gtid, role = line.split(",")
        # gtid is now hashed
        gtid = hash_city(gtid)
        data_dict[gtid] = {"name": name, "role": role}

"""
Produces a hash of the gtid
params - gtid (9 digit str gtid)
return - hex string of the hash
"""
def hash_city(gtid):
    # hash constructor takes in a series of bytes as a param, so use str.encode()
    hash_obj = hashlib.sha3_512(gtid.encode())
    # hash is a hex string of the hash
    hash = hash_obj.hexdigest()
    return hash


data_scrape()
