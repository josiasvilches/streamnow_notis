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
