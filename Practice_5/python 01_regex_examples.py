#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practice 5: Python Regular Expressions
Задание 2.1: Примеры всех функций модуля re (W3Schools)
"""

import re


def example_search():
    """re.search() - находит первое совпадение"""
    print("=" * 60)
    print("1. re.search() - Поиск первого совпадения")
    print("=" * 60)
    
    text = "Цена товара: 154,00 тенге, скидка 10%"
    
    # Поиск цены
    match = re.search(r'\d+,\d{2}', text)
    print(f"Текст: {text}")
    print(f"Паттерн: \\d+,\\d{{2}}")
    print(f"Результат: {match.group() if match else 'Не найдено'}")
    print(f"Позиция: {match.span() if match else 'N/A'}")
    print()


def example_findall():
    """re.findall() - находит все совпадения"""
    print("=" * 60)
    print("2. re.findall() - Поиск всех совпадений")
    print("=" * 60)
    
    text = "Товары: 154,00 тг, 51,00 тг, 32,00 тг, 120,00 тг"
    
    prices = re.findall(r'\d+,\d{2}', text)
    print(f"Текст: {text}")
    print(f"Паттерн: \\d+,\\d{{2}}")
    print(f"Все цены: {prices}")
    print(f"Количество: {len(prices)}")
    print()


def example_match():
    """re.match() - проверяет совпадение в начале строки"""
    print("=" * 60)
    print("3. re.match() - Совпадение в начале строки")
    print("=" * 60)
    
    text1 = "ИТОГО: 18 009,00"
    text2 = "Чек ИТОГО: 18 009,00"
    
    match1 = re.match(r'ИТОГО', text1)
    match2 = re.match(r'ИТОГО', text2)
    
    print(f"Текст 1: '{text1}'")
    print(f"Паттерн: ИТОГО")
    print(f"Результат: {'✅ Найдено' if match1 else '❌ Не найдено'}")
    print()
    print(f"Текст 2: '{text2}'")
    print(f"Паттерн: ИТОГО")
    print(f"Результат: {'✅ Найдено' if match2 else '❌ Не найдено'}")
    print()


def example_split():
    """re.split() - разделение строки по паттерну"""
    print("=" * 60)
    print("4. re.split() - Разделение строки")
    print("=" * 60)
    
    text = "Натрия хлорид, 200 мл, фл, 154,00"
    
    parts = re.split(r',\s*', text)
    print(f"Текст: {text}")
    print(f"Паттерн: ,\\s*")
    print(f"Части: {parts}")
    print()


def example_sub():
    """re.sub() - замена подстрок"""
    print("=" * 60)
    print("5. re.sub() - Замена паттернов")
    print("=" * 60)
    
    text = "Чек №2331180266 от 18.04.2019"
    
    # Заменить дату
    masked = re.sub(r'\d{2}\.\d{2}\.\d{4}', '[DATE]', text)
    print(f"Оригинал: {text}")
    print(f"Паттерн: \\d{{2}}\\.\\d{{2}}\\.\\d{{4}}")
    print(f"Замена: [DATE]")
    print(f"Результат: {masked}")
    print()
    
    # Заменить номер чека
    masked2 = re.sub(r'№\d+', '№XXXX', text)
    print(f"Результат 2: {masked2}")
    print()


def example_metacharacters():
    """Мета-символы RegEx"""
    print("=" * 60)
    print("6. Мета-символы (. ^ $ * + ? [] {} | () \\)")
    print("=" * 60)
    
    text = "Цена 154,00 и 1 200,00 тенге"
    
    patterns = [
        (r'Ц.*а', "Ц...а (любые символы между)"),
        (r'^Цена', "^Цена (начало строки)"),
        (r'тенге$', "тенге$ (конец строки)"),
        (r'\d+', "\\d+ (одна или более цифр)"),
        (r'\d{3}', "\\d{3} (ровно 3 цифры)"),
        (r'[0-9]+', "[0-9]+ (цифры из набора)"),
    ]
    
    for pattern, description in patterns:
        matches = re.findall(pattern, text)
        print(f"{description}: {matches}")
    print()


def example_special_sequences():
    """Специальные последовательности"""
    print("=" * 60)
    print("7. Спец-последовательности (\\d \\w \\s \\D \\W \\S)")
    print("=" * 60)
    
    text = "Чек №2331180266 18.04.2019 11:13:58"
    
    sequences = [
        (r'\d+', "\\d+ - все цифры"),
        (r'\D+', "\\D+ - всё кроме цифр"),
        (r'\w+', "\\w+ - слова (буквы, цифры, _)"),
        (r'\W+', "\\W+ - не слова (пробелы, знаки)"),
        (r'\s+', "\\s+ - пробельные символы"),
        (r'\S+', "\\S+ - всё кроме пробелов (первые 5)"),
    ]
    
    for pattern, description in sequences:
        matches = re.findall(pattern, text)
        if pattern == r'\S+':
            matches = matches[:5]  # Показать только первые 5
        print(f"{description}: {matches}")
    print()


def example_quantifiers():
    """Квантификаторы"""
    print("=" * 60)
    print("8. Квантификаторы (* + ? {n} {n,} {n,m})")
    print("=" * 60)
    
    text = "Товары: 1, 12, 123, 1234, 12345"
    
    quantifiers = [
        (r'\d*', "\\d* - 0 или более цифр (первые 5)"),
        (r'\d+', "\\d+ - 1 или более цифр"),
        (r'\d?', "\\d? - 0 или 1 цифра (первые 10)"),
        (r'\d{3}', "\\d{3} - ровно 3 цифры"),
        (r'\d{2,}', "\\d{2,} - 2 или более цифр"),
        (r'\d{2,4}', "\\d{2,4} - от 2 до 4 цифр"),
    ]
    
    for pattern, description in quantifiers:
        matches = re.findall(pattern, text)
        if pattern in [r'\d*', r'\d?']:
            matches = matches[:10]
        print(f"{description}: {matches}")
    print()


def example_flags():
    """Флаги RegEx"""
    print("=" * 60)
    print("9. Флаги (IGNORECASE, MULTILINE, DOTALL)")
    print("=" * 60)
    
    text = """итого: 18 009,00
