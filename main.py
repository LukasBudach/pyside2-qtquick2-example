import os
import sys

import time

from PySide2.QtCore import QUrl, QObject, Signal, Slot, Property, QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from res import resources  # load res built by pyrcc5


class EpochBridge(QObject):
    def __init__(self, parent=None):
        super(EpochBridge, self).__init__(parent)
        self._train_acc = '0 %'
        self._epoch = 0
        self._progress = 0

    def _train_acc(self):
        return self._train_acc

    def set_train_acc(self, v):
        self._train_acc = str(v) + ' %'

    @Signal
    def train_acc_changed(self, v):
        pass

    epoch_changed = Signal(int, name='epoch_changed')

    @Property(int, notify=epoch_changed)
    def epoch(self):
        return self._epoch

    @epoch.setter
    def set_epoch(self, v):
        if self._epoch == v:
            return
        self._epoch = v
        self.epoch_changed.emit(v)
        print('Epoch: ' + str(v))

    progress_changed = Signal(int, name='progress_changed')

    @Property(int, notify=progress_changed)
    def progress(self):
        return self._progress

    @progress.setter
    def set_progress(self, v):
        if self._progress == v:
            return
        self._progress = v
        self.progress_changed.emit(v)
        print('Progress: ' + str(v))

    train_acc = Property(str, _train_acc, set_train_acc, notify=train_acc_changed)


class SettingsBridge(QObject):
    def __init__(self, parent=None):
        super(SettingsBridge, self).__init__(parent)
        self._epochs = 10

    def _epochs(self):
        return self._epochs

    def set_epochs(self, v):
        self._epochs = v

    @Signal
    def epochs_changed(self):
        pass

    epochs = Property(int, _epochs, set_epochs, notify=epochs_changed)


class ControlBridge(QObject):
    def __init__(self, epoch_bridge, settings_bridge, parent=None):
        super(ControlBridge, self).__init__(parent)
        self.epoch_bridge = epoch_bridge
        self.settings_bridge = settings_bridge

    @Slot()
    def start_simulation(self):
        for i in range(self.settings_bridge.epochs):
            self.epoch_bridge.epoch = i
            for j in range(101):
                self.epoch_bridge.progress = j
                QCoreApplication.processEvents()
                time.sleep(0.25)

# Set the QtQuick Style
# Acceptable values: Default, Fusion, Imagine, Material, Universal.
os.environ['QT_QUICK_CONTROLS_STYLE'] = "Material"

# Create an instance of the application
# QApplication MUST be declared in global scope to avoid segmentation fault
app = QApplication(sys.argv)

# Create QML engine
engine = QQmlApplicationEngine()

bridges = {
    'epoch_bridge': EpochBridge(),
    'settings_bridge': SettingsBridge()
}

bridges['control_bridge'] = ControlBridge(epoch_bridge=bridges['epoch_bridge'], settings_bridge=bridges['settings_bridge'])

for name in bridges:
    engine.rootContext().setContextProperty(name, bridges[name])

# Load the qml file into the engine
engine.load(QUrl('res/qml/main.qml'))

# Qml file error handling
if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec_())
