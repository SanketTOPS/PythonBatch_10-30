mystr="This is not poor code"

n=mystr.find('not')
p=mystr.find('poor')

if p>n and n>0 and p>0:
    mystr=mystr.replace(mystr[n:(p+4)],'good')
    print(mystr)
else:
    print(mystr)


