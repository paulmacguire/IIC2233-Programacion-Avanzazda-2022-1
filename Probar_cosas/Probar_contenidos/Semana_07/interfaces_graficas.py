import sys
from PyQt5.QtWidgets import QWidget, QApplication


class MiVentana(QWidget):
    def __init__(self):
        super().__init__()

        # Definimos la geometría de la ventana.
        # Parámetros: (x_superior_izq, y_superior_izq, ancho, alto)
        self.setGeometry(300, 200, 300, 300)

        # Podemos dar nombre a la ventana (Opcional)
        self.setWindowTitle('Mi Primera Ventana')


if __name__ == '__main__':
    app = QApplication([])    ## Creamos ls base de la app: QApplication
    ventana = MiVentana()     ## Construirmos un QWidget que será nuestra ventana
    ventana.show()            ## Mostramos la ventna
    sys.exit(app.exec_())     ## La aplicación se inicia con app.exec_(). Esto habilita el loop de eventos
                              ## Su valor de retorno es un código de salida que luego lo tome sys.exit()