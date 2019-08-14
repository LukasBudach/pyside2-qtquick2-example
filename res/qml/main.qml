import QtQuick 2.13
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.4
import QtCharts 2.2

ApplicationWindow {
  title: 'My amazing neural network app'
  visible: true
  minimumHeight: 900
  minimumWidth: 1600
  Material.theme: Material[subTheme.currentText]
  Material.accent: Material[accentColor.currentText]
  Material.primary: Material[primaryColor.currentText]

  header: ToolBar {
    RowLayout {
      anchors.fill: parent
      ToolButton {
        icon.source: '../images/baseline-menu-24px.svg'
        onClicked: sideNav.open()
      }
      Label {
        text: 'Neural network control panel'
        elide: Label.ElideRight
        horizontalAlignment: Qt.AlignHCenter
        verticalAlignment: Qt.AlignVCenter
        Layout.fillWidth: true
      }
      ToolButton {
        text: 'Start Training'
        id: btn_startTraining
        onClicked: () => {
            control_bridge.start_simulation()
            btn_startTraining.enabled = false
        }
      }
      ToolButton { text: 'Pause Training' }
      ToolSeparator {}
      ToolButton {
        icon.source: '../images/baseline-more_vert-24px.svg'
        onClicked: menu.open()
        Menu {
          id: menu
          y: parent.height
          MenuItem { text: 'New...' }
          MenuItem { text: 'Open...' }
          MenuItem { text: 'Save' }
        }
      }
    }
  }
  Drawer {
    id: sideNav
    width: 200
    height: parent.height
    ColumnLayout {
      width: parent.width
      Label {
          text: 'Drawer'
          horizontalAlignment: Text.AlignHCenter
          verticalAlignment: Text.AlignVCenter
          font.pixelSize: 20
          Layout.fillWidth: true
      }
      Repeater {
        model: 5
        SideNavButton {
          icon.source: '../images/baseline-category-24px.svg'
          text: 'List ' + index
          Layout.fillWidth: true
        }
      }
    }
  }
  Pane {
    padding: 10
    anchors.fill: parent
    GridLayout {
      anchors.fill: parent
      flow: GridLayout.TopToBottom
      rows: 3

      CellBox {
        title: 'Datasets'
        GridLayout {
            anchors.fill: parent
            columns: 3
            Label {
                text: 'Train Dataset'
                Layout.alignment: Qt.AlignHCenter
            }
            TextField {
                width: parent.width
                placeholderText: 'Train Data goes here...'
                selectByMouse: true
            }
            RoundButton {
                text: '...'
                Layout.alignment: Qt.AlignHCenter
            }

            Label {
                text: 'Test Dataset'
                Layout.alignment: Qt.AlignHCenter
            }
            TextField {
                width: parent.width
                placeholderText: 'Test Data goes here...'
                selectByMouse: true
            }
            RoundButton {
                text: '...'
                Layout.alignment: Qt.AlignHCenter
            }
        }
      }

      CellBox {
        title: 'Network Settings'
        GridLayout {
            anchors.fill: parent
            columns: 2
            Label {
                text: 'Total Training Epochs'
                Layout.alignment: Qt.AlignHCenter
            }
            SpinBox {
                id: totalEpochs
                editable: true
                value: settings_bridge.epochs
                from: 1
                to: 999999
                Layout.fillWidth: true
                onValueChanged: settings_bridge.epochs = value
                Component.onCompleted: settings_bridge.epochs = value
            }

            Label {
                text: 'Batch Size'
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
                text: 'Neighborhood Size'
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
                text: 'Optimization Metric'
                Layout.alignment: Qt.AlignHCenter
            }
            SpinBox {
                value: 100
                Layout.fillWidth: true
            }
        }
      }

      CellBox {
        Layout.columnSpan: 2; Layout.preferredHeight: 100;
        title: 'Console Output'
        Column {
          // ScrollView will not work if we use ColumnLayout as
          // ColumnLayout always measures its size depending on its
          // contents.
          anchors.fill: parent
          spacing: 10
          ScrollView {
            width: parent.width
            height: 150
            TextArea {
              text: 'Multi-line text editor...\nThis is a new line.'
              selectByMouse: true
              persistentSelection: true
              readOnly: true
            }
          }
        }
      }

      CellBox {
          Layout.rowSpan: 2
          title: 'Current Info'
          ColumnLayout {
              anchors.fill: parent

              GridLayout {
                Layout.alignment: Qt.AlignTop
                columns: 2

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignLeft
                    text: 'Current Epoch'
                }
                Label {
                    text: epoch_bridge.epoch
                    horizontalAlignment: Text.AlignRight
                    Layout.fillWidth: true
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignLeft
                    text: 'Train Accuracy'
                }
                Label {
                    text: epoch_bridge.train_acc
                    horizontalAlignment: Text.AlignRight
                    Layout.fillWidth: true
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignLeft
                    text: 'Train Loss'
                }
                Label {
                    text: '0.03'
                    horizontalAlignment: Text.AlignRight
                    Layout.fillWidth: true
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignLeft
                    text: 'Test Accuracy'
                }
                Label {
                    text: '95.4%'
                    horizontalAlignment: Text.AlignRight
                    Layout.fillWidth: true
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignLeft
                    text: 'Test Loss'
                }
                Label {
                    text: '0.05'
                    horizontalAlignment: Text.AlignRight
                    Layout.fillWidth: true
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignLeft
                    text: 'mAP'
                }
                Label {
                    text: '90%'
                    horizontalAlignment: Text.AlignRight
                    Layout.fillWidth: true
                }

                Label {
                    Layout.fillWidth: true
                    horizontalAlignment: Text.AlignLeft
                    text: 'mIoU'
                }
                Label {
                    text: '92%'
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
                      text: 'Epoch Progress: '
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
        Layout.rowSpan: 3; Layout.minimumWidth: 700
        Layout.preferredWidth: height // Keep the ratio right!
        TabBar {
          id: bar
          width: parent.width
          TabButton { text: 'Test Loss' }
          TabButton { text: 'Accuracies' }
        }
        StackLayout {
          width: parent.width
          height: parent.height - y
          anchors.top: bar.bottom
          currentIndex: bar.currentIndex
          LargeChartView {
            ValueAxis {
              id: valueAxisLossSeries
              min: 0
              max: 5
              tickCount: 6
              labelFormat: '%.0f'
            }

            SplineSeries {
              name: 'Test Loss'
              axisX: valueAxisLossSeries
              XYPoint { x: 0; y: 0 }
              XYPoint { x: 1; y: 2.67 }
              XYPoint { x: 2; y: 1.34 }
              XYPoint { x: 3; y: 0.51 }
              XYPoint { x: 4; y: 0.21 }
              XYPoint { x: 5; y: 0.05 }
            }
          }

          LargeChartView {
            ValueAxis {
              id: valueAxisSplineSeries
              min: 0
              max: 5
              tickCount: 6
              labelFormat: '%.0f'
            }

            SplineSeries {
              name: 'Test Acc.'
              axisX: valueAxisSplineSeries
              XYPoint { x: 0; y: 0 }
              XYPoint { x: 1; y: 0.5 }
              XYPoint { x: 2; y: 0.75 }
              XYPoint { x: 3; y: 0.87 }
              XYPoint { x: 4; y: 0.92 }
              XYPoint { x: 5; y: 0.95 }
            }
            SplineSeries {
              name: 'mAP'
              axisX: valueAxisSplineSeries
              XYPoint { x: 0; y: 0 }
              XYPoint { x: 1; y: 0.45 }
              XYPoint { x: 2; y: 0.80 }
              XYPoint { x: 3; y: 0.78 }
              XYPoint { x: 4; y: 0.85 }
              XYPoint { x: 5; y: 0.90 }
            }
            SplineSeries {
              name: 'mIoU'
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
          Label { text: 'Normal Popup' }
          CheckBox { text: 'E-mail' }
          CheckBox { text: 'Calendar' }
          CheckBox { text: 'Contacts' }
        }
      }
      Popup {
        id: modalPopup
        modal: true
        ColumnLayout {
          anchors.fill: parent
          Label { text: 'Modal Popup' }
          CheckBox { text: 'E-mail' }
          CheckBox { text: 'Calendar' }
          CheckBox { text: 'Contacts' }
        }
      }
      Dialog {
        id: dialog
        title: 'Dialog'
        Label { text: 'The standard dialog.' }
        footer: DialogButtonBox {
          standardButtons: DialogButtonBox.Ok | DialogButtonBox.Cancel
        }
      }
    }
  }

  /**********************************************************
  Footer
  **********************************************************/
  footer: RowLayout {
    width: parent.width
    RowLayout {
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter
      Label { text: 'Theme customization: ' }
      Label {
        id: qtquick2Themes
        objectName: 'qtquick2Themes'
        Layout.fillWidth: true
      }
    }
    RowLayout {
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter
      Label { text: 'QtQuick Charts Themes: ' }
      ComboBox {
        id: qtquickChartsThemes
        model: [
          'ChartThemeLight', 'ChartThemeBlueCerulean',
          'ChartThemeDark', 'ChartThemeBrownSand',
          'ChartThemeBlueNcs', 'ChartThemeHighContrast',
          'ChartThemeBlueIcy', 'ChartThemeQt'
        ]
        Layout.fillWidth: true
        currentIndex: 2
      }
    }
    RowLayout {
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter
      Label { text: 'Sub-Theme: ' }
      ComboBox {
        id: subTheme
        model: ['Dark', 'Light']
        Layout.fillWidth: true
        enabled: true
      }
    }
    RowLayout {
      property var materialColors: [
        'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
        'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime',
        'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Grey',
        'BlueGrey'
      ]
      Layout.margins: 10
      Layout.alignment: Qt.AlignHCenter

      Label { text: 'Primary' }
      ComboBox {
        id: primaryColor
        Layout.fillWidth: true
        enabled: true
        model: parent.materialColors
        currentIndex: 6
      }

      Label { text: 'Accent' }
      ComboBox {
        id: accentColor
        Layout.fillWidth: true
        enabled: true
        model: parent.materialColors
        currentIndex: 7
      }
    }
  }
}