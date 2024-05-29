from django.shortcuts import render


def orders(m):
    return render(m, 'shop/orders.html')

def catalog(n):
    return render(n, 'shop/catalog.html')

def order_create(b):
    return render(b, 'shop/order_create.html')
