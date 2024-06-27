class Person:
    def __init__(self, fam, name, otchestvo, year, diagnosis, hospital_days):
        self.fam = fam
        self.name = name
        self.otchestvo = otchestvo
        self.year = year
        self.diagnosis = diagnosis
        self.hospital_days = hospital_days

    def getPatients_forTable(self):
        w = []
        print(self.fam+' '+self.name+' '+self.otchestvo)
        x = self.fam+' '+self.name+' '+self.otchestvo
        w.append(x)
        w.append(self.year)
        w.append(self.diagnosis)
        w.append(self.hospital_days)
        print(w)
        return w

class Grup:
    def __init__(self):
        self.A = {}
        self.count = 0

    def __str__(self):
        s = ''
        for x in range(len(self.A)):  
            if x in self.A: 
                s += f'Person {x+1}:\n'
                s += str(self.A[x])
                s += '\n'
        return s
    
    def appendEmployee(self, str_Employee):
        parts = str_Employee.strip().split(" ")  # Split the string into parts
        if len(parts) >= 6:  
            self.A[self.count] = Person(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
            self.count += 1
            with open('text.txt', 'a', encoding='utf-8') as file:
                file.write('\n' + str_Employee)  # Write the complete string to the file
        else:
            print(f"Skipping line: {str_Employee} ()")

    def read_data_from_file(self, filename):
        self.A = {}
        x = 0
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if line[-1] == '\n':
                    line = line[:-1]
                parts = line.strip().split(" ")

                if len(parts) >= 6:  
                    self.A[x] = Person(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5])
                    x += 1
                    self.count += 1
                else:
                    print(f"Skipping line: {line} (Not enough parts)") 

                    
       
