# mean
file = open("mean-median-mode-frequency.csv", "r")
t = file.read(129)

file.close

t1 = t.split(",")
'''
t1 = t.split(" ")
t1 = t.split("\n")
t1 = t.split("'")
'''
print(t1)
#print(t1)

x = len(t1)

x1 = x
for o in range(0, x):
    t1[o] = int(t1[o])


i = 0
sum1 = 0
while x > 0:
    sum1 = t1[i] + sum1
    x = x-1
    i = i+1

ans = sum1 / x1

print(ans)
'''

file = open("mean-median-mode-frequency.csv", "w")
file = del(129)
file.close
#median
file = open("mean-median-mode-frequency.csv", "r")
t = file.read(129)
print(t)
file.close
'''