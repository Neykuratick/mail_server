from typing import Callable
from app.exceptions.empty_arguments import EmptyArgumentsError


def expect_arguments(func: Callable):
    async def wrapper(*args, **kwargs):
        arguments = func.__code__.co_varnames[: func.__code__.co_argcount]  # noqa

        if not kwargs and len(args) < 2:
            raise EmptyArgumentsError(arguments)

        return await func(*args, **kwargs)

    return wrapper
