


box = ['1', '3', '5', '7', '100000']
ans = max(int(box))

print(ans)








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