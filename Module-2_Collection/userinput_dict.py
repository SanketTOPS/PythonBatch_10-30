stdata=dict()

n=int(input("How many pairs you want for dict? = "))

for i in range(n):
    key=input("Enter your key:")
    value=input("Enter your value:")
    stdata[key]=value

print(stdata)
