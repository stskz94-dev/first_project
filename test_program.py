try:
    import python
except ImportError as error:
    raise AssertionError('Модуль `python` не обнаружен.') from error

EXPECTED_FUNC_NAME = 'say_hello'


def test_say_hello_exists():
    assert hasattr(
        python, EXPECTED_FUNC_NAME
    ), f'Функция `{EXPECTED_FUNC_NAME}` не обнаружена в модуле `python`'


def test_say_hello_run_without_exceptions():
    try:
        python.say_hello()
    except Exception as e:
        raise AssertionError(
            f'При запуске функции `{EXPECTED_FUNC_NAME}` возникло '
            f'исключение: {type(e).__name__}: {e}`'
        ) from e
