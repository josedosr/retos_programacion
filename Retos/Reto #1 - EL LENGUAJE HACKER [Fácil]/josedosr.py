def leet_converter(text):

    leet = {"A": "4", "B": "I3", "C": "[", "D": ")", "E": "3", "F": "|=", "G": "&", "H": "#", "I": "1",
            "J": ",_|", "K": ">|", "L": "1", "M": "/\/\\", "N": " ^/", "O": "0", "P": " |*", "Q": "(_,)",
            "R": "I2", "S": "5", "T": "7", "U": "(_)", "V": "\/", "W": "\/\/", "X": "><", "Y": "j", "Z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
    
    text_converted = ''

    
    for char in text:
        if char.upper() in leet.keys():
            text_converted += leet[char.upper()]
        else:
            text_converted += char
    
    return text_converted

print(leet_converter("Leet"))
print(leet_converter("Aquí está un texto de prueba para ver si funciona el reto!"))
print(leet_converter(input("Texto a traducir: ")))
