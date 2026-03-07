#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practice 5: Python Regular Expressions
Задание 2.2: Парсер чеков EUROPHARMA (Казахстан)
"""

import re
import json
from datetime import datetime


class ReceiptParser:
    """Класс для парсинга чеков"""
    
    def __init__(self, filename='raw.txt'):
        self.filename = filename
        self.content = None
        self.data = {}
    
    def load_file(self):
        """Загрузка файла чека"""
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                self.content = file.read()
            return True
        except FileNotFoundError:
            print(f"❌ Файл {self.filename} не найден!")
            return False
        except Exception as e:
            print(f"❌ Ошибка чтения: {e}")
            return False
    
    def extract_store_info(self):
        """Информация о магазине"""
        info = {'name': None, 'bin': None, 'address': None, 'cashier': None}
        
        # Название
        match = re.search(r'Филиал\s+(.+?)(?:\n|$)', self.content)
        if match:
            info['name'] = match.group(1).strip()
        
        # БИН
        match = re.search(r'БИН\s+(\d+)', self.content)
        if match:
            info['bin'] = match.group(1)
        
        # Адрес
        match = re.search(r'г\.\s*([^,\n]+),([^,\n]+),\s*([^,\n]+)', self.content)
        if match:
            info['address'] = f"г. {match.group(1).strip()}, {match.group(2).strip()}, {match.group(3).strip()}"
        
        # Кассир
        match = re.search(r'Кассир\s+(.+?)(?:\n|$)', self.content)
        if match:
            info['cashier'] = match.group(1).strip()
        
        return info
    
    def extract_date_time(self):
        """Дата и время"""
        info = {'date': None, 'time': None, 'datetime': None}
        
        match = re.search(r'Время:\s*(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', self.content)
        if match:
            info['date'] = match.group(1)
            info['time'] = match.group(2)
            info['datetime'] = f"{match.group(1)} {match.group(2)}"
        
        return info
    
    def extract_products(self):
        """Товары из чека"""
        products = []
        
        # Паттерн для многострочного блока товара
        pattern = r'(\d+)\.\s*\n([^\n]+(?:\n[^\n]+)*?)\n\s*([\d\s]+,\d{3})\s*x\s*([\d\s]+,\d{2})\s*\n\s*([\d\s]+,\d{2})'
        
        matches = re.findall(pattern, self.content, re.MULTILINE)
        
        for match in matches:
            num, name, qty, price, total = match
            
            products.append({
                'number': int(num),
                'name': name.strip(),
                'quantity': float(qty.replace(' ', '').replace(',', '.')),
                'price_per_unit': float(price.replace(' ', '').replace(',', '.')),
                'total': float(total.replace(' ', '').replace(',', '.'))
            })
        
        return products
    
    def extract_total(self):
        """Итоговая сумма"""
        match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', self.content)
        if match:
            return float(match.group(1).replace(' ', '').replace(',', '.'))
        return None
    
    def extract_payment(self):
        """Способ оплаты"""
        info = {'method': None, 'amount': None}
        
        match = re.search(r'Банковская карта:\s*([\d\s]+,\d{2})', self.content)
        if match:
            info['method'] = 'Банковская карта'
            info['amount'] = float(match.group(1).replace(' ', '').replace(',', '.'))
        
        return info
    
    def extract_tax(self):
        """НДС"""
        match = re.search(r'в т\.ч\.\s*НДС\s*(\d+)%:\s*([\d\s]+,\d{2})', self.content)
        if match:
            return {
                'rate': int(match.group(1)),
                'amount': float(match.group(2).replace(' ', '').replace(',', '.'))
            }
        return None
    
    def extract_receipt_numbers(self):
        """Номера чека и фискальные данные"""
        info = {}
        
        patterns = {
            'receipt_number': r'Чек\s*№?(\d+)',
            'order_number': r'Порядковый номер чека\s*№?(\d+)',
            'fiscal_sign': r'Фискальный признак:\s*(\d+)',
            'kassa': r'Касса\s+([\d\-]+)',
            'shift': r'Смена\s+(\d+)'
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, self.content)
            if match:
                info[key] = match.group(1)
        
        return info
    
    def parse(self):
        """Основной метод парсинга"""
        if not self.load_file():
            return None
        
        products = self.extract_products()
        
        self.data = {
            'store_info': self.extract_store_info(),
            'date_time': self.extract_date_time(),
            'receipt_numbers': self.extract_receipt_numbers(),
            'products': products,
            'products_count': len(products),
            'subtotal': sum([p['total'] for p in products]) if products else 0,
            'total': self.extract_total(),
            'tax': self.extract_tax(),
            'payment': self.extract_payment(),
            'parsed_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        return self.data
    
    def display(self):
        """Вывод результатов"""
        if not self.data:
            print("❌ Нет данных")
            return
        
        print("\n" + "🧾" * 30)
        print("       РЕЗУЛЬТАТЫ ПАРСИНГА ЧЕКА")
        print("🧾" * 30 + "\n")
        
        # Магазин
        store = self.data['store_info']
        print("🏪 МАГАЗИН:")
        if store['name']:
            print(f"   {store['name']}")
        if store['bin']:
            print(f"   БИН: {store['bin']}")
        
        # Дата
        dt = self.data['date_time']
        print(f"\n📅 Дата: {dt['date']}")
        print(f"🕐 Время: {dt['time']}")
        
        # Товары
        print(f"\n🛒 Товары ({self.data['products_count']} шт.):")
        for p in self.data['products'][:5]:  # Первые 5
            print(f"   {p['number']}. {p['name'][:40]}... {p['total']:.2f} ₸")
        if self.data['products_count'] > 5:
            print(f"   ... и ещё {self.data['products_count'] - 5} товаров")
        
        # Итого
        print(f"\n💰 ИТОГО: {self.data['total']:.2f} ₸")
        
        # Оплата
        if self.data['payment']['method']:
            print(f"💳 Оплата: {self.data['payment']['method']}")
        
        print("\n" + "🧾" * 30 + "\n")
    
    def save_json(self, filename='parsed_receipt.json'):
        """Сохранение в JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print(f"✅ Сохранено в {filename}")


def main():
    """Точка входа"""
    print("\n🔍 Парсинг чека EUROPHARMA...\n")
    
    parser = ReceiptParser('raw.txt')
    data = parser.parse()
    
    if data:
        parser.display()
        parser.save_json()
    else:
        print("❌ Ошибка парсинга")


if __name__ == "__main__":
    main()