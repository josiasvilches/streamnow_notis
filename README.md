
# StreamNow — Sistema de notificaciones

Este repositorio contiene una implementación didáctica de un sistema de notificaciones inspirado en una plataforma de streaming. El objetivo es demostrar patrones de diseño (Singleton, Factory Method, Observer, Strategy) y proporcionar un conjunto de pruebas unitarias.

## Resumen rápido

- Singleton: `NotificationConfig` centraliza la configuración de los canales (email, push, SMS).
- Factory Method: `NotificationFactory` crea instancias concretas de `EmailNotification`, `PushNotification` y `SMSNotification`.
- Observer: `EventManager`, `User` y `Event` permiten que los usuarios se suscriban a eventos y reciban notificaciones.
- Strategy: Estrategias de envío (`DailyEmailStrategy`, `RealtimePushStrategy`, `CriticalSMSStrategy`) para cambiar la política de entrega en tiempo de ejecución.
- Logging: `NotificationLogger` escribe un historial sencillo en `notifications.log`.

## Archivos principales

- `main.py` — Script de demostración con funciones `demo_*` y un entrypoint para ejecutar la demo.
- `config.py` — `NotificationConfig` (Singleton).
- `notifications.py` — Clases de notificación y `NotificationFactory`.
- `observer.py` — `Event`, `User` y `EventManager`.
- `strategies.py` — Implementaciones de estrategias de notificación.
- `logger.py` — `NotificationLogger` para historial.
- `constantes.py` — Constantes usadas por el sistema.
- `USER_STORIES.md` — Historias de usuario y criterios de aceptación.

## Contrato breve (inputs/outputs)

- Input: eventos (`Event`) generados por el sistema.
- Output: llamadas de envío (simuladas con `print`) y entradas en `notifications.log`.
- Errores: la `NotificationFactory` lanza `ValueError` si se solicita un tipo de notificación desconocido.

## Casos borde cubiertos

- Usuario sin suscripciones: no recibe notificaciones.
- Tipo de notificación inválido: `ValueError` en la factory.
- Cambio de estrategia en tiempo de ejecución: soportado.

## Cómo ejecutar

Recomendado: usar un entorno virtual y Python 3.8+.

PowerShell (en la raíz del proyecto):

```powershell
# crear/activar virtualenv (si no lo tenés)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instalar dependencias de desarrollo
pip install -r requirements.txt  # opcional si existe

# ejecutar la demo
python .\main.py

# ejecutar tests con coverage
.\.venv\Scripts\python.exe -m pytest --cov=. --cov-report=term-missing
```

La demo imprimirá secciones demostrando los patrones y actualizará `notifications.log` cuando se ejecute la integración.

## Nota sobre cobertura

El repositorio incluye una configuración de coverage (`.coveragerc`) que excluye ciertos scripts auxiliares y la carpeta `tests` de la métrica global, para medir únicamente el código de la aplicación.

## Cómo contribuir

- Haz un fork, crea una rama y abre un Pull Request con cambios pequeños y claros.
- Añade tests cuando añadas o cambies comportamiento.

