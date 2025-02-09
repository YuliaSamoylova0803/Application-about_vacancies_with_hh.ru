from abc import ABC

from src.saver import JSONSaver, Saver


def test_json_saver_issubclass():
    assert issubclass(JSONSaver, Saver)
    assert issubclass(Saver, ABC)
