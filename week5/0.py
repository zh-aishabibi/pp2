import re
import csv

with open('row.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'(\d+)\.\s*(.*?)\s+(\d+,\d+)\s*x\s*(\d+,\d+)'

results = re.findall(pattern, text)

with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order', 'name', 'quantity', 'price'])
    
    for result in results:
        order = result[0]
        name = result[1].strip()
        quantity = result[2].replace(',', '.')
        price = result[3].replace(',', '.')
        
        writer.writerow([order, name, quantity, price])

print("Data has been written to 'data.csv'.")
