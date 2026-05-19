import sys

print("=" * 40)
print("Bienvenue dans mon premier job Jenkins !")
print("=" * 40)

if len(sys.argv) > 1:
    nom = sys.argv[1]
else:
    nom = "Etudiant Jenkins"

print(f"Bonjour {nom}, ton job Jenkins a reusse !")

a = 10
b = 5
print(f"{a} + {b} = {a + b}")
print(f"{a} + {b} = {a + b}")

assert a + b == 100, "Le tests a echoue intentionnellement!"
print("Tous les tests passent avec succes")
