import turtle
import time
import random

posponer = 0.1

#marcador
score = 0
high_score = 0

# configuración de ventana
wn = turtle.Screen()
wn.title("Un juego de mierda")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#snake head
cabeza = turtle.Turtle()
cabeza.speed(0)  #para que no se mueva en un principio
cabeza.shape("square")
cabeza.color("white")
cabeza.penup()
cabeza.goto(0,0) # para que la cabeza esté en el centro
cabeza.direction = "stop"

#Comida

comida = turtle.Turtle()
comida.speed(0)  
comida.shape("circle")
comida.color("yellow")
comida.penup()
comida.goto(0,100)

# segmentos/ cuerpo serpiente , o sea lista
segmentos = []


#texto marcador
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup() # para que no aparezca la plumita que pinta el texto
texto.hideturtle()
texto.goto(0,260)
texto.write("Score:0      High Score: 0", align = "center", font = ("Courier", 24,"normal"))


#Funciones

def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"	
def izquierda():
	cabeza.direction = "left"
def derecha():
	cabeza.direction = "right"

def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y + 20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y - 20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x - 20)
	
	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x + 20)			

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")					
wn.onkeypress(abajo, "Down")		
wn.onkeypress(derecha, "Right")		
wn.onkeypress(izquierda, "Left")		

while True:
	wn.update()

	#Colisiones bordes
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"

		#esconder cola de la serpiente o sea segmentos
		for segmento in segmentos:
			segmento.goto(1000,1000)
		#limpiar  lista de segmentos	
		segmentos.clear()

		#resetear marcador
		score = 0
		texto.clear()
		texto.write("Score:{}      High Score: {}".format(score, high_score),
				 align = "center", font = ("Courier", 24,"normal"))

    #colisiones comida
	if cabeza.distance(comida) < 20:
		x = random.randint(-280,280)
		y = random.randint(-280,280)
		comida.goto(x,y)

#nuevo segmento
		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)  
		nuevo_segmento.shape("square")
		nuevo_segmento.color("green")
		nuevo_segmento.penup()
		segmentos.append(nuevo_segmento)



		#aumentar marcador
		score += 10
		if score > high_score:
			high_score = score

			texto.clear()
			texto.write("Score:{}      High Score: {}".format(score, high_score),
				 align = "center", font = ("Courier", 24,"normal"))



		#mover el cuerpo de la serpiente
	totalSeg = len(segmentos)	
	for index in range(totalSeg -1, 0, -1):
		x = segmentos[index - 1].xcor()
		y = segmentos[index - 1].ycor()
		segmentos[index].goto(x,y)

	if totalSeg > 0:
		x = cabeza.xcor()
		y = cabeza.ycor()	
		segmentos[0].goto(x,y)
		
	
	mov()

	#colisiones con el cuerpo
	for segmento in segmentos:
		if segmento.distance(cabeza) < 20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"

			#esconder los segmentos
			for segmento in segmentos:
				segmento.goto(1000,1000)

			segmentos.clear()	

			#resetear marcador
			score = 0
			texto.clear()
			texto.write("Score:{}      High Score: {}".format(score, high_score),
				 align = "center", font = ("Courier", 24,"normal"))

	time.sleep(posponer)


turtle.mainloop()