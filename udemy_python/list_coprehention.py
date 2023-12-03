celcius = [1,2,3,4,5,6]
# ini list coprehention
farenheit = [((9/5)*i+32) for i in celcius]
print(farenheit)
# ini dibagi dengan modulus
farenheit = [((9/5)*i+32) for i in celcius if i%2==1]
print(farenheit)