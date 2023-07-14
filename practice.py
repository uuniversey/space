
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

data = [5, 2, 4, 6, 1, 3]
insertion_sort(data)
print(data)  # 출력: [1, 2, 3, 4, 5, 6]



















# cases = int(input())

# box = [input()]
# data = box[0].split(' ')
# clear = sorted(data)

# for a in range(cases-1):
#     if (len(clear)) % 2 == 1:
#         clear.pop(0)
#     else:
#         clear.pop()

# print(clear)






'''
cases = int(input())

ans=[]
for case in range(cases):
    data = input()
    box = 0

    for num in data.split(" "):
        box = max(box, int(num))

    ans.append(box)
        

for idx, val in enumerate(ans):
    print("#{} {}".format(idx+1, val))
'''