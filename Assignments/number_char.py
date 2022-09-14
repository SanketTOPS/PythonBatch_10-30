mystr="This is Python and This is VSCode."

cn=dict()
print(mystr)
#rint(mystr.split())
x=mystr.split()

for i in x:
    #print(i)
    if i in cn:
        cn[i]+=1
    else:
        cn[i]=1
print(cn)