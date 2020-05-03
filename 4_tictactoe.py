from tkinter import *
import emoji
import random

raiz = Tk()

miFrame = Frame(raiz)
miFrame.pack()
raiz.title("3 en ralla")

# resultados
resultados = [0,0,0,0,0,0,0,0,0]
mano = 0



# emoticonos x e y
AA = (emoji.emojize(':heavy_check_mark:'))   
BB = (emoji.emojize(':heavy_multiplication_x:'))

AA = "AA"
BB = "BB"

# pantalla
pantalla = Entry(miFrame)
pantalla.grid(row=0, column=0, columnspan=3)



# que jugador empieza?
def comenzar_juego():

    global mano1
    if (random.randrange(0,2)) == 0:    
#    if 0 == 1:
        pantalla.insert(0, "Comienza A (Mac)")
        # 1º movimiento de A
        x=[0,8,2,6]
        resultados[x[random.randrange(0,4)]] = AA
        L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
        L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        global mano
        mano_partida()
        print(mano)
        print(resultados)
        mano_5_esquina()
        
    else:
        pantalla.insert(0, "Comienza B (Persona)")
        
# boton start        
star_boton = Button(miFrame, text="Start", command=comenzar_juego)
star_boton.place(relx = 0.05, rely = 0.3)
star_boton.grid(column=0, row=4)


def mano_partida():
    global mano
    if 0 in resultados:
        mano += 1
        print(mano)

def esquina_contraria(x):
    global mano1
    if AA in mano1:
        print("esquina contraria")
        print(x.index("AA"))
        if x.index(AA) == 0:
            codigoA9()        
        elif x.index(AA) == 2: 
            codigoA7()
        elif x.index(AA) == 6: 
            codigoA3()
        elif x.index(AA) == 8: 
            codigoA1()        

        

        
def BNoEmpiezaCon5():
    
    global resultados
    
    global linea1
    global linea2
    global linea3
    global linea4
    global linea5
    global linea6
    global linea7
    global linea8

    linea1 = (resultados[0],resultados[1], resultados[2])
    linea2 = (resultados[3],resultados[4], resultados[5])
    linea3 = (resultados[6],resultados[7], resultados[8])
    linea4 = (resultados[0],resultados[3], resultados[6])
    linea5 = (resultados[1],resultados[4], resultados[7])
    linea6 = (resultados[2],resultados[5], resultados[8])
    linea7 = (resultados[0],resultados[4], resultados[8])
    linea8 = (resultados[2],resultados[4], resultados[6]) 
    
    cambios = 0
    
    print("BNoEmpiezaCon5")
    print("donde esta AA")
    print(resultados.index("AA"))
    print("donde esta BB")
    print(resultados.index("BB"))
    if resultados.index(AA) == 0:
        if BB not in linea1:
#            print("1 Linea1 libre")
            codigoA3()
#            print("A3")
            
            cambios += 1
            if cambios > 0:
                return
            return            
            
        if BB not in linea4:
#            print("2 Linea4 libre")
            codigoA7()
#            print("A7")
            
            cambios += 1
            if cambios > 0:
                return
            return              

    elif resultados.index(AA) == 2: 
        if BB not in linea1:
#            print("3 Linea1 libre")
            codigoA1()
#            print("A1")
            
            cambios += 1
            if cambios > 0:
                return
            return 
        
        if BB not in linea6:
#            print("4 Linea6 libre")
            codigoA9()
#            print("A9")
            
            cambios += 1
            if cambios > 0:
                return
            return 

    elif resultados.index(AA) == 6: 
        if BB not in linea4:
#            print("5 Linea4 libre")
            codigoA1()
#            print("A1")
            
            cambios += 1
            if cambios > 0:
                return
            return 
        
        if BB not in linea3:
#            print("6 Linea3 libre")
            codigoA9()
#            print("A9")
            
            cambios += 1
            if cambios > 0:
                return
            return 

    elif resultados.index(AA) == 8: 
        if BB not in linea3:
#            print("7 Linea3 libre")
            codigoA7()
#            print("A7")
            
            cambios += 1
            if cambios > 0:
                return
            return 
        
        if BB not in linea6:
#            print("8 Linea6 libre")
            codigoA3()
#            print("A3")
            
            cambios += 1
            if cambios > 0:
                return
            return 
    

        
        
        
        
        
        
def ataque_defensa():
    print("ataque/defensa")
    
    global resultados
    
    global linea1
    global linea2
    global linea3
    global linea4
    global linea5
    global linea6
    global linea7
    global linea8

    
    # lineas analisis
    linea1 = (resultados[0],resultados[1], resultados[2])
    linea2 = (resultados[3],resultados[4], resultados[5])
    linea3 = (resultados[6],resultados[7], resultados[8])
    linea4 = (resultados[0],resultados[3], resultados[6])
    linea5 = (resultados[1],resultados[4], resultados[7])
    linea6 = (resultados[2],resultados[5], resultados[8])
    linea7 = (resultados[0],resultados[4], resultados[8])
    linea8 = (resultados[2],resultados[4], resultados[6])   
    
    
    cambios = 0


    
    
