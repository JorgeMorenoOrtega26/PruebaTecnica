import requests, re

# Clave API
apiKey = "reqres_a3e65b9585c14eccb03b7f3a18228fa8"

# Método para realizar la llamada API de usuarios
def test_mailCheck():
    response = requests.get(
        'https://reqres.in/api/users?page=2',
        headers={"x-api-key": apiKey})
    
    # Comprobamosd que la respuesta es OK
    assert response.status_code == 200

    # Capturamos el json en una variable y comprobamos que existe el campo data
    resultado = response.json()
    assert "data" in resultado

    # Patron a seguir para validar correos (X@X.X)
    mailRegex = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]"
    
    listaEmails = []
    listaEmailsInvalidos = []

    # Iteramos por toda la lista de usuarios
    for user in resultado["data"]:
        # Comprobamos que el usuario tiene email
        assert "email" in user

        # Capturamos el email del usuario
        email = user.get("email")

        # Verificamos por regex si el email del usuario es valido o invalido
        assert re.match(mailRegex, email), f"EMAIL INVALIDO: {email}"