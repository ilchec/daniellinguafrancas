def test_valid(cldf_dataset, cldf_logger):
    assert cldf_dataset.validate(log=cldf_logger)


def test_forms(cldf_dataset):
    assert len(list(cldf_dataset["FormTable"])) == 16048
    assert any(f["Form"] == "č'ianč'vela" for f in cldf_dataset["FormTable"])


def test_parameters(cldf_dataset):
    assert len(list(cldf_dataset["ParameterTable"])) == 160


def test_languages(cldf_dataset):
    assert len(list(cldf_dataset["LanguageTable"])) == 96


def test_cognates(cldf_dataset):
    assert len(list(cldf_dataset["CognateTable"])) == 16048
    assert any(f["Form"] == "лъанц1ц1и" for f in cldf_dataset["CognateTable"])
