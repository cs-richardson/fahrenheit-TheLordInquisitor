# Prompt the user to input a celsius temperature and convert it to fahrenheit. 
# Program written by Son Nguyen

while True:

    try:
        
        celsiusTemp = float(input ("Please input a Celsius temperature: "))

        fahrenheitTemp = celsiusTemp * 9.0 / 5.0 + 32.0
        
        print(fahrenheitTemp,"º")
        
        break
    
    except:
        
        print("Please input a numerical value")



        

    
