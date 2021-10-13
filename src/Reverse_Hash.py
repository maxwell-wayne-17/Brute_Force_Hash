import hashlib
from datetime import datetime
import time

# **** ADD TIME TRACKER ****
def crack_3_upper_case(og_hash):
    start = datetime.now()
    string = 'AAA'
    b = bytes(string, 'utf-8')

    if og_hash == hashlib.md5(b).hexdigest():
        print(b)
        return b

    # Go through length 3
    for x in range(b[0], b[0] + 26):
        for y in range(b[1], b[1] + 26):
            for z in range(b[2], b[2] + 26):
                combo = chr(x) + chr(y) + chr(z)
                combo_hash = hashlib.md5(combo.encode())
                if (combo_hash.hexdigest() == og_hash):
                    print ("found + ", combo)
                    end = (datetime.now() - start)
                    print("Time taken: ", end)
                    return combo
                #print(combo)

    end = (datetime.now() - start)
    print("Time taken: ", end)

def crack_5_lower_case(og_hash):
    start = datetime.now()
    string = 'aaaaa'
    by = bytes(string, 'utf-8')

    if og_hash == hashlib.md5(by).hexdigest():
        print(by)
        return by

    # Go through length 3
    for a in range(by[0], by[0] + 26):
        for b in range(by[1], by[1] + 26):
            for c in range(by[2], by[2] + 26):
                for d in range(by[3], by[3] + 26):
                    for e in range(by[4], by[4] + 26):
                        combo = chr(a) + chr(b) + chr(c) + chr(d) + chr(e)
                        combo_hash = hashlib.md5(combo.encode())
                        if (combo_hash.hexdigest() == og_hash):
                            print ("found + ", combo)
                            end = (datetime.now() - start)
                            print("Time taken: ", end)
                            return combo
                #print(combo)

    end = (datetime.now() - start)
    print("Time taken: ", end)


test_hash = 'dkenw'
b = bytes(test_hash, 'utf-8')
result = hashlib.md5(test_hash.encode())
bytes_result = hashlib.md5(b)
crack_5_lower_case( "cb535d2f3539f897db558c0c0d3e661c" )
