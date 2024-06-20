# ------------- Importaciones -----------
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# ------------- Crear aplicación PyQt5 ---------
app = QApplication(sys.argv)

# -------------- Crear una ventana simple ------------------
window = QWidget()
window.setWindowTitle('Mi primera aplicación PyQt')
window.setGeometry(100, 100, 400, 300) #(pos x, pos y | width, height)

# -------------- Mostrar la ventana + Ejecutar aplicación ----------------
window.show()
sys.exit(app.exec_())