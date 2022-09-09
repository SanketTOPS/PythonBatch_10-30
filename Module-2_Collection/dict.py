stdata={'id':1,'name':'sanket','sub':'python'}

#print(stdata)
#print(stdata['name'])
#print(stdata.get('sub'))

#print(len(stdata))

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo..")"""

#print(stdata.keys())
#print(stdata.values())

#print(stdata)
#stdata['id']=2
print(stdata)

"""for i in stdata:
    print(i)"""

"""for i in stdata.values():
    print(i)"""

"""for i in stdata.items():
    print(i)"""

stdata['city']='Rajkot'
#stdata.pop('sub')
#del stdata['name']
stdata.clear()
print(stdata)