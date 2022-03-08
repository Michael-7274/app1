# can also do like this
# print("print(\"hello\")")
# r="hii buddy"
# print(r[3])

# print('String\b')
# a=1,2,3
# print(type(a))
# print(123_456_789+300)
# a=6
# print('hi'+str(a))
# a=True
# print(type(a))
# print(str(a))
# print(type(a))
# print(5**2)
# print(3*(3+1)/3)
# print(3/4)

a=float(input("Enter Your bill amount: "))
b=input("Enter Your tip percentage(in number): ")
b1=0
for x in range(len(b)):
    if b[x]=='%':
        break
    elif b[x]=='.':
        b1+=int(b[x+1])*0.1
        if b[x+2]=='%':
            break
        elif b[x+2]!='%':
            b1+=int(b[x+2])*0.01
            break
        else:
            break
    else:
        b1+=int(b[x])*(10**(len(b)-x-1))

print(b1)
c=int(input("How many people are splitting the bill? "))
a+=(a*b1/100)
a1=a/c
print(f"Amount to pay {round(a1,2)}")
