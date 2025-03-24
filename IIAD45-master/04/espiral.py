import turtle

miTortuga = turtle.Turtle()
miVentana = turtle.Screen()

def dibujarEspiral(miTortuga, longitudLinea):
    if longitudLinea > 0:
        miTortuga.forward(longitudLinea)
        miTortuga.right(45)
        dibujarEspiral(miTortuga,longitudLinea-5)

miTortuga.penup()
miTortuga.goto(-80,200)
miTortuga.pendown()
miTortuga.shape("turtle")

dibujarEspiral(miTortuga,120)

miVentana.exitonclick()