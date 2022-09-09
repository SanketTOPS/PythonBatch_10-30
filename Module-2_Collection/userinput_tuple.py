city=[] #list object

n=int(input("Enter number of city's elements, you want:"))

for i in range(n):
    ct=input("Enter your city:")
    city.append(ct)

print(tuple(city)) #convert into tuple