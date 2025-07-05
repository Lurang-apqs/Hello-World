#functions
# block of code to do a specific task
# if u hit m1 button on mouse , the gun should fire a bullet

#definition of function
# def fire():
#     print("i just shot")

# #calling the function
# fire()

def takeDamageAfterShooting(x,y):
    x -= y
    print("Lurang health after shot:"  + str(x))

lurangHealth = 100

gunDamage = 20
print("Lurang helath before shot: "  + str(lurangHealth))
takeDamageAfterShooting(lurangHealth,gunDamage)



