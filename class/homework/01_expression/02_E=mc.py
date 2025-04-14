light_speed : int = 299792458

def main():
    mass: float = float(input("Enter kilos of mass: "))

    energy : float = mass * (light_speed ** 2)

    
    print("e = m * C^2...")
    print(f"m = {str(mass)} kg")
    print(f"C = {str(light_speed)}m/s")
    
    print(str(energy) + " joules of energy!")



if __name__ == '__main__':
    main()