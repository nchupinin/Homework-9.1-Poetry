import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор логирует работу функции в консоль или файл.
    Args:
        filename: Путь к файлу для логирования. Если None, логи выводятся в консоль.
    Returns:
        Декоратор, который оборачивает целевую функцию.
    """

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Логирование начала выполнения
            start_message = f"Начало выполнения функции {function.__name__} с аргументами {args}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(start_message + "\n")
            else:
                print(start_message)

            try:
                result = function(*args, **kwargs)
                # Логирование успешного завершения
                success_message = f"Функция {function.__name__} завершилась успешно. Результат: {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(success_message + "\n")
                else:
                    print(success_message)
                return result

            except Exception as e:
                # Логирование ошибки
                error_message = (
                    f"Функция {function.__name__} вызвала ошибку {type(e).__name__} "
                    f"с аргументами {args}, {kwargs}. Ошибка: {str(e)}"
                )
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(error_message + "\n")
                else:
                    print(error_message)
                raise

        return wrapper

    return decorator
