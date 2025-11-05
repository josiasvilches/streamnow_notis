"""Clases de notificaciones y factory usando patron Factory Method.

Mejoras aplicadas: se permite inyección de `NotificationConfig` en `Notification` y
se convierte la fábrica en un registro extensible para respetar OCP.
"""

from abc import ABC, abstractmethod
from typing import Optional, Type, Dict

from config import NotificationConfig
from strategies import (
    DailyEmailStrategy,
    RealtimePushStrategy,
    CriticalSMSStrategy,
    NotificationStrategy,
)
from constantes import NOTIFICATION_TYPE_EMAIL, NOTIFICATION_TYPE_PUSH, NOTIFICATION_TYPE_SMS


class Notification(ABC):
    """Clase abstracta base para todas las notificaciones."""
    
    def __init__(self, config: Optional[NotificationConfig] = None):
        """Inicializa la notificacion con configuracion y estrategia.

        Args:
            config: Permite inyectar una instancia de `NotificationConfig` (para tests o
                    casos avanzados). Si es None se usa el Singleton por defecto.
        """
        self._config: NotificationConfig = config or NotificationConfig()
        self._strategy: Optional[NotificationStrategy] = None
    
    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        """Envia la notificacion.

        Args:
            message: Mensaje a enviar.
            recipient: Destinatario de la notificacion.
        """
        ...
    
    def set_strategy(self, strategy):
        """Establece la estrategia de envio.
        
        Args:
            strategy: Instancia de NotificationStrategy.
        """
        self._strategy = strategy
    
    def get_strategy(self):
        """Obtiene la estrategia actual.
        
        Returns:
            NotificationStrategy: Estrategia de envio actual.
        """
        return self._strategy


class EmailNotification(Notification):
    """Notificacion por email."""
    
    def __init__(self):
        """Inicializa la notificacion de email con estrategia diaria."""
        super().__init__()
        self._strategy = DailyEmailStrategy()
    
    def send(self, message, recipient):
        """Envia notificacion por email.
        
        Args:
            message: Mensaje a enviar.
            recipient: Destinatario del email.
        """
        email_config = self._config.get_email_config()
        if self._strategy:
            self._strategy.send(message, recipient)


class PushNotification(Notification):
    """Notificacion push."""
    
    def __init__(self):
        """Inicializa la notificacion push con estrategia en tiempo real."""
        super().__init__()
        self._strategy = RealtimePushStrategy()
    
    def send(self, message, recipient):
        """Envia notificacion push.
        
        Args:
            message: Mensaje a enviar.
            recipient: Destinatario del push.
        """
        push_config = self._config.get_push_config()
        if self._strategy:
            self._strategy.send(message, recipient)


class SMSNotification(Notification):
    """Notificacion por SMS."""
    
    def __init__(self):
        """Inicializa la notificacion SMS con estrategia critica."""
        super().__init__()
        self._strategy = CriticalSMSStrategy()
    
    def send(self, message, recipient):
        """Envia notificacion por SMS.
        
        Args:
            message: Mensaje a enviar.
            recipient: Destinatario del SMS.
        """
        sms_config = self._config.get_sms_config()
        if self._strategy:
            self._strategy.send(message, recipient)


class NotificationFactory:
    """Factory registrable para crear instancias de notificaciones.

    Cambiado a un registro interno para soportar OCP: nuevas clases pueden
    registrarse sin editar la fábrica.
    """

    _registry: Dict[str, Type[Notification]] = {}

    @classmethod
    def register_notification(cls, notification_type: str, notification_cls: Type[Notification]) -> None:
        cls._registry[notification_type] = notification_cls

    @classmethod
    def create_notification(cls, notification_type: str) -> Notification:
        try:
            notification_cls = cls._registry[notification_type]
        except KeyError:
            raise ValueError(f"Tipo de notificacion no valido: {notification_type}")
        return notification_cls()


# Registro de las notificaciones built-in para mantener compatibilidad
NotificationFactory.register_notification(NOTIFICATION_TYPE_EMAIL, EmailNotification)
NotificationFactory.register_notification(NOTIFICATION_TYPE_PUSH, PushNotification)
NotificationFactory.register_notification(NOTIFICATION_TYPE_SMS, SMSNotification)