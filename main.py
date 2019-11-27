class City:
    def __init__(self, nom, departement):
        self.nom_ville = nom
        self.numero_departement= departement
    def __show_localisation__(self):
        print("la ville de {} se trouve dans le departement {}".format(self.nom_ville, self.numero_departement))
    def __change_localisation__(self,nom,departement):
        self.nom_ville = nom
        self.numero_departement= departement
ville1 = City("Roubaix", 59)
ville1.__show_localisation__()
ville2 = City("Paris", 75)
ville3 = City("Marseille", 13)
ville4 = City("Lens", 62)
ville5 = City("Tourcoing", 59)
ville1.__change_localisation__("Dakar", 242)
ville1.__show_localisation__()
