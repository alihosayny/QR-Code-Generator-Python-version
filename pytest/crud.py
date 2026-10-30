class Etudiant:
    def __init__(self,nom,age,filliere):
        self.name = nom
        self.age = age
        self.fill = filliere

    def ajouter(self):
        print(self.name + str(self.age) + self.fill)

etd = Etudiant("ali",25,"dev")        
etd.ajouter()