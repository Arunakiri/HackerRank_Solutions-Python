len_set = int(input())

storage = set(map(int, input().split()))

op_len = int(input())

for i in range(op_len):
    operation, length = input().split()
    if operation == 'intersection_update':
        temp_storage = set(map(int, input().split()))
        storage.intersection_update(temp_storage)
    elif operation == 'update':
        temp_storage = set(map(int, input().split()))
        storage.update(temp_storage)
    elif operation == 'symmetric_difference_update':
        temp_storage = set(map(int, input().split()))
        storage.symmetric_difference_update(temp_storage)
    elif operation == 'difference_update':
        temp_storage = set(map(int, input().split()))
        storage.difference_update(temp_storage)

print(sum(storage))
