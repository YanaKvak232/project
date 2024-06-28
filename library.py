class Person:
    def __init__(self, fam="", name="", otchestvo="", year="", diagnosis="", hospital_days=""):
        self.fam = fam
        self.name = name
        self.otchestvo = otchestvo
        self.year = year
        self.diagnosis = diagnosis
        self.hospital_days = hospital_days

    def getPatients_forTable(self):
        w = []
        w.append(self.fam)
        w.append(self.name)
        w.append(self.otchestvo)
        w.append(self.year)
        w.append(self.diagnosis)
        w.append(self.hospital_days)
        return w
    
    def equval_Person(self,B):
        return self.fam == B.fam and \
               self.name == B.name and \
               self.otchestvo == B.otchestvo and \
               self.year == B.year and \
               self.diagnosis == B.diagnosis and \
               self.hospital_days == B.hospital_days
class Grup:
    def __init__(self):
        self.A = {}
        self.count = 0
    
    def str(self):
        s = ''
        for x in range(len(self.A)): 
            if x in self.A:
                s += f'Person {x+1}:\n'
                s += str(self.A[x])
                s += '\n'
        return s   

    def appendPerson(self, List):
        new_Person = Person(*List)
        self.A[self.count] = new_Person

        self.count += 1
    
    def editPerson(self,x,List):
        P = Person(*List)
        self.A[x] = P

    def Str_Person(self, line):
        if line [-1] == '\n' : line = line[:-1]
        parts = line.strip().split("&")  # Assuming data is comma-separated
        return Person(*parts)
    
    def read_data(self, file_name):
        self.A = {}
        x = 0
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                self.A[x] = self.Str_Person(line)

                x += 1
                self.count += 1

    def find_keyPerson(self, List):

        P = Person(*List)
        for x in self.A :
            
            if self.A[x].equval_Person(P) :
               return x

        return -1    

    def delPerson(self, List):
        P = Person(*List)
        for x in self.A :
            if self.A[x].equval_Person(P):
                del self.A[x] 
                self.count = self.count- 1
    
                break