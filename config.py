"""Configuracion global del sistema usando patron Singleton."""

import threading


class NotificationConfig:
    """Configuracion centralizada del sistema de notificaciones.
    
    Implementa el patron Singleton para garantizar una unica instancia
    de configuracion accesible desde cualquier modulo del sistema.
    """
    
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        """Crea o retorna la unica instancia de la configuracion.
        
        Returns:
            NotificationConfig: Instancia unica de configuracion.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Inicializa la configuracion solo una vez."""
        if self._initialized:
            return
        
        self._email_config = {
            "smtp_host": "smtp.streamnow.com",
            "smtp_port": 587,
            "sender": "notifications@streamnow.com"
        }
        
        self._push_config = {
            "api_endpoint": "https://api.streamnow.com/push",
            "api_key": "push_api_key_12345"
        }
        
        self._sms_config = {
            "api_endpoint": "https://api.streamnow.com/sms",
            "api_key": "sms_api_key_67890"
        }
        
        self._initialized = True
    
    def get_email_config(self):
        """Obtiene la configuracion de email.
        
        Returns:
            dict: Configuracion de email.
        """
        return self._email_config.copy()
    
    def get_push_config(self):
        """Obtiene la configuracion de push.
        
        Returns:
            dict: Configuracion de push.
        """
        return self._push_config.copy()
    
    def get_sms_config(self):
        """Obtiene la configuracion de SMS.
        
        Returns:
            dict: Configuracion de SMS.
        """
        return self._sms_config.copy()
    
    def update_email_config(self, config):
        """Actualiza la configuracion de email.
        
        Args:
            config: Diccionario con nuevos valores de configuracion.
        """
        self._email_config.update(config)
    
    def update_push_config(self, config):
        """Actualiza la configuracion de push.
        
        Args:
            config: Diccionario con nuevos valores de configuracion.
        """
        self._push_config.update(config)
    
    def update_sms_config(self, config):
        """Actualiza la configuracion de SMS.
        
        Args:
            config: Diccionario con nuevos valores de configuracion.
        """
        self._sms_config.update(config)