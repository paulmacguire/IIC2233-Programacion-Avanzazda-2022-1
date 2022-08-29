import sys

from PyQt5.QtWidgets import QApplication

from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego, Martillo
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_postjuego import VentanaPostjuego


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])

    # Instanciación de ventanas
    ventana_inicio = VentanaInicio()
    ventana_juego = VentanaJuego()
    ventana_postjuego = VentanaPostjuego()

    # Instanciación de lógica
    martillo = Martillo()
    logica_inicio = LogicaInicio()
    logica_juego = LogicaJuego(martillo)

    # ~~ Conexiones de señales ~~
    # COMPLETAR

    ventana_inicio.senal_enviar_login.connect(logica_inicio.comprobar_usuario)

    logica_inicio.senal_respuesta_validacion.connect(ventana_inicio.recibir_validacion)

    logica_inicio.senal_abrir_juego.connect(ventana_juego.mostrar_ventana)
    

    ventana_inicio.show()
    app.exec()
