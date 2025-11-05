"""Sistema de logging para registrar notificaciones enviadas."""

import os
from datetime import datetime
from constantes import LOG_FILE_PATH


class NotificationLogger:
    """Logger para registrar el historial de notificaciones enviadas."""
    
    _instance = None
    
    def __new__(cls):
        """Crea o retorna la unica instancia del logger.
        
        Returns:
            NotificationLogger: Instancia unica del logger.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        """Inicializa el logger solo una vez."""
        if self._initialized:
            return
        
        self._log_file = LOG_FILE_PATH
        self._initialized = True
    
    def log(self, notification_type, strategy_name, recipient, message):
        """Registra una notificacion enviada.
        
        Args:
            notification_type: Tipo de notificacion.
            strategy_name: Nombre de la estrategia usada.
            recipient: Destinatario de la notificacion.
            message: Mensaje enviado.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] Tipo: {notification_type} | Estrategia: {strategy_name} | Destinatario: {recipient} | Mensaje: {message}\n"
        
        try:
            with open(self._log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except Exception as e:
            print(f"Error al escribir en el log: {e}")
    
    def get_logs(self):
        """Obtiene todos los logs registrados.
        
        Returns:
            str: Contenido del archivo de logs.
        """
        if not os.path.exists(self._log_file):
            return "No hay logs registrados."
        
        try:
            with open(self._log_file, "r", encoding="utf-8") as f:
                return f.read()
        except Exception as e:
            return f"Error al leer logs: {e}"
    
    def clear_logs(self):
        """Limpia el archivo de logs."""
        try:
            if os.path.exists(self._log_file):
                os.remove(self._log_file)
        except Exception as e:
            print(f"Error al limpiar logs: {e}")