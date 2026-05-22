import turtle

# Fenêtre Turtle avec affichage de texte
screen = turtle.Screen()
screen.title("Texte")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Positionnement centré
pen.penup()
pen.goto(0, 60)
pen.write("Roméo AKLE ", align="center", font=("Arial", 24, "normal"))

pen.goto(0, 20)
pen.write("Eleve ingenieur à l'EPAC", align="center", font=("Arial", 18, "normal"))

# Laisse la fenêtre ouverte
turtle.done()


