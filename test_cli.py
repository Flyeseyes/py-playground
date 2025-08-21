import sys
from cli import main

def test_cli_prints_name(capsys, monkeypatch):
    # låtsas som att programmet körts så här:  cli.py Natiq
    monkeypatch.setattr(sys, "argv", ["cli.py", "Natiq"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hej Natiq!"
