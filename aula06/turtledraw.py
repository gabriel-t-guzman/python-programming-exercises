# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle



def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    #put your code here
    """bol = True, planeaba usar el bol como variable para detectar t.up o t.down pero no hizo falta"""
    with open("drawing.txt", "r") as file: # abrir el archivo
        for line in file: # leer cada linea OJO si haces esto, y readline, cada linea se leera dos veces ocasionando salos de lectura
            line = line.rstrip() # un strip para eliminar espacios en blanco
            if line == "UP" : t.up();continue # un if que detecta el up y continua
            if line == "DOWN": t.down();continue # un if que detecta el down y continua
            line = line.split() #split para dividir los numeros recibidos de una lista
            x,y= float(line[0]),float(line[1]) # lista que asignamos a variables y tornamos floats
            print (x,y) # print para asegurar 
            t.goto(x,y) # moviminetos de la tortuga


        
    # Use t.up(), t.down() and t.goto(x, y)


    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()

