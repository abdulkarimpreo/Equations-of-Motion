# Motion Calculator using equations of motion

def final_velocity(u, a, t):
    return (u+(a*t))

def distance(u, a, t):
    return ((u*t)+(0.5*a*(t**2)))

def find_velocity_square(u, a, s):
    return  ((u**2)+2*a*s)

print("<<< Motion Calculator >>>")
print("1. Find final velocity (v = u + at)")
print("2. distance (s = ut + 1/2 * a *t^2)")
print("3. Find velocity squared (v^2 = u^2 + 2as)")

choice = int(input("Enter yout choice (1-3): "))

if choice == 1:
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    t = float(input("Enter time (t): "))
    print(f"Final velocity (v) = {final_velocity(u, a, t)} m/s")

elif choice == 2:
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    t = float(input("Enter time (t): "))
    print(f"Distance (s) = {distance(u, a, t)} m")

elif choice == 3:
    u = float(input("Enter initial velocity (u): "))
    a = float(input("Enter acceleration (a): "))
    s = float(input("Enter distance (s): "))
    print(f" v**2 = {find_velocity_square(u, a, s)}")

else:
    print("Invalid choice!")
