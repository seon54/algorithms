import hashlib

hash_table = [None for i in range(16)]

def get_key(data):
    hash_obj = hashlib.sha256()
    hash_obj.update(data.encode())
    return int(hash_obj.hexdigest(), 16)

def hash_func(key):
    return key % len(hash_table)

def save_data_chaining(data, value):
    index_key = get_key(data)
    address = hash_func(index_key)
    if hash_table[address]:
        for d in hash_table[address]:
            if d[0] == index_key:
                d[1] = value
                return
        hash_table[address].append([index_key, value])
    else:
        hash_table[address] = [[index_key, value]]

def read_data_chaninig(data):
    index_key = get_key(data)
    address = hash_func(index_key)
    if hash_table[address]:
        for d in hash_table[address]:
            if d[0] == index_key:
                return d[1]
    return None

def save_data_linear(data, value):
    index_key = get_key(data)
    address = hash_func(index_key)
    if hash_table[address]:
        for i in range(address, len(hash_table)):
            if not hash_table[i]:
                hash_table[i] = [index_key, value]
                return
            if hash_table[i][0] == index_key:
                hash_table[i][1] = value
                return
    else:
        hash_table[address] = [index_key, value]

save_data_chaining('abc', 1000)
save_data_chaining('ccc', 25400)

