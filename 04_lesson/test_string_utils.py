from string_utils import StringUtils
import pytest


@pytest.fixture
def utils():
    
    return StringUtils()


# Тесты для метода reverse
def test_reverse(utils):
    # Положительные случаи
    assert utils.reverse('hello') == 'olleh'
    assert utils.reverse('world') == 'dlrow'

    # Негативные случаи
    with pytest.raises(TypeError):
        utils.reverse(123)  # Некорректный тип данных


# Тесты для метода uppercase
def test_uppercase(utils):
    # Положительные случаи
    assert utils.uppercase('hello') == 'HELLO'
    assert utils.uppercase('wOrLd') == 'WORLD'

    # Негативный случай
    with pytest.raises(AttributeError):
        utils.uppercase(None)  # Некорректный тип данных


# Тесты для метода lowercase
def test_lowercase(utils):
    # Положительные случаи
    assert utils.lowercase('HELLO') == 'hello'
    assert utils.lowercase('WoRlD') == 'world'

    # Негативный случай
    with pytest.raises(AttributeError):
        utils.lowercase([1, 2])  # Некорректный тип данных


# Тесты для метода trim
def test_trim(utils):
    # Положительные случаи
    assert utils.trim('   hello   ') == 'hello'
    assert utils.trim('\n\nhello\t') == 'hello'

    # Негативный случай
    with pytest.raises(AttributeError):
        utils.trim({'key': 'value'})  # Некорректный тип данных
