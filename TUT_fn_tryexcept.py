def calc_risk(age,income):
    risk=income/age
    return risk 


try:
    age=int(input("Enter age: "))
    income=int(input("Enter income: "))
    print(calc_risk(age,income))
except ValueError:
    print("WARNING: Invalid value") 
except ZeroDivisionError:
    print("WARNING: Age cannot be zero")

