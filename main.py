# Найти самое длинное слово в строке

# stroka = input("Введите строку: ")
# max_word = ''
# for word in stroka.split():
#     if len(word) > len(max_word):
#         max_word = word
# print(max_word)

# Преобразовать текст в кортеж слов с удалением знаков препинания и других небуквенных знаков

stroka = input("Введите строку: ")
symbols = '''!()-[]{};?@#$%:'"\,./^&amp;*_'''
for i in stroka:
    if i in symbols:
        stroka = stroka.replace(i, "")
print(tuple(stroka))





