class Ovqat:
    def __init__(self, nom, kaloriya):
        self.nom = nom
        self.kaloriya = kaloriya

class DietPlanner:
    def __init__(self):
        self.ovqatlar = []

    def qo'sh(self, ovqat):
        self.ovqatlar.append(ovqat)

    def umumiy_kaloriya(self):
        return sum(ovqat.kaloriya for ovqat in self.ovqatlar)

    def kunlik_ovqatlanish(self):
        return len(self.ovqatlar)

# Misol:
diet_planner = DietPlanner()
diet_planner.qo'sh(Ovqat("Non", 100))
diet_planner.qo'sh(Ovqat("Qovuruvchi", 200))
diet_planner.qo'sh(Ovqat("Meva", 50))

print("Umumiy kaloriya:", diet_planner.umumiy_kaloriya())
print("Kunlik ovqatlanish:", diet_planner.kunlik_ovqatlanish())
