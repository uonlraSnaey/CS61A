def partition_number(n, m, temp=[]):

    if n == 0:
        if temp:
            yield temp
    else:
        for i in range(min(m, n), 0, -1):
            yield from partition_number(n - i, i, temp + [i])

n = 10
m = 2

all_partitions = list(partition_number(n, m))
print(f"数字 {n} 在最大数限制为 {m} 下的所有分区结果为：{all_partitions}")
