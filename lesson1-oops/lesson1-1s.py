class student():
    def __init__(self,name,username,age,school,meg,set,form,password):
        self.name=name
        self.username=username
        self.age=age
        self.school=school
        self.meg=meg
        self.set=set
        self.form=form
        self.password=password
    def showdetails(self):
        print("student details")
        print("name: "+self.name)
        print("username: "+self.username)
        print("age: "+str (self.age))
        print("school: "+self.school)
        print("meg: "+str (self.meg))
        print("set: "+str (self.set))
        print("form: "+self.form)
    def login(self,not_a_scam):
        if not_a_scam==self.password:
            print("password correct your banking app may be opened")
        else:
            print("you are so luckey I would have had  so much money")
stud1=student("riusui","123rere",12,"bms",7,2,"a","dfgrger")
print(stud1.username)
stud2=student("osamu","123osos",14,"BGCS",8,4,"s","dkjfbuik")
print(stud2.name)
stud2.showdetails()
not_a_scam=input("please input your password(this is not a scamming website)")
stud2.login(not_a_scam)