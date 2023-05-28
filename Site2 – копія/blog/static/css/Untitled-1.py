class student():
    name=""
    age=0
    def write(self):
        file=open("file.txt","a+")
        file.write(self.name+" "+str(self.age)+"\n")
    def show(self):
        self.wire()
        print(f"Name : {self.name}\n)"
            f"Age : {self.age}")   
arr=[]
i=0
size=int(input("Enter size people "))
while i<size:
    arr.append(student())
    i+=1
i=0
while i<size:
    arr[i].name=input("Enter your name ")
    arr[i].age=int(input("Enter your age "))
    i+=1
i=0
