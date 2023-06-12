import pytest


class TestExtras:
    def test_true(self):
        assert True

    @pytest.mark.xfail
    def test_false(self):
        assert False
