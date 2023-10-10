s = input()
buff_num = s[0]
ms = []
buff_ms = []
for i in s:
    if i != buff_num:
        ms.append(buff_ms)
        buff_ms = []
        buff_num = i
    buff_ms.append(i)
ms.append(buff_ms)
for i in ms:
    print(i[0], len(i))
