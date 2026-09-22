class person:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("amith","developer")
b=person("divya","HR")
a.info()
b.info()