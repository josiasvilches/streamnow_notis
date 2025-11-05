"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10
Fecha de generacion: 2025-11-05 00:12:28
Total de archivos integrados: 18
Total de directorios procesados: 3
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. buscar_paquete.py
#   3. config.py
#   4. constantes.py
#   5. demo.py
#   6. logger.py
#   7. main.py
#   8. notifications.py
#   9. observer.py
#   10. strategies.py
#
# DIRECTORIO: examples
#   11. __init__.py
#   12. demo.py
#
# DIRECTORIO: tests
#   13. test_config.py
#   14. test_demo_execution.py
#   15. test_factory_and_notifications.py
#   16. test_logger.py
#   17. test_observer.py
#   18. test_strategies_and_notifications.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/18: __init__.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 2/18: buscar_paquete.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\buscar_paquete.py
# ==============================================================================

"""
Script para buscar el paquete python_forestacion desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    # Agregar más exclusiones en obtener_subdirectorios()
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_forestacion")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_forestacion")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_forestacion")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_forestacion")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_forestacion")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

# ==============================================================================
# ARCHIVO 3/18: config.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\config.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 4/18: constantes.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\constantes.py
# ==============================================================================

"""Constantes globales del sistema de notificaciones."""

NOTIFICATION_TYPE_EMAIL = "email"
NOTIFICATION_TYPE_PUSH = "push"
NOTIFICATION_TYPE_SMS = "sms"

EVENT_TYPE_NEW_CONTENT = "new_content"
EVENT_TYPE_LIVE_EVENT = "live_event"
EVENT_TYPE_SUBSCRIPTION_EXPIRY = "subscription_expiry"

STRATEGY_DAILY = "daily"
STRATEGY_REALTIME = "realtime"
STRATEGY_CRITICAL = "critical"

LOG_FILE_PATH = "notifications.log"

# ==============================================================================
# ARCHIVO 5/18: demo.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\demo.py
# ==============================================================================

"""Módulo separado que contiene las funciones de demostración y pruebas
que antes vivían en `main.py`.

Separar el código de demostración del entrypoint principal hace el proyecto
más limpio y evita que `main.py` inflija ruido a la cobertura o a la
integración continua.
"""

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


def test_singleton():
    """Prueba el patron Singleton de NotificationConfig."""
    print("=== Prueba de Singleton ===")
    config1 = NotificationConfig()
    config2 = NotificationConfig()
    
    if config1 is config2:
        print("Singleton funciona correctamente: ambas instancias son la misma")
    else:
        raise Exception("Error: Singleton no funciona correctamente")
    
    print(f"Configuracion Email: {config1.get_email_config()['sender']}")
    print(f"Configuracion Push: {config1.get_push_config()['api_endpoint']}")
    print()


def test_factory():
    """Prueba el patron Factory Method."""
    print("=== Prueba de Factory Method ===")
    
    email_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_EMAIL)
    push_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_PUSH)
    sms_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_SMS)
    
    print(f"Email Notification creada: {email_notification.__class__.__name__}")
    print(f"Push Notification creada: {push_notification.__class__.__name__}")
    print(f"SMS Notification creada: {sms_notification.__class__.__name__}")
    print()


def test_strategy():
    """Prueba el patron Strategy."""
    print("=== Prueba de Strategy ===")
    
    push_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_PUSH)
    print(f"Estrategia inicial: {push_notification.get_strategy().get_strategy_name()}")
    push_notification.send("Nuevo episodio disponible", "Usuario1")
    
    print("\nCambiando estrategia a DailyEmailStrategy...")
    push_notification.set_strategy(DailyEmailStrategy())
    print(f"Nueva estrategia: {push_notification.get_strategy().get_strategy_name()}")
    push_notification.send("Nuevo episodio disponible", "Usuario1")
    print()


def test_observer():
    """Prueba el patron Observer."""
    print("=== Prueba de Observer ===")
    
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


def test_integration():
    """Prueba el flujo completo de integracion."""
    print("=== Prueba de Integracion Completa ===")
    
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

        test_singleton()
        test_factory()
        test_strategy()
        test_observer()
        test_integration()

        print("=" * 50)
        print("DEMO COMPLETADO EXITOSAMENTE")
    except Exception as e:
        print(f"Error en la ejecucion del demo: {e}")
        raise


if __name__ == "__main__":
    run_demo()


# ==============================================================================
# ARCHIVO 6/18: logger.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\logger.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 7/18: main.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\main.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 8/18: notifications.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\notifications.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 9/18: observer.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\observer.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 10/18: strategies.py
# Directorio: .
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\strategies.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: examples
################################################################################

# ==============================================================================
# ARCHIVO 11/18: __init__.py
# Directorio: examples
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\examples\__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 12/18: demo.py
# Directorio: examples
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\examples\demo.py
# ==============================================================================

"""Módulo separado (examples/demo.py) que contiene las funciones de demostración y pruebas
que antes vivían en `main.py`.

