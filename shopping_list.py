print("Lista zakupów")
shopping_dict = {
     'piekarnia': ['chleb', 'bułki','pączek'],
     'warzywniak':['marchew', 'seler','rukola']
}

for  k, v in shopping_dict.items():
    print(f"Idę do {k}, kupuję tu następujące rzeczy: {v}")