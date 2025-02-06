def calculate():
    M = 0
    S = 0
    while True:
        m = float(input("Here is your credit: "))
        n = float(input("Here is your score: "))
        M += m
        S += m * n
        p = input("Go on? ")
        if p.lower() != 'q':
            continue
        else:
            break
    if M == 0:
        return 0
    return S/M


# For p in calculate(), you‘d better input a letter, not pushing other bottoms.

def case1(s):
    if s < 1.0:
        print('Warning! Your GPA is low! Please work harder in the next semester!')

    elif s >= 3.8:
        print('Excellent! Your GPA is quite high! Please keep going!')


def case2(s):
    if s < 60:
        print('Warning! Your GPA is low! Please work harder in the next semester!')
    elif s >= 90:
        print('Excellent! Your GPA is quite high! Please keep going!')


choice = input("Enter your choice: ")

if choice == 'GPA':
    final = calculate()
    case1(final)
elif choice == 'score':
    final = calculate()
    case2(final)
else:
    print('Please restart and input it again! ')

print('Your GPA is', '%.4f' % final, end='\r')



# -*- coding: utf-8 -*- 
# Here is the coding of calculating GPA(score): 

M = 0
S = 0

while True:
	print("Enter your datas: ")
	n = float(input("Here is your score: ")) 
	m = float(input("Here is your credit: ")) 
	M += m 
	S += m * n 
	s = S / M 
	p = input("Go on? ") 
	if p != 'q': 
		continue 
	break

if s < 1.0: 
	print('Warning! Your GPA is low! Please work harder in the next semester!') 
elif s >= 3.8: 
	print('Excellent! Your GPA is quite high! Please keep going!') 

print('Your GPA is', '%.4f' % s, end='\r')
