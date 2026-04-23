import requests

# Clave API
apiKey = "reqres_a3e65b9585c14eccb03b7f3a18228fa8"

# Método para realizar la llamada API de usuarios
def test_loginOK():
    response = requests.post(
        'https://reqres.in/api/login',
        json={"email": "eve.holt@reqres.in", "password": "cityslicka"},
        headers={"x-api-key": apiKey})
    
    # Comprobamos que la respuesta es OK
    assert response.status_code == 200

    # Validamos que la respuesta es correcta
    resultado = response.json()
    assert "token" in resultado