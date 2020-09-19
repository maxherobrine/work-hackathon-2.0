
'''text = """Начальник склада , работаю больше года ,Работа в 1С , приемка и оформление товара на склад ,
отправка товара в регионы, наемными машинами и Ж.Д. поездами.Инвентаризация товара на складе ."""

text2 = 'и т.д. и т.п.'
text3 = 'а.б.в.г.д. лол'
text1 = 'А.Б.В.Г., lол'''



def merge_reduction(text: str):
    i = 0
    cout = 0
    size = len(text)
    while i < size:
        if text[i] == ' ':
            if text[i + 1].isalpha() and text[i + 2] == '.':
                text = text[:(i + 2)] + text[(i + 3):]
                size -= 1
            else:
                i += 1
        elif text[i] == '.' and i < size - 1:
            cout = 0
            if i < size - 1 and text[i + 1].isupper():
                if i < size-2:
                    if text[i + 2] == ' ' or text[i + 2] == '.':
                        text = text[:(i - cout)] + text[(i - cout + 1):]
                        size -= 1
                else:
                    text = text[:(i)] + text[(i + 1):]
                    size -= 1
                i+=1
            else:
                while i < size - 1 and not text[i].isalpha():
                    cout += 1
                    i += 1
                    if i == (size - 1):
                        text = text[:(i - cout)] + text[(i - cout + 1):]
                        size -= 1
                if i < size - 1 and text[i].islower():
                    text = text[:(i - cout)] + text[(i - cout + 1):]
                    size -= 1
                    i = i - cout + 1
        else:
            i += 1
    return text


'''print(merge_reduction(text3))
print(merge_reduction(text2))
print(merge_reduction(text1))

print(merge_reduction(text))'''