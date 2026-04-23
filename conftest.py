# conftest.py
import pytest
import re
from playwright.sync_api import Page, expect

usuario = 'standard_user'
password = 'secret_sauce'

@pytest.fixture
def test_loginEnWeb(page: Page):
    # Cargamos la página web
    page.goto("https://www.saucedemo.com/")

    # Esperamos a que la página web cargue
    expect(page).to_have_title(re.compile("Swag Labs"))

    # Introducimos el usuario
    page.get_by_placeholder('Username').fill(usuario)
    # Introducimos la contraseña
    page.get_by_placeholder('Password').fill(password)
    
    # Hacemos el login
    page.get_by_role('button', name='Login').click()

    # Esperamos a que la página pase del login
    expect(page.locator('.title')).to_have_text('Products')

    return page