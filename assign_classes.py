# open file
# debug = open('debug', 'w')
question = open('act_test.csv')
labels = open('solution.csv', 'w')
labels.write('activity_id,outcome\n')

# read first line
row = question.readline()

while row != '':
	flag = 0
	count = 0
	track = 0
	while row[count] != '\n':
		if row[count] == ',':
			track += 1
		if track == 0:
			start_id = count
		if track == 1:
			stop_id = count
		if track == 2:
			starter = count
		if track == 3:
			index_0 = count
		if track == 4:
			index_1 = count
		if track == 5:
			index_2 = count
		if track == 6:
			index_3 = count
		if track == 7:
			index_4 = count
		if track == 8:
			index_5 = count
		if track == 9:
			index_6 = count
		if track == 10:
			index_7 = count
		if track == 11:
			index_8 = count
		if track == 12:
			index_9 = count
		if track == 13:
			index_A = count
		count += 1
	act_id = row[start_id + 2:stop_id + 1]
	a_type = row[starter + 2:index_0 + 1]
	char_1 = row[index_0 + 2:index_1 + 1]
	char_2 = row[index_1 + 2:index_2 + 1]
	char_3 = row[index_2 + 2:index_3 + 1]
	char_4 = row[index_3 + 2:index_4 + 1]
	char_5 = row[index_4 + 2:index_5 + 1]
	char_6 = row[index_5 + 2:index_6 + 1]
	char_7 = row[index_6 + 2:index_7 + 1]
	char_8 = row[index_7 + 2:index_8 + 1]
	char_9 = row[index_8 + 2:index_9 + 1]
	char_A = row[index_9 + 2:index_A + 1]
	# debug.write(a_type + '\n')
	if a_type != 'type 1':
		retrieve = open(a_type + '.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_A:
				print act_id + ',' + line[-2:-1]
				labels.write(act_id + ',' + line[-2:-1] + '\n')
				flag = 1
				break
			line = retrieve.readline()
		retrieve.close()
		if flag == 0:
			labels.write(act_id + ',0\n')
	else:
		print act_id.strip()
		est = 0
		# find char_1
		retrieve = open(a_type + ' char 1.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_1:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_2
		retrieve = open(a_type + ' char 2.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_2:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_3
		retrieve = open(a_type + ' char 3.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_3:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_4
		retrieve = open(a_type + ' char 4.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_4:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_5
		retrieve = open(a_type + ' char 5.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_5:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_6
		retrieve = open(a_type + ' char 6.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_6:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_7
		retrieve = open(a_type + ' char 7.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_7:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_8
		retrieve = open(a_type + ' char 8.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_8:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		# find char_9
		retrieve = open(a_type + ' char 9.txt')
		line = retrieve.readline()
		while line != '':
			count = 0
			track = 0
			while line[count] != '\n':
				if line[count] == ',':
					track += 1
				if track == 0:
					end = count
				count += 1
			char = line[0:end + 1]
			if char == char_9:
				print ',' + line[-2:-1]
				est += int(line[-2:-1])
				break
			line = retrieve.readline()
		retrieve.close()
		labels.write(act_id + ',')
		p = float(est) / 9
		if p > 0.5:
			labels.write('1')
		else:
			labels.write('0')
		labels.write('\n')
	row = question.readline()

# debug.close()
question.close()
labels.close()