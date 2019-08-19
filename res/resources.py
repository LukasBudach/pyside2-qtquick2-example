# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Do Aug 15 10:03:21 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xf0\
i\
mport QtCharts 2\
.2\x0d\x0a\x0d\x0aChartView \
{\x0d\x0a  animationOp\
tions: ChartView\
.SeriesAnimation\
s\x0d\x0a  antialiasin\
g: true\x0d\x0a  margi\
ns.top: 0\x0d\x0a  mar\
gins.bottom: 0\x0d\x0a\
  margins.left: \
0\x0d\x0a  margins.rig\
ht: 0\x0d\x0a  theme: \
ChartView[qtquic\
kChartsThemes.cu\
rrentText]\x0d\x0a}\x0d\x0a\
\x00\x00\x00h\
i\
mport QtQuick.Co\
ntrols 2.4\x0d\x0a\x0d\x0aBu\
tton {\x0d\x0a  flat: \
true\x0d\x0a  backgrou\
nd.anchors.fill:\
 this\x0d\x0a  spacing\
: 40\x0d\x0a}\
\x00\x00\x00\xaa\
i\
mport QtQuick.Co\
ntrols 2.4\x0d\x0aimpo\
rt QtQuick.Layou\
ts 1.11\x0d\x0a\x0d\x0aGroup\
Box {\x0d\x0a  Layout.\
fillWidth: true\x0d\
\x0a  Layout.fillHe\
ight: true\x0d\x0a  La\
yout.minimumWidt\
h: 200\x0d\x0a  clip: \
true\x0d\x0a}\x0d\x0a\
\x00\x00<\xa1\
i\
mport QtQuick 2.\
13\x0d\x0aimport QtQui\
ck.Layouts 1.11\x0d\
\x0aimport QtQuick.\
Controls 2.4\x0d\x0aim\
port QtQuick.Con\
trols.Material 2\
.4\x0d\x0aimport QtCha\
rts 2.2\x0d\x0aimport \
QtQuick.Dialogs \
1.0\x0d\x0a\x0d\x0aApplicati\
onWindow {\x0d\x0a  id\
: mainWindow\x0d\x0a  \
title: 'My amazi\
ng neural networ\
k app'\x0d\x0a  visibl\
e: true\x0d\x0a  minim\
umHeight: 900\x0d\x0a \
 minimumWidth: 1\
600\x0d\x0a  Material.\
theme: Material[\
subTheme.current\
Text]\x0d\x0a  Materia\
l.accent: Materi\
al[accentColor.c\
urrentText]\x0d\x0a  M\
aterial.primary:\
 Material[primar\
yColor.currentTe\
xt]\x0d\x0a\x0d\x0a  signal \
lossreemitted(in\
t epoch, double \
loss)\x0d\x0a  signal \
consolereemitted\
(string log)\x0d\x0a\x0d\x0a\
  Component.onCo\
mpleted: {\x0d\x0a    \
  control_bridge\
.epoch_done.conn\
ect(mainWindow.l\
ossreemitted)\x0d\x0a \
     control_bri\
dge.log_event.co\
nnect(mainWindow\
.consolereemitte\
d)\x0d\x0a  }\x0d\x0a  onLos\
sreemitted: {\x0d\x0a \
     yAxisLossSe\
ries.max = Math.\
max(yAxisLossSer\
ies.max, loss)\x0d\x0a\
      yAxisLossS\
eries.min = Math\
.min(yAxisLossSe\
ries.min, loss)\x0d\
\x0a      lossSerie\
s.append(epoch, \
loss)\x0d\x0a  }\x0d\x0a  on\
Consolereemitted\
: {\x0d\x0a      conso\
leTextfield.appe\
nd(log)\x0d\x0a  }\x0d\x0a\x0d\x0a\
  header: ToolBa\
r {\x0d\x0a    RowLayo\
ut {\x0d\x0a      anch\
ors.fill: parent\
\x0d\x0a      ToolButt\
on {\x0d\x0a        ic\
on.source: '../i\
mages/baseline-m\
enu-24px.svg'\x0d\x0a \
       onClicked\
: sideNav.open()\
\x0d\x0a      }\x0d\x0a     \
 Label {\x0d\x0a      \
  text: 'Neural \
network control \
panel'\x0d\x0a        \
elide: Label.Eli\
deRight\x0d\x0a       \
 horizontalAlign\
ment: Qt.AlignHC\
enter\x0d\x0a        v\
erticalAlignment\
: Qt.AlignVCente\
r\x0d\x0a        Layou\
t.fillWidth: tru\
e\x0d\x0a      }\x0d\x0a    \
  ToolButton {\x0d\x0a\
        text: 'S\
tart Training'\x0d\x0a\
        id: btn_\
startTraining\x0d\x0a \
       onClicked\
: () => {\x0d\x0a     \
       btn_start\
Training.enabled\
 = false\x0d\x0a      \
      control_br\
idge.start_simul\
ation()\x0d\x0a       \
 }\x0d\x0a      }\x0d\x0a   \
   ToolButton { \
text: 'Pause Tra\
ining' }\x0d\x0a      \
ToolSeparator {}\
\x0d\x0a      ToolButt\
on {\x0d\x0a        ic\
on.source: '../i\
mages/baseline-m\
ore_vert-24px.sv\
g'\x0d\x0a        onCl\
icked: menu.open\
()\x0d\x0a        Menu\
 {\x0d\x0a          id\
: menu\x0d\x0a        \
  y: parent.heig\
ht\x0d\x0a          Me\
nuItem { text: '\
New...' }\x0d\x0a     \
     MenuItem { \
text: 'Open...' \
}\x0d\x0a          Men\
uItem { text: 'S\
ave' }\x0d\x0a        \
}\x0d\x0a      }\x0d\x0a    \
}\x0d\x0a  }\x0d\x0a  Drawer\
 {\x0d\x0a    id: side\
Nav\x0d\x0a    width: \
200\x0d\x0a    height:\
 parent.height\x0d\x0a\
    ColumnLayout\
 {\x0d\x0a      width:\
 parent.width\x0d\x0a \
     Label {\x0d\x0a  \
        text: 'D\
rawer'\x0d\x0a        \
  horizontalAlig\
nment: Text.Alig\
nHCenter\x0d\x0a      \
    verticalAlig\
nment: Text.Alig\
nVCenter\x0d\x0a      \
    font.pixelSi\
ze: 20\x0d\x0a        \
  Layout.fillWid\
th: true\x0d\x0a      \
}\x0d\x0a      Repeate\
r {\x0d\x0a        mod\
el: 5\x0d\x0a        S\
ideNavButton {\x0d\x0a\
          icon.s\
ource: '../image\
s/baseline-categ\
ory-24px.svg'\x0d\x0a \
         text: '\
List ' + index\x0d\x0a\
          Layout\
.fillWidth: true\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a    }\x0d\x0a  }\
\x0d\x0a  Pane {\x0d\x0a    \
padding: 10\x0d\x0a   \
 anchors.fill: p\
arent\x0d\x0a    GridL\
ayout {\x0d\x0a      a\
nchors.fill: par\
ent\x0d\x0a      flow:\
 GridLayout.TopT\
oBottom\x0d\x0a      r\
ows: 3\x0d\x0a\x0d\x0a      \
CellBox {\x0d\x0a     \
   title: 'Datas\
ets'\x0d\x0a        Gr\
idLayout {\x0d\x0a    \
        anchors.\
fill: parent\x0d\x0a  \
          column\
s: 3\x0d\x0a          \
  Label {\x0d\x0a     \
           text:\
 'Folder with tr\
ain files:'\x0d\x0a   \
             Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
            }\x0d\x0a \
           TextF\
ield {\x0d\x0a        \
        id: trai\
nPath\x0d\x0a         \
       width: pa\
rent.width\x0d\x0a    \
            plac\
eholderText: 'Pa\
th to train data\
 folder...'\x0d\x0a   \
             sel\
ectByMouse: true\
\x0d\x0a            }\x0d\
\x0a            Rou\
ndButton {\x0d\x0a    \
            text\
: '...'\x0d\x0a       \
         Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a    \
            onCl\
icked: () => {\x0d\x0a\
                \
    fileDialog.o\
pen()\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a\x0d\x0a     \
       Label {\x0d\x0a\
                \
text: 'Folder wi\
th test files:'\x0d\
\x0a               \
 Layout.alignmen\
t: Qt.AlignHCent\
er\x0d\x0a            \
}\x0d\x0a            T\
extField {\x0d\x0a    \
            plac\
eholderText: 'Pa\
th to test data \
folder...'\x0d\x0a    \
            sele\
ctByMouse: true\x0d\
\x0a            }\x0d\x0a\
            Roun\
dButton {\x0d\x0a     \
           text:\
 '...'\x0d\x0a        \
        Layout.a\
lignment: Qt.Ali\
gnHCenter\x0d\x0a     \
       }\x0d\x0a      \
  }\x0d\x0a      }\x0d\x0a\x0d\x0a\
      CellBox {\x0d\
\x0a        title: \
'Network Setting\
s'\x0d\x0a        Grid\
Layout {\x0d\x0a      \
      anchors.fi\
ll: parent\x0d\x0a    \
        columns:\
 2\x0d\x0a            \
Label {\x0d\x0a       \
         text: '\
Total Training E\
pochs'\x0d\x0a        \
        Layout.a\
lignment: Qt.Ali\
gnHCenter\x0d\x0a     \
       }\x0d\x0a      \
      SpinBox {\x0d\
\x0a               \
 id: totalEpochs\
\x0d\x0a              \
  editable: true\
\x0d\x0a              \
  value: setting\
s_bridge.epochs\x0d\
\x0a               \
 from: 1\x0d\x0a      \
          to: 99\
9999\x0d\x0a          \
      Layout.fil\
lWidth: true\x0d\x0a  \
              on\
ValueChanged: se\
ttings_bridge.ep\
ochs = value\x0d\x0a  \
              Co\
mponent.onComple\
ted: settings_br\
idge.epochs = va\
lue\x0d\x0a           \
 }\x0d\x0a\x0d\x0a          \
  Label {\x0d\x0a     \
           text:\
 'Batch Size'\x0d\x0a \
               L\
ayout.alignment:\
 Qt.AlignHCenter\
\x0d\x0a            }\x0d\
\x0a            Spi\
nBox {\x0d\x0a        \
        editable\
: true\x0d\x0a        \
        value: 3\
2\x0d\x0a             \
   from: 2\x0d\x0a    \
            to: \
2048\x0d\x0a          \
      Layout.fil\
lWidth: true\x0d\x0a  \
          }\x0d\x0a\x0d\x0a \
           Label\
 {\x0d\x0a            \
    text: 'Neigh\
borhood Size'\x0d\x0a \
               L\
ayout.alignment:\
 Qt.AlignHCenter\
\x0d\x0a            }\x0d\
\x0a            Spi\
nBox {\x0d\x0a        \
        editable\
: true\x0d\x0a        \
        value: 2\
048\x0d\x0a           \
     from: 512\x0d\x0a\
                \
to: 8192\x0d\x0a      \
          Layout\
.fillWidth: true\
\x0d\x0a            }\x0d\
\x0a\x0d\x0a            L\
abel {\x0d\x0a        \
        text: 'O\
ptimization Metr\
ic'\x0d\x0a           \
     Layout.alig\
nment: Qt.AlignH\
Center\x0d\x0a        \
    }\x0d\x0a         \
   SpinBox {\x0d\x0a  \
              va\
lue: 100\x0d\x0a      \
          Layout\
.fillWidth: true\
\x0d\x0a            }\x0d\
\x0a        }\x0d\x0a    \
  }\x0d\x0a\x0d\x0a      Cel\
lBox {\x0d\x0a        \
Layout.columnSpa\
n: 2; Layout.pre\
ferredHeight: 10\
0;\x0d\x0a        titl\
e: 'Console Outp\
ut'\x0d\x0a        Scr\
ollView {\x0d\x0a     \
     anchors.fil\
l: parent\x0d\x0a     \
     TextArea {\x0d\
\x0a            anc\
hors.fill: paren\
t\x0d\x0a            i\
d: consoleTextfi\
eld\x0d\x0a           \
 placeholderText\
: 'Console outpu\
t...'\x0d\x0a         \
   selectByMouse\
: true\x0d\x0a        \
    persistentSe\
lection: true\x0d\x0a \
           readO\
nly: true\x0d\x0a     \
     }\x0d\x0a        \
}\x0d\x0a      }\x0d\x0a\x0d\x0a  \
    CellBox {\x0d\x0a \
         Layout.\
rowSpan: 2\x0d\x0a    \
      title: 'Cu\
rrent Info'\x0d\x0a   \
       ColumnLay\
out {\x0d\x0a         \
     anchors.fil\
l: parent\x0d\x0a\x0d\x0a   \
           GridL\
ayout {\x0d\x0a       \
         Layout.\
alignment: Qt.Al\
ignTop\x0d\x0a        \
        columns:\
 2\x0d\x0a\x0d\x0a          \
      Label {\x0d\x0a \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
               h\
orizontalAlignme\
nt: Text.AlignLe\
ft\x0d\x0a            \
        text: 'C\
urrent Epoch'\x0d\x0a \
               }\
\x0d\x0a              \
  Label {\x0d\x0a     \
               t\
ext: epoch_bridg\
e.epoch\x0d\x0a       \
             hor\
izontalAlignment\
: Text.AlignRigh\
t\x0d\x0a             \
       Layout.fi\
llWidth: true\x0d\x0a \
               }\
\x0d\x0a\x0d\x0a            \
    Label {\x0d\x0a   \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
             hor\
izontalAlignment\
: Text.AlignLeft\
\x0d\x0a              \
      text: 'Tra\
in Accuracy'\x0d\x0a  \
              }\x0d\
\x0a               \
 Label {\x0d\x0a      \
              te\
xt: '0 %'\x0d\x0a     \
               h\
orizontalAlignme\
nt: Text.AlignRi\
ght\x0d\x0a           \
         Layout.\
fillWidth: true\x0d\
\x0a               \
 }\x0d\x0a\x0d\x0a          \
      Label {\x0d\x0a \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
               h\
orizontalAlignme\
nt: Text.AlignLe\
ft\x0d\x0a            \
        text: 'T\
rain Loss'\x0d\x0a    \
            }\x0d\x0a \
               L\
abel {\x0d\x0a        \
            text\
: '0.00'\x0d\x0a      \
              ho\
rizontalAlignmen\
t: Text.AlignRig\
ht\x0d\x0a            \
        Layout.f\
illWidth: true\x0d\x0a\
                \
}\x0d\x0a\x0d\x0a           \
     Label {\x0d\x0a  \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
              ho\
rizontalAlignmen\
t: Text.AlignLef\
t\x0d\x0a             \
       text: 'Te\
st Accuracy'\x0d\x0a  \
              }\x0d\
\x0a               \
 Label {\x0d\x0a      \
              te\
xt: epoch_bridge\
.test_accuracy +\
 ' %'\x0d\x0a         \
           horiz\
ontalAlignment: \
Text.AlignRight\x0d\
\x0a               \
     Layout.fill\
Width: true\x0d\x0a   \
             }\x0d\x0a\
\x0d\x0a              \
  Label {\x0d\x0a     \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
           horiz\
ontalAlignment: \
Text.AlignLeft\x0d\x0a\
                \
    text: 'Test \
Loss'\x0d\x0a         \
       }\x0d\x0a      \
          Label \
{\x0d\x0a             \
       text: epo\
ch_bridge.test_l\
oss\x0d\x0a           \
         horizon\
talAlignment: Te\
xt.AlignRight\x0d\x0a \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
           }\x0d\x0a\x0d\x0a\
                \
Label {\x0d\x0a       \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
         horizon\
talAlignment: Te\
xt.AlignLeft\x0d\x0a  \
                \
  text: 'mAP'\x0d\x0a \
               }\
\x0d\x0a              \
  Label {\x0d\x0a     \
               t\
ext: '90%'\x0d\x0a    \
                \
horizontalAlignm\
ent: Text.AlignR\
ight\x0d\x0a          \
          Layout\
.fillWidth: true\
\x0d\x0a              \
  }\x0d\x0a\x0d\x0a         \
       Label {\x0d\x0a\
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
horizontalAlignm\
ent: Text.AlignL\
eft\x0d\x0a           \
         text: '\
mIoU'\x0d\x0a         \
       }\x0d\x0a      \
          Label \
{\x0d\x0a             \
       text: '92\
%'\x0d\x0a            \
        horizont\
alAlignment: Tex\
t.AlignRight\x0d\x0a  \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
          }\x0d\x0a\x0d\x0a \
             }\x0d\x0a\
\x0d\x0a              \
GridLayout {\x0d\x0a  \
                \
Layout.alignment\
: Qt.AlignBottom\
\x0d\x0a              \
    columns: 2\x0d\x0a\
\x0d\x0a              \
    Label {\x0d\x0a   \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
                \
 horizontalAlign\
ment: Text.Align\
Left\x0d\x0a          \
            text\
: 'Epoch Progres\
s: '\x0d\x0a          \
        }\x0d\x0a     \
             Lab\
el {\x0d\x0a          \
            text\
: epoch_bridge.p\
rogress\x0d\x0a       \
               h\
orizontalAlignme\
nt: Text.AlignRi\
ght\x0d\x0a           \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
         id: pro\
gressLabel\x0d\x0a    \
              }\x0d\
\x0a               \
   ProgressBar {\
\x0d\x0a              \
        Layout.f\
illWidth: true\x0d\x0a\
                \
      Layout.col\
umnSpan: 2\x0d\x0a    \
                \
  value: epoch_b\
ridge.progress /\
 100;\x0d\x0a         \
         }\x0d\x0a    \
          }\x0d\x0a   \
       }\x0d\x0a      \
}\x0d\x0a\x0d\x0a      /****\
****************\
****************\
****************\
******\x0d\x0a      Gr\
aphs\x0d\x0a      ****\
****************\
****************\
****************\
******/\x0d\x0a      C\
ellBox {\x0d\x0a      \
  Layout.rowSpan\
: 3; Layout.mini\
mumWidth: 700\x0d\x0a \
       Layout.pr\
eferredWidth: he\
ight // Keep the\
 ratio right!\x0d\x0a \
       TabBar {\x0d\
\x0a          id: b\
ar\x0d\x0a          wi\
dth: parent.widt\
h\x0d\x0a          Tab\
Button { text: '\
Test Loss' }\x0d\x0a  \
        TabButto\
n { text: 'Accur\
acies' }\x0d\x0a      \
  }\x0d\x0a        Sta\
ckLayout {\x0d\x0a    \
      width: par\
ent.width\x0d\x0a     \
     height: par\
ent.height - y\x0d\x0a\
          anchor\
s.top: bar.botto\
m\x0d\x0a          cur\
rentIndex: bar.c\
urrentIndex\x0d\x0a   \
       LargeChar\
tView {\x0d\x0a       \
     ValueAxis {\
\x0d\x0a              \
id: xAxisLossSer\
ies\x0d\x0a           \
   titleText: 'E\
poch'\x0d\x0a         \
     min: 0\x0d\x0a   \
           max: \
settings_bridge.\
epochs\x0d\x0a        \
      tickCount:\
 settings_bridge\
.epochs + 1\x0d\x0a   \
           label\
Format: '%.0f'\x0d\x0a\
            }\x0d\x0a \
           Value\
Axis {\x0d\x0a        \
      id: yAxisL\
ossSeries\x0d\x0a     \
         min: 0\x0d\
\x0a              m\
ax: 0.5\x0d\x0a       \
     }\x0d\x0a\x0d\x0a      \
      SplineSeri\
es {\x0d\x0a          \
    name: 'Test \
Loss'\x0d\x0a         \
     id: lossSer\
ies\x0d\x0a           \
   axisX: xAxisL\
ossSeries\x0d\x0a     \
         axisY: \
yAxisLossSeries\x0d\
\x0a            }\x0d\x0a\
          }\x0d\x0a\x0d\x0a \
         LargeCh\
artView {\x0d\x0a     \
       ValueAxis\
 {\x0d\x0a            \
  id: valueAxisS\
plineSeries\x0d\x0a   \
           min: \
0\x0d\x0a             \
 max: 5\x0d\x0a       \
       tickCount\
: 6\x0d\x0a           \
   labelFormat: \
'%.0f'\x0d\x0a        \
    }\x0d\x0a\x0d\x0a       \
     SplineSerie\
s {\x0d\x0a           \
   name: 'Test A\
cc.'\x0d\x0a          \
    axisX: value\
AxisSplineSeries\
\x0d\x0a              \
XYPoint { x: 0; \
y: 0 }\x0d\x0a        \
      XYPoint { \
x: 1; y: 0.5 }\x0d\x0a\
              XY\
Point { x: 2; y:\
 0.75 }\x0d\x0a       \
       XYPoint {\
 x: 3; y: 0.87 }\
\x0d\x0a              \
XYPoint { x: 4; \
y: 0.92 }\x0d\x0a     \
         XYPoint\
 { x: 5; y: 0.95\
 }\x0d\x0a            \
}\x0d\x0a            S\
plineSeries {\x0d\x0a \
             nam\
e: 'mAP'\x0d\x0a      \
        axisX: v\
alueAxisSplineSe\
ries\x0d\x0a          \
    XYPoint { x:\
 0; y: 0 }\x0d\x0a    \
          XYPoin\
t { x: 1; y: 0.4\
5 }\x0d\x0a           \
   XYPoint { x: \
2; y: 0.80 }\x0d\x0a  \
            XYPo\
int { x: 3; y: 0\
.78 }\x0d\x0a         \
     XYPoint { x\
: 4; y: 0.85 }\x0d\x0a\
              XY\
Point { x: 5; y:\
 0.90 }\x0d\x0a       \
     }\x0d\x0a        \
    SplineSeries\
 {\x0d\x0a            \
  name: 'mIoU'\x0d\x0a\
              ax\
isX: valueAxisSp\
lineSeries\x0d\x0a    \
          XYPoin\
t { x: 0; y: 0 }\
\x0d\x0a              \
XYPoint { x: 1; \
y: 0.43 }\x0d\x0a     \
         XYPoint\
 { x: 2; y: 0.68\
 }\x0d\x0a            \
  XYPoint { x: 3\
; y: 0.84 }\x0d\x0a   \
           XYPoi\
nt { x: 4; y: 0.\
90 }\x0d\x0a          \
    XYPoint { x:\
 5; y: 0.92 }\x0d\x0a \
           }\x0d\x0a  \
        }\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a\x0d\
\x0a      /********\
****************\
****************\
****************\
**\x0d\x0a      Pop-Up\
s\x0d\x0a      *******\
****************\
****************\
****************\
***/\x0d\x0a      Popu\
p {\x0d\x0a        id:\
 normalPopup\x0d\x0a  \
      ColumnLayo\
ut {\x0d\x0a          \
anchors.fill: pa\
rent\x0d\x0a          \
Label { text: 'N\
ormal Popup' }\x0d\x0a\
          CheckB\
ox { text: 'E-ma\
il' }\x0d\x0a         \
 CheckBox { text\
: 'Calendar' }\x0d\x0a\
          CheckB\
ox { text: 'Cont\
acts' }\x0d\x0a       \
 }\x0d\x0a      }\x0d\x0a   \
   Popup {\x0d\x0a    \
    id: modalPop\
up\x0d\x0a        moda\
l: true\x0d\x0a       \
 ColumnLayout {\x0d\
\x0a          ancho\
rs.fill: parent\x0d\
\x0a          Label\
 { text: 'Modal \
Popup' }\x0d\x0a      \
    CheckBox { t\
ext: 'E-mail' }\x0d\
\x0a          Check\
Box { text: 'Cal\
endar' }\x0d\x0a      \
    CheckBox { t\
ext: 'Contacts' \
}\x0d\x0a        }\x0d\x0a  \
    }\x0d\x0a      Dia\
log {\x0d\x0a        i\
d: dialog\x0d\x0a     \
   title: 'Dialo\
g'\x0d\x0a        Labe\
l { text: 'The s\
tandard dialog.'\
 }\x0d\x0a        foot\
er: DialogButton\
Box {\x0d\x0a         \
 standardButtons\
: DialogButtonBo\
x.Ok | DialogBut\
tonBox.Cancel\x0d\x0a \
       }\x0d\x0a      \
}\x0d\x0a\x0d\x0a      FileD\
ialog {\x0d\x0a       \
 id: fileDialog\x0d\
\x0a        title: \
\x22Choose a folder\
...\x22\x0d\x0a        se\
lectFolder: true\
\x0d\x0a        select\
Multiple: false\x0d\
\x0a        folder:\
 shortcuts.home\x0d\
\x0a        onAccep\
ted: {\x0d\x0a        \
    var path = f\
ileDialog.fileUr\
l.toString()\x0d\x0a  \
          // reo\
mve prefix \x22file\
:///\x22\x0d\x0a         \
   path = path.r\
eplace(/^(file:\x5c\
/{3})/,\x22\x22)\x0d\x0a    \
        // unesc\
ape HTML codes\x0d\x0a\
            clea\
nPath = decodeUR\
IComponent(path)\
;\x0d\x0a            t\
rainPath.text = \
cleanPath\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a \
   }\x0d\x0a  }\x0d\x0a\x0d\x0a  /\
****************\
****************\
****************\
**********\x0d\x0a  Fo\
oter\x0d\x0a  ********\
****************\
****************\
****************\
**/\x0d\x0a  footer: R\
owLayout {\x0d\x0a    \
width: parent.wi\
dth\x0d\x0a    RowLayo\
ut {\x0d\x0a      Layo\
ut.margins: 10\x0d\x0a\
      Layout.ali\
gnment: Qt.Align\
HCenter\x0d\x0a      L\
abel { text: 'Th\
eme customizatio\
n: ' }\x0d\x0a      La\
bel {\x0d\x0a        i\
d: qtquick2Theme\
s\x0d\x0a        objec\
tName: 'qtquick2\
Themes'\x0d\x0a       \
 Layout.fillWidt\
h: true\x0d\x0a      }\
\x0d\x0a    }\x0d\x0a    Row\
Layout {\x0d\x0a      \
Layout.margins: \
10\x0d\x0a      Layout\
.alignment: Qt.A\
lignHCenter\x0d\x0a   \
   Label { text:\
 'QtQuick Charts\
 Themes: ' }\x0d\x0a  \
    ComboBox {\x0d\x0a\
        id: qtqu\
ickChartsThemes\x0d\
\x0a        model: \
[\x0d\x0a          'Ch\
artThemeLight', \
'ChartThemeBlueC\
erulean',\x0d\x0a     \
     'ChartTheme\
Dark', 'ChartThe\
meBrownSand',\x0d\x0a \
         'ChartT\
hemeBlueNcs', 'C\
hartThemeHighCon\
trast',\x0d\x0a       \
   'ChartThemeBl\
ueIcy', 'ChartTh\
emeQt'\x0d\x0a        \
]\x0d\x0a        Layou\
t.fillWidth: tru\
e\x0d\x0a        curre\
ntIndex: 2\x0d\x0a    \
  }\x0d\x0a    }\x0d\x0a    \
RowLayout {\x0d\x0a   \
   Layout.margin\
s: 10\x0d\x0a      Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
      Label { te\
xt: 'Sub-Theme: \
' }\x0d\x0a      Combo\
Box {\x0d\x0a        i\
d: subTheme\x0d\x0a   \
     model: ['Da\
rk', 'Light']\x0d\x0a \
       Layout.fi\
llWidth: true\x0d\x0a \
       enabled: \
true\x0d\x0a      }\x0d\x0a \
   }\x0d\x0a    RowLay\
out {\x0d\x0a      pro\
perty var materi\
alColors: [\x0d\x0a   \
     'Red', 'Pin\
k', 'Purple', 'D\
eepPurple', 'Ind\
igo', 'Blue',\x0d\x0a \
       'LightBlu\
e', 'Cyan', 'Tea\
l', 'Green', 'Li\
ghtGreen', 'Lime\
',\x0d\x0a        'Yel\
low', 'Amber', '\
Orange', 'DeepOr\
ange', 'Brown', \
'Grey',\x0d\x0a       \
 'BlueGrey'\x0d\x0a   \
   ]\x0d\x0a      Layo\
ut.margins: 10\x0d\x0a\
      Layout.ali\
gnment: Qt.Align\
HCenter\x0d\x0a\x0d\x0a     \
 Label { text: '\
Primary' }\x0d\x0a    \
  ComboBox {\x0d\x0a  \
      id: primar\
yColor\x0d\x0a        \
Layout.fillWidth\
: true\x0d\x0a        \
enabled: true\x0d\x0a \
       model: pa\
rent.materialCol\
ors\x0d\x0a        cur\
rentIndex: 6\x0d\x0a  \
    }\x0d\x0a\x0d\x0a      L\
abel { text: 'Ac\
cent' }\x0d\x0a      C\
omboBox {\x0d\x0a     \
   id: accentCol\
or\x0d\x0a        Layo\
ut.fillWidth: tr\
ue\x0d\x0a        enab\
led: true\x0d\x0a     \
   model: parent\
.materialColors\x0d\
\x0a        current\
Index: 7\x0d\x0a      \
}\x0d\x0a    }\x0d\x0a  }\x0d\x0a}\
\
\x00\x00\x00\xc7\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22>\x0d\x0a    <path d=\
\x22M0 0h24v24H0z\x22 \
fill=\x22none\x22/>\x0d\x0a \
   <path d=\x22M3 1\
8h18v-2H3v2zm0-5\
h18v-2H3v2zm0-7v\
2h18V6H3z\x22/>\x0d\x0a</\
svg>\x0d\x0a\
\x00\x00\x01+\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22>\x0d\x0a    <path d=\
\x22M0 0h24v24H0z\x22 \
fill=\x22none\x22/>\x0d\x0a \
   <path d=\x22M12 \
8c1.1 0 2-.9 2-2\
s-.9-2-2-2-2 .9-\
2 2 .9 2 2 2zm0 \
2c-1.1 0-2 .9-2 \
2s.9 2 2 2 2-.9 \
2-2-.9-2-2-2zm0 \
6c-1.1 0-2 .9-2 \
2s.9 2 2 2 2-.9 \
2-2-.9-2-2-2z\x22/>\
\x0d\x0a</svg>\x0d\x0a\
\x00\x00\x00\xf5\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 width=\x2224\
\x22 height=\x2224\x22 vi\
ewBox=\x220 0 24 24\
\x22>\x0d\x0a    <path d=\
\x22M12 2l-5.5 9h11\
z\x22/>\x0d\x0a    <circl\
e cx=\x2217.5\x22 cy=\x22\
17.5\x22 r=\x224.5\x22/>\x0d\
\x0a    <path d=\x22M3\
 13.5h8v8H3z\x22/>\x0d\
\x0a    <path fill=\
\x22none\x22 d=\x22M0 0h2\
4v24H0z\x22/>\x0d\x0a</sv\
g>\x0d\x0a\
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x\xc3\
\x00r\
\x00e\x00s\
\x00\x06\
\x07\x03}\xc3\
\x00i\
\x00m\x00a\x00g\x00e\x00s\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x12\
\x08\xbdU\xfc\
\x00L\
\x00a\x00r\x00g\x00e\x00C\x00h\x00a\x00r\x00t\x00V\x00i\x00e\x00w\x00.\x00q\x00m\
\x00l\
\x00\x11\
\x03S\x87\xdc\
\x00S\
\x00i\x00d\x00e\x00N\x00a\x00v\x00B\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\
\x00\x0b\
\x09\xf8\xd2<\
\x00C\
\x00e\x00l\x00l\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x16\
\x03d\xbe\x87\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00m\x00e\x00n\x00u\x00-\x002\x004\x00p\
\x00x\x00.\x00s\x00v\x00g\
\x00\x1b\
\x0d\xe1;G\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00m\x00o\x00r\x00e\x00_\x00v\x00e\x00r\
\x00t\x00-\x002\x004\x00p\x00x\x00.\x00s\x00v\x00g\
\x00\x1a\
\x0b\xaf\xda'\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00c\x00a\x00t\x00e\x00g\x00o\x00r\x00y\
\x00-\x002\x004\x00p\x00x\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x1e\x00\x02\x00\x00\x00\x04\x00\x00\x00\x07\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x00\xae\x00\x00\x00\x00\x00\x01\x00\x00>\xb3\
\x00\x00\x01\x1c\x00\x00\x00\x00\x00\x01\x00\x00@\xad\
\x00\x00\x00\xe0\x00\x00\x00\x00\x00\x01\x00\x00?~\
\x00\x00\x00T\x00\x00\x00\x00\x00\x01\x00\x00\x00\xf4\
\x00\x00\x00\x98\x00\x00\x00\x00\x00\x01\x00\x00\x02\x0e\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00|\x00\x00\x00\x00\x00\x01\x00\x00\x01`\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
