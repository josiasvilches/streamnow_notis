"""Sistema de Notificaciones - Demostración completa.

Este módulo contiene las funciones de demostración que muestran el uso de los
patrones implementados (Singleton, Factory, Observer, Strategy). Las funciones
antes llamadas `test_*` han sido renombradas a `demo_*`.
"""

# Standard library
import sys

# Local application
from config import NotificationConfig
from observer import EventManager, User, Event
from notifications import NotificationFactory
from strategies import DailyEmailStrategy, RealtimePushStrategy, CriticalSMSStrategy
from logger import NotificationLogger
from constantes import (
    NOTIFICATION_TYPE_EMAIL,
    NOTIFICATION_TYPE_PUSH,
    NOTIFICATION_TYPE_SMS,
    EVENT_TYPE_NEW_CONTENT,
    EVENT_TYPE_LIVE_EVENT,
    EVENT_TYPE_SUBSCRIPTION_EXPIRY,
)


def demo_singleton():
    """Demuestra el patrón Singleton usando NotificationConfig."""
    print("=== Demo: Singleton ===")
    config1 = NotificationConfig()
    config2 = NotificationConfig()
    
    if config1 is config2:
        print("Singleton funciona correctamente: ambas instancias son la misma")
    else:
        raise Exception("Error: Singleton no funciona correctamente")
    
    print(f"Configuracion Email: {config1.get_email_config()['sender']}")
    print(f"Configuracion Push: {config1.get_push_config()['api_endpoint']}")
    print()


def demo_factory():
    """Demuestra el patrón Factory Method."""
    print("=== Demo: Factory Method ===")
    
    email_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_EMAIL)
    push_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_PUSH)
    sms_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_SMS)
    
    print(f"Email Notification creada: {email_notification.__class__.__name__}")
    print(f"Push Notification creada: {push_notification.__class__.__name__}")
    print(f"SMS Notification creada: {sms_notification.__class__.__name__}")
    print()


def demo_strategy():
    """Demuestra el patrón Strategy."""
    print("=== Demo: Strategy ===")
    
    push_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_PUSH)
    print(f"Estrategia inicial: {push_notification.get_strategy().get_strategy_name()}")
    push_notification.send("Nuevo episodio disponible", "Usuario1")
    
    print("\nCambiando estrategia a DailyEmailStrategy...")
    push_notification.set_strategy(DailyEmailStrategy())
    print(f"Nueva estrategia: {push_notification.get_strategy().get_strategy_name()}")
    push_notification.send("Nuevo episodio disponible", "Usuario1")
    print()


def demo_observer():
    """Demuestra el patrón Observer."""
    print("=== Demo: Observer ===")
    
    event_manager = EventManager()
    
    user1 = User("001", "Juan Perez", NOTIFICATION_TYPE_PUSH)
    user2 = User("002", "Maria Lopez", NOTIFICATION_TYPE_EMAIL)
    user3 = User("003", "Carlos Garcia", NOTIFICATION_TYPE_SMS)
    
    user1.add_subscription(EVENT_TYPE_NEW_CONTENT)
    user1.add_subscription(EVENT_TYPE_LIVE_EVENT)
    
    user2.add_subscription(EVENT_TYPE_NEW_CONTENT)
    
    user3.add_subscription(EVENT_TYPE_SUBSCRIPTION_EXPIRY)
    
    event_manager.subscribe(user1)
    event_manager.subscribe(user2)
    event_manager.subscribe(user3)
    
    print("Generando evento de nuevo contenido...")
    new_content_event = Event(EVENT_TYPE_NEW_CONTENT, "Nueva temporada de tu serie favorita disponible")
    event_manager.notify(new_content_event)
    
    print("\nGenerando evento en vivo...")
    live_event = Event(EVENT_TYPE_LIVE_EVENT, "Transmision en vivo comenzando ahora")
    event_manager.notify(live_event)
    
    print("\nGenerando evento de vencimiento de suscripcion...")
    expiry_event = Event(EVENT_TYPE_SUBSCRIPTION_EXPIRY, "Tu suscripcion vence en 3 dias")
    event_manager.notify(expiry_event)
    
    print("\nDesuscribiendo a Juan de eventos de nuevo contenido...")
    user1.remove_subscription(EVENT_TYPE_NEW_CONTENT)
    
    print("Generando nuevo evento de contenido...")
    new_content_event2 = Event(EVENT_TYPE_NEW_CONTENT, "Pelicula exclusiva agregada al catalogo")
    event_manager.notify(new_content_event2)
    print()


def demo_integration():
    """Demuestra el flujo completo de integración."""
    print("=== Demo: Integracion Completa ===")
    
    logger = NotificationLogger()
    logger.clear_logs()
    
    config = NotificationConfig()
    event_manager = EventManager()
    
    user1 = User("101", "Ana Martinez", NOTIFICATION_TYPE_PUSH)
    user2 = User("102", "Pedro Rodriguez", NOTIFICATION_TYPE_EMAIL)
    user3 = User("103", "Laura Sanchez", NOTIFICATION_TYPE_SMS)
    
    user1.add_subscription(EVENT_TYPE_NEW_CONTENT)
    user1.add_subscription(EVENT_TYPE_LIVE_EVENT)
    user2.add_subscription(EVENT_TYPE_NEW_CONTENT)
    user3.add_subscription(EVENT_TYPE_SUBSCRIPTION_EXPIRY)
    
    event_manager.subscribe(user1)
    event_manager.subscribe(user2)
    event_manager.subscribe(user3)
    
    print("Sistema configurado. Generando eventos...")
    print()
    
    event1 = Event(EVENT_TYPE_NEW_CONTENT, "Documental exclusivo agregado")
    print("Evento 1: Nuevo contenido")
    event_manager.notify(event1)
    
    notification1 = NotificationFactory.create_notification(user1.get_notification_type())
    logger.log(
        user1.get_notification_type(),
        notification1.get_strategy().get_strategy_name(),
        user1.get_name(),
        event1.get_message()
    )
    
    notification2 = NotificationFactory.create_notification(user2.get_notification_type())
    logger.log(
        user2.get_notification_type(),
        notification2.get_strategy().get_strategy_name(),
        user2.get_name(),
        event1.get_message()
    )
    
    print()
    event2 = Event(EVENT_TYPE_LIVE_EVENT, "Concierto en vivo iniciando")
    print("Evento 2: Evento en vivo")
    event_manager.notify(event2)
    
    notification3 = NotificationFactory.create_notification(user1.get_notification_type())
    logger.log(
        user1.get_notification_type(),
        notification3.get_strategy().get_strategy_name(),
        user1.get_name(),
        event2.get_message()
    )
    
    print()
    event3 = Event(EVENT_TYPE_SUBSCRIPTION_EXPIRY, "Renovar suscripcion para continuar")
    print("Evento 3: Vencimiento de suscripcion")
    event_manager.notify(event3)
    
    notification4 = NotificationFactory.create_notification(user3.get_notification_type())
    logger.log(
        user3.get_notification_type(),
        notification4.get_strategy().get_strategy_name(),
        user3.get_name(),
        event3.get_message()
    )
    
    print()


def run_demo():
    try:
        print("Iniciando demo de notificaciones StreamNow")
        print("=" * 50)
        print()

        demo_singleton()
        demo_factory()
        demo_strategy()
        demo_observer()
        demo_integration()

        print("=" * 50)
        print("DEMO COMPLETADO EXITOSAMENTE")
    except Exception as e:
        print(f"Error en la ejecucion del demo: {e}")
        raise


def main():
    # por compatibilidad con ejemplo anterior
    run_demo()


if __name__ == "__main__":
    main()