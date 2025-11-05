"""Sistema de observadores usando patron Observer.

Mejora: permite inyección de la fábrica de notificaciones en `User` para
facilitar pruebas y cumplir DIP.
"""

from abc import ABC, abstractmethod
from typing import Optional

from notifications import NotificationFactory


class Observer(ABC):
    """Interfaz abstracta para observadores."""
    
    @abstractmethod
    def update(self, event):
        """Metodo llamado cuando ocurre un evento.
        
        Args:
            event: Evento que desencadeno la notificacion.
        """
        pass


class User(Observer):
    """Usuario que puede suscribirse a eventos y recibir notificaciones."""
    
    def __init__(self, user_id: str, name: str, notification_type: str, notification_factory: Optional[NotificationFactory] = None):
        """Inicializa un usuario.
        
        Args:
            user_id: Identificador unico del usuario.
            name: Nombre del usuario.
            notification_type: Tipo de notificacion preferida.
        """
        self._user_id = user_id
        self._name = name
        self._notification_type = notification_type
        self._subscribed_events = set()
        # Permite inyectar una fábrica (por defecto se usa la fábrica del módulo)
        self._notification_factory = notification_factory or NotificationFactory
    
    def get_user_id(self):
        """Obtiene el ID del usuario.
        
        Returns:
            str: ID del usuario.
        """
        return self._user_id
    
    def get_name(self):
        """Obtiene el nombre del usuario.
        
        Returns:
            str: Nombre del usuario.
        """
        return self._name
    
    def get_notification_type(self):
        """Obtiene el tipo de notificacion preferida.
        
        Returns:
            str: Tipo de notificacion.
        """
        return self._notification_type
    
    def add_subscription(self, event_type):
        """Suscribe al usuario a un tipo de evento.
        
        Args:
            event_type: Tipo de evento al que suscribirse.
        """
        self._subscribed_events.add(event_type)
    
    def remove_subscription(self, event_type):
        """Desuscribe al usuario de un tipo de evento.
        
        Args:
            event_type: Tipo de evento del que desuscribirse.
        """
        self._subscribed_events.discard(event_type)
    
    def is_subscribed_to(self, event_type):
        """Verifica si el usuario esta suscrito a un evento.
        
        Args:
            event_type: Tipo de evento a verificar.
            
        Returns:
            bool: True si esta suscrito, False en caso contrario.
        """
        return event_type in self._subscribed_events
    
    def update(self, event):
        """Recibe notificacion de un evento.
        
        Args:
            event: Evento que desencadeno la notificacion.
        """
        if self.is_subscribed_to(event.get_type()):
            notification = self._notification_factory.create_notification(self._notification_type)
            notification.send(event.get_message(), self._name)


class Event:
    """Representa un evento del sistema."""
    
    def __init__(self, event_type, message):
        """Inicializa un evento.
        
        Args:
            event_type: Tipo de evento.
            message: Mensaje asociado al evento.
        """
        self._event_type = event_type
        self._message = message
    
    def get_type(self):
        """Obtiene el tipo de evento.
        
        Returns:
            str: Tipo de evento.
        """
        return self._event_type
    
    def get_message(self):
        """Obtiene el mensaje del evento.
        
        Returns:
            str: Mensaje del evento.
        """
        return self._message


class EventManager:
    """Gestor de eventos que implementa el patron Observer.
    
    Administra la lista de observadores y notifica cuando ocurren eventos.
    """
    
    def __init__(self):
        """Inicializa el gestor de eventos."""
        self._observers = []
    
    def subscribe(self, observer):
        """Suscribe un observador al gestor de eventos.
        
        Args:
            observer: Observador a suscribir.
        """
        if observer not in self._observers:
            self._observers.append(observer)
    
    def unsubscribe(self, observer):
        """Desuscribe un observador del gestor de eventos.
        
        Args:
            observer: Observador a desuscribir.
        """
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify(self, event):
        """Notifica a todos los observadores de un evento.
        
        Args:
            event: Evento a notificar.
        """
        for observer in self._observers:
            observer.update(event)