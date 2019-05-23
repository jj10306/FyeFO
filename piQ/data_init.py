from os import path
import hashlib
#hashing info from:
# https://pythonprogramming.net/password-hashing-flask-tutorial/

data_dict = dict()

def data_scrape():

    #gets absolute path of current directory: /Users/Jakob/Desktop/pi_queue/FyeFO/piQ
    basepath = path.dirname(__file__)
    #steps back two levels and into /data directory where file is located
    filepath = path.abspath(path.join(basepath, "../../data", "summer_2019_hashed_data.csv"))
    roster = open(filepath, "r")

    # roster = open("clean_data.csv")
    roster.readline()
    student_lines = roster.readlines()

    for line in student_lines:
        line = line.strip()
<<<<<<< HEAD
        last, first, gtid, role = line.split(",")

        last = last.strip('"').strip()
        first = first.strip('"').strip()
        # gtid is now hashed
        # gtid = hash_city(gtid) //uncomment this line if csv data's gtid's are not hashed yet
        data_dict[gtid] = {"name": first + " " + last, "role": role}
=======
        name, gitid, role = line.split(",")
        hashed_gtid = hash_city(gitid)
        # gtid is now hashed
        data_dict[hashed_gtid] = {"name": name, "role": role}
>>>>>>> 361a29bda4ead8a853eb85c8dcd5bd75e1cb3467

"""
Produces a hash of the gtids
params - gtid (9 digit str gtid)
return - hex string of the hash
"""
def hash_city(gtid):
    # hash constructor takes in a series of bytes as a param, so use str.encode()
    hash_obj = hashlib.sha512(gtid.encode())
    # hash is a hex string of the hash
    hash = hash_obj.hexdigest()
    return hash


data_scrape()
