a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

d = b**2 - 4*a*c

# ответы с нецелыми корнями округляются
if d > 0:
	x1 = (-b + (d **1/2)) / (2 * a) 
	x2 = (-b - (d **1/2)) / (2 * a)
	print('x1 = ', int(x1), 'x2 = ' , int(x2))
elif d == 0:
	x = -b / (2 * a)
	print('x = ', int(x))
elif d < 0: 
	print('no korney :)')
