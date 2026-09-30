from patrones import detectar_fuerza_bruta
import pytest


@pytest.fixture
def hallazgos_fuerza_bruta():
    return [
        {
            "timestamp": "2026-09-02 10:00:05",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:10",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:12",
            "mensaje": "Failed login for user admin"
        }
    ]


def test_detecta_fuerza_bruta(hallazgos_fuerza_bruta):
    resultado = detectar_fuerza_bruta(hallazgos_fuerza_bruta)

    assert resultado["fuerza_bruta"] is True


def test_no_detecta_fuerza_bruta():

    hallazgos = [
        {
            "timestamp": "2026-09-02 10:00:05",
            "tipo": "WARNING",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:40",
            "tipo": "WARNING",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:01:20",
            "tipo": "WARNING",
            "mensaje": "Failed login attempt"
        }
    ]

    resultado = detectar_fuerza_bruta(hallazgos)

    assert resultado["fuerza_bruta"] is False


def test_detecta_fuerza_bruta_en_limite():
        
        hallazgos = [
            {
                "timestamp": "2026-09-02 10:00:00",
                "tipo": "WARNING",
                "mensaje": "Failed login attempt"
            },
            {
                "timestamp": "2026-09-02 10:00:10",
                "tipo": "WARNING",
                "mensaje": "Failed login attempt"
            },
            {
                "timestamp": "2026-09-02 10:00:30",
                "tipo": "WARNING",
                "mensaje": "Failed login attempt"
            }
        ]

        resultado = detectar_fuerza_bruta(hallazgos)

        assert resultado["fuerza_bruta"] is True