# ATAQUE ------------------
    

    cambios = 0

    alertas1 = 0
    for posicion in linea1:
        if posicion == AA:
            alertas1 += 1
    print("L1 suma: " + str(alertas1)) 
    print(linea1)
    if alertas1 == 2:
        if resultados[0] == 0:
            codigoA1()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[1] == 0:
            codigoA2()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[2] == 0:
            codigoA3()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea1 = (resultados[0],resultados[1], resultados[2])  
        print(linea1)



    alertas2 = 0
    for posicion in linea2:
        if posicion == AA:
            alertas2 += 1
    print("L2 suma: " + str(alertas2))  
    print(linea2)
    if alertas2 == 2:
        if resultados[3] == 0:
            codigoA4()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[5] == 0:
            codigoA6()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea2 = (resultados[3],resultados[4], resultados[5]) 
        print(linea2)



    alertas3 = 0
    for posicion in linea3:
        if posicion == AA:
            alertas3 += 1
    print("L3 suma: " + str(alertas3))
    print(linea3)
    if alertas3 == 2:
        if resultados[6] == 0:
            codigoA7()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[7] == 0:
            codigoA8()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[8] == 0:
            codigoA9()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea1 = (resultados[6],resultados[7], resultados[8])  
        print(linea3)     



    alertas4 = 0
    for posicion in linea4:
        if posicion == AA:
            alertas4 += 1
    print("L4 suma: " + str(alertas4))
    print(linea4)
    if alertas4 == 2:
        if resultados[0] == 0:
            codigoA1()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[3] == 0:
            codigoA4()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[6] == 0:
            codigoA7()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea4 = (resultados[0],resultados[3], resultados[6]) 
        print(linea4) 



    alertas5 = 0
    for posicion in linea5:
        if posicion == AA:
            alertas5 += 1
    print("L5 suma: " + str(alertas5))  
    print(linea5)
    if alertas5 == 2:
        if resultados[1] == 0:
            codigoA2()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[7] == 0:
            codigoA8()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea5 = (resultados[1],resultados[4], resultados[7]) 
        print(linea5)



    alertas6 = 0
    for posicion in linea6:
        if posicion == AA:
            alertas6 += 1
    print("L6 suma: " + str(alertas6)) 
    print(linea6)
    if alertas6 == 2:
        if resultados[2] == 0:
            codigoA3()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[5] == 0:
            codigoA6()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[8] == 0:
            codigoA9()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea6 = (resultados[2],resultados[5], resultados[8]) 
        print(linea6)



    alertas7 = 0
    for posicion in linea7:
        if posicion == AA:
            alertas7 += 1
    print("L7 suma: " + str(alertas7))  
    print(linea7) 
    if alertas7 == 2:
        if resultados[0] == 0:
            codigoA1()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[8] == 0:
            codigoA9()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea7 = (resultados[0],resultados[4], resultados[8])    
        print(linea7)

    
    alertas8 = 0
    for posicion in linea8:
        if posicion == AA:
            alertas8 += 1
    print("L8 suma: " + str(alertas8))  
    print(linea8)
    if alertas8 == 2:
        if resultados[2] == 0:
            codigoA3()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[6] == 0:
            codigoA7()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea8 = (resultados[2],resultados[4], resultados[6]) 
        print(linea8) 
        
        
        
        
    
    
    
    
    
    
