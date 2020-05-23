data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count = count + 1
		if count % 10000 == 0:  #%代表求餘數
			print(len(data))
print('檔案讀取玩了，總共有', len(data), '筆資料')

#print(data) 印出全部
#print(data[0])
#pirnt('------------------')
#print(data[1])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為', sum_len/len(data))


# 清單做篩選


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言有good')
print(good[0])


new_good = [d for d in data if 'good' in d]  #上面的快寫法

print('一共有', len(new_good), '筆留言有good')
print(new_good[0])




