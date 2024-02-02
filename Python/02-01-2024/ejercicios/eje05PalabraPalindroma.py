word = (input("Ingrese la frase o palabra: "))
edWord = word.lower().replace(" ", "")

newWord = list(range(len(edWord)))

for i in range(len(edWord)):
    newWord[len(edWord)-i-1] = edWord[i]
    
newWord = "".join(newWord)

if(edWord == newWord):
    print("Es palindroma")
else:
    print("No es palindroma")