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
