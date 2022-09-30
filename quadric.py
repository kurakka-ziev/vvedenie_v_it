s = 0
while s == 0: 
    try: 
        a = int(input('a = '))
        if a == 0:
            print("don't make a = 0 pls \n")
            continue
        b = int(input('b = '))
        c = int(input('c = '))
    except:
        print('Vvedite chislo, a ne da')
        continue
    s = 1

d = b**2 - 4*a*c
print("d = ", d)
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
