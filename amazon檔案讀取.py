data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 1000 == 0:  #%代表求餘數
			print(len(data))
print(len(data))

#print(data) 印出全部
print(data[0])
pirnt('------------------')
print(data[1])