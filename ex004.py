var = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(var))
print('A palavra {} só tem espaços?'.format(var), var.isspace())
print('O {} um número?'.format(var), var.isnumeric())
print('É alfabetico?', var.isalpha())
print('É alfanumérico?', var.isalnum())
print('Está em maiusculas?', var.isupper())
print('Está em minusculas?', var.islower())
print('Está capitalizada?', var.istitle())
