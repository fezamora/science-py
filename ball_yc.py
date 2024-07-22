#import math
import fileball 
v0 = float(input("Ingrese velocidad inicial (m/s): "))
t = float(input("Ingrese el tiempo en el que desea analizar (segundos): "))

yc = fileball.height_ball(v0,t)

t1,t2 = fileball.time_ball(v0,yc)    

print("En t = %.2f s, la altura es %.2f m." % (t,yc))
print("En t = %.2f s y t=%.2f s, la altura es %.2f m."%(t1,t2,yc))