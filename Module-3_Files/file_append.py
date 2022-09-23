fl=open('myfile.txt','a')

stid=input("Enter ID:")
stnm=input("Enter Name:")
stsub=input("Enter Subject:")

fl.write(f"Student ID:{stid}\n")
fl.write(f"Student Name:{stnm}\n")
fl.write(f"Student Subject:{stsub}\n")