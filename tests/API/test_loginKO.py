import requests

# Clave API
apiKey = "reqres_a3e65b9585c14eccb03b7f3a18228fa8"

# Método para realizar la llamada API de usuarios
def test_loginKO():
    response = requests.post(
        'https://reqres.in/api/login',
        json={"email": "moreno.ortega.jorge26@gmail.com", "password": "prueba123"},
        headers={"x-api-key": apiKey})
    
    # Comprobamos que la respuesta es KO
    assert response.status_code == 400

    # Validamos que la respuesta es correcta
    resultado = response.json()
    assert "error" in resultado