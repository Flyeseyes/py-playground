from cli import main


def test_cli_prints_name(capsys):
    main(["Natiq"])
    assert capsys.readouterr().out.strip() == "Hej Natiq!"


def test_cli_upper(capsys):
    main(["Natiq", "--upper"])
    assert capsys.readouterr().out.strip() == "HEJ NATIQ!"
