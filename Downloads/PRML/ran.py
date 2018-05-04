import random


def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)




w=open('train.csv','w')
for g in range(40):
	w.write(random_line('act_train.csv')+'\n')
