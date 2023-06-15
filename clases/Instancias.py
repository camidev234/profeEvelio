from Instructor import *
from Coordinador import *


o = Instructor("Ing de software", "Desarrollo Movil", "Desarrollador Sr", 80000000, 1, 100, "Camilo", 1000000, 30031230618)
print(o.get_Info())
dos = Instructor("Astronauta", "alunizador", "comandante", 500000000, 2, "A15", "Martin", "luna", 373874)
print(dos.get_Info())
tres = Instructor("futbolista", "mediocampista", "entrenamiento deportivo", 1000000, 3, "El Bicho", "Faustino", "Rusia", 2468473)
print(tres.get_Info())
c = Coordinador("15/06/2023", "oficina 6", "Academico", 3, "sk45", "cazuca", 30237453)
print(c.get_Info())
l = Coordinador("10/06/2001", "cide", 2, "2022", "Carlos", "terreros", 24734937)
print(l.get_Info())
