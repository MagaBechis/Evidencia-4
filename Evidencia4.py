import time


class Horno:
    MAX_TEMPERATURA = 250
    MIN_TEMPERATURA = 0

    def __init__(self, modelo, marca, año_fabricación):
        self._modelo = modelo
        self._marca = marca
        self._año_fabricación = año_fabricación
        self._temperatura_actual = 0
        self._estado = "apagado"
        self._temporizador = 0
        self._modo_coccion = None

    @property
    def temperatura_actual(self):
        return self._temperatura_actual

    @property
    def estado(self):
        return self._estado

    @property
    def temporizador(self):
        return self._temporizador

    @property
    def modo_coccion(self):
        return self._modo_coccion

    def encender(self):
        self._estado = "encendido"

    def apagar(self):
        self._estado = "apagado"
        self._temperatura_actual = 0
        self._temporizador = 0
        self._modo_coccion = None

    def controlar_temperatura(self, temperatura):
        """
        Establece la temperatura actual dentro de los límites permitidos.
        """
        if self._estado == "encendido":
            if Horno.MIN_TEMPERATURA <= temperatura <= Horno.MAX_TEMPERATURA:
                self._temperatura_actual = temperatura
            else:
                raise ValueError(
                    f"La temperatura debe estar entre {Horno.MIN_TEMPERATURA} y {Horno.MAX_TEMPERATURA}."
                )
        else:
            raise Exception(
                "El horno debe estar encendido para establecer la temperatura."
            )

    def establecer_temporizador(self, segundos):
        """
        Establece un temporizador en segundos.
        """
        if self._estado == "encendido":
            self._temporizador = segundos
            print(f"Temporizador establecido en {self._temporizador} segundos.")
        else:
            raise Exception(
                "El horno debe estar encendido para establecer un temporizador."
            )

    def iniciar_temporizador(self):
        """
        Inicia el temporizador y cuenta regresivamente.
        """
        if self._temporizador > 0:
            print("Temporizador iniciado.")
            for i in range(self._temporizador, 0, -1):
                print(f"{i} segundos restantes...")
                time.sleep(1)
            print("El tiempo ha expirado.")
            self.apagar()
        else:
            print("El temporizador debe ser establecido primero.")

    def cambiar_modo_coccion(self, modo):
        """
        Cambia el modo de cocción.
        """
        if self._estado == "encendido":
            self._modo_coccion = modo
            print(f"Modo de cocción cambiado a: {self._modo_coccion}")
        else:
            raise Exception(
                "El horno debe estar encendido para cambiar el modo de cocción."
            )

    def __str__(self):
        return (
            f"Horno {self._modelo} de marca {self._marca}, estado: {self._estado}, "
            f"temperatura actual: {self._temperatura_actual}, "
            f"temporizador: {self._temporizador}, modo de cocción: {self._modo_coccion}"
        )

    def obtener_estado(self):
        return {
            "modelo": self._modelo,
            "marca": self._marca,
            "año_fabricación": self._año_fabricación,
            "estado": self._estado,
            "temperatura_actual": self._temperatura_actual,
            "temporizador": self._temporizador,
            "modo_coccion": self._modo_coccion,
        }