# DEFENSA -------------------
    alertas1 = 0
    for posicion in linea1:
        if posicion == BB:
            alertas1 += 1
    print("L1 suma: " + str(alertas1)) 
    print(linea1)
    if alertas1 == 2:
        if resultados[0] == 0:
            codigoA1()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[1] == 0:
            codigoA2()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[2] == 0:
            codigoA3()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea1 = (resultados[0],resultados[1], resultados[2])  
        print(linea1)



    alertas2 = 0
    for posicion in linea2:
        if posicion == BB:
            alertas2 += 1
    print("L2 suma: " + str(alertas2))  
    print(linea2)
    if alertas2 == 2:
        if resultados[3] == 0:
            codigoA4()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[5] == 0:
            codigoA6()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea2 = (resultados[3],resultados[4], resultados[5]) 
        print(linea2)



    alertas3 = 0
    for posicion in linea3:
        if posicion == BB:
            alertas3 += 1
    print("L3 suma: " + str(alertas3))
    print(linea3)
    if alertas3 == 2:
        if resultados[6] == 0:
            codigoA7()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[7] == 0:
            codigoA8()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[8] == 0:
            codigoA9()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea1 = (resultados[6],resultados[7], resultados[8])  
        print(linea3)     



    alertas4 = 0
    for posicion in linea4:
        if posicion == BB:
            alertas4 += 1
    print("L4 suma: " + str(alertas4))
    print(linea4)
    if alertas4 == 2:
        if resultados[0] == 0:
            codigoA1()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[3] == 0:
            codigoA4()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[6] == 0:
            codigoA7()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea4 = (resultados[0],resultados[3], resultados[6]) 
        print(linea4) 



    alertas5 = 0
    for posicion in linea5:
        if posicion == BB:
            alertas5 += 1
    print("L5 suma: " + str(alertas5))  
    print(linea5)
    if alertas5 == 2:
        if resultados[1] == 0:
            codigoA2()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[7] == 0:
            codigoA8()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea5 = (resultados[1],resultados[4], resultados[7]) 
        print(linea5)



    alertas6 = 0
    for posicion in linea6:
        if posicion == BB:
            alertas6 += 1
    print("L6 suma: " + str(alertas6)) 
    print(linea6)
    if alertas6 == 2:
        if resultados[2] == 0:
            codigoA3()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[5] == 0:
            codigoA6()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[8] == 0:
            codigoA9()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea6 = (resultados[2],resultados[5], resultados[8]) 
        print(linea6)



    alertas7 = 0
    for posicion in linea7:
        if posicion == BB:
            alertas7 += 1
    print("L7 suma: " + str(alertas7))  
    print(linea7) 
    if alertas7 == 2:
        if resultados[0] == 0:
            codigoA1()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[8] == 0:
            codigoA9()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea7 = (resultados[0],resultados[4], resultados[8])    
        print(linea7)

    
    alertas8 = 0
    for posicion in linea8:
        if posicion == BB:
            alertas8 += 1
    print("L8 suma: " + str(alertas8))  
    print(linea8)
    if alertas8 == 2:
        if resultados[2] == 0:
            codigoA3()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[4] == 0:
            codigoA5()
            cambios += 1
            if cambios > 0:
                return
            return
        elif resultados[6] == 0:
            codigoA7()
            cambios += 1
            if cambios > 0:
                return
            return
        else:
            print("ok 2BB y 1AA")
        linea8 = (resultados[2],resultados[4], resultados[6]) 
        print(linea8) 



        
        
# defensa del primer momiento BB       
def empiezaBB():
    global resultados
    global mano
    
    print("funciona empiezaBB")
    if resultados[4] == BB:
        # 1º movimiento de A
        x=[0,8,2,6]
        resultados[x[random.randrange(0,4)]] = AA
        L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
        L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        mano_partida()
        print(mano)
        print(resultados)
        mano_5_esquina()
    else:
        resultados[4] = AA 
        L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
        L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
        mano_partida()
        print(mano)
        print(resultados)
        mano_5_esquina()
     
    
    
global mano1
    
    
def mano_5_esquina():
    
    global mano
    
    
    if mano == 5:
        print("mano_5_esquina")
        print("esquina contraria mano1")
        print(esquina_contraria(mano1))

    if mano == 4:
        print("mano_5_esquina")
        print("esquina contraria mano1")
        print(esquina_contraria(mano1))
        
#    if mano == 1:
#        print("mano_5_esquina")
#        mano1 = resultados[:]
#        print(mano1)
    
#    print(mano1)





        
        

def maquina_piensa():
    global mano
    print("pensando")    
   
    #Esquina contraria si 1º movimiento de B es centro
    if mano == 1 and BB in resultados:
        print("empieza BB")
        empiezaBB()


    #Esquina contraria si 1º movimiento de B es centro
    if mano == 2 and resultados[4] == BB:
        print("esquina_contraria")
        esquina_contraria(resultados)

        
        
    # si dos mias --> pone una mia   
    # si dos del contrario segidas --> pone una mia
    print("ataque_defensa")
    ataque_defensa()
    
    
    #si 1º movimiento de BB no es centro
    if mano == 2 and resultados[4] != BB:
        print("BNoEmpiezaCon5")
        BNoEmpiezaCon5()
        
    
    # 5º mano
    if mano == 4:
        print("mano_5_esquina")
        mano_5_esquina()
        
    print("mano_5_esquina")
    mano_5_esquina()
    
    # Si hay 3 iguales proclama marcador
    print("marcador")
    marcador()

    
    
    
# PULSAR BOTON       
def codigoA1():
    if resultados[0] == 0:
        resultados[0] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
  

        
def codigoA2():
    if resultados[1] == 0:
        resultados[1] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
  
    
def codigoA3():
    if resultados[2] == 0:
        resultados[2] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
  
    
def codigoA4():
    if resultados[3] == 0:    
        resultados[3] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
 
    
def codigoA5():
    if resultados[4] == 0:
        resultados[4] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
   
    
