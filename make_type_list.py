# activity type
act = 'type 1'

# open file
people = open('act_train.csv')
analysis = open(act, 'w')

# read first line
row = people.readline()

# get type x activity
while row != '':
	count = 0
	track = 0
	while row[count] != '\n':
		if row[count] == ',':
			track += 1
		if track == 2:
			start_act = count
		if track == 3:
			stop_act = count
		if track == 11:
			start_char = count
		if track == 12:
			stop_char = count
		count += 1
	act_type = row[start_act + 2:stop_act + 1]
	act_char = row[start_char + 2:stop_char + 1]
	if act_type == act:
		analysis.write(act_char + ',' + row[-2:-1] + '\n')
		print row[0:10]
	row = people.readline()

people.close()
analysis.close()