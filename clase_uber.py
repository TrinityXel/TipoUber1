# Copyright © 2022 TrinityXel

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
from enum import Enum


class Estado(Enum):
    LIBRE = 0
    OCUPADO = 1
    REPARACION = 2


class Tipo(Enum):
    ECONOMICO = 0
    PREMIUM = 1


class Uber(object):
    """docstring for Uber"""
    def __init__(self, estrellas: int = 5, **kwargs):

        # TODO: Crear funcion para comprobar llaves vacias
        # Constantes
        self._kwargs = kwargs
        # Por si necesitas acceder individualmente
        # self._placa = kwargs["placa"]
        # self._marca = kwargs["marca"]
        # self._año = kwargs["año"]
        self._tipo = kwargs["tipo"]

        # Variables
        self._estado = Estado.LIBRE
        self._viajes = 0
        self._montoActual = 0
        self._montoTotal = 0
        self._estrellas = estrellas

    def mostrar(self):
        linea = ""
        for llave, valor in self._kwargs.items():
            linea += "{}: {}\n".format(llave, valor)

        linea += "Viajes: {}\n".format(self._viajes)
        linea += "Monto: ${:,}\n".format(self._montoActual)
        linea += "Calificacion:"

        for _ in range(self._estrellas):
            linea += " ☆"

        linea += "\nRecaudado: ${:,}\n".format(self._montoTotal)
        linea += "Estado: {}".format(self.get_estado())

        print(linea)

    def reset(self):
        """
        Indica que solo se ponga en 0 los Viajes
        modificar si también ocupa el monto, recaudado, etc.
        """
        self._viajes = 0

    def enviar_reparacion(self):
        """docstring for enviar_reparacion"""
        self._estado = Estado.REPARACION

    def recibir_reparacion(self):
        """docstring for recibir_reparacion"""
        self._estado = Estado.LIBRE

    def viaje(self, kilometros: int):
        """
            Calculará el costo total del viaje
            dependiendo del tipo y kilometraje

        """
        precio = (500, 300) [self._tipo == Tipo.ECONOMICO]

        self._viajes += 1
        self._montoActual = precio*kilometros
        self._montoTotal += self._montoActual

    def set_calificacion(self, calificacion):
        """
        Calculará el promedio en base a 
        calificacion actual y nueva
        Tomará como calificacion máxima 5, 
        aunque ingrese número mayor
        """
        calificacion = 5 if calificacion > 5 else calificacion
        estrellas = (self._estrellas + calificacion) // 2
        self._estrellas = estrellas

    def get_tipo(self):
        return self._tipo

    def get_estado(self):
        estado = "Libre"
        if self._estado == Estado.OCUPADO:
            estado = "Ocupado"
        elif self._estado == Estado.REPARACION:
            estado = "En reparación"

        return estado

    def get_viajes(self):
        return self._viajes
