import cities

class City:
    def __init__(self, dict, name):
        self.name = name
        self.population = None
        self.department = None
        self.capital = True
        self.mayor = None
        for nom_cle, nom_valeur in dict.items():
            if hasattr(self, nom_cle):
                setattr(self, nom_cle, nom_valeur)
    
