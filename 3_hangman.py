import json
import random

# import data of the dictionary
dictionary = json.load(open("data.json"))

# Random word
palabra_adivinar = random.choice(list(dictionary.keys())).lower()

# palabra con espacios
palabra_espacios = []

#letras que se van diciendo en las tiradas
letras_dichas = []

#intentos 
intentos = 10

# palabra con espacios
for letra in palabra_adivinar:
    palabra_espacios += "_"

    
def ahorcado(x):
    if x == 0:print("      +\n" + "      |\n" + "      |\n" + "      |       \n" + "      |\n" + "      |\n" + "=========")
    if x == 1:print("  +---+\n" + "      |\n" + "      |\n" + "      |       \n" + "      |\n" + "      |\n" + "=========")
    if x == 2:print("  +---+\n" + "  |   |\n" + "      |\n" + "      |       \n" + "      |\n" + "      |\n" + "=========")
    if x == 3:print("  +---+\n" + "  |   |\n" + "  O   |\n" + "      |       \n" + "      |\n" + "      |\n" + "=========")
    if x == 4:print("  +---+\n" + "  |   |\n" + "  O   |\n" + "  |   |       \n" + "      |\n" + "      |\n" + "=========")
    if x == 5:print("  +---+\n" + "  |   |\n" + "  O/  |\n" + "  |   |       \n" + "      |\n" + "      |\n" + "=========")
    if x == 6:print("  +---+\n" + "  |   |\n" + " \O/  |\n" + "  |   |       \n" + "      |\n" + "      |\n" + "=========")
    if x == 7:print("  +---+\n" + "  |   |\n" + " \O/  |\n" + "  |   |       \n" + "   \  |\n" + "      |\n" + "=========")
    if x == 8:print("  +---+\n" + "  |   |\n" + " \O/  |\n" + "  |   |       \n" + " / \  |\n" + "      |\n" + "=========")
    if x == 9:print("  +---+\n" + "  |   |\n" + "  O   |\n" + " /|\  |       \n" + " / \  |\n" + "      |\n" + "========= Game over")
      
    
print("Adivina la palabra:" + (' '.join(palabra_espacios)) + " en menos de 10 tiradas.")
  
#Check the letter    
for intento in range(intentos):
    #Numero de partida / total
    print(str("\nTirada: ") + str(intento+1) + str("/")+ str(intentos))

    #letra que se mete en la tira
    letra_dicha = (input("Está esta letra?: ")).lower()
   
    while letra_dicha not in "abcdefghijklmnñopqrstuvwxyz ":
        print(str(letra_dicha) + ": caracter no correcto")
        letra_dicha = (input("Vuelve a probar: ")).lower()    
    if letra_dicha in "abcdefghijklmnñopqrstuvwxyz ":
        letras_dichas += letra_dicha    
         
    #analiza las letras elegidas
    palabra_espacios = []
    for letra_palabra in palabra_adivinar:
        if letra_palabra in letras_dichas:
            palabra_espacios += letra_palabra
        else:
            palabra_espacios += "_"    
           
    # match score
    print("Adivina la palabra: " + (' '.join(palabra_espacios)))
    print("Letras dichas: " + (", ".join(letras_dichas)))
   
    #Revision, win?
    analisis = 0
    for x in palabra_adivinar:
        for letra in letras_dichas:
            if letra == x:
                analisis += 1
                        
    if analisis == len(palabra_adivinar):
        print("Ganas!!")  
        break
    
    #print hangman
    ahorcado(intento)
