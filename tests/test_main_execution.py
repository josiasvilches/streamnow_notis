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
