#!/usr/bin/env python3
print("if the program fails ,please install colorama using pip install colorama")
from datetime import datetime
import math
from colorama import Style,Fore,init
init()
print(Fore.RED+"="*40)
print(Fore.GREEN+"welcome to multicalc ver. 0.1,select the type you want")
print("1 for finance like CI or SI")
print("2 for conversion of dollar to native currency(NOTE:ONLY SUPPORTS EURO")
print("3 for normal calculator like add,sub,div,mul")
a=int(input("enter the number:"))
print("="*40)
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
	if(b != 0):
		return div
	else:
		print("invalid operation")
file=open("dgclac.log","a")
file.write(datetime.now().strftime("logged at %H:%M:%S on %d-%m-%Y\n"))
file.write("------STARTING MULTICALC 0.1V------\n")
file.write("waiting for answer......\n")
if(a==1):
	print("ci(1) or si(2):")
	ap=int(input("please enter 1 or 2:"))
	if(ap==1):
		p=float(input("principal:"))
		r=float(input("rate:"))
		t=float(input("years:"))
		print(ci(p,r,t))
		file.write("used choosed 1")
	elif(ap==2):
		p1=float(input("principal:"))
		r1=float(input("rate:"))
		y1=float(input("years:"))
		print(si(p1,r1,y1))
		file.write("user choosed 2")
	else:
		file.write("exited with error code 2 in block finance")
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
	file.write("Error code 1,invalid input found")

print(Fore.RED+"="*40)
print("Thanks for using program")
print("dev-Vardhan from india 😃:)")
print("="*40)

