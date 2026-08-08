#Average of number
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        total=0
        for score in self.marks:
            total += score
        avg=total/len(self.marks)
        print("Average of markd is:",avg)



s1=student("Disha",[90,80,20])
s1.average()