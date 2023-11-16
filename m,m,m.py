file = open("mean-median-mode-frequency.csv", "r")
f = file.read()
file.close

t = f[0:129]
g = f[131:271]
h = f[273:451]

# mean
t1 = t.split(",")
x = len(t1)
x1 = x

for a in range(0, x):
    t1[a] = int(t1[a])
i = 0
sum1 = 0

while x > 0:
    sum1 = t1[i] + sum1
    x = x-1
    i = i+1

mean = sum1 / x1
print("Mean is ", mean)

#median
g1 = g.split(",")
g1 = sorted(g1)
v = len(g1)
d = v//2
median = 0

if (v % 2) != 0:
    median = g1[d]
elif (v % 2) == 0:
    median = (d + (d+1)) / 2
    
print("Median is " , median)

#mode
h1 = h.split(",")
q = len(h1)
p = 0
y = 0

while p <= q:
    if y != h1[y]:
        print(y)
        y = y + 1
    p = p + 1    