from collections import Counter

n = int(input())
rooms = list(map(int, input().split()))

room_dict = Counter(rooms)

for key, val in room_dict.items():
    if room_dict[key] == 1:
        print(key)
