while True:
    try: 
        number = int(input("please enter a number: "))
        print(f"you have entered: {number}")
        n = 1/number
    except ValueError:
        print("Please enter valid value")
    except ZeroDivisionError:
        print("Please enter number above 0")
    else:
        print(f"result: {n}")
    finally:
        print("In the final block")
