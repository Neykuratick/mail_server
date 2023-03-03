class EmptyArgumentsError(RuntimeError):
    def __int__(self, arguments: list[str]):
        msg = f"Provide at least one argument of {arguments}"
        super().__init__(msg)
