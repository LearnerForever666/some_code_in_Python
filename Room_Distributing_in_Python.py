# It is a code which may helps you to distribute your room when you are in puzzle.
# And as you see,it is my FIRST code in Python which is uploaded to the Github.
'''
author: LearnerForever
Date: 2021 Sep 27th
'''
import random
distr=[[],[],[]]
name=['A','B','C','D','E','F','G','H']
for n in name:
    num = random.randint(0, 2)
    distr[num].append(n)
print(distr)
