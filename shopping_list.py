print("Lista zakupów")
shopping_dict = {
     'piekarnia': ['chleb', 'bułki','pączek'],
     'warzywniak':['marchew', 'seler','rukola']
}

total_number = 0
for  k, v in shopping_dict.items():
    v2 = [ item.capitalize() for item in v]
    total_number += len(v2)
    print(f"Idę do {k.capitalize()}, kupuję tu następujące rzeczy: {v2}")

print(f"W sumie kupuję {total_number} produktów.");
