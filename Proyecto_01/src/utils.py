def saludo(nombre: str) -> str:
    """
    Retorna un saludo cordial para el nombre proveído.
    """
    if not nombre:
        return "¡Hola, mundo!"
    return f"¡Hola, {nombre}!"


def sumar(a: float, b: float) -> float:
    """
    Retorna la suma de dos números.
    """
    return a + b
