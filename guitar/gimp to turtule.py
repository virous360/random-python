import positions

list_output_gimp =(516.0, 970.0, 516.0, 970.0, 516.0, 970.0, 523.0, 969.0, 523.0, 969.0, 523.0, 969.0, 523.0, 1045.0, 523.0, 1045.0, 523.0, 1045.0, 516.0, 1045.0, 516.0, 1045.0, 516.0, 1045.0)



turtle_pos_list = []
#reformat as arrays of points
for i in range(0,len(list_output_gimp),2):
    xy=positions.get_turtle_position(list_output_gimp[i]//1,list_output_gimp[i+1]//1)
    turtle_pos_list.append(xy)

print(str(turtle_pos_list))
with open("out.txt","w") as f:
    f.write(str(set(turtle_pos_list)))
    