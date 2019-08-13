import os
import sys

from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from res import resources  # load res built by pyrcc5


# Set the QtQuick Style
# Acceptable values: Default, Fusion, Imagine, Material, Universal.
os.environ['QT_QUICK_CONTROLS_STYLE'] = "Material"

# Create an instance of the application
# QApplication MUST be declared in global scope to avoid segmentation fault
app = QApplication(sys.argv)

# Create QML engine
engine = QQmlApplicationEngine()

# Load the qml file into the engine
engine.load(QUrl('res/qml/main.qml'))

# Qml file error handling
if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec_())
