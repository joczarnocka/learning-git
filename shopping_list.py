print("Lista zakupów")
shopping_dict = {
     'piekarnia': ['chleb', 'bułki','pączek'],
     'warzywniak':['marchew', 'seler','rukola']
}

for  k, v in shopping_dict.items():
    v2 = [ item.capitalize() for item in v]
    print(f"Idę do {k.capitalize()}, kupuję tu następujące rzeczy: {v2}")
