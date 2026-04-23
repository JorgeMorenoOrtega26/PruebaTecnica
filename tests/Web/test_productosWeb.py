import re
import pytest
from playwright.sync_api import Page, expect

nombreProductos = ['Sauce Labs Backpack',
             'Sauce Labs Bike Light',
             'Sauce Labs Bolt T-Shirt',
             'Sauce Labs Fleece Jacket',
             'Sauce Labs Onesie',
             'Test.allTheThings() T-Shirt (Red)']

def test_revisionProductos(test_loginEnWeb: Page):
    # Comprobamos que los el número de items concuerde con el tamaño de la lista
    productos = test_loginEnWeb.locator('.inventory_item_name')
    expect(productos).to_have_count(len(nombreProductos))
    
    # Buscamos que todos los productos existan
    for producto in nombreProductos:
        expect(productos.filter(has_text=nombreProductos))

def test_agregarProductos(test_loginEnWeb: Page):
    # Añadimos una mochila al carrito
    test_loginEnWeb.locator('#add-to-cart-sauce-labs-backpack').click()

    # Añadimos una luz de bicicleta al carrito
    test_loginEnWeb.locator('#add-to-cart-sauce-labs-bike-light').click()

    # Comprobamos que el número de objetos añadidos a la cesta es el correcto
    expect(test_loginEnWeb.locator('.shopping_cart_badge')).to_have_text('2')
