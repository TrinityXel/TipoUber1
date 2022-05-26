# one line to give the program's name and a brief description.
# Copyright © 2022 yourname

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

from clase_uber import Uber, Tipo


def main():
    uber = Uber(estrellas=5, placa="AAA-BBB-CCC",
                marca="Jeep",
                año="2021",
                tipo=Tipo.PREMIUM)

    uber.viaje(30)
    uber.viaje(50)
    uber.set_calificacion(100)
    uber.mostrar()


if __name__ == "__main__":
    main()
