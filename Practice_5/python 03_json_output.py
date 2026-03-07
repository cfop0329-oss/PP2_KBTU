#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practice 5: Python Regular Expressions
Задание 2.2 (доп.): Работа с JSON выводом
"""

import json
from datetime import datetime


def load_parsed_data(filename='parsed_receipt.json'):
    """Загрузка распарсенных данных"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Файл {filename} не найден!")
        print("💡 Сначала запустите 02_receipt_parser.py")
        return None


def display_summary(data):
    """Краткая сводка"""
    print("\n" + "=" * 60)
    print("           КРАТКАЯ СВОДКА ПО ЧЕКУ")
    print("=" * 60 + "\n")
    
    print(f"🏪 Магазин: {data['store_info']['name']}")
    print(f"📅 Дата: {data['date_time']['date']}")
    print(f"🛒 Товаров: {data['products_count']}")
    print(f"💰 Сумма: {data['total']:.2f} ₸")
    print(f"💳 Оплата: {data['payment']['method']}")
    print()


def calculate_statistics(data):
    """Статистика по товарам"""
    print("=" * 60)
    print("           СТАТИСТИКА ПО ТОВАРАМ")
    print("=" * 60 + "\n")
    
    products = data['products']
    
    if not products:
        print("Нет данных о товарах")
        return
    
    # Самый дорогой товар
    most_expensive = max(products, key=lambda x: x['price_per_unit'])
    print(f"💎 Самый дорогой: {most_expensive['name'][:40]}")
    print(f"   Цена: {most_expensive['price_per_unit']:.2f} ₸")
    
    # Самый дешёвый
    cheapest = min(products, key=lambda x: x['price_per_unit'])
    print(f"\n💰 Самый дешёвый: {cheapest['name'][:40]}")
    print(f"   Цена: {cheapest['price_per_unit']:.2f} ₸")
    
    # Средняя цена
    avg_price = sum(p['price_per_unit'] for p in products) / len(products)
    print(f"\n📊 Средняя цена: {avg_price:.2f} ₸")
    
    # Общее количество единиц
    total_qty = sum(p['quantity'] for p in products)
    print(f"📦 Всего единиц: {total_qty:.3f}")
    print()


def export_to_csv(data, filename='receipt_summary.csv'):
    """Экспорт товаров в CSV"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("№,Название,Количество,Цена,Сумма\n")
        for p in data['products']:
            name = p['name'].replace(',', ';')  # Замена запятых
            f.write(f"{p['number']},{name},{p['quantity']},{p['price_per_unit']},{p['total']}\n")
    
    print(f"✅ Экспортировано в {filename}")


def create_report(data, filename='receipt_report.txt'):
    """Создание текстового отчёта"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("           ОТЧЁТ ПО ЧЕКУ\n")
        f.write("=" * 60 + "\n\n")
        
        f.write(f"Дата генерации: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Магазин: {data['store_info']['name']}\n")
        f.write(f"Дата покупки: {data['date_time']['datetime']}\n\n")
        
        f.write("ТОВАРЫ:\n")
        f.write("-" * 60 + "\n")
        for p in data['products']:
            f.write(f"{p['number']}. {p['name']}\n")
            f.write(f"   {p['quantity']} x {p['price_per_unit']:.2f} = {p['total']:.2f} ₸\n")
        
        f.write("\n" + "-" * 60 + "\n")
        f.write(f"ИТОГО: {data['total']:.2f} ₸\n")
        f.write(f"Оплата: {data['payment']['method']}\n")
        f.write("=" * 60 + "\n")
    
    print(f"✅ Отчёт создан: {filename}")


def main():
    """Точка входа"""
    print("\n📊 Обработка распарсенных данных...\n")
    
    data = load_parsed_data()
    
    if data:
        display_summary(data)
        calculate_statistics(data)
        export_to_csv(data)
        create_report(data)
        
        print("\n✅ Все файлы созданы успешно!\n")
    else:
        print("❌ Не удалось загрузить данные")


if __name__ == "__main__":
    main()