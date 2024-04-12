result = int(input())
result_max = 0
while result != -1:
    if result > result_max:
        result_max = result
    result = int(input())
print(result_max)
    