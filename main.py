# 1. Удалить пробелы и привести строку к нижнему регистру
# 2. Проверить строку на палиндром
# 3. Вернуть результат
# 4. Примеры использования

def is_palindrome(s: str) -> bool:
    # 1. Удалить пробелы и привести строку к нижнему регистру
    cleaned_string = ''.join(s.split()).lower()

    # 2. Проверить строку на палиндром
    reversed_string = cleaned_string[::-1]

    # 3. Вернуть результат
    return cleaned_string == reversed_string


# Примеры использования:
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello"))  # False
