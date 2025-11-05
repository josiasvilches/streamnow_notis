"""Entry point ligero: delega la demo en `demo.py`.

El archivo pesado con las funciones de demo se movió a `demo.py`. Mantener
`main.py` pequeño facilita su inclusión en pipelines y evita mezclar demo con
la lógica del paquete.
"""

from examples.demo import run_demo


if __name__ == "__main__":
    run_demo()