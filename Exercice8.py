def addition(a, b):
    resultat = a + b
    return resultat
x = 5 #Le 5 était considéré comme un str, donc j'ai enlever les guillemets
y = 3
z = addition(x, y)
print("Résultat:", z)