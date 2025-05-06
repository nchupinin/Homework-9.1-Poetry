from pathlib import Path
from typing import Any, Union

import pytest

from src.decorators import log


# Тестовые функции с аннотациями типов
@log("test_log.txt")
def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


@log("test_log.txt")
def divide(a: Union[int, float], b: Union[int, float]) -> float:
    return a / b


@log()
def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a * b


def test_log_decorator_with_file(tmp_path: Path) -> None:
    """Проверка записи логов в файл."""
    log_file = tmp_path / "test_log.txt"

    @log(str(log_file))
    def test_func(x: int, y: int) -> int:
        return x**y

    test_func(2, 3)

    assert log_file.exists()
    with open(log_file, "r", encoding="utf-8") as f:
        logs = f.read()
        assert "Начало выполнения функции test_func" in logs
        assert "завершилась успешно" in logs


def test_log_decorator_with_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка вывода логов в консоль."""
    multiply(3, 4)

    captured = capsys.readouterr()
    assert "Начало выполнения функции multiply" in captured.out
    assert "завершилась успешно" in captured.out


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (2, 3, 5),  # Успешное сложение
        (10, -5, 5),  # Успешное сложение с отрицательным числом
    ],
)
def test_add_function_with_log(a: int, b: int, expected_result: int, tmp_path: Path) -> None:
    """Проверка функции add с логированием в файл."""
    log_file = tmp_path / "add_log.txt"

    @log(str(log_file))
    def add(a: int, b: int) -> int:
        return a + b

    result = add(a, b)
    assert result == expected_result

    with open(log_file, "r", encoding="utf-8") as f:
        logs = f.read()
        assert f"Результат: {result}" in logs


@pytest.mark.parametrize(
    "a, b, expected_exception",
    [
        (10, 0, ZeroDivisionError),  # Деление на ноль
        ("10", 2, TypeError),  # Неправильный тип данных
    ],
)
def test_divide_function_with_error_log(a: Any, b: Any, expected_exception: type[Exception], tmp_path: Path) -> None:
    """Проверка обработки ошибок в декораторе."""
    log_file = tmp_path / "error_log.txt"

    @log(str(log_file))
    def divide(a: Any, b: Any) -> float:
        return a / b  # type: ignore[operator]

    with pytest.raises(expected_exception):
        divide(a, b)

    with open(log_file, "r", encoding="utf-8") as f:
        logs = f.read()
        assert f"вызвала ошибку {expected_exception.__name__}" in logs


def test_log_without_filename(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка, что без filename логи выводятся в консоль."""

    @log()
    def subtract(a: int, b: int) -> int:
        return a - b

    result = subtract(5, 3)
    assert result == 2

    captured = capsys.readouterr()
    assert "Начало выполнения функции subtract" in captured.out
    assert "завершилась успешно" in captured.out
