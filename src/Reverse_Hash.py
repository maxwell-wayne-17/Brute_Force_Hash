import hashlib
from datetime import datetime
import time


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


def crack_9_11_lower_upper_case(og_hash):
    start = datetime.now()

    # Check length 9
    string9 = 'aaaaaaaaa'
    by9 = bytes(string9, 'utf-8')
    if og_hash == hashlib.md5(by9).hexdigest():
        print(by9)
        return by9

    for a in range(by9[0], by9[0] + 52):
        for b in range(by9[1], by9[1] + 52):
            for c in range(by9[2], by9[2] + 52):
                for d in range(by9[3], by9[3] + 52):
                    for e in range(by9[4], by9[4] + 52):
                        for f in range(by9[5], by9[5] + 52):
                            for g in range(by9[6], by9[6] + 52):
                                for h in range(by9[7], by9[7] + 52):
                                    for i in range(by9[8], by9[8] + 52):
                                        combo = chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f) + chr(g) + chr(h) + chr(i)
                                        combo_hash = hashlib.md5(combo.encode())
                                        if (combo_hash.hexdigest() == og_hash):
                                            print ("found + ", combo)
                                            end = (datetime.now() - start)
                                            print("Time taken: ", end)
                                            return combo

    # Check length 10
    string10 = 'aaaaaaaaaa'
    by10 = bytes(string10, 'utf-8')
    if og_hash == hashlib.md5(by10).hexdigest():
        print(by10)
        return by10

    for a in range(by10[0], by10[0] + 52):
        for b in range(by10[1], by10[1] + 52):
            for c in range(by10[2], by10[2] + 52):
                for d in range(by10[3], by10[3] + 52):
                    for e in range(by10[4], by10[4] + 52):
                        for f in range(by10[5], by10[5] + 52):
                            for g in range(by10[6], by10[6] + 52):
                                for h in range(by10[7], by10[7] + 52):
                                    for i in range(by10[8], by10[8] + 52):
                                        for j in range(by10[9], by10[9] + 52):
                                            combo = chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f) + chr(g) + chr(
                                                h) + chr(i) + chr(j)
                                            combo_hash = hashlib.md5(combo.encode())
                                            if (combo_hash.hexdigest() == og_hash):
                                                print("found + ", combo)
                                                end = (datetime.now() - start)
                                                print("Time taken: ", end)
                                                return combo

    # Check length 11
    string11 = 'aaaaaaaaaaa'
    by11 = bytes(string11, 'utf-8')
    if og_hash == hashlib.md5(by11).hexdigest():
        print(by11)
        return by11

    for a in range(by11[0], by11[0] + 52):
        for b in range(by11[1], by11[1] + 52):
            for c in range(by11[2], by11[2] + 52):
                for d in range(by11[3], by11[3] + 52):
                    for e in range(by11[4], by11[4] + 52):
                        for f in range(by11[5], by11[5] + 52):
                            for g in range(by11[6], by11[6] + 52):
                                for h in range(by11[7], by11[7] + 52):
                                    for i in range(by11[8], by11[8] + 52):
                                        for j in range(by11[9], by11[9] + 52):
                                            for k in range(by11[10], by11[10] + 52):
                                                combo = chr(a) + chr(b) + chr(c) + chr(d) + chr(e) + chr(f) + chr(g) + \
                                                        chr(h) + chr(i) + chr(j)
                                                combo_hash = hashlib.md5(combo.encode())
                                                if (combo_hash.hexdigest() == og_hash):
                                                    print("found + ", combo)
                                                    end = (datetime.now() - start)
                                                    print("Time taken: ", end)
                                                    return combo


    end = (datetime.now() - start)
    print("Time taken: ", end)


test_hash = 'dkenw'
b = bytes(test_hash, 'utf-8')
result = hashlib.md5(test_hash.encode())
bytes_result = hashlib.md5(b)
crack_5_lower_case("cb535d2f3539f897db558c0c0d3e661c")

