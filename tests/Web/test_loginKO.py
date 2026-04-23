import re
from playwright.sync_api import Page, expect

usuario = 'asdasd'
password = 'dsadsa'

def test_loginKO(page: Page):
    # Cargamos la página web
    page.goto("https://www.saucedemo.com/")

    # Esperamos a que la página web cargue
    expect(page).to_have_title(re.compile("Swag Labs"))

    # Introducimos el usuario incorrecto
    page.get_by_placeholder('Username').fill(usuario)
    # Introducimos la contraseña incorrecta
    page.get_by_placeholder('Password').fill(password)

    # Pulsamos el botón de login
    page.get_by_role('button', name='Login').click()

    # Comprobamos que el mensaje de error aparece
    expect(page.locator('[data-test="error"]')).to_be_visible()