def codigoA6():
    if resultados[5] == 0:
        resultados[5] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
  
    
def codigoA7():
    if resultados[6] == 0:
        resultados[6] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
   
    
def codigoA8():
    if resultados[7] == 0:
        resultados[7] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    
def codigoA9():
    if resultados[8] == 0:
        resultados[8] = AA
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
  
    
 

    
def codigoB1():
    if resultados[0] == 0:
        resultados[0] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()   
    
def codigoB2():
    if resultados[1] == 0:
        resultados[1] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()   
        
def codigoB3():
    if resultados[2] == 0:
        resultados[2] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()   
        
def codigoB4():
    if resultados[3] == 0:
        resultados[3] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()
    
def codigoB5():
    if resultados[4] == 0:
        resultados[4] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()
    
def codigoB6():
    if resultados[5] == 0:
        resultados[5] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()    
    
def codigoB7():
    if resultados[6] == 0:
        resultados[6] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()   
        
def codigoB8():
    if resultados[7] == 0:
        resultados[7] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()   
    
def codigoB9():
    if resultados[8] == 0:
        resultados[8] = BB
    L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
    L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    mano_partida()
    print(resultados)
    maquina_piensa()   
        
    






#Marcador
# solo se imprime al principio, luego todo funciona con los botones
L0 = Label(raiz, text=" {} | {} | {} \n———————\n {} | {} | {} \n———————\n {} | {} | {} ".format(resultados[0],resultados[1],resultados[2],resultados[3],resultados[4],resultados[5],resultados[6],resultados[7],resultados[8]))
L0.place(relx = 0.5, rely = 0.75, anchor = CENTER)






# ------ JUGADOR B ---------------- 
texto_boton = "B"
# ------ A Fila 1 -----    
B1 = Button(miFrame, text=texto_boton, command=codigoB1)
B1.place(relx = 0.05, rely = 0.3)
B1.grid(column=0, row=1)

B2 = Button(miFrame, text=texto_boton, command=codigoB2)
B2.place(relx = 0.20, rely = 0.3)
B2.grid(column=1, row=1)

B3 = Button(miFrame, text=texto_boton, command=codigoB3)
B3.place(relx = 0.35, rely = 0.3)
B3.grid(column=2, row=1)

# ------ A Fila 2 -----    
B4 = Button(miFrame, text=texto_boton, command=codigoB4)
B4.place(relx = 0.05, rely = 0.3)
B4.grid(column=0, row=2)

B5 = Button(miFrame, text=texto_boton, command=codigoB5)
B5.place(relx = 0.20, rely = 0.3)
B5.grid(column=1, row=2)

B6 = Button(miFrame, text=texto_boton, command=codigoB6)
B6.place(relx = 0.35, rely = 0.3)
B6.grid(column=2, row=2)

# ------ A Fila 3 -----    
B7 = Button(miFrame, text=texto_boton, command=codigoB7)
B7.place(relx = 0.05, rely = 0.3)
B7.grid(column=0, row=3)

B8 = Button(miFrame, text=texto_boton, command=codigoB8)
B8.place(relx = 0.20, rely = 0.3)
B8.grid(column=1,row=3)

B9 = Button(miFrame, text=texto_boton, command=codigoB9)
B9.place(relx = 0.35, rely = 0.3)
B9.grid(column=2, row=3)







# RESULTADO JUEGO

def marcador():
#    print("marcador")
    
    global resultados
    
    global linea1
    global linea2
    global linea3
    global linea4
    global linea5
    global linea6
    global linea7
    global linea8

    
    # lineas analisis
    linea1 = (resultados[0],resultados[1], resultados[2])
    linea2 = (resultados[3],resultados[4], resultados[5])
    linea3 = (resultados[6],resultados[7], resultados[8])
    linea4 = (resultados[0],resultados[3], resultados[6])
    linea5 = (resultados[1],resultados[4], resultados[7])
    linea6 = (resultados[2],resultados[5], resultados[8])
    linea7 = (resultados[0],resultados[4], resultados[8])
    linea8 = (resultados[2],resultados[4], resultados[6])   
    
    todas_lineas =[linea1, linea2, linea3, linea4, linea5, linea6, linea7, linea8]

    for linea in todas_lineas:
#        print(linea)
        
        datoAA = 0
        datoBB = 0
        
        for posicion in linea:
            if posicion == AA:
                datoAA += 1 
#            print(datoAA)
            
            if datoAA == 3:
#                print("Gana AA")
                pantalla.insert(0, "Gana AA")
#            print(datoAA)            
            
            
            if posicion == BB:
                datoBB += 1
#            print(datoBB)
            
            if datoBB == 3:
#                print("Gana BB")
                pantalla.insert(0, "Gana BB")
#            print(datoBB)
            



raiz.geometry('192x212')

raiz.mainloop()
