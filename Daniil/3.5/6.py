slov = {'а': 'a',
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


def format_string(s: str):
    ans = ""
    for i in s:
        if i.lower() in slov:
            if i.isupper():
                ans += slov[i.lower()].capitalize()
            else:
                ans += slov[i]
        else:
            ans += i
    return ans


with open("cyrillic.txt", encoding="utf-8", mode="r") as read_file:
    with open("transliteration.txt", encoding="utf-8", mode="w") as write_file:
        data = [format_string(i) for i in read_file.readlines()]
        write_file.writelines(data)
