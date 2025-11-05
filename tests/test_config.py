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
