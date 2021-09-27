import random
distr=[[],[],[]]
name=['A','B','C','D','E','F','G','H']
for n in name:
    num = random.randint(0, 2)
    distr[num].append(n)
print(distr)