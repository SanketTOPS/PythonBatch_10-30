def getdata(id,name,sub):
    print("Student ID:",id)
    print("Student Name:",name)
    print("Student Subject:",sub)

#getdata(101,'Sanket','Python') #static 

stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")

getdata(stid,stnm,stsub) #dynamic
