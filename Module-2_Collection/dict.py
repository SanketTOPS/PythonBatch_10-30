stdata={'id':101,'name':'sanket','sub':'python'}
"""print(stdata)
print(stdata['name'])
print(stdata.get("sub"))

print(stdata.keys())
print(stdata.values())"""

"""if 'city' in stdata:
    print("Yes...")
else:
    print("Noo")"""



"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""
"""print(stdata)
stdata['id']=102
stdata['name']='Nirav'
"""

#print(stdata)
#print(len(stdata))
stdata["city"]="rajkot"
#print(stdata)
#stdata.pop("sub")
#del stdata['name']
#del stdata
#stdata.clear()
print(stdata)

newdict=stdata.copy()
print(newdict)