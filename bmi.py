def calculater(height, weight):   
    return (weight/(height**2))

def data(height, weight):
    if(height > 5):
         height /= 100

    if(height <= 0) or (weight <= 0):
        return f"Incorrect information entry, try again!"
    
    value = calculater(height, weight)
    print(value)
    
    if(value < 18.5):
        return f"You are underweight.\nYour BMI:{value}"
        
    elif(18.5 <= value < 25):
        return f"You are healthy weight.\nYour BMI:{value}"
        
    elif(25 <= value < 30):
        return f"You are overweight.\nYour BMI:{value}"
        
    elif(30 <= value):
        return f"You are obese.\nYour BMI:{value}"
        
    else:
        return f"Incorrect information entry, try again."