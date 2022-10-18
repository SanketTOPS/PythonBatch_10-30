class mitesh:
    mid=0
    msub=''

    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.msub=input("Enter Mitesh's Subject:")

class nirav:
    nid=0
    nsub=''

    def n_getdata(self):
        self.nid=input("Enter Nirav's ID:")
        self.n_sub=input("Enter Nirav's Subject:")

class ashok:
    aid=0
    asub=''

    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.asub=input("Enter Ashoks's Subject:")

class college(mitesh,nirav,ashok):
    def alldata(self):
        print("------Mitesh Data-----")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Subject:",self.msub)
        print("------Nirav Data-----")
        print("Nirav's ID:",self.nid)
        print("Nirav's Subject:",self.nsub)
        print("------Ashok Data-----")
        print("Ashok's ID:",self.aid)
        print("Ashok's Subject:",self.asub)

cl=college()
cl.m_getdata()
cl.n_getdata()
cl.a_getdata()
cl.alldata()

