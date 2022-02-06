num_list = [int(each) for each in input().split()]
num_wise_count = dict()
for i in range(1, 10):
    num_wise_count[i] = 0

for num in num_list:
    for i in range(1, 10):
        if num % i == 0:
            num_wise_count[i] += 1
print(num_wise_count)
