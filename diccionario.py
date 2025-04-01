meme_dict = {
            "CRINGE":  "Algo excepcionalmente raro o embarazoso", #este si sirve
            "LOL": "Una respuesta común a algo gracioso",
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

#si palabra esta en diccionario......
if word in meme_dict.keys():

    print(word)
    # ¿Qué debemos hacer si se encuentra la palabra?
else:

    #
    print('Significado no encontrado')
    
