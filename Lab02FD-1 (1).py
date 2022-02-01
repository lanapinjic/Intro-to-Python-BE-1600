#Falling Distance, d=1/2*g*(t**2) d=distance, g=9.8, t=time in seconds 

def falling_distance (t):
    distance = 0.5 * 9.8 * (t**2)
    print("Falling distance for an object that has been falling for",t,"seconds is", distance, "meters")


t = int(input(" Enter the duration of time that the object is falling "))
falling_distance(t)

                 
    
    
