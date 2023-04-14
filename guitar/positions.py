#script 
xmax = 1000 
ymax = 1400
xmin = int(- xmax//2)
ymin = int(- ymax//2)
x_values = {}
y_values = {}
for i in range(xmax+1):
    x_values[i] = xmin
    xmin += 1
for i in range(ymax+1):
    y_values[i] = ymin
    ymin += 1

def get_turtle_position(x,y):
    return (x_values[int(x)] * 0.5, - y_values[int(y)] * 0.5)