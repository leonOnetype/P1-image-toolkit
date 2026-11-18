import p1_image_toolkit


def test_package_impotable() -> None:
    """Le package s'importe sans erreur"""
    assert p1_image_toolkit is not None


def test_main_runs(capsys) -> None:
    """fa fonction main générée par uv s'exécute et affiche un message"""
    p1_image_toolkit.main()
    sortie = capsys.readouterr().out
    assert "p1-image-toolkit" in sortie
