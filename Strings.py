ex = "abcdefghijjklmnopqrstuvwxyz"

ex1 = ex[0]
ex2 = ex[-1]
ex3 = ex[0:5]
ex4 = ex.upper()
ex5 = ex.lower()
ex6 = ex.count("r")
ex7 = ex.find("k")
ex8 = ex.replace("j","i")
ex9 = ex.islower()
exa = ex.isupper()
exb = ex.isalnum()
exc = ex.isalpha()
exd = ex.isdigit()
exe = ex.index("d")
exf = ex.strip("x")

ll = []
l = ["hi","how","are","you","?"]
l[0] = "hello"
l1 = l[1]
l2 = l[-1]
l3 = l[0:3]
l4 = l[2:]
del l[4]
l5 = l.append("?")
l6 = l.extend(l)
l7 = l.insert(5,"but")
l8 = l.remove("?")
l9 = l.pop(6)
la = ll.clear()
lb = l.index("are")
lc = l.count("hello")
ld = l.sort()
le = sorted(l)
lf = l.reverse()
lg = l.copy