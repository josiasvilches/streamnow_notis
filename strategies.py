"""Estrategias de envio de notificaciones usando patron Strategy."""

from abc import ABC, abstractmethod
from constantes import STRATEGY_DAILY, STRATEGY_REALTIME, STRATEGY_CRITICAL


class NotificationStrategy(ABC):
    """Interfaz abstracta para estrategias de envio de notificaciones."""
    
    @abstractmethod
    def send(self, message, recipient):
        """Envia una notificacion segun la estrategia definida.
        
        Args:
            message: Mensaje a enviar.
            recipient: Destinatario de la notificacion.
        """
        pass
    
    @abstractmethod
    def get_strategy_name(self):
        """Obtiene el nombre de la estrategia.
        
        Returns:
            str: Nombre de la estrategia.
        """
        pass


class DailyEmailStrategy(NotificationStrategy):
    """Estrategia de envio diario para notificaciones por email.
    
    Agrupa las notificaciones y las envia una vez al dia.
    """
    
    def send(self, message, recipient):
        """Envia email con estrategia diaria.
        
        Args:
            message: Mensaje a enviar.
            recipient: Destinatario del email.
        """
        print(f"(EMAIL): Programado envio diario para {recipient}: {message}")
    
    def get_strategy_name(self):
        """Obtiene el nombre de la estrategia.
        
        Returns:
            str: Nombre de la estrategia.
        """
        return STRATEGY_DAILY


class RealtimePushStrategy(NotificationStrategy):
    """Estrategia de envio en tiempo real para notificaciones push.
    
    Envia las notificaciones inmediatamente cuando se generan.
    """
    
    def send(self, message, recipient):
        """Envia push en tiempo real.
        
        Args:
            message: Mensaje a enviar.
            recipient: Destinatario del push.
        """
        print(f"(PUSH): {message}")
    
    def get_strategy_name(self):
        """Obtiene el nombre de la estrategia.
        
        Returns:
            str: Nombre de la estrategia.
        """
        return STRATEGY_REALTIME


class CriticalSMSStrategy(NotificationStrategy):
    """Estrategia de envio critico para notificaciones SMS.
    
    Envia notificaciones de alta prioridad inmediatamente.
    """
    
    def send(self, message, recipient):
        """Envia SMS con prioridad critica.
        
        Args:
            message: Mensaje a enviar.
            recipient: Destinatario del SMS.
        """
        print(f"(SMS): CRITICO - {message}")
    
    def get_strategy_name(self):
        """Obtiene el nombre de la estrategia.
        
        Returns:
            str: Nombre de la estrategia.
        """
        return STRATEGY_CRITICAL