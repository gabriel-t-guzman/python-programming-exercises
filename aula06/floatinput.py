import math

def floatInput(prompt, mini=0, maxi=100):
    assert mini < maxi
    try:
        res = float(input(prompt))
        if mini>res or res>maxi:
            raise ValueError("out")
        return res
    except ValueError as e:
        if "out" in str(e):
             if mini > res: maxi = +math.inf;print(f"Error: Value should be in [{mini},{maxi}]");return floatInput(prompt,mini,maxi)
             if maxi < res: mini = -math.inf;print(f"Error: Value should be in [{mini},{maxi}]");return floatInput(prompt,mini,maxi)
        else: 
            print(f"ERROR: Not a float!")
            return floatInput(prompt,mini,maxi)



def main():
    print("a) Try entering invalid values such as 1/2 or 3,1416.")
    v = floatInput("Value? ")
    print("v:", v)

    print("b) Try entering invalid values such as 15%, 110 or -1.")
    h = floatInput("Humidity (%)? ", 0, 100)
    print("h:", h)

    print("c) Try entering invalid values such as 23C or -274.")
    t = floatInput("Temperature (Celsius)? ", mini=-273.15)
    print("t:", t)

   # d) What happens if you uncomment this?
   # impossible = floatInput("Value in [3, 0]? ", mini=3, maxi=0)

    return

if __name__ == "__main__":
    main()
