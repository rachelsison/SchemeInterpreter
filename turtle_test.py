from turtle import *
"""
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
"""
penup()
setposition(-100, -100)
pendown()

def hax(side, depth):
	if depth < 0:
		return
	angle = 60
	angles = []
	positions = []
	for i in range(6):
		if i%2 == 0:
			positions.append(position())
			angles.append(heading())
		forward(side)
		left(angle)
	penup()
	setposition(positions[0])
	pendown()
	setheading(angles[0])
	hax((side/2), depth-1)

	penup()
	setposition(positions[1])
	pendown()
	setheading(angles[1])
	hax((side/2), depth-1)

	penup()
	setposition(positions[2])
	pendown()
	setheading(angles[2])
	hax((side/2), depth-1)

	return




	




