import QtQuick 2.13
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.4
import QtCharts 2.2
import QtQuick.Dialogs 1.0

import "../components"

Page {
    signal lossreemitted(int epoch, double loss)
    signal totalepochschanged(int epochs)

    Component.onCompleted: {
        control_bridge.epoch_done.connect(trainPage.lossreemitted)
        settings_bridge.epochs_changed.connect(trainPage.totalepochschanged)
    }

    onLossreemitted: {
        yAxisLossSeries.max = Math.max(yAxisLossSeries.max, loss)
        yAxisLossSeries.min = Math.min(yAxisLossSeries.min, loss)
        lossSeries.append(epoch, loss)
    }
    onTotalepochschanged: {
        totalEpochs.value = epochs
    }

    name: "Train"
    id: trainPage
    GridLayout {
        flow: GridLayout.TopToBottom
        rows: 2

        CellBox {
            title: "Datasets"
            GridLayout {
                anchors.fill: parent
                columns: 3
                Label {
                    text: "Folder with train files:"
                    Layout.alignment: Qt.AlignHCenter
                }
                TextField {
                    id: trainPath
                    width: parent.width
                    placeholderText: "Path to train data folder..."
                    selectByMouse: true
                }
                RoundButton {
                    text: "..."
                    Layout.alignment: Qt.AlignHCenter
                    onClicked: () => {
                        trainFileDialog.open()
                    }
                }

                Label {
                    text: "Folder with test files:"
                    Layout.alignment: Qt.AlignHCenter
                }
                TextField {
                    id: testPath
                    width: parent.width
                    placeholderText: "Path to test data folder..."
                    selectByMouse: true
                }
                RoundButton {
                    text: "..."
                    Layout.alignment: Qt.AlignHCenter
                    onClicked: () => {
                        testFileDialog.open()
                    }
                }
            }
        }

        CellBox {
            title: "Network Settings"
            GridLayout {
                anchors.fill: parent
                columns: 2
                Label {
                    text: "Total Training Epochs"
                    Layout.alignment: Qt.AlignHCenter
                }
                SpinBox {
                    id: totalEpochs
                    editable: true
                    from: 1
                    to: 999999
                    Layout.fillWidth: true
                    onValueChanged: settings_bridge.epochs = value
                }

                Label {
                    text: "Batch Size"
                    Layout.alignment: Qt.AlignHCenter
                }
                SpinBox {
                    editable: true
                    value: 32
                    from: 2
                    to: 2048
                    Layout.fillWidth: true
                }

                Label {
                    text: "Neighborhood Size"
                    Layout.alignment: Qt.AlignHCenter
                }
                SpinBox {
                    editable: true
                    value: 2048
                    from: 512
                    to: 8192
                    Layout.fillWidth: true
                }

                Label {
                    text: "Optimization Metric"
                    Layout.alignment: Qt.AlignHCenter
                }
                SpinBox {
                    value: 100
                    Layout.fillWidth: true
                }
            }
        }

        CellBox {
            Layout.rowSpan: 2
            title: "Current Info"
            ColumnLayout {
                anchors.fill: parent

                GridLayout {
                    Layout.alignment: Qt.AlignTop
                    columns: 2

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "Current Epoch"
                    }
                    Label {
                        text: epoch_bridge.epoch
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                    }

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "Train Accuracy"
                    }
                    Label {
                        text: "0 %"
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                    }

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "Train Loss"
                    }
                    Label {
                        text: "0.00"
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                    }

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "Test Accuracy"
                    }
                    Label {
                        text: epoch_bridge.test_accuracy + " %"
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                    }

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "Test Loss"
                    }
                    Label {
                        text: epoch_bridge.test_loss
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                    }

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "mAP"
                    }
                    Label {
                        text: "90%"
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                    }

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "mIoU"
                    }
                    Label {
                        text: "92%"
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                    }

                }

                GridLayout {
                    Layout.alignment: Qt.AlignBottom
                    columns: 2

                    Label {
                        Layout.fillWidth: true
                        horizontalAlignment: Text.AlignLeft
                        text: "Epoch Progress: "
                    }
                    Label {
                        text: epoch_bridge.progress
                        horizontalAlignment: Text.AlignRight
                        Layout.fillWidth: true
                        id: progressLabel
                    }
                    ProgressBar {
                        Layout.fillWidth: true
                        Layout.columnSpan: 2
                        value: epoch_bridge.progress / 100;
                    }
                }
            }
        }

        /**********************************************************
        Graphs
        **********************************************************/
        CellBox {
            Layout.rowSpan: 2; Layout.minimumWidth: 700
            Layout.preferredWidth: height // Keep the ratio right!
            TabBar {
                id: bar
                width: parent.width
                TabButton { text: "Test Loss" }
                TabButton { text: "Accuracies" }
            }
            StackLayout {
                width: parent.width
                height: parent.height - y
                anchors.top: bar.bottom
                currentIndex: bar.currentIndex
                LargeChartView {
                    ValueAxis {
                        id: xAxisLossSeries
                        titleText: "Epoch"
                        min: 0
                        max: settings_bridge.epochs
                        tickCount: settings_bridge.epochs + 1
                        labelFormat: "%.0f"
                    }
                    ValueAxis {
                        id: yAxisLossSeries
                        min: 0
                        max: 0.5
                    }

                    SplineSeries {
                        name: "Test Loss"
                        id: lossSeries
                        axisX: xAxisLossSeries
                        axisY: yAxisLossSeries
                    }
                }

                LargeChartView {
                    ValueAxis {
                        id: valueAxisSplineSeries
                        min: 0
                        max: 5
                        tickCount: 6
                        labelFormat: "%.0f"
                    }

                    SplineSeries {
                        name: "Test Acc."
                        axisX: valueAxisSplineSeries
                        XYPoint { x: 0; y: 0 }
                        XYPoint { x: 1; y: 0.5 }
                        XYPoint { x: 2; y: 0.75 }
                        XYPoint { x: 3; y: 0.87 }
                        XYPoint { x: 4; y: 0.92 }
                        XYPoint { x: 5; y: 0.95 }
                    }
                    SplineSeries {
                        name: "mAP"
                        axisX: valueAxisSplineSeries
                        XYPoint { x: 0; y: 0 }
                        XYPoint { x: 1; y: 0.45 }
                        XYPoint { x: 2; y: 0.80 }
                        XYPoint { x: 3; y: 0.78 }
                        XYPoint { x: 4; y: 0.85 }
                        XYPoint { x: 5; y: 0.90 }
                    }
                    SplineSeries {
                        name: "mIoU"
                        axisX: valueAxisSplineSeries
                        XYPoint { x: 0; y: 0 }
                        XYPoint { x: 1; y: 0.43 }
                        XYPoint { x: 2; y: 0.68 }
                        XYPoint { x: 3; y: 0.84 }
                        XYPoint { x: 4; y: 0.90 }
                        XYPoint { x: 5; y: 0.92 }
                    }
                }
            }
        }

        /**********************************************************
        Pop-Ups
        **********************************************************/
        Popup {
            id: normalPopup
            ColumnLayout {
                anchors.fill: parent
                Label { text: "Normal Popup" }
                CheckBox { text: "E-mail" }
                CheckBox { text: "Calendar" }
                CheckBox { text: "Contacts" }
            }
        }
        Popup {
            id: modalPopup
            modal: true
            ColumnLayout {
                anchors.fill: parent
                Label { text: "Modal Popup" }
                CheckBox { text: "E-mail" }
                CheckBox { text: "Calendar" }
                CheckBox { text: "Contacts" }
            }
        }
        Dialog {
            id: dialog
            title: "Dialog"
            Label { text: "The standard dialog." }
            footer: DialogButtonBox {
                standardButtons: DialogButtonBox.Ok | DialogButtonBox.Cancel
            }
        }

        FileDialog {
            id: trainFileDialog
            title: "Choose a folder..."
            selectFolder: true
            selectMultiple: false
            folder: shortcuts.home
            onAccepted: {
                var path = trainFileDialog.fileUrl.toString()
                // reomve prefix "file:///"
                path = path.replace(/^(file:\/{3})/,"")
                // unescape HTML codes
                var cleanPath = decodeURIComponent(path);
                trainPath.text = cleanPath
            }
        }

        FileDialog {
            id: testFileDialog
            title: "Choose a folder..."
            selectFolder: true
            selectMultiple: false
            folder: shortcuts.home
            onAccepted: {
                var path = testFileDialog.fileUrl.toString()
                // reomve prefix "file:///"
                path = path.replace(/^(file:\/{3})/,"")
                // unescape HTML codes
                var cleanPath = decodeURIComponent(path);
                testPath.text = cleanPath
            }
        }
    }
}