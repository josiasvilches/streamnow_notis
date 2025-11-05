🥇 Épica 1: Configuración global del sistema

Patrón relacionado: Singleton

HU1.1 – Configuración centralizada

Como desarrollador del sistema
quiero disponer de una única instancia de configuración global
para acceder de forma segura a las credenciales, plantillas y endpoints de las APIs de notificación.

Criterios de aceptación:

Existe una clase NotificationConfig accesible desde cualquier módulo.

No se pueden crear múltiples instancias de configuración.

Los valores pueden actualizarse dinámicamente en tiempo de ejecución.

🥈 Épica 2: Generación de notificaciones

Patrón relacionado: Factory Method

HU2.1 – Creación de distintos tipos de notificación

Como sistema de envío de notificaciones
quiero generar instancias de EmailNotification, PushNotification o SMSNotification según el tipo de canal
para manejar la creación de forma desacoplada y extensible.

Criterios de aceptación:

Existe una NotificationFactory con un método create_notification(type) que devuelve la clase concreta.

Los nuevos tipos de notificación pueden agregarse sin modificar código existente.

🥉 Épica 3: Suscripción a eventos

Patrón relacionado: Observer

HU3.1 – Suscripción de usuarios a eventos

Como usuario de StreamNow
quiero suscribirme a tipos de eventos específicos (nuevo contenido, eventos en vivo, vencimiento de suscripción)
para recibir notificaciones solo de lo que me interesa.

Criterios de aceptación:

El usuario puede suscribirse y desuscribirse de eventos.

Los eventos generan notificaciones solo para los usuarios suscriptos.

HU3.2 – Notificación automática ante eventos

Como sistema
quiero notificar automáticamente a todos los usuarios suscriptos cuando ocurra un evento
para mantenerlos informados sin intervención manual.

Criterios de aceptación:

EventManager gestiona la lista de observadores.

Cada evento dispara notify(event) que invoca el método update() de los observadores correspondientes.

🧠 Épica 4: Estrategias de envío

Patrón relacionado: Strategy

HU4.1 – Envío personalizado según canal

Como sistema de notificaciones
quiero definir estrategias distintas de envío según el tipo de canal
para optimizar la frecuencia y prioridad de cada medio.

Criterios de aceptación:

Email usa estrategia de envío diario (DailyEmailStrategy).

Push usa estrategia en tiempo real (RealtimePushStrategy).

SMS usa estrategia crítica (CriticalSMSStrategy).

Las estrategias son intercambiables sin modificar las clases concretas de notificación.

HU4.2 – Cambiar estrategia en tiempo de ejecución

Como administrador del sistema
quiero poder cambiar la estrategia de envío sin alterar el código
para adaptar la política de notificaciones a nuevas necesidades.

Criterios de aceptación:

El sistema permite modificar la estrategia de cada canal en ejecución.

Las clases concretas de notificación aceptan inyección de una nueva estrategia.

⚙️ Épica 5: Integración y flujo completo
HU5.1 – Flujo integral de notificación

Como administrador del sistema
quiero que al dispararse un evento se cree automáticamente la notificación correcta
para que los usuarios sean informados con el canal y estrategia apropiada.

Criterios de aceptación:

Un evento genera una notificación por cada usuario suscripto.

NotificationFactory determina el canal.

Cada canal usa su Strategy de envío.

Las configuraciones se leen desde NotificationConfig.

🌟 Extra (Opcional para prácticas avanzadas)
HU6.1 – Registro de logs de notificaciones

Como desarrollador
quiero registrar las notificaciones enviadas y sus estrategias usadas
para analizar métricas y depurar el sistema.