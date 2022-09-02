mylist=['PHP','Android','Python','C','C++']

ls=[]
for i in mylist:
    ls.append((len(i)))
ls.sort()
print(ls)
print(ls[-1])