Separar el código de demostración del entrypoint principal hace el proyecto
más limpio y evita que `main.py` inflija ruido a la cobertura o a la
integración continua.
"""

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


def test_singleton():
    """Prueba el patron Singleton de NotificationConfig."""
    print("=== Prueba de Singleton ===")
    config1 = NotificationConfig()
    config2 = NotificationConfig()
    
    if config1 is config2:
        print("Singleton funciona correctamente: ambas instancias son la misma")
    else:
        raise Exception("Error: Singleton no funciona correctamente")
    
    print(f"Configuracion Email: {config1.get_email_config()['sender']}")
    print(f"Configuracion Push: {config1.get_push_config()['api_endpoint']}")
    print()


def test_factory():
    """Prueba el patron Factory Method."""
    print("=== Prueba de Factory Method ===")
    
    email_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_EMAIL)
    push_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_PUSH)
    sms_notification = NotificationFactory.create_notification(NOTIFICATION_TYPE_SMS)
    
    print(f"Email Notification creada: {email_notification.__class__.__name__}")
    """Este archivo ya no contiene la demo — su contenido fue movido a `main.py`.

    Conservar un stub aquí evita errores si alguien intenta importar
    `examples.demo` por compatibilidad. Ejecuta `python main.py` para lanzar
    la demostración integrada.
    """

    def placeholder_examples_demo():
        print("El demo fue movido a main.py. Ejecuta `python main.py`.")



################################################################################
# DIRECTORIO: tests
################################################################################

# ==============================================================================
# ARCHIVO 13/18: test_config.py
# Directorio: tests
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_config.py
# ==============================================================================

from config import NotificationConfig


def test_singleton_same_instance():
    c1 = NotificationConfig()
    c2 = NotificationConfig()
    assert c1 is c2


def test_update_and_reflects_across_instances(tmp_path):
    cfg = NotificationConfig()
    original_sender = cfg.get_email_config().get("sender")
    cfg.update_email_config({"sender": "test@local"})

    cfg2 = NotificationConfig()
    assert cfg2.get_email_config()["sender"] == "test@local"

    # restore original to avoid side effects for other tests
    cfg.update_email_config({"sender": original_sender})


# ==============================================================================
# ARCHIVO 14/18: test_demo_execution.py
# Directorio: tests
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_demo_execution.py
# ==============================================================================

from examples import demo


def test_run_demo_completes(capsys):
    # Ejecuta la demo completa (es determinista en este repo) y verifica
    # que finaliza con el mensaje esperado.
    demo.run_demo()
    captured = capsys.readouterr()
    assert "DEMO COMPLETADO EXITOSAMENTE" in captured.out


# ==============================================================================
# ARCHIVO 15/18: test_factory_and_notifications.py
# Directorio: tests
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_factory_and_notifications.py
# ==============================================================================

import builtins
from notifications import (
    NotificationFactory,
    EmailNotification,
    PushNotification,
    SMSNotification,
)
from constantes import (
    NOTIFICATION_TYPE_EMAIL,
    NOTIFICATION_TYPE_PUSH,
    NOTIFICATION_TYPE_SMS,
)


def test_factory_creates_known_types():
    e = NotificationFactory.create_notification(NOTIFICATION_TYPE_EMAIL)
    p = NotificationFactory.create_notification(NOTIFICATION_TYPE_PUSH)
    s = NotificationFactory.create_notification(NOTIFICATION_TYPE_SMS)

    assert isinstance(e, EmailNotification)
    assert isinstance(p, PushNotification)
    assert isinstance(s, SMSNotification)


def test_factory_register_custom(tmp_path, capsys):
    # Define a temporary notification class
    class DummyNotification(EmailNotification):
        def send(self, message, recipient):
            print(f"DUMMY:{recipient}:{message}")

    NotificationFactory.register_notification("dummy_test", DummyNotification)
    d = NotificationFactory.create_notification("dummy_test")
    assert isinstance(d, DummyNotification)
    d.send("hola", "user")
    captured = capsys.readouterr()
    assert "DUMMY:user:hola" in captured.out


# ==============================================================================
# ARCHIVO 16/18: test_logger.py
# Directorio: tests
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_logger.py
# ==============================================================================

import os
from logger import NotificationLogger


def test_logger_write_read_and_clear(tmp_path):
    logger = NotificationLogger()
    # use the default log file path
    logger.clear_logs()
    logger.log("email", "daily", "dest", "hello")
    content = logger.get_logs()
    assert "Tipo: email" in content
    # clear and verify
    logger.clear_logs()
    assert logger.get_logs() == "No hay logs registrados."


# ==============================================================================
# ARCHIVO 17/18: test_observer.py
# Directorio: tests
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_observer.py
# ==============================================================================

from observer import EventManager, User, Event
from constantes import EVENT_TYPE_NEW_CONTENT, NOTIFICATION_TYPE_PUSH


def test_user_subscribe_and_receive(capsys):
    manager = EventManager()
    user = User("u1", "Tester", NOTIFICATION_TYPE_PUSH)
    user.add_subscription(EVENT_TYPE_NEW_CONTENT)
    manager.subscribe(user)

    evt = Event(EVENT_TYPE_NEW_CONTENT, "Nueva cosa")
    manager.notify(evt)

    captured = capsys.readouterr()
    # Push strategy prints the message prefixed with (PUSH):
    assert "(PUSH): Nueva cosa" in captured.out or "(PUSH):Nueva cosa" in captured.out


def test_unsubscribed_user_not_receive(capsys):
    manager = EventManager()
    user = User("u2", "NoSub", NOTIFICATION_TYPE_PUSH)
    # no subscription
    manager.subscribe(user)

    evt = Event(EVENT_TYPE_NEW_CONTENT, "Mensaje")
    manager.notify(evt)

    captured = capsys.readouterr()
    assert captured.out.strip() == ""


# ==============================================================================
# ARCHIVO 18/18: test_strategies_and_notifications.py
# Directorio: tests
# Ruta completa: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_strategies_and_notifications.py
# ==============================================================================

from notifications import NotificationFactory
from strategies import DailyEmailStrategy, RealtimePushStrategy
from constantes import NOTIFICATION_TYPE_PUSH, NOTIFICATION_TYPE_EMAIL


def test_change_strategy_and_send(capsys):
    n = NotificationFactory.create_notification(NOTIFICATION_TYPE_PUSH)
    # default strategy should be realtime
    assert n.get_strategy().get_strategy_name() == RealtimePushStrategy().get_strategy_name()
    # change to daily email strategy
    n.set_strategy(DailyEmailStrategy())
    assert n.get_strategy().get_strategy_name() == DailyEmailStrategy().get_strategy_name()
    n.send("Hola", "Usuario")
    captured = capsys.readouterr()
    assert "Programado envio diario" in captured.out



################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 18
# Generado: 2025-11-05 00:12:28
################################################################################
