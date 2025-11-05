
# StreamNow - Sistema de Notificaciones (Ejemplo Académico)

Este repositorio contiene una implementación didáctica de un sistema de notificaciones inspirado en una plataforma de streaming (StreamNow). El objetivo del proyecto es demostrar varios patrones de diseño (Singleton, Factory Method, Observer, Strategy) aplicados para resolver problemas reales de envío de notificaciones.

## Contenido / Resumen

- Patrón Singleton: `NotificationConfig` centraliza la configuración de los canales (email, push, SMS).
- Patrón Factory Method: `NotificationFactory` crea instancias concretas de `EmailNotification`, `PushNotification` y `SMSNotification`.
- Patrón Observer: `EventManager`, `User` y `Event` permiten que los usuarios se suscriban a eventos y reciban notificaciones automáticamente.
- Patrón Strategy: Diferentes estrategias de envío (`DailyEmailStrategy`, `RealtimePushStrategy`, `CriticalSMSStrategy`) permiten cambiar la política de entrega en tiempo de ejecución.
- Logging sencillo de notificaciones: `NotificationLogger` registra los envíos en `notifications.log`.

## Archivos principales

- `main.py` — Script de demostración que ejecuta pruebas unitarias manuales de los patrones (singleton, factory, strategy, observer e integración).
- `config.py` — Implementa `NotificationConfig` (Singleton) con getters y setters para email/push/sms.
- `notifications.py` — Clases abstractas y concretas de notificación más la `NotificationFactory`.
- `observer.py` — `Event`, `User` (observador) y `EventManager` (sujeto) para el sistema de suscripciones.
- `strategies.py` — Implementaciones de las estrategias de envío (Strategy pattern).
- `logger.py` — `NotificationLogger` para guardar un historial simple en `notifications.log`.
- `constantes.py` — Constantes usadas por todo el sistema (tipos de notificación, eventos, nombres de estrategia y ruta de log).
- `USER_STORIES.md` — Historias de usuario y criterios de aceptación que guían el diseño.

## Contrato breve (inputs/outputs)

- Input: eventos (`Event`) generados por el sistema.
- Output: llamadas de envío a las distintas notificaciones (simuladas con `print`) y entradas en el log (`notifications.log`).
- Errores: Excepciones si se solicita un tipo de notificación desconocido (raised desde `NotificationFactory`).

## Ejemplos de casos borde considerados

- Usuario sin suscripciones: no recibe notificaciones.
- Tipo de notificación inválido: lanza `ValueError` en la factory.
- Cambio de estrategia en tiempo de ejecución: soportado por `set_strategy` en cada notificación.

## Cómo ejecutar (Windows PowerShell)

1. Asegúrate de tener Python 3.8+ instalado y accesible como `python`.
2. Abre PowerShell en la carpeta del proyecto (`c:\Josias\UM\3ro\DisenoSistemas\parcial 29-10`).

Comando para ejecutar la demo:

```powershell
python .\main.py
```

Salida esperada: el script imprimirá pasos de prueba mostrando que los patrones funcionan, y generará (o actualizará) `notifications.log` con los registros del flujo de integración.

Demo/ejemplos:

- El código de demostración se encuentra ahora en `examples/demo.py`.
- Puedes ejecutar la demo directamente desde `examples` o usando el entrypoint `main.py`:

```powershell
python .\examples\demo.py
# o (delegado por main)
python .\main.py
```

## Ejemplo rápido (qué observar)

- Verás secciones "=== Prueba de Singleton ===", "=== Prueba de Factory Method ===", "=== Prueba de Strategy ===" y "=== Prueba de Observer ===" en la salida.
- El archivo `notifications.log` contendrá líneas con marca de tiempo indicando tipo de notificación, estrategia, destinatario y mensaje cuando `test_integration()` lo registre.

## Notas para desarrolladores

- El proyecto está pensado para ser educativo — las operaciones de envío (email/push/sms) están simuladas mediante `print` y uso de la configuración desde `NotificationConfig`.
- Para integrar servicios reales, reemplaza las implementaciones en `strategies.py` por llamadas reales a APIs usando la configuración de `config.py`.

## Cómo contribuir

- Crea un fork y abre un Pull Request con cambios pequeños y explicativos.
- Añade tests que cubran nuevas funcionalidades o cambios de comportamiento.

## Licencia

Se sugiere usar MIT para proyectos de práctica/ejemplo. Puedes añadir un archivo `LICENSE` si quieres publicar este repositorio.

---

Si quieres, puedo añadir un `requirements.txt`, pruebas unitarias básicas o un archivo `LICENSE` (MIT) automáticamente. Indícame qué prefieres que haga a continuación.

