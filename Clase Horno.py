from Evidencia4 import Horno


mi_horno = Horno(modelo="EOC3540X", marca="Electrolux", año_fabricación=2020)

mi_horno.encender()
print(mi_horno)

try:
    mi_horno.controlar_temperatura(180)
    print(f"Temperatura actual: {mi_horno.temperatura_actual}°C")
except ValueError as e:
    print(e)

try:
    mi_horno.establecer_temporizador(10)
except Exception as e:
    print(e)

try:
    mi_horno.cambiar_modo_coccion("Asar")
except Exception as e:
    print(e)

mi_horno.iniciar_temporizador()

print(mi_horno)
