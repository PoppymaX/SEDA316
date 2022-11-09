import random


if __name__ == "__main__":
    char_length = 1000000
    palabra = "cona"
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    output = []

    for i in range(char_length):
        selection = random.choice(abc)
        output.append(selection)

    output_2 = "".join(output)
    print(output_2)
    output_3 = output_2.replace(palabra, "|")
    quantity = output_3.count("|")
    print("Longitud de la seleccion aleatoria:", len(output))
    print("Numero de veces que la palabra '{}' aparecio en la seleccion aleatoria: {}".format(palabra, quantity))
