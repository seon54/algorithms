# 동전 문제

def coin(price: int):
    coin_list = [500, 100, 50, 1]
    coin_list.sort(reverse=True)
    cnt = 0

    for coin in coin_list:
        cnt += (price // coin)
        price %= coin

    return cnt

print(coin(4720))


# 부분 배낭 문제

def fractional_knapsack(data_list, capacity):    
    data_list=sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    print(f'data list = {data_list}')
    total_value = 0
    details = dict()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details[data[0]] = data[1]
        else:
            fraction = capacity / data[0]
            capacity -= fraction * data[0]
            total_value += data[1] * fraction
            details[fraction * data[0]] = data[1] * fraction

    print(details)

    return total_value

# (무게, 가치)
data_list = [(20, 1), (15, 6), (15, 12), (20, 10), (25, 8), (30, 5)]

print(fractional_knapsack(data_list, 40))