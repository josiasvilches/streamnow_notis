from examples import demo


def test_run_demo_completes(capsys):
    # Ejecuta la demo completa (es determinista en este repo) y verifica
    # que finaliza con el mensaje esperado.
    demo.run_demo()
    captured = capsys.readouterr()
    assert "DEMO COMPLETADO EXITOSAMENTE" in captured.out
