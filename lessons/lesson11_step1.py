# Составные сообщения об ошибках
# Форматирование строк с помощью конкатенации

actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")
print('===============')

# Форматирование строк с помощью str.format
"Let's count together: {}, then goes {}, and then {}".format("one", "two", "three")
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
print('===============')

# Форматирование строк с помощью f-strings
# Пример 1:
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
print('===============')
# Пример 2:
actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")
print('===============')
# Пример 3:
print(f"{2+3}")
print('===============')

# # неправильно:
# assert self.catalog_link.text  == "Каталог", \
#     f"Wrong language, got {self.catalog_link.text} instead of 'Каталог'"
#
# # правильно:
# catalog_text = self.catalog_link.text # считываем текст и записываем его в переменную
# assert catalog_text == "Каталог", \
#     f"Wrong language, got {catalog_text} instead of 'Каталог'"

s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
