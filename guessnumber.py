import random

s = input('你最小要猜多少? ')
e = input('你最大要猜多少? ')
s = int(s)
e = int(e)

r = random.randint(s, e)
num = 0
while True:
	num = num + 1
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
print('你總共猜了',num,'次')
