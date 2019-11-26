class City:
    def __init__(self, nom, departement):
        self.nom_ville = nom
        self.numero_departement= departement
ville = City("lille", 59)

print("la ville de {} se trouve dans le departement {}".format(ville.nom_ville, ville.numero_departement))

ville.nom_ville = "Roubaix"
print("la ville de {} se trouve dans le departement {}".format(ville.nom_ville, ville.numero_departement))

ville2 = City("Paris", 75)
ville3 = City("Marseille", 13)
ville4 = City("Lens", 62)
ville5 = City("Tourcoing", 59)
print("la ville de {} se trouve dans le departement {}".format(ville2.nom_ville, ville2.numero_departement))
print("la ville de {} se trouve dans le departement {}".format(ville3.nom_ville, ville3.numero_departement))
print("la ville de {} se trouve dans le departement {}".format(ville4.nom_ville, ville4.numero_departement))
print("la ville de {} se trouve dans le departement {}".format(ville5.nom_ville, ville5.numero_departement))
ville5.nom_ville = ("Lyon")
ville5.numero_departement = 69
print("la ville de {} se trouve dans le departement {}".format(ville5.nom_ville, ville5.numero_departement))
