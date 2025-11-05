import importlib


def test_run_demo_completes(capsys):
    # Ejecuta la demo integrada en main.py y verifica que finaliza correctamente.
    main = importlib.import_module('main')
    main.run_demo()
    captured = capsys.readouterr()
    assert "DEMO COMPLETADO EXITOSAMENTE" in captured.out
