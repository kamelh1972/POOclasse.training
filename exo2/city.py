from  cities import *
class City:
    def __init__(self, i):
        self.name = None
        self.population = None
        self.department = None
        self.mayor = None
        self.capital = None

        for nom_cle, nom_valeur in i.items():
            if hasattr(self, nom_cle):
                setattr(self, nom_cle, nom_valeur)

    def show_information(self):
            text = "------------------\n\
            name: {}\n\
            population: {}\n\
            department: {}\n\
            mayor: {}\n\
            capital: {}\n"

            print(text.format(self.name, self.population, self.department, self.mayor, self.capital))
