count_all = int(input("Введите количество товара: "))
products_list = []
for i in range (1, count_all + 1):
    name_products = input(f'Введите название {i}-го продукта: ')
    price_products = float(input(f'Введите цену {i}-го продукта: '))
    count_products = int(input(f'Введите количество {i}-го продукта: '))
    mera_products = input(f'Введите единицу измерения {i}-го продукта: ')
    dict_products = {'название': name_products, 'цена': price_products, 'количество': count_products,
                    'ед.': mera_products}
    set_products = (i, dict_products)
    products_list.append(set_products)
print('Сформированный список: ', products_list)

name_val = []
price_val = []
count_val = []
mera_val = []
for product in products_list:
    dict_ = product[1]

    name_values = list(dict_.values())[0]
    name_val.append(name_values)
    price_values = list(dict_.values())[1]
    price_val.append(price_values)
    count_values = list(dict_.values())[2]
    count_val.append(count_values)
    mera_values = list(dict_.values())[3]
    mera_val.append(mera_values)

final_dict = {list(dict_products.keys())[0] : name_val, list(dict_products.keys())[1] : price_val,
              list(dict_products.keys())[2] : count_val, list(dict_products.keys())[3] : mera_val}

print('Результат обработки: ', final_dict)
