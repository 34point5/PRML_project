import os

# activity type
act = 'type 1'

# open file
analysis = open(act)
result = open(act + ' char 9.txt', 'a')
new_analysis = open('temp', 'w')

# read first line
row = analysis.readline()
count = 0
track = 0
while row[count] != '\n':
	if row[count] == ',':
		track += 1
	if track == 0:
		stop = count
	count += 1
act_char = row[0:stop + 1]
trial = 1
success = int(row[-2:-1])

row = analysis.readline()

# study type x activity
while row != '':
	count = 0
	track = 0
	while row[count] != '\n':
		if row[count] == ',':
			track += 1
		if track == 0:
			stop = count
		count += 1
	act_char_new = row[0:stop + 1]
	if act_char_new == act_char:
		success += int(row[-2:-1])
		trial += 1
	else:
		new_analysis.write(row)
	row = analysis.readline()

p = float(success) / trial
if p > 0.5:
	result.write(act_char + ',' + str(1) + '\n')
else:
	result.write(act_char + ',' + str(0) + '\n')

print 1

os.remove(act)
os.rename('temp', act)

analysis.close()
result.close()
new_analysis.close()