# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Mon Aug 19 13:19:05 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
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
\x00\x00\x003\
[\
Controls]\x0d\x0aStyle\
=Material\x0d\x0aFallb\
ackStyle=Default\
\x0d\x0a\
\x00\x00?P\
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
    trainFileDia\
log.open()\x0d\x0a    \
            }\x0d\x0a \
           }\x0d\x0a\x0d\x0a\
            Labe\
l {\x0d\x0a           \
     text: 'Fold\
er with test fil\
es:'\x0d\x0a          \
      Layout.ali\
gnment: Qt.Align\
HCenter\x0d\x0a       \
     }\x0d\x0a        \
    TextField {\x0d\
\x0a               \
 id: testPath\x0d\x0a \
               w\
idth: parent.wid\
th\x0d\x0a            \
    placeholderT\
ext: 'Path to te\
st data folder..\
.'\x0d\x0a            \
    selectByMous\
e: true\x0d\x0a       \
     }\x0d\x0a        \
    RoundButton \
{\x0d\x0a             \
   text: '...'\x0d\x0a\
                \
Layout.alignment\
: Qt.AlignHCente\
r\x0d\x0a             \
   onClicked: ()\
 => {\x0d\x0a         \
           testF\
ileDialog.open()\
\x0d\x0a              \
  }\x0d\x0a           \
 }\x0d\x0a        }\x0d\x0a \
     }\x0d\x0a\x0d\x0a      \
