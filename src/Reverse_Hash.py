import hashlib
import itertools

def crack_3_upper_case(og_hash):
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
                    return combo
                #print(combo)




test_hash = 'AAA'
b = bytes(test_hash, 'utf-8')
result = hashlib.md5(test_hash.encode())
bytes_result = hashlib.md5(b)
crack_3_upper_case( "b05815e0fb5626ccb478b49a4e85d3a8" )