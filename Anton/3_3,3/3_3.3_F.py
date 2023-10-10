{str(letter): text.lower().count(letter) for letter in sorted(text.lower()) if ord(letter) > 64}
