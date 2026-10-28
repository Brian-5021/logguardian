from patrones import detectar_fuerza_bruta
import pytest


@pytest.fixture
def hallazgos_fuerza_bruta():
    return [
        {
            "timestamp": "2026-09-02 10:00:05",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:10",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:12",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login for user admin"
        }
    ]


def test_detecta_fuerza_bruta(hallazgos_fuerza_bruta):
    resultado = detectar_fuerza_bruta(hallazgos_fuerza_bruta)

    assert resultado["fuerza_bruta"] is True
    assert resultado["ip"] == "192.168.1.50"


def test_no_detecta_fuerza_bruta():

    hallazgos = [
        {
            "timestamp": "2026-09-02 10:00:05",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:40",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:01:20",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
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
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:10",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:30",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        }
    ]

    resultado = detectar_fuerza_bruta(hallazgos)

    assert resultado["fuerza_bruta"] is True


def test_no_mezcla_eventos_de_diferentes_ips():

    hallazgos = [
        {
            "timestamp": "2026-09-02 10:00:05",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:10",
            "tipo": "WARNING",
            "ip": "10.0.0.20",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:12",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        }
    ]

    resultado = detectar_fuerza_bruta(hallazgos)

    assert resultado["fuerza_bruta"] is False


def test_detecta_fuerza_bruta_con_eventos_desordenados():
    hallazgos = [
        {
            "timestamp": "2026-09-02 10:00:20",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:05",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        },
        {
            "timestamp": "2026-09-02 10:00:12",
            "tipo": "WARNING",
            "ip": "192.168.1.50",
            "mensaje": "Failed login attempt"
        }
    ]

    resultado = detectar_fuerza_bruta(hallazgos)

    assert resultado["fuerza_bruta"] is True
    assert resultado["ip"] == "192.168.1.50"
    assert resultado["duracion_segundos"] == 15.0


def test_detecta_fuerza_bruta_con_eventos_desordenados_y_un_evento_fuera_de_ventana():
    hallazgos = [
            {
                "timestamp": "2026-09-02 10:00:20",
                "tipo": "WARNING",
                "ip": "192.168.1.50",
                "mensaje": "Failed login attempt"
            },
            {
                "timestamp": "2026-09-02 10:00:05",
                "tipo": "WARNING",
                "ip": "192.168.1.50",
                "mensaje": "Failed login attempt"
            },
            {
                "timestamp": "2026-09-02 10:00:12",
                "tipo": "WARNING",
                "ip": "192.168.1.50",
                "mensaje": "Failed login attempt"
            },
            {
                "timestamp": "2026-09-02 10:01:20",
                "tipo": "WARNING",
                "ip": "192.168.1.50",
                "mensaje": "Failed login attempt"
            }

        ]

    resultado = detectar_fuerza_bruta(hallazgos)

    assert resultado["total_eventos"] == 4
    assert resultado["fuerza_bruta"] is True
    assert len(resultado["eventos_detectados"]) == 3