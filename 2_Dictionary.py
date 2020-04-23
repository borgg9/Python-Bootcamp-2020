import json
from difflib import get_close_matches

# import data of the dictionary
dictionary = json.load(open("data.json"))

def lookup_dictionary(x):    
    if word in dictionary:
        print("The definition of " + ("\033[1m" + str(word).capitalize() + "\033[0m" ) + " is:")
        x=0
        for definition in dictionary[word]:
            x += 1
            print(str(x) + ". " + str(definition))
    else:
        print("Sorry, " + ("\033[1m" + str(word).capitalize() + "\033[0m" ) + " is not in the dictionary, try another.")
        
        #Una unica palabra similar
        if len(get_close_matches(word, dictionary.keys(), cutoff=0.80)) == 1:
            print("You mean " + str(get_close_matches(word, dictionary.keys(), cutoff=0.80)[0].capitalize()) + " instead of " + str(word).capitalize() + " (y/n)?")
            correct_word = input("y/n?: ")
            if correct_word == "y":
                print("\n" + str(get_close_matches(word, dictionary.keys(), cutoff=0.80)[0].capitalize()) + " is the correct.")
               
                word_ok = get_close_matches(word, dictionary.keys(), cutoff=0.80)[0]            
                
                if word_ok in dictionary:
                    print("The definition of " + ("\033[1m" + str(word_ok).capitalize() + "\033[0m" ) + " is:")
                    x=0
                    for definition in ((dictionary[word_ok])):
                        x += 1
                        print(str(x) + ". " + str(definition))                
            else:
                print("So try again")

        
        
        
        
        
        
        #Varias palabras similares
        if len(get_close_matches(word, dictionary.keys(), cutoff=0.80))  > 1:
            print("Maybe you are referring to one of these:")
            x=0
            for possible in (get_close_matches(word, dictionary.keys(), cutoff=0.80)):
                x += 1
                print(str(x) + ". " + str(possible).capitalize())

            correct_word = input("Enter the number of the correct one ('n' if none): ")
            if correct_word == ("n"):
                print("So try again")
            
            else:
                correct_word = int(correct_word) - 1
                print("\n" + str(get_close_matches(word, dictionary.keys(), cutoff=0.80)[int(correct_word)].capitalize()) + " is the correct.")

                word_ok = get_close_matches(word, dictionary.keys(), cutoff=0.80)[int(correct_word)]            

                if word_ok in dictionary:
                    print("The definition of " + ("\033[1m" + str(word_ok).capitalize() + "\033[0m" ) + " is:")
                    x=0
                    for definition in ((dictionary[word_ok])):
                        x += 1
                        print(str(x) + ". " + str(definition))
                        


word = (input("What word do you want to look up?: ")).lower()

lookup_dictionary(word)
