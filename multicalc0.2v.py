import math
def si(a,b,c):
	res=(a*b*c)/100
	return res
def ci(a,b,c):
	cl=a*((1+b/100)**c)
	return cl
def monINR(a):
	m=a*86
	return m
def monFRA(a):
	m=a*0.86
	return m
def add(a,b):
	ad=a+b
	return ad
def sub(a,b):
	su=a-b
	return sub
def mul(a,b):
	mul=a*b
	return mul
def div(a,b):
	div=a/b
	return div
print("="*40) 
print("welcome to multicalc ver. 0.1,select the type you want")
print("1 for finance like CI or SI")
print("2 for conversion of dollar to native currency(NOTE:ONLY SUPPORTS EURO AND INR)")
print("3 for normal calculator like add,sub,div,mul")
a=int(input("enter the number:"))
print("="*40)
if(a==1):
	print("ci(1) or si(2):")
	ap=int(input("please enter 1 or 2:"))
	if(ap==1):
		p=float(input("principal:"))
		r=float(input("rate:"))
		t=float(input("years:"))
		print(ci(p,r,t))
	else:
		p1=float(input("principal:"))
		r1=float(input("rate:"))
		y1=float(input("years:"))
		print(si(p1,r1,y1))
elif(a==2):
	e=int(input("enter 1 to convert dollar to euro or 2 to convert dollar to inr:"))
	if(e==1):
		e2=float(input("enter value:"))
		print(monFRA(e2),"EUR")
	else:
		e3=float(input("enter value:"))
		print(monINR(e3),"INR")
elif(a==3):
	f=int(input("enter 1 for add,2 for sub,3 for div and 4 for mul"))
	if(f==1):
		er=float(input("enter first value:"))
		en=float(input("enter second value:"))
		print(add(er,en))
	elif(f==2):
		er1=float(input("enter first value:"))
		en1=float(input("enter second value:"))
		print(sub(er1,en1))
	elif(f==3):
		er2=float(input("enter first value:"))
		en2=float(input("enter second value:"))
		print(div(er2,en2))
	else:
		er3=float(input("enter first value:"))
		en3=float(input("enter second value:"))
		print(mul(er3,en3))
else:
	print("invalid operation")

print("="*40)
print("Thanks for using program")
print("dev-Vardhan from india 😃:)")
print("="*40)
