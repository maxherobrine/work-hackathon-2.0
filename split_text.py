import re

'''
text = """Член бригады ресторана
Обязанности (МакКафе):
- открытое и эффективное общение с посетителем;
- правильное приготовления горячих или холодных напитков, десертов и выпечки;
- поддержание безупречного порядка и чистоты;
- авторское оформление витрины.

Обязанности (Макдоналдс):
- открытое и эффективное общение с посетителем;
- предугадывание желаний посетителя (консультирование и помощь в выборе продукции и т.д.)"""

text2 = 'и т.д. и т.п.'
text3 = 'а.б.в.г.д. лол'
text1 = 'А.Б.В.Г., lол'
'''
def split_text(text: str):
    i=0
    cout = 0
    size = len(text)
    while i < size:
        if text[i] == ' ' and i < size-3:
            if text[i+1].isalpha() and text[i + 2] == '.':
                text = text[:(i + 2)] + text[(i + 3):]
                size -= 1
            else:
                i+=1
        elif text[i] == '.' and i < size-1:
            cout= 0
            if i < size-1 and text[i+1].isupper():
                text = text[:(i)] + text[(i + 1):]
                size -= 1
            else:
                while i < size-1 and not text[i].isalpha():
                    cout +=1
                    i += 1
                    if i == (size - 1):
                        text = text[:(i - cout)] + text[(i - cout + 1):]
                        size -= 1
                if i < size-1 and text[i].islower():
                    text = text[:(i - cout)] + text[(i - cout + 1):]
                    size -=1
                    i = i - cout + 1
        else:
            i+=1

    split_regex = re.compile(r'[.!?…]')
    sentences = [t for t in split_regex.split(text)]
    return sentences

'''
print(merge_reduction(text3))
print(merge_reduction(text2))
print(merge_reduction(text1))
#print(merge_reduction(text))
'''