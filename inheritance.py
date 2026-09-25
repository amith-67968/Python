class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showdetails(self):
        print(f'The name of the Employee:{self.id} is {self.name}')
e=employee("Amith",100)
e.showdetails()