
dict_symbols_cyr = {
    'А': 'a',
    'Б': 'b',
    'В': 'w',
    'Г': 'g',
    'Д': 'd',
    'Е': 'e',
    'Ё': 'e',
    'Ж': 'v',
    'З': 'z',
    'И': 'i',
    'Й': 'j',
    'К': 'k',
    'Л': 'l',
    'М': 'm',
    'Н': 'n',
    'О': 'o',
    'П': 'p',
    'Р': 'r',
    'С': 's',
    'Т': 't',
    'У': 'u',
    'Ф': 'f',
    'Х': 'h',
    'Ц': 'c',
    'Ч': '~',
    'Ш': '{',
    'Щ': '}',
    'Ъ': 'x',
    'Ы': 'y',
    'Ь': 'x',
    'Э': '|',
    'Ю': '\'',
    'Я': 'q',
    'а': 'A',
    'б': 'B',
    'в': 'W',
    'г': 'G',
    'д': 'D',
    'е': 'E',
    'ё': 'E',
    'ж': 'V',
    'з': 'Z',
    'и': 'I',
    'й': 'J',
    'к': 'K',
    'л': 'L',
    'м': 'M',
    'н': 'N',
    'о': 'O',
    'п': 'P',
    'р': 'R',
    'с': 'S',
    'т': 'T',
    'у': 'U',
    'ф': 'F',
    'х': 'H',
    'ц': 'C',
    'ч': '^',
    'ш': '[',
    'щ': ']',
    'ъ': 'X',
    'ы': 'Y',
    'ь': 'X',
    'э': '\\',
    'ю': '@',
    'я': 'Q',
}


class CharsetEncoder():
    def __init__(self):
        pass

    def encode_message(self, message):
        result = message
        for cyr_symbol, lat_symbol in dict_symbols_cyr.items():
            result = result.replace(cyr_symbol, lat_symbol)
        return result
