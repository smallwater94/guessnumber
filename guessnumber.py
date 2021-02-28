import random

r = random.randint(1, 10)
y = 0
while True:
	y = y + 1
	gus = input('請猜數字: ')
	gus = int(gus)
	if gus == r :
		break
	else:
		if gus > r :
			print('太大了')
		elif gus < r :
			print('太小了')

print('猜對了! 遊戲結束')
print('你總共猜了',y,'次')
