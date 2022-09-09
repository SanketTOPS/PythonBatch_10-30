myset={'A','B','C','D','E','D','A','E'}

#print(myset[0])

#print(len(myset))

"""if 'X' in myset:
    print("Yes...")
else:
    print("Noo")"""

# ------------------------------ #

"""for i in myset:
    print(i)"""

# ------------------------------ #


#myset.add('F')
#myset.update(['G','H','I','J'])
#myset.remove('G')
#myset.pop()
#print(myset)
#newset=myset.copy()
#print(newset)

# ------------------------------------------------ #

print(myset)

newset={'P','Q','R','S','T','A','B','D'}
print(newset)

#x=myset.union(newset)
x=myset.intersection(newset)
print(x)
