import pytest
from src.problema1 import main
from io import StringIO


# Simula la entrada del usuario
@pytest.fixture
def user_input(monkeypatch):
    user_input = StringIO()
    monkeypatch.setattr("sys.stdin", user_input)
    return user_input


# Captura la salida del programa
@pytest.fixture
def capsys(capsys):
    return capsys


# Prueba para la función main()
def test_main(user_input, capsys):
    # Simula la entrada del usuario
    user_input.write("3\n")  # Número de coordenadas: 3
    user_input.write("1\n")  # Coordenada 1, x
    user_input.write("2\n")  # Coordenada 1, y
    user_input.write("3\n")  # Coordenada 2, x
    user_input.write("4\n")  # Coordenada 2, y
    user_input.write("2\n")  # Coordenada 3, x
    user_input.write("2\n")  # Coordenada 3, y
    user_input.write("q\n")  # Salir del programa
    user_input.seek(0)  # Vuelve al inicio del flujo de entrada

    # Ejecuta la función principal
    main()

    # Captura la salida del programa
    captured = capsys.readouterr()

    # Verifica que el programa haya respondido como se esperaba
    assert "La distancia total recorrida es:" in captured.out
    assert "Los vectores tienen longitudes diferentes" not in captured.out
    assert "Gracias por utilizar el programa. ¡Hasta luego!" in captured.out
