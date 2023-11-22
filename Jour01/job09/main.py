class Produit:
    def __init__(self, nom, prix_unitaire, quantite_en_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_en_stock = quantite_en_stock

    def ajuster_prix_inflation(self, pourcentage):
        self.prix_unitaire *= (1 + pourcentage / 100)

class Inventaire:
    def __init__(self):
        self.inventaire = {}

    def ajouter_produit(self, produit, quantite):
        if produit in self.inventaire:
            self.inventaire[produit].quantite_en_stock += quantite
        else:
            self.inventaire[produit] = produit

    def retirer_produit(self, produit, quantite):
        if produit in self.inventaire:
            if self.inventaire[produit].quantite_en_stock >= quantite:
                self.inventaire[produit].quantite_en_stock -= quantite
                if self.inventaire[produit].quantite_en_stock == 0:
                    del self.inventaire[produit]
            else:
                print("Quantité insuffisante.")
        else:
            print("Produit non trouvé dans l'inventaire.")

    def ajuster_prix_inflation(self, pourcentage):
        for produit in self.inventaire:
            produit.ajuster_prix_inflation(pourcentage)

    def afficher_inventaire(self):
        print("\nInventaire actuel :")
        for produit, info in self.inventaire.items():
            print(f"Nom: {produit.nom} | Prix unitaire: {produit.prix_unitaire} | Quantité en stock: {info.quantite_en_stock}")

# Fonction pour saisir la quantité d'achat
def saisir_quantite_achat():
    try:
        quantite = int(input("Entrez la quantité que vous souhaitez acheter : "))
        if quantite <= 0:
            print("La quantité doit être supérieure à zéro.")
            return saisir_quantite_achat()
        return quantite
    except ValueError:
        print("Veuillez entrer un nombre entier.")
        return saisir_quantite_achat()

# Exemple d'utilisation
if __name__ == "__main__":
    boisson = Produit("boisson", 2.5, 70)
   

    inventaire = Inventaire()

    inventaire.ajouter_produit(boisson, 10)
  
    inventaire.afficher_inventaire()

    # Ajuster les prix en raison de l'inflation
    pourcentage_inflation = 10
    inventaire.ajuster_prix_inflation(pourcentage_inflation)

    inventaire.afficher_inventaire()
