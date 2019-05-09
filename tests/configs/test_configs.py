import pathlib
from src.config.yaml import Config
import pytest


@pytest.fixture(scope="package")
def config_file_location():
    return pathlib.Path(__file__).parents[1] \
        .joinpath("resources") \
        .joinpath("fake_config.yaml")


def test_config_imports_file(config_file_location):
    """
    Checks that the file imports and the version is brought in
    """

    assert Config(str(config_file_location)).file_location == "E:\\A\\iMaterialistFiles\\"
