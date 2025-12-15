"""
Enunciado:

En este ejercicio práctico, aprenderás a utilizar el módulo itertools de Python, enfocándote
en la función product para generar combinaciones de contraseñas. Se te proveerá un conjunto
limitado de caracteres, incluyendo letras mayúsculas, minúsculas, dígitos y símbolos especiales.
Tu objetivo será utilizar estas letras para crear todas las posibles combinaciones de contraseñas
de una longitud específica.

Instrucciones:
    - Define una función generate_passwords() que acepte los siguientes parámetros: conjuntos de 
    caracteres que incluyan letras mayúsculas ('AZ'), letras minúsculas ('xy'), dígitos ('09') y
    símbolos especiales ('@#'), y la longitud deseada de las contraseñas.
    - Dentro de la función, utiliza la función product de itertools para generar todas las posibles 
    combinaciones de estos caracteres, formando contraseñas de la longitud especificada.
    - Convierte cada combinación de caracteres de las contraseñas generadas en una cadena y 
    almacénalas en una lista.
    - Retorna la lista de contraseñas generadas.
    - Fuera de la función, llama a generate_passwords() con los parámetros adecuados y almacena el 
    resultado.
    - Calcula y muestra el número total de contraseñas generadas.
    - Imprime las primeras 10 contraseñas de la lista para verificar tu solución.

Salida esperada:
    Number of passwords generated: 4096
    First 10 passwords generated: ['AAAA', 'AAAB', 'AAAC', 'AAAD', 'AAAx', 'AAAy', 'AAAz',
    'AAA0', 'AAA1', 'AAA2']
"""

import itertools
from typing import List


def generate_passwords(password_length: int) -> List[str]:
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'     
    digits = '0123456789'  
    special_symbols = '@#$%'
    uc_subset = uppercase_letters[0] + uppercase_letters[-1]
    lc_subset = lowercase_letters[-3:-1]
    digits_subset = digits[0] + digits[-1]
    special_subset = special_symbols[0:2]
    characters = uc_subset + lc_subset + digits_subset + special_subset
    possible_passwords = itertools.product(characters, repeat=password_length)
    password_list: List[str] = [''.join(password) for password in possible_passwords]
    return password_list
    


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    PASSWORD_LENGHT = 4
    password_list = generate_passwords(PASSWORD_LENGHT)
    print(f"Number of passwords generated: {len(password_list)}")
    print("First 10 passwords generated:", password_list[:10])
