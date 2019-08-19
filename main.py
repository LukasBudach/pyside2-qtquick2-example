import os
import sys

import time
import math

from PySide2.QtCore import QUrl, QObject, Signal, Slot, Property, QCoreApplication
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from res import resources  # load res built by pyrcc5


class EpochBridge(QObject):
    def __init__(self, parent=None):
        super(EpochBridge, self).__init__(parent)
        self._test_acc = 0
        self._test_loss = 0
        self._epoch = 0
        self._progress = 0

    test_acc_changed = Signal(float, name='test_acc_changed')

    @Property(float, notify=test_acc_changed)
    def test_accuracy(self):
        return self._test_acc

    @test_accuracy.setter
    def set_test_accuracy(self, v):
        self._test_acc = v
        self.test_acc_changed.emit(v)

    test_loss_changed = Signal(float, name='test_loss_changed')

    @Property(float, notify=test_loss_changed)
    def test_loss(self):
        return self._test_loss

    @test_loss.setter
    def set_test_loss(self, v):
        self._test_loss = math.trunc(v * 100) / 100.0
        self.test_loss_changed.emit(v)

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


class SettingsBridge(QObject):
    def __init__(self, parent=None):
        super(SettingsBridge, self).__init__(parent)
        self._epochs = 5

    epochs_changed = Signal(int, name='epochs_changed')

    @Property(int, notify=epochs_changed)
    def epochs(self):
        return self._epochs

    @epochs.setter
    def set_epochs(self, v):
        self._epochs = v
        self.epochs_changed.emit(v)


class ControlBridge(QObject):
    def __init__(self, epoch_bridge, settings_bridge, parent=None):
        super(ControlBridge, self).__init__(parent)
        self.epoch_bridge = epoch_bridge
        self.settings_bridge = settings_bridge

    epoch_done = Signal(int, float, name='epoch_done')
    log_event = Signal(str, name='log_event')

    @Slot()
    def start_simulation(self):
        for i in range(1, (self.settings_bridge.epochs + 1)):
            self.epoch_bridge.epoch = i
            for j in range(101):
                self.epoch_bridge.progress = j
                QCoreApplication.processEvents()
                time.sleep(0.01)
            self.epoch_bridge.test_accuracy = min((i*i) * 3.978, 100)
            self.epoch_bridge.test_loss = 1/i
            self.epoch_done.emit(self.epoch_bridge.epoch, self.epoch_bridge.test_loss)
            self.log_event.emit('Epoch ' + str(i) + ' done')


# Set the QtQuick configuration file path
os.environ['QT_QUICK_CONTROLS_CONF'] = "res/qml/qtquickcontrols2.conf"

# Need to set an organization name in order to suppress warning thrown
# see https://forum.qt.io/topic/104546/qml-file-dialog-warning
QCoreApplication.setOrganizationName("Some organization")

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