CellBox {\x0d\x0a     \
   title: 'Netwo\
rk Settings'\x0d\x0a  \
      GridLayout\
 {\x0d\x0a            \
anchors.fill: pa\
rent\x0d\x0a          \
  columns: 2\x0d\x0a  \
          Label \
{\x0d\x0a             \
   text: 'Total \
Training Epochs'\
\x0d\x0a              \
  Layout.alignme\
nt: Qt.AlignHCen\
ter\x0d\x0a           \
 }\x0d\x0a            \
SpinBox {\x0d\x0a     \
           id: t\
otalEpochs\x0d\x0a    \
            edit\
able: true\x0d\x0a    \
            valu\
e: settings_brid\
ge.epochs\x0d\x0a     \
           from:\
 1\x0d\x0a            \
    to: 999999\x0d\x0a\
                \
Layout.fillWidth\
: true\x0d\x0a        \
        onValueC\
hanged: settings\
_bridge.epochs =\
 value\x0d\x0a        \
        Componen\
t.onCompleted: s\
ettings_bridge.e\
pochs = value\x0d\x0a \
           }\x0d\x0a\x0d\x0a\
            Labe\
l {\x0d\x0a           \
     text: 'Batc\
h Size'\x0d\x0a       \
         Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a    \
        }\x0d\x0a     \
       SpinBox {\
\x0d\x0a              \
  editable: true\
\x0d\x0a              \
  value: 32\x0d\x0a   \
             fro\
m: 2\x0d\x0a          \
      to: 2048\x0d\x0a\
                \
Layout.fillWidth\
: true\x0d\x0a        \
    }\x0d\x0a\x0d\x0a       \
     Label {\x0d\x0a  \
              te\
xt: 'Neighborhoo\
d Size'\x0d\x0a       \
         Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a    \
        }\x0d\x0a     \
       SpinBox {\
\x0d\x0a              \
  editable: true\
\x0d\x0a              \
  value: 2048\x0d\x0a \
               f\
rom: 512\x0d\x0a      \
          to: 81\
92\x0d\x0a            \
    Layout.fillW\
idth: true\x0d\x0a    \
        }\x0d\x0a\x0d\x0a   \
         Label {\
\x0d\x0a              \
  text: 'Optimiz\
ation Metric'\x0d\x0a \
               L\
ayout.alignment:\
 Qt.AlignHCenter\
\x0d\x0a            }\x0d\
\x0a            Spi\
nBox {\x0d\x0a        \
        value: 1\
00\x0d\x0a            \
    Layout.fillW\
idth: true\x0d\x0a    \
        }\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a\x0d\
\x0a      CellBox {\
\x0d\x0a        Layout\
.columnSpan: 2; \
Layout.preferred\
Height: 100;\x0d\x0a  \
      title: 'Co\
nsole Output'\x0d\x0a \
       ScrollVie\
w {\x0d\x0a          a\
nchors.fill: par\
ent\x0d\x0a          T\
extArea {\x0d\x0a     \
       anchors.f\
ill: parent\x0d\x0a   \
         id: con\
soleTextfield\x0d\x0a \
           place\
holderText: 'Con\
sole output...'\x0d\
\x0a            sel\
ectByMouse: true\
\x0d\x0a            pe\
rsistentSelectio\
n: true\x0d\x0a       \
     readOnly: t\
rue\x0d\x0a          }\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a\x0d\x0a      Ce\
llBox {\x0d\x0a       \
   Layout.rowSpa\
n: 2\x0d\x0a          \
title: 'Current \
Info'\x0d\x0a         \
 ColumnLayout {\x0d\
\x0a              a\
nchors.fill: par\
ent\x0d\x0a\x0d\x0a         \
     GridLayout \
{\x0d\x0a             \
   Layout.alignm\
ent: Qt.AlignTop\
\x0d\x0a              \
  columns: 2\x0d\x0a\x0d\x0a\
                \
Label {\x0d\x0a       \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
         horizon\
talAlignment: Te\
xt.AlignLeft\x0d\x0a  \
                \
  text: 'Current\
 Epoch'\x0d\x0a       \
         }\x0d\x0a    \
            Labe\
l {\x0d\x0a           \
         text: e\
poch_bridge.epoc\
h\x0d\x0a             \
       horizonta\
lAlignment: Text\
.AlignRight\x0d\x0a   \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
         }\x0d\x0a\x0d\x0a  \
              La\
bel {\x0d\x0a         \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
       horizonta\
lAlignment: Text\
.AlignLeft\x0d\x0a    \
                \
text: 'Train Acc\
uracy'\x0d\x0a        \
        }\x0d\x0a     \
           Label\
 {\x0d\x0a            \
        text: '0\
 %'\x0d\x0a           \
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
  text: 'Train L\
oss'\x0d\x0a          \
      }\x0d\x0a       \
         Label {\
\x0d\x0a              \
      text: '0.0\
0'\x0d\x0a            \
        horizont\
alAlignment: Tex\
t.AlignRight\x0d\x0a  \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
          }\x0d\x0a\x0d\x0a \
               L\
abel {\x0d\x0a        \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
        horizont\
alAlignment: Tex\
t.AlignLeft\x0d\x0a   \
                \
 text: 'Test Acc\
uracy'\x0d\x0a        \
        }\x0d\x0a     \
           Label\
 {\x0d\x0a            \
        text: ep\
och_bridge.test_\
accuracy + ' %'\x0d\
\x0a               \
     horizontalA\
lignment: Text.A\
lignRight\x0d\x0a     \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
       }\x0d\x0a\x0d\x0a    \
            Labe\
l {\x0d\x0a           \
         Layout.\
fillWidth: true\x0d\
\x0a               \
     horizontalA\
lignment: Text.A\
lignLeft\x0d\x0a      \
              te\
xt: 'Test Loss'\x0d\
\x0a               \
 }\x0d\x0a            \
    Label {\x0d\x0a   \
                \
 text: epoch_bri\
dge.test_loss\x0d\x0a \
                \
   horizontalAli\
gnment: Text.Ali\
gnRight\x0d\x0a       \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
     }\x0d\x0a\x0d\x0a      \
          Label \
{\x0d\x0a             \
       Layout.fi\
llWidth: true\x0d\x0a \
                \
   horizontalAli\
gnment: Text.Ali\
gnLeft\x0d\x0a        \
            text\
: 'mAP'\x0d\x0a       \
         }\x0d\x0a    \
            Labe\
l {\x0d\x0a           \
         text: '\
90%'\x0d\x0a          \
          horizo\
ntalAlignment: T\
ext.AlignRight\x0d\x0a\
                \
    Layout.fillW\
idth: true\x0d\x0a    \
            }\x0d\x0a\x0d\
\x0a               \
 Label {\x0d\x0a      \
              La\
yout.fillWidth: \
true\x0d\x0a          \
          horizo\
ntalAlignment: T\
ext.AlignLeft\x0d\x0a \
                \
   text: 'mIoU'\x0d\
\x0a               \
 }\x0d\x0a            \
    Label {\x0d\x0a   \
                \
 text: '92%'\x0d\x0a  \
                \
  horizontalAlig\
nment: Text.Alig\
nRight\x0d\x0a        \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
    }\x0d\x0a\x0d\x0a       \
       }\x0d\x0a\x0d\x0a    \
          GridLa\
yout {\x0d\x0a        \
          Layout\
.alignment: Qt.A\
lignBottom\x0d\x0a    \
              co\
lumns: 2\x0d\x0a\x0d\x0a    \
              La\
bel {\x0d\x0a         \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
           horiz\
ontalAlignment: \
Text.AlignLeft\x0d\x0a\
                \
      text: 'Epo\
ch Progress: '\x0d\x0a\
                \
  }\x0d\x0a           \
       Label {\x0d\x0a\
                \
      text: epoc\
h_bridge.progres\
s\x0d\x0a             \
         horizon\
talAlignment: Te\
xt.AlignRight\x0d\x0a \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
   id: progressL\
abel\x0d\x0a          \
        }\x0d\x0a     \
             Pro\
gressBar {\x0d\x0a    \
                \
  Layout.fillWid\
th: true\x0d\x0a      \
                \
Layout.columnSpa\
n: 2\x0d\x0a          \
            valu\
e: epoch_bridge.\
progress / 100;\x0d\
\x0a               \
   }\x0d\x0a          \
    }\x0d\x0a         \
 }\x0d\x0a      }\x0d\x0a\x0d\x0a \
     /**********\
****************\
****************\
****************\
\x0d\x0a      Graphs\x0d\x0a\
      **********\
****************\
****************\
****************\
/\x0d\x0a      CellBox\
 {\x0d\x0a        Layo\
ut.rowSpan: 3; L\
ayout.minimumWid\
th: 700\x0d\x0a       \
 Layout.preferre\
dWidth: height /\
/ Keep the ratio\
 right!\x0d\x0a       \
 TabBar {\x0d\x0a     \
     id: bar\x0d\x0a  \
        width: p\
arent.width\x0d\x0a   \
       TabButton\
 { text: 'Test L\
oss' }\x0d\x0a        \
  TabButton { te\
xt: 'Accuracies'\
 }\x0d\x0a        }\x0d\x0a \
       StackLayo\
ut {\x0d\x0a          \
width: parent.wi\
dth\x0d\x0a          h\
eight: parent.he\
ight - y\x0d\x0a      \
    anchors.top:\
 bar.bottom\x0d\x0a   \
       currentIn\
dex: bar.current\
Index\x0d\x0a         \
 LargeChartView \
{\x0d\x0a            V\
alueAxis {\x0d\x0a    \
          id: xA\
xisLossSeries\x0d\x0a \
             tit\
leText: 'Epoch'\x0d\
\x0a              m\
in: 0\x0d\x0a         \
     max: settin\
gs_bridge.epochs\
\x0d\x0a              \
tickCount: setti\
ngs_bridge.epoch\
s + 1\x0d\x0a         \
     labelFormat\
: '%.0f'\x0d\x0a      \
      }\x0d\x0a       \
     ValueAxis {\
\x0d\x0a              \
id: yAxisLossSer\
ies\x0d\x0a           \
   min: 0\x0d\x0a     \
         max: 0.\
5\x0d\x0a            }\
\x0d\x0a\x0d\x0a            \
SplineSeries {\x0d\x0a\
              na\
me: 'Test Loss'\x0d\
\x0a              i\
d: lossSeries\x0d\x0a \
             axi\
sX: xAxisLossSer\
ies\x0d\x0a           \
   axisY: yAxisL\
ossSeries\x0d\x0a     \
       }\x0d\x0a      \
    }\x0d\x0a\x0d\x0a       \
   LargeChartVie\
w {\x0d\x0a           \
 ValueAxis {\x0d\x0a  \
            id: \
valueAxisSplineS\
eries\x0d\x0a         \
     min: 0\x0d\x0a   \
           max: \
5\x0d\x0a             \
 tickCount: 6\x0d\x0a \
             lab\
elFormat: '%.0f'\
\x0d\x0a            }\x0d\
\x0a\x0d\x0a            S\
plineSeries {\x0d\x0a \
             nam\
e: 'Test Acc.'\x0d\x0a\
              ax\
isX: valueAxisSp\
lineSeries\x0d\x0a    \
          XYPoin\
t { x: 0; y: 0 }\
\x0d\x0a              \
XYPoint { x: 1; \
y: 0.5 }\x0d\x0a      \
        XYPoint \
{ x: 2; y: 0.75 \
}\x0d\x0a             \
 XYPoint { x: 3;\
 y: 0.87 }\x0d\x0a    \
          XYPoin\
t { x: 4; y: 0.9\
2 }\x0d\x0a           \
   XYPoint { x: \
5; y: 0.95 }\x0d\x0a  \
          }\x0d\x0a   \
         SplineS\
eries {\x0d\x0a       \
       name: 'mA\
P'\x0d\x0a            \
  axisX: valueAx\
isSplineSeries\x0d\x0a\
              XY\
Point { x: 0; y:\
 0 }\x0d\x0a          \
    XYPoint { x:\
 1; y: 0.45 }\x0d\x0a \
             XYP\
oint { x: 2; y: \
0.80 }\x0d\x0a        \
      XYPoint { \
x: 3; y: 0.78 }\x0d\
\x0a              X\
YPoint { x: 4; y\
: 0.85 }\x0d\x0a      \
        XYPoint \
{ x: 5; y: 0.90 \
}\x0d\x0a            }\
\x0d\x0a            Sp\
lineSeries {\x0d\x0a  \
            name\
: 'mIoU'\x0d\x0a      \
        axisX: v\
alueAxisSplineSe\
ries\x0d\x0a          \
    XYPoint { x:\
 0; y: 0 }\x0d\x0a    \
          XYPoin\
t { x: 1; y: 0.4\
3 }\x0d\x0a           \
   XYPoint { x: \
2; y: 0.68 }\x0d\x0a  \
            XYPo\
int { x: 3; y: 0\
.84 }\x0d\x0a         \
     XYPoint { x\
: 4; y: 0.90 }\x0d\x0a\
              XY\
Point { x: 5; y:\
 0.92 }\x0d\x0a       \
     }\x0d\x0a        \
  }\x0d\x0a        }\x0d\x0a\
      }\x0d\x0a\x0d\x0a     \
 /**************\
****************\
****************\
************\x0d\x0a  \
    Pop-Ups\x0d\x0a   \
   *************\
****************\
****************\
*************/\x0d\x0a\
      Popup {\x0d\x0a \
       id: norma\
lPopup\x0d\x0a        \
ColumnLayout {\x0d\x0a\
          anchor\
s.fill: parent\x0d\x0a\
          Label \
{ text: 'Normal \
Popup' }\x0d\x0a      \
    CheckBox { t\
ext: 'E-mail' }\x0d\
\x0a          Check\
Box { text: 'Cal\
endar' }\x0d\x0a      \
    CheckBox { t\
ext: 'Contacts' \
}\x0d\x0a        }\x0d\x0a  \
    }\x0d\x0a      Pop\
up {\x0d\x0a        id\
: modalPopup\x0d\x0a  \
      modal: tru\
e\x0d\x0a        Colum\
nLayout {\x0d\x0a     \
     anchors.fil\
l: parent\x0d\x0a     \
     Label { tex\
t: 'Modal Popup'\
 }\x0d\x0a          Ch\
eckBox { text: '\
E-mail' }\x0d\x0a     \
     CheckBox { \
text: 'Calendar'\
 }\x0d\x0a          Ch\
eckBox { text: '\
Contacts' }\x0d\x0a   \
     }\x0d\x0a      }\x0d\
\x0a      Dialog {\x0d\
\x0a        id: dia\
log\x0d\x0a        tit\
le: 'Dialog'\x0d\x0a  \
      Label { te\
xt: 'The standar\
d dialog.' }\x0d\x0a  \
      footer: Di\
alogButtonBox {\x0d\
\x0a          stand\
ardButtons: Dial\
ogButtonBox.Ok |\
 DialogButtonBox\
.Cancel\x0d\x0a       \
 }\x0d\x0a      }\x0d\x0a\x0d\x0a \
     FileDialog \
{\x0d\x0a        id: t\
rainFileDialog\x0d\x0a\
        title: \x22\
Choose a folder.\
..\x22\x0d\x0a        sel\
ectFolder: true\x0d\
\x0a        selectM\
ultiple: false\x0d\x0a\
        folder: \
shortcuts.home\x0d\x0a\
        onAccept\
ed: {\x0d\x0a         \
   var path = tr\
ainFileDialog.fi\
leUrl.toString()\
\x0d\x0a            //\
 reomve prefix \x22\
file:///\x22\x0d\x0a     \
       path = pa\
th.replace(/^(fi\
le:\x5c/{3})/,\x22\x22)\x0d\x0a\
            // u\
nescape HTML cod\
es\x0d\x0a            \
var cleanPath = \
decodeURICompone\
nt(path);\x0d\x0a     \
       trainPath\
.text = cleanPat\
h\x0d\x0a        }\x0d\x0a  \
    }\x0d\x0a\x0d\x0a      F\
ileDialog {\x0d\x0a   \
     id: testFil\
eDialog\x0d\x0a       \
 title: \x22Choose \
a folder...\x22\x0d\x0a  \
      selectFold\
er: true\x0d\x0a      \
  selectMultiple\
: false\x0d\x0a       \
 folder: shortcu\
ts.home\x0d\x0a       \
 onAccepted: {\x0d\x0a\
            var \
path = testFileD\
ialog.fileUrl.to\
String()\x0d\x0a      \
      // reomve \
prefix \x22file:///\
\x22\x0d\x0a            p\
ath = path.repla\
ce(/^(file:\x5c/{3}\
)/,\x22\x22)\x0d\x0a        \
    // unescape \
HTML codes\x0d\x0a    \
        var clea\
nPath = decodeUR\
IComponent(path)\
;\x0d\x0a            t\
estPath.text = c\
leanPath\x0d\x0a      \
  }\x0d\x0a      }\x0d\x0a  \
  }\x0d\x0a  }\x0d\x0a\x0d\x0a  /*\
****************\
****************\
****************\
*********\x0d\x0a  Foo\
ter\x0d\x0a  *********\
****************\
****************\
****************\
*/\x0d\x0a  footer: Ro\
wLayout {\x0d\x0a    w\
idth: parent.wid\
th\x0d\x0a    RowLayou\
t {\x0d\x0a      Layou\
t.margins: 10\x0d\x0a \
     Layout.alig\
nment: Qt.AlignH\
Center\x0d\x0a      La\
bel { text: 'The\
me customization\
: ' }\x0d\x0a      Lab\
el {\x0d\x0a        id\
: qtquick2Themes\
\x0d\x0a        object\
Name: 'qtquick2T\
hemes'\x0d\x0a        \
Layout.fillWidth\
: true\x0d\x0a      }\x0d\
\x0a    }\x0d\x0a    RowL\
ayout {\x0d\x0a      L\
ayout.margins: 1\
0\x0d\x0a      Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a    \
  Label { text: \
'QtQuick Charts \
Themes: ' }\x0d\x0a   \
   ComboBox {\x0d\x0a \
       id: qtqui\
ckChartsThemes\x0d\x0a\
        model: [\
\x0d\x0a          'Cha\
rtThemeLight', '\
ChartThemeBlueCe\
rulean',\x0d\x0a      \
    'ChartThemeD\
ark', 'ChartThem\
eBrownSand',\x0d\x0a  \
        'ChartTh\
emeBlueNcs', 'Ch\
artThemeHighCont\
rast',\x0d\x0a        \
  'ChartThemeBlu\
eIcy', 'ChartThe\
meQt'\x0d\x0a        ]\
\x0d\x0a        Layout\
.fillWidth: true\
\x0d\x0a        curren\
tIndex: 2\x0d\x0a     \
 }\x0d\x0a    }\x0d\x0a    R\
owLayout {\x0d\x0a    \
  Layout.margins\
: 10\x0d\x0a      Layo\
ut.alignment: Qt\
.AlignHCenter\x0d\x0a \
     Label { tex\
t: 'Sub-Theme: '\
 }\x0d\x0a      ComboB\
ox {\x0d\x0a        id\
: subTheme\x0d\x0a    \
    model: ['Dar\
k', 'Light']\x0d\x0a  \
      Layout.fil\
lWidth: true\x0d\x0a  \
      enabled: t\
rue\x0d\x0a      }\x0d\x0a  \
  }\x0d\x0a    RowLayo\
ut {\x0d\x0a      prop\
erty var materia\
lColors: [\x0d\x0a    \
    'Red', 'Pink\
', 'Purple', 'De\
epPurple', 'Indi\
go', 'Blue',\x0d\x0a  \
      'LightBlue\
', 'Cyan', 'Teal\
', 'Green', 'Lig\
htGreen', 'Lime'\
,\x0d\x0a        'Yell\
ow', 'Amber', 'O\
range', 'DeepOra\
nge', 'Brown', '\
Grey',\x0d\x0a        \
'BlueGrey'\x0d\x0a    \
  ]\x0d\x0a      Layou\
t.margins: 10\x0d\x0a \
     Layout.alig\
nment: Qt.AlignH\
Center\x0d\x0a\x0d\x0a      \
Label { text: 'P\
rimary' }\x0d\x0a     \
 ComboBox {\x0d\x0a   \
     id: primary\
Color\x0d\x0a        L\
ayout.fillWidth:\
 true\x0d\x0a        e\
nabled: true\x0d\x0a  \
      model: par\
ent.materialColo\
rs\x0d\x0a        curr\
entIndex: 6\x0d\x0a   \
   }\x0d\x0a\x0d\x0a      La\
bel { text: 'Acc\
ent' }\x0d\x0a      Co\
mboBox {\x0d\x0a      \
  id: accentColo\
r\x0d\x0a        Layou\
t.fillWidth: tru\
e\x0d\x0a        enabl\
ed: true\x0d\x0a      \
  model: parent.\
materialColors\x0d\x0a\
        currentI\
ndex: 7\x0d\x0a      }\
\x0d\x0a    }\x0d\x0a  }\x0d\x0a}\
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
\x00\x0b\
\x09\xf8\xd2<\
\x00C\
\x00e\x00l\x00l\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
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
\x00\x1b\
\x0d\xe1;G\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00m\x00o\x00r\x00e\x00_\x00v\x00e\x00r\
\x00t\x00-\x002\x004\x00p\x00x\x00.\x00s\x00v\x00g\
\x00\x16\
\x03d\xbe\x87\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00m\x00e\x00n\x00u\x00-\x002\x004\x00p\
\x00x\x00.\x00s\x00v\x00g\
\x00\x1a\
\x0b\xaf\xda'\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00c\x00a\x00t\x00e\x00g\x00o\x00r\x00y\
\x00-\x002\x004\x00p\x00x\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x1e\x00\x02\x00\x00\x00\x05\x00\x00\x00\x07\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x01\x1a\x00\x00\x00\x00\x00\x01\x00\x00B\xc8\
\x00\x00\x01L\x00\x00\x00\x00\x00\x01\x00\x00C\x93\
\x00\x00\x00\xde\x00\x00\x00\x00\x00\x01\x00\x00A\x99\
\x00\x00\x00\xb6\x00\x00\x00\x00\x00\x01\x00\x00A-\
\x00\x00\x00v\x00\x00\x00\x00\x00\x01\x00\x00\x00\xe5\
\x00\x00\x00F\x00\x00\x00\x00\x00\x01\x00\x00\x00\xae\
\x00\x00\x00\x8c\x00\x00\x00\x00\x00\x01\x00\x00@9\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
