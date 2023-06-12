import pytest


class TestExtras:
    def test_true(self):
        assert True

    @pytest.mark.xfail
    def test_false(self):
        assert False

    @pytest.mark.parametrize('obj',['cook','call','sit'])
    def test_word(self, obj):
        assert obj == 'cook'
