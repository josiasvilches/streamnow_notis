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
