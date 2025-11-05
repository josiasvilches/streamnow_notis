"""
Archivo integrador generado automaticamente
Directorio: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests
Fecha: 2025-11-05 00:29:45
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: test_config.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_config.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 2/7: test_demo_execution.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_demo_execution.py
# ================================================================================

import importlib


def test_run_demo_completes(capsys):
    # Ejecuta la demo integrada en main.py y verifica que finaliza correctamente.
    main = importlib.import_module('main')
    main.run_demo()
    captured = capsys.readouterr()
    assert "DEMO COMPLETADO EXITOSAMENTE" in captured.out


# ================================================================================
# ARCHIVO 3/7: test_factory_and_notifications.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_factory_and_notifications.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 4/7: test_logger.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_logger.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 5/7: test_main_execution.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_main_execution.py
# ================================================================================

import importlib


def test_main_runs_and_outputs_complete_message(capsys):
    # Import main module freshly to ensure functions are available
    main = importlib.import_module('main')

    # Run main (which delegates to run_demo) and capture stdout
    main.main()

    captured = capsys.readouterr()
    out = captured.out

    # Check for key strings printed by the demo
    assert "Iniciando demo de notificaciones StreamNow" in out
    assert "DEMO COMPLETADO EXITOSAMENTE" in out


# ================================================================================
# ARCHIVO 6/7: test_observer.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_observer.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 7/7: test_strategies_and_notifications.py
# Ruta: C:\Josias\UM\3ro\DisenoSistemas\parcial 29-10\tests\test_strategies_and_notifications.py
# ================================================================================

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