ИТОГО: 18 009,00
Итого: 18 009,00"""
    
    # Без флага
    matches1 = re.findall(r'ИТОГО', text)
    print(f"Без флага (ИТОГО): {len(matches1)} совпадений")
    
    # С IGNORECASE
    matches2 = re.findall(r'ИТОГО', text, re.IGNORECASE)
    print(f"С re.IGNORECASE: {len(matches2)} совпадений")
    print()
    
    # MULTILINE пример
    text2 = "Первая строка\nВторая строка\nТретья строка"
    matches3 = re.findall(r'^Вторая', text2, re.MULTILINE)
    print(f"MULTILINE (^Вторая): {matches3}")
    print()


def example_character_classes():
    """Наборы символов"""
    print("=" * 60)
    print("10. Наборы символов ([abc] [^abc] [a-z])")
    print("=" * 60)
    
    text = "Товары: A, B, C, 1, 2, 3, +, -, *"
    
    classes = [
        (r'[ABC]', "[ABC] - буквы A, B или C"),
        (r'[^ABC]', "[^ABC] - всё кроме A, B, C (первые 10)"),
        (r'[0-9]', "[0-9] - любая цифра"),
        (r'[А-Я]', "[А-Я] - кириллические заглавные"),
        (r'[а-я]', "[а-я] - кириллические строчные (первые 10)"),
    ]
    
    for pattern, description in classes:
        matches = re.findall(pattern, text)
        if '[^ABC]' in pattern or '[а-я]' in pattern:
            matches = matches[:10]
        print(f"{description}: {matches}")
    print()


def example_groups():
    """Группы и захват"""
    print("=" * 60)
    print("11. Группы () и захват данных")
    print("=" * 60)
    
    text = "2,000 x 154,00 = 308,00"
    
    # Захват количества, цены и суммы
    pattern = r'(\d+,\d{3})\s*x\s*(\d+,\d{2})\s*=\s*(\d+,\d{2})'
    match = re.search(pattern, text)
    
    if match:
        print(f"Текст: {text}")
        print(f"Паттерн: (\\d+,\\d{{3}})\\s*x\\s*(\\d+,\\d{{2}})...")
        print(f"Вся строка: {match.group(0)}")
        print(f"Группа 1 (кол-во): {match.group(1)}")
        print(f"Группа 2 (цена): {match.group(2)}")
        print(f"Группа 3 (сумма): {match.group(3)}")
    print()


def main():
    """Запуск всех примеров"""
    print("\n" + "📚" * 30)
    print("   PRACTICE 5: PYTHON REGULAR EXPRESSIONS")
    print("   Задание 2.1: Примеры функций модуля re")
    print("📚" * 30 + "\n")
    
    example_search()
    example_findall()
    example_match()
    example_split()
    example_sub()
    example_metacharacters()
    example_special_sequences()
    example_quantifiers()
    example_flags()
    example_character_classes()
    example_groups()
    
    print("=" * 60)
    print("✅ Все примеры RegEx функций выполнены!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()