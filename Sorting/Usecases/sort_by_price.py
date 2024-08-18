
# Sorting a list of items by price in an online store.

add_to_cart = []
def add_product(product_name,price):
    new_product = {'name':product_name,'price':price}

    if not add_to_cart:
        add_to_cart.append(new_product)
    else:
        add = False
        for i in range(len(add_to_cart)):
            if add_to_cart[i]['price']>price:
                add_to_cart.insert(i, new_product)
                add = True
                break
        if not add:
                add_to_cart.append(new_product)



add_product('product1',600)
add_product('product2',49.9999)
add_product('product3',49.99)
add_product('product4',900)

for p in add_to_cart:
    print(f"Item: {p['name']}, Price: ${p['price']}")
