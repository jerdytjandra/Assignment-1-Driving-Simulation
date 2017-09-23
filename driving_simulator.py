print("Hello, welcome to the driving simulator.")
print("\n" +"loading...")
print("\n" +"Let us begin!")

print("\n" + "Initial Velocity: 0  m/s" )
print( "Speed Limit:      60 m/s")

u=0
t=int(input("\n" +"Enter the time:"))
a=int(input("Enter the acceleration:"))
d=int(input("Enter the distance:"))

##Equation##
v   = u + a*t
s   = t*(v+u)/2

print("\n" + "You are driving from A to B 0...")
print("\n" + "(The * indicates every 10 m)")

for i in range (t + 1):
    b= (a/2)*(i**2)
    print("Duration: " + str(i) + " Distance: "+ '*' * int(b/10))

if s>d:
    print("\n" + "You have reached your destination.")
    print("\t" + "Your maximum speed was: " + str(s) +"m")
else  :
    print("\n" + "You did not reach your destination.")
    print("\t" + "Your maximum speed was:" + str(s) +"m")

if v >= 60:
    print("\n" + "You went over the speed limit.")
    print("\t" + "You reached a maximum speed of: " + str(v) + "m/s")
elif v < 60:
    print("\n" + "You did not go over the speed limit.")
    print("\t" + "You reached a maximum speed of: " + str(v) + "m/s")

