# #there is a built in round function
# x = 3.55
# a = round(x)
# print(x)
# print(a)
# #find absolute value of somehting
# y = -2828
# b = abs(y)
# print(y)
# print(b)
# #find the power of things
# result=pow(6,7)
# print(result)
# #finding min and max of nums
# minimum=min(a,b,x,y)
# print(minimum)
# maximum=max(a,b,x,y)
# print(maximum)

# #importing math module
# import math
# print(math.pi)#pi
# print(math.e)#exponential constant
# answer=math.sqrt(9)#square root of a number
# b=4.2
# n = 232.2321
# answer = math.ceil(b)#rounds num up
# answer2 = math.floor(n)#rounds num down
# print(answer)
# print(answer2)

# #EXERCISE 1
# import math
# print("I will be figuring out the circumference")
# r = float(input("What is the radius?: "))
# answer = math.pi*r*2
# print(f"The circumference is {round(answer)}cm")#(answer, 2) for round to 2 decimal points

#EXERCISE 2
import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = math.sqrt(pow(a, 2) * pow(b, 2))
print(c)

