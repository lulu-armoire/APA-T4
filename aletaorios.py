"""
Lulu Armoire Palomar 
Tasca 4
"""

class Aleat:
    """
    Clase que implementa un iterador de números aleatorios usando el algoritmo LGC.

    Atributos:
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        semilla (int): Valor inicial x0 (0≤x0<m).
        _x (int): Estado actual del generador.

    Métodos:
        __next__(): Devuelve el siguiente número aleatorio.
        __call__(semilla): Reinicia la secuencia con una nueva semilla.

    Ejemplos:
        >>> rand = Aleat(m=32, a=9, c=13, x0=11)
        >>> for _ in range(4):
        ...     print(next(rand))
        16
        29
        18
        15
        >>> rand(29)
        >>> for _ in range(4):
        ...     print(next(rand))
        18
        15
        20
        1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """
        Inicializa el generador con los parámetros dados.
        
        Args:
            m (int): Módulo 
            a (int): Multiplicador.
            c (int): Incremento.
            x0 (int): Semilla inicial (por defecto 1212121).
        """
        self.m = m
        self.a = a
        self.c = c
        self.semilla = x0
        self._x = x0

    def __next__(self):
        """
        Genera y devuelve el siguiente número aleatorio de la secuencia.
        """
        self._x = (self.a * self._x + self.c) % self.m
        return self._x

    def __call__(self, semilla):
        """
        Reinicia la secuencia con una nueva semilla.

        Argumentos:
            semilla (int): Nueva semilla para reiniciar el generador.
        """
        self.semilla = semilla
        self._x = semilla


def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora que usa el algoritmo LGC para números aleatorios.

    Argumentos:
        m (int): Módulo (>0). 
        a (int): Multiplicador (0<a<m).
        c (int): Incremento (0≤c<m).
        x0 (int): Semilla inicial (0≤x0<m).

    Ejemplos: 
        >>> rand = aleat(m=64, a=5, c=46, x0=36)
        >>> for _ in range(4):
        ...     print(next(rand))
        34
        24
        38
        44
        >>> rand.send(24)
        38
        >>> for _ in range(4):
        ...     print(next(rand))
        44
        10
        32
        14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        # send() permite reiniciar con una nueva semilla
        nueva_semilla = yield x
        if nueva_semilla is not None:
            x = nueva_semilla


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)