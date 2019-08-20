import QtQuick 2.13
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.4
import QtQuick.Controls.Material 2.4
import QtQuick.Dialogs 1.0
import QtQuick.Controls.Styles 1.4

import "components"
import "pages"

ApplicationWindow {
    id: mainWindow
    title: "My amazing neural network app"
    visible: true
    minimumHeight: 900
    minimumWidth: 1600
    Material.theme: Material[subTheme.currentText]
    Material.accent: Material[accentColor.currentText]
    Material.primary: Material[primaryColor.currentText]

    signal consolereemitted(string log)

    Component.onCompleted: {
        console_stream.event_logged.connect(mainWindow.consolereemitted)
    }

    onConsolereemitted: {
        consoleTextfield.append(log)
    }


    header: ToolBar {
        RowLayout {
            anchors.fill: parent
            ToolButton {
            icon.source: "../images/baseline-menu-24px.svg"
            onClicked: sideNav.open()
            }
            Label {
                text: "Neural network control panel"
                elide: Label.ElideRight
                horizontalAlignment: Qt.AlignHCenter
                verticalAlignment: Qt.AlignVCenter
                Layout.fillWidth: true
            }
            ToolButton {
                text: "Start Training"
                id: btn_startTraining
                onClicked: () => {
                    btn_startTraining.enabled = false
                    control_bridge.start_simulation()
                }
            }
            ToolButton { text: "Pause Training" }
            ToolSeparator {}
            ToolButton {
                icon.source: "../images/baseline-more_vert-24px.svg"
                onClicked: menu.open()
                Menu {
                    id: menu
                    y: parent.height
                    MenuItem { text: "New..." }
                    MenuItem { text: "Open..." }
                    MenuItem { text: "Save" }
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
                text: "Drawer"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.pixelSize: 20
                Layout.fillWidth: true
            }
            Repeater {
                model: 5
                SideNavButton {
                    icon.source: "../images/baseline-category-24px.svg"
                    text: "List " + index
                    Layout.fillWidth: true
                }
            }
        }
    }
    Pane {
        id: body
        padding: 10
        anchors.fill: parent
        ColumnLayout {
            anchors.fill: parent
            NoteBook {
                Preprocess {}
                Train {}
                Predict {}
            }

            CellBox {
                Layout.preferredHeight: 100;
                title: "Console Output"
                ScrollView {
                    anchors.fill: parent
                    TextArea {
                        id: consoleTextfield
                        placeholderText: "Console output..."
                        selectByMouse: true
                        persistentSelection: true
                        readOnly: true
                        wrapMode: Text.WordWrap
                    }
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
            Label { text: "Theme customization: " }
            Label {
                id: qtquick2Themes
                objectName: "qtquick2Themes"
                Layout.fillWidth: true
            }
        }
        RowLayout {
            Layout.margins: 10
            Layout.alignment: Qt.AlignHCenter
            Label { text: "QtQuick Charts Themes: " }
            ComboBox {
                id: qtquickChartsThemes
                model: [
                    "ChartThemeLight", "ChartThemeBlueCerulean",
                    "ChartThemeDark", "ChartThemeBrownSand",
                    "ChartThemeBlueNcs", "ChartThemeHighContrast",
                    "ChartThemeBlueIcy", "ChartThemeQt"
                ]
                Layout.fillWidth: true
                currentIndex: 2
            }
        }
        RowLayout {
            Layout.margins: 10
            Layout.alignment: Qt.AlignHCenter
            Label { text: "Sub-Theme: " }
            ComboBox {
                id: subTheme
                model: ["Dark", "Light"]
                Layout.fillWidth: true
                enabled: true
            }
        }
        RowLayout {
            property var materialColors: [
                "Red", "Pink", "Purple", "DeepPurple", "Indigo", "Blue",
                "LightBlue", "Cyan", "Teal", "Green", "LightGreen", "Lime",
                "Yellow", "Amber", "Orange", "DeepOrange", "Brown", "Grey",
                "BlueGrey"
            ]
            Layout.margins: 10
            Layout.alignment: Qt.AlignHCenter

            Label { text: "Primary" }
            ComboBox {
                id: primaryColor
                Layout.fillWidth: true
                enabled: true
                model: parent.materialColors
                currentIndex: 6
            }

            Label { text: "Accent" }
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