import math

numero_A = int(input("Fala um número como a:"))

numero_B = int(input("Fale um número como b:"))

numero_C = int(input("Fale um número como c:"))

delta = (numero_B ** 2) - 4 * (numero_A * numero_C)

if delta > 0:
    bhaskara = ((-numero_B) + math.sqrt(delta)) / 2 * numero_A
    bhaskara2 = ((-numero_B) - math.sqrt(delta)) / 2 * numero_A
    print("Duas Raízes: ", int(bhaskara), int(bhaskara2), sep=',')

elif delta == 0:
    bhaskara =(-numero_B) / (2 * numero_A)
    print("Uma raiz real:", int(bhaskara))

else:
    print("Sem raízes reais!")

// 

import math

number_A = int(input("Choose a number to be A:"))

number_B = int(input("Choose a number to be B:"))

number_C = int(input("Choose a number to be C:"))

delta = (number_B ** 2) - 4 * (number_A * number_C)

if delta > 0:
    bhaskara = ((-number_B) + math.sqrt(delta)) / 2 * number_A
    bhaskara2 = ((-number_B) - math.sqrt(delta)) / 2 * number_A
    print("Two solutions: ", int(bhaskara), int(bhaskara2), sep=',')
  
  elif delta == 0:
    bhaskara =(-number_B) / (2 * number_A)
    print("one float solution:", int(bhaskara))

else:
    print("No float solutions!")
