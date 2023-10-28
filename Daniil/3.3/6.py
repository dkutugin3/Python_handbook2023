{a: text.lower().count(a) for a in set(text.replace(" ", "").lower()) if a.isalpha()}
