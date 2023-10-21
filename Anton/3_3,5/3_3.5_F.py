def solution():
    rule = {'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'е': 'e',
            'ё': 'e',
            'ж': 'zh',
            'з': 'z',
            'и': 'i',
            'й': 'i',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'kh',
            'ц': 'tc',
            'ч': 'ch',
            'ш': 'sh',
            'щ': 'shch',
            'ъ': '',
            'ы': 'y',
            'ь': '',
            'э': 'e',
            'ю': 'iu',
            'я': 'ia',
            ' ': ' '}
    with open("cyrillic.txt", "r", encoding="UTF-8") as file:
        text = file.read()
        res = ''
        for char in text:
            if char.lower() in rule.keys():
                if char.isupper():
                    res += rule[char.lower()].capitalize()
                else:
                    res += rule[char]
            else:
                res += char
        with open("transliteration.txt", "w", encoding="UTF-8") as out:
            out.write(res)


def main():
    solution()


if __name__ == "__main__":
    main()
