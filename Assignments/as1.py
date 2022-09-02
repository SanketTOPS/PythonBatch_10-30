mystr="This is Python and This is VSCode."

cn=dict()
wrd=mystr.split()
#print(wrd)

for i in wrd:
    if i in cn:
        cn[i]+=1
    else:
        cn[i]=1
print(cn)


