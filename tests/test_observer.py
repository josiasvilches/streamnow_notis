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
