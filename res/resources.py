# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Mon Aug 19 13:41:28 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00?\x92\
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
(string log)\x0d\x0a  \
signal totalepoc\
hschanged(int ep\
ochs)\x0d\x0a\x0d\x0a  Compo\
nent.onCompleted\
: {\x0d\x0a      contr\
ol_bridge.epoch_\
done.connect(mai\
nWindow.lossreem\
itted)\x0d\x0a      co\
ntrol_bridge.log\
_event.connect(m\
ainWindow.consol\
ereemitted)\x0d\x0a   \
   settings_brid\
ge.epochs_change\
d.connect(mainWi\
ndow.totalepochs\
changed)\x0d\x0a  }\x0d\x0a \
 onLossreemitted\
: {\x0d\x0a      yAxis\
LossSeries.max =\
 Math.max(yAxisL\
ossSeries.max, l\
oss)\x0d\x0a      yAxi\
sLossSeries.min \
= Math.min(yAxis\
LossSeries.min, \
loss)\x0d\x0a      los\
sSeries.append(e\
poch, loss)\x0d\x0a  }\
\x0d\x0a  onConsoleree\
mitted: {\x0d\x0a     \
 consoleTextfiel\
d.append(log)\x0d\x0a \
 }\x0d\x0a\x0d\x0a  onTotale\
pochschanged: {\x0d\
\x0a    totalEpochs\
.value = epochs\x0d\
\x0a  }\x0d\x0a\x0d\x0a  header\
: ToolBar {\x0d\x0a   \
 RowLayout {\x0d\x0a  \
    anchors.fill\
: parent\x0d\x0a      \
ToolButton {\x0d\x0a  \
      icon.sourc\
e: '../images/ba\
seline-menu-24px\
.svg'\x0d\x0a        o\
nClicked: sideNa\
v.open()\x0d\x0a      \
}\x0d\x0a      Label {\
\x0d\x0a        text: \
'Neural network \
control panel'\x0d\x0a\
        elide: L\
abel.ElideRight\x0d\
\x0a        horizon\
talAlignment: Qt\
.AlignHCenter\x0d\x0a \
       verticalA\
lignment: Qt.Ali\
gnVCenter\x0d\x0a     \
   Layout.fillWi\
dth: true\x0d\x0a     \
 }\x0d\x0a      ToolBu\
tton {\x0d\x0a        \
text: 'Start Tra\
ining'\x0d\x0a        \
id: btn_startTra\
ining\x0d\x0a        o\
nClicked: () => \
{\x0d\x0a            b\
tn_startTraining\
.enabled = false\
\x0d\x0a            co\
ntrol_bridge.sta\
rt_simulation()\x0d\
\x0a        }\x0d\x0a    \
  }\x0d\x0a      ToolB\
utton { text: 'P\
ause Training' }\
\x0d\x0a      ToolSepa\
rator {}\x0d\x0a      \
ToolButton {\x0d\x0a  \
      icon.sourc\
e: '../images/ba\
seline-more_vert\
-24px.svg'\x0d\x0a    \
    onClicked: m\
enu.open()\x0d\x0a    \
    Menu {\x0d\x0a    \
      id: menu\x0d\x0a\
          y: par\
ent.height\x0d\x0a    \
      MenuItem {\
 text: 'New...' \
}\x0d\x0a          Men\
uItem { text: 'O\
pen...' }\x0d\x0a     \
     MenuItem { \
text: 'Save' }\x0d\x0a\
        }\x0d\x0a     \
 }\x0d\x0a    }\x0d\x0a  }\x0d\x0a\
  Drawer {\x0d\x0a    \
id: sideNav\x0d\x0a   \
 width: 200\x0d\x0a   \
 height: parent.\
height\x0d\x0a    Colu\
mnLayout {\x0d\x0a    \
  width: parent.\
width\x0d\x0a      Lab\
el {\x0d\x0a          \
text: 'Drawer'\x0d\x0a\
          horizo\
ntalAlignment: T\
ext.AlignHCenter\
\x0d\x0a          vert\
icalAlignment: T\
ext.AlignVCenter\
\x0d\x0a          font\
.pixelSize: 20\x0d\x0a\
          Layout\
.fillWidth: true\
\x0d\x0a      }\x0d\x0a     \
 Repeater {\x0d\x0a   \
     model: 5\x0d\x0a \
       SideNavBu\
tton {\x0d\x0a        \
  icon.source: '\
../images/baseli\
ne-category-24px\
.svg'\x0d\x0a         \
 text: 'List ' +\
 index\x0d\x0a        \
  Layout.fillWid\
th: true\x0d\x0a      \
  }\x0d\x0a      }\x0d\x0a  \
  }\x0d\x0a  }\x0d\x0a  Pane\
 {\x0d\x0a    padding:\
 10\x0d\x0a    anchors\
.fill: parent\x0d\x0a \
   GridLayout {\x0d\
\x0a      anchors.f\
ill: parent\x0d\x0a   \
   flow: GridLay\
out.TopToBottom\x0d\
\x0a      rows: 3\x0d\x0a\
\x0d\x0a      CellBox \
{\x0d\x0a        title\
: 'Datasets'\x0d\x0a  \
      GridLayout\
 {\x0d\x0a            \
anchors.fill: pa\
rent\x0d\x0a          \
  columns: 3\x0d\x0a  \
          Label \
{\x0d\x0a             \
   text: 'Folder\
 with train file\
s:'\x0d\x0a           \
     Layout.alig\
nment: Qt.AlignH\
Center\x0d\x0a        \
    }\x0d\x0a         \
   TextField {\x0d\x0a\
                \
id: trainPath\x0d\x0a \
               w\
idth: parent.wid\
th\x0d\x0a            \
    placeholderT\
ext: 'Path to tr\
ain data folder.\
..'\x0d\x0a           \
     selectByMou\
se: true\x0d\x0a      \
      }\x0d\x0a       \
     RoundButton\
 {\x0d\x0a            \
    text: '...'\x0d\
\x0a               \
 Layout.alignmen\
t: Qt.AlignHCent\
er\x0d\x0a            \
    onClicked: (\
) => {\x0d\x0a        \
            trai\
nFileDialog.open\
()\x0d\x0a            \
    }\x0d\x0a         \
   }\x0d\x0a\x0d\x0a        \
    Label {\x0d\x0a   \
             tex\
t: 'Folder with \
test files:'\x0d\x0a  \
              La\
yout.alignment: \
Qt.AlignHCenter\x0d\
\x0a            }\x0d\x0a\
            Text\
Field {\x0d\x0a       \
         id: tes\
tPath\x0d\x0a         \
       width: pa\
rent.width\x0d\x0a    \
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
           onCli\
cked: () => {\x0d\x0a \
                \
   testFileDialo\
g.open()\x0d\x0a      \
          }\x0d\x0a   \
         }\x0d\x0a    \
    }\x0d\x0a      }\x0d\x0a\
\x0d\x0a      CellBox \
{\x0d\x0a        title\
: 'Network Setti\
ngs'\x0d\x0a        Gr\
idLayout {\x0d\x0a    \
        anchors.\
fill: parent\x0d\x0a  \
          column\
s: 2\x0d\x0a          \
  Label {\x0d\x0a     \
           text:\
 'Total Training\
 Epochs'\x0d\x0a      \
          Layout\
.alignment: Qt.A\
lignHCenter\x0d\x0a   \
         }\x0d\x0a    \
        SpinBox \
{\x0d\x0a             \
   id: totalEpoc\
hs\x0d\x0a            \
    editable: tr\
ue\x0d\x0a            \
    from: 1\x0d\x0a   \
             to:\
 999999\x0d\x0a       \
         Layout.\
fillWidth: true\x0d\
\x0a               \
 onValueChanged:\
 settings_bridge\
.epochs = value\x0d\
\x0a            }\x0d\x0a\
\x0d\x0a            La\
bel {\x0d\x0a         \
       text: 'Ba\
tch Size'\x0d\x0a     \
           Layou\
t.alignment: Qt.\
AlignHCenter\x0d\x0a  \
          }\x0d\x0a   \
         SpinBox\
 {\x0d\x0a            \
    editable: tr\
ue\x0d\x0a            \
    value: 32\x0d\x0a \
               f\
rom: 2\x0d\x0a        \
        to: 2048\
\x0d\x0a              \
  Layout.fillWid\
th: true\x0d\x0a      \
      }\x0d\x0a\x0d\x0a     \
       Label {\x0d\x0a\
                \
text: 'Neighborh\
ood Size'\x0d\x0a     \
           Layou\
t.alignment: Qt.\
AlignHCenter\x0d\x0a  \
          }\x0d\x0a   \
         SpinBox\
 {\x0d\x0a            \
    editable: tr\
ue\x0d\x0a            \
    value: 2048\x0d\
\x0a               \
 from: 512\x0d\x0a    \
            to: \
8192\x0d\x0a          \
      Layout.fil\
lWidth: true\x0d\x0a  \
          }\x0d\x0a\x0d\x0a \
           Label\
 {\x0d\x0a            \
    text: 'Optim\
ization Metric'\x0d\
\x0a               \
 Layout.alignmen\
t: Qt.AlignHCent\
er\x0d\x0a            \
}\x0d\x0a            S\
pinBox {\x0d\x0a      \
          value:\
 100\x0d\x0a          \
      Layout.fil\
lWidth: true\x0d\x0a  \
          }\x0d\x0a   \
     }\x0d\x0a      }\x0d\
\x0a\x0d\x0a      CellBox\
 {\x0d\x0a        Layo\
ut.columnSpan: 2\
; Layout.preferr\
edHeight: 100;\x0d\x0a\
        title: '\
Console Output'\x0d\
\x0a        ScrollV\
iew {\x0d\x0a         \
 anchors.fill: p\
arent\x0d\x0a         \
 TextArea {\x0d\x0a   \
         anchors\
.fill: parent\x0d\x0a \
           id: c\
onsoleTextfield\x0d\
\x0a            pla\
ceholderText: 'C\
onsole output...\
'\x0d\x0a            s\
electByMouse: tr\
ue\x0d\x0a            \
persistentSelect\
ion: true\x0d\x0a     \
       readOnly:\
 true\x0d\x0a         \
 }\x0d\x0a        }\x0d\x0a \
     }\x0d\x0a\x0d\x0a      \
CellBox {\x0d\x0a     \
     Layout.rowS\
pan: 2\x0d\x0a        \
  title: 'Curren\
t Info'\x0d\x0a       \
   ColumnLayout \
{\x0d\x0a             \
 anchors.fill: p\
arent\x0d\x0a\x0d\x0a       \
       GridLayou\
t {\x0d\x0a           \
     Layout.alig\
nment: Qt.AlignT\
op\x0d\x0a            \
    columns: 2\x0d\x0a\
\x0d\x0a              \
  Label {\x0d\x0a     \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
           horiz\
ontalAlignment: \
Text.AlignLeft\x0d\x0a\
                \
    text: 'Curre\
nt Epoch'\x0d\x0a     \
           }\x0d\x0a  \
              La\
bel {\x0d\x0a         \
           text:\
 epoch_bridge.ep\
och\x0d\x0a           \
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
  text: 'Train A\
ccuracy'\x0d\x0a      \
          }\x0d\x0a   \
             Lab\
el {\x0d\x0a          \
          text: \
'0 %'\x0d\x0a         \
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
    text: 'Train\
 Loss'\x0d\x0a        \
        }\x0d\x0a     \
           Label\
 {\x0d\x0a            \
        text: '0\
.00'\x0d\x0a          \
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
   text: 'Test A\
ccuracy'\x0d\x0a      \
          }\x0d\x0a   \
             Lab\
el {\x0d\x0a          \
          text: \
epoch_bridge.tes\
t_accuracy + ' %\
'\x0d\x0a             \
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
text: 'Test Loss\
'\x0d\x0a             \
   }\x0d\x0a          \
      Label {\x0d\x0a \
                \
   text: epoch_b\
ridge.test_loss\x0d\
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
xt: 'mAP'\x0d\x0a     \
           }\x0d\x0a  \
              La\
bel {\x0d\x0a         \
           text:\
 '90%'\x0d\x0a        \
            hori\
zontalAlignment:\
 Text.AlignRight\
\x0d\x0a              \
      Layout.fil\
lWidth: true\x0d\x0a  \
              }\x0d\
\x0a\x0d\x0a             \
   Label {\x0d\x0a    \
                \
Layout.fillWidth\
: true\x0d\x0a        \
            hori\
zontalAlignment:\
 Text.AlignLeft\x0d\
\x0a               \
     text: 'mIoU\
'\x0d\x0a             \
   }\x0d\x0a          \
      Label {\x0d\x0a \
                \
   text: '92%'\x0d\x0a\
                \
    horizontalAl\
ignment: Text.Al\
ignRight\x0d\x0a      \
              La\
yout.fillWidth: \
true\x0d\x0a          \
      }\x0d\x0a\x0d\x0a     \
         }\x0d\x0a\x0d\x0a  \
            Grid\
Layout {\x0d\x0a      \
            Layo\
ut.alignment: Qt\
.AlignBottom\x0d\x0a  \
                \
columns: 2\x0d\x0a\x0d\x0a  \
                \
Label {\x0d\x0a       \
               L\
ayout.fillWidth:\
 true\x0d\x0a         \
             hor\
izontalAlignment\
: Text.AlignLeft\
\x0d\x0a              \
        text: 'E\
poch Progress: '\
\x0d\x0a              \
    }\x0d\x0a         \
         Label {\
\x0d\x0a              \
        text: ep\
och_bridge.progr\
ess\x0d\x0a           \
           horiz\
ontalAlignment: \
Text.AlignRight\x0d\
\x0a               \
       Layout.fi\
llWidth: true\x0d\x0a \
                \
     id: progres\
sLabel\x0d\x0a        \
          }\x0d\x0a   \
               P\
rogressBar {\x0d\x0a  \
                \
    Layout.fillW\
idth: true\x0d\x0a    \
                \
  Layout.columnS\
pan: 2\x0d\x0a        \
              va\
lue: epoch_bridg\
e.progress / 100\
;\x0d\x0a             \
     }\x0d\x0a        \
      }\x0d\x0a       \
   }\x0d\x0a      }\x0d\x0a\x0d\
\x0a      /********\
****************\
****************\
****************\
**\x0d\x0a      Graphs\
\x0d\x0a      ********\
****************\
****************\
****************\
**/\x0d\x0a      CellB\
ox {\x0d\x0a        La\
yout.rowSpan: 3;\
 Layout.minimumW\
idth: 700\x0d\x0a     \
   Layout.prefer\
redWidth: height\
 // Keep the rat\
io right!\x0d\x0a     \
   TabBar {\x0d\x0a   \
       id: bar\x0d\x0a\
          width:\
 parent.width\x0d\x0a \
         TabButt\
on { text: 'Test\
 Loss' }\x0d\x0a      \
    TabButton { \
text: 'Accuracie\
s' }\x0d\x0a        }\x0d\
\x0a        StackLa\
yout {\x0d\x0a        \
  width: parent.\
width\x0d\x0a         \
 height: parent.\
height - y\x0d\x0a    \
      anchors.to\
p: bar.bottom\x0d\x0a \
         current\
Index: bar.curre\
ntIndex\x0d\x0a       \
   LargeChartVie\
w {\x0d\x0a           \
 ValueAxis {\x0d\x0a  \
            id: \
xAxisLossSeries\x0d\
\x0a              t\
itleText: 'Epoch\
'\x0d\x0a             \
 min: 0\x0d\x0a       \
       max: sett\
ings_bridge.epoc\
hs\x0d\x0a            \
  tickCount: set\
tings_bridge.epo\
chs + 1\x0d\x0a       \
       labelForm\
at: '%.0f'\x0d\x0a    \
        }\x0d\x0a     \
       ValueAxis\
 {\x0d\x0a            \
  id: yAxisLossS\
eries\x0d\x0a         \
     min: 0\x0d\x0a   \
           max: \
0.5\x0d\x0a           \
 }\x0d\x0a\x0d\x0a          \
  SplineSeries {\
\x0d\x0a              \
name: 'Test Loss\
'\x0d\x0a             \
 id: lossSeries\x0d\
\x0a              a\
xisX: xAxisLossS\
eries\x0d\x0a         \
     axisY: yAxi\
sLossSeries\x0d\x0a   \
         }\x0d\x0a    \
      }\x0d\x0a\x0d\x0a     \
     LargeChartV\
iew {\x0d\x0a         \
   ValueAxis {\x0d\x0a\
              id\
: valueAxisSplin\
eSeries\x0d\x0a       \
       min: 0\x0d\x0a \
             max\
: 5\x0d\x0a           \
   tickCount: 6\x0d\
\x0a              l\
abelFormat: '%.0\
f'\x0d\x0a            \
}\x0d\x0a\x0d\x0a           \
 SplineSeries {\x0d\
\x0a              n\
ame: 'Test Acc.'\
\x0d\x0a              \
axisX: valueAxis\
SplineSeries\x0d\x0a  \
            XYPo\
int { x: 0; y: 0\
 }\x0d\x0a            \
  XYPoint { x: 1\
; y: 0.5 }\x0d\x0a    \
          XYPoin\
t { x: 2; y: 0.7\
5 }\x0d\x0a           \
   XYPoint { x: \
3; y: 0.87 }\x0d\x0a  \
            XYPo\
int { x: 4; y: 0\
.92 }\x0d\x0a         \
     XYPoint { x\
: 5; y: 0.95 }\x0d\x0a\
            }\x0d\x0a \
           Splin\
eSeries {\x0d\x0a     \
         name: '\
mAP'\x0d\x0a          \
    axisX: value\
AxisSplineSeries\
\x0d\x0a              \
XYPoint { x: 0; \
y: 0 }\x0d\x0a        \
      XYPoint { \
x: 1; y: 0.45 }\x0d\
\x0a              X\
YPoint { x: 2; y\
: 0.80 }\x0d\x0a      \
        XYPoint \
{ x: 3; y: 0.78 \
}\x0d\x0a             \
 XYPoint { x: 4;\
 y: 0.85 }\x0d\x0a    \
          XYPoin\
t { x: 5; y: 0.9\
0 }\x0d\x0a           \
 }\x0d\x0a            \
SplineSeries {\x0d\x0a\
              na\
me: 'mIoU'\x0d\x0a    \
          axisX:\
 valueAxisSpline\
Series\x0d\x0a        \
      XYPoint { \
x: 0; y: 0 }\x0d\x0a  \
            XYPo\
int { x: 1; y: 0\
.43 }\x0d\x0a         \
     XYPoint { x\
: 2; y: 0.68 }\x0d\x0a\
              XY\
Point { x: 3; y:\
 0.84 }\x0d\x0a       \
       XYPoint {\
 x: 4; y: 0.90 }\
\x0d\x0a              \
XYPoint { x: 5; \
y: 0.92 }\x0d\x0a     \
       }\x0d\x0a      \
    }\x0d\x0a        }\
\x0d\x0a      }\x0d\x0a\x0d\x0a   \
   /************\
****************\
****************\
**************\x0d\x0a\
      Pop-Ups\x0d\x0a \
     ***********\
****************\
****************\
***************/\
\x0d\x0a      Popup {\x0d\
\x0a        id: nor\
malPopup\x0d\x0a      \
  ColumnLayout {\
\x0d\x0a          anch\
ors.fill: parent\
\x0d\x0a          Labe\
l { text: 'Norma\
l Popup' }\x0d\x0a    \
      CheckBox {\
 text: 'E-mail' \
}\x0d\x0a          Che\
ckBox { text: 'C\
alendar' }\x0d\x0a    \
      CheckBox {\
 text: 'Contacts\
' }\x0d\x0a        }\x0d\x0a\
      }\x0d\x0a      P\
opup {\x0d\x0a        \
id: modalPopup\x0d\x0a\
        modal: t\
rue\x0d\x0a        Col\
umnLayout {\x0d\x0a   \
       anchors.f\
ill: parent\x0d\x0a   \
       Label { t\
ext: 'Modal Popu\
p' }\x0d\x0a          \
CheckBox { text:\
 'E-mail' }\x0d\x0a   \
       CheckBox \
{ text: 'Calenda\
r' }\x0d\x0a          \
CheckBox { text:\
 'Contacts' }\x0d\x0a \
       }\x0d\x0a      \
}\x0d\x0a      Dialog \
{\x0d\x0a        id: d\
ialog\x0d\x0a        t\
itle: 'Dialog'\x0d\x0a\
        Label { \
text: 'The stand\
ard dialog.' }\x0d\x0a\
        footer: \
DialogButtonBox \
{\x0d\x0a          sta\
ndardButtons: Di\
alogButtonBox.Ok\
 | DialogButtonB\
ox.Cancel\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a\x0d\
\x0a      FileDialo\
g {\x0d\x0a        id:\
 trainFileDialog\
\x0d\x0a        title:\
 \x22Choose a folde\
r...\x22\x0d\x0a        s\
electFolder: tru\
e\x0d\x0a        selec\
tMultiple: false\
\x0d\x0a        folder\
: shortcuts.home\
\x0d\x0a        onAcce\
pted: {\x0d\x0a       \
     var path = \
trainFileDialog.\
fileUrl.toString\
()\x0d\x0a            \
// reomve prefix\
 \x22file:///\x22\x0d\x0a   \
         path = \
path.replace(/^(\
file:\x5c/{3})/,\x22\x22)\
\x0d\x0a            //\
 unescape HTML c\
odes\x0d\x0a          \
  var cleanPath \
= decodeURICompo\
nent(path);\x0d\x0a   \
         trainPa\
th.text = cleanP\
ath\x0d\x0a        }\x0d\x0a\
      }\x0d\x0a\x0d\x0a     \
 FileDialog {\x0d\x0a \
       id: testF\
ileDialog\x0d\x0a     \
   title: \x22Choos\
e a folder...\x22\x0d\x0a\
        selectFo\
lder: true\x0d\x0a    \
    selectMultip\
le: false\x0d\x0a     \
   folder: short\
cuts.home\x0d\x0a     \
   onAccepted: {\
\x0d\x0a            va\
r path = testFil\
eDialog.fileUrl.\
toString()\x0d\x0a    \
        // reomv\
e prefix \x22file:/\
//\x22\x0d\x0a           \
 path = path.rep\
lace(/^(file:\x5c/{\
3})/,\x22\x22)\x0d\x0a      \
      // unescap\
e HTML codes\x0d\x0a  \
          var cl\
eanPath = decode\
URIComponent(pat\
h);\x0d\x0a           \
 testPath.text =\
 cleanPath\x0d\x0a    \
    }\x0d\x0a      }\x0d\x0a\
    }\x0d\x0a  }\x0d\x0a\x0d\x0a  \
/***************\
****************\
****************\
***********\x0d\x0a  F\
ooter\x0d\x0a  *******\
****************\
****************\
****************\
***/\x0d\x0a  footer: \
RowLayout {\x0d\x0a   \
 width: parent.w\
idth\x0d\x0a    RowLay\
out {\x0d\x0a      Lay\
out.margins: 10\x0d\
\x0a      Layout.al\
ignment: Qt.Alig\
nHCenter\x0d\x0a      \
Label { text: 'T\
heme customizati\
on: ' }\x0d\x0a      L\
abel {\x0d\x0a        \
id: qtquick2Them\
es\x0d\x0a        obje\
ctName: 'qtquick\
2Themes'\x0d\x0a      \
  Layout.fillWid\
th: true\x0d\x0a      \
}\x0d\x0a    }\x0d\x0a    Ro\
wLayout {\x0d\x0a     \
 Layout.margins:\
 10\x0d\x0a      Layou\
t.alignment: Qt.\
AlignHCenter\x0d\x0a  \
    Label { text\
: 'QtQuick Chart\
s Themes: ' }\x0d\x0a \
     ComboBox {\x0d\
\x0a        id: qtq\
uickChartsThemes\
\x0d\x0a        model:\
 [\x0d\x0a          'C\
hartThemeLight',\
 'ChartThemeBlue\
Cerulean',\x0d\x0a    \
      'ChartThem\
eDark', 'ChartTh\
emeBrownSand',\x0d\x0a\
          'Chart\
ThemeBlueNcs', '\
ChartThemeHighCo\
ntrast',\x0d\x0a      \
    'ChartThemeB\
lueIcy', 'ChartT\
hemeQt'\x0d\x0a       \
 ]\x0d\x0a        Layo\
ut.fillWidth: tr\
ue\x0d\x0a        curr\
entIndex: 2\x0d\x0a   \
   }\x0d\x0a    }\x0d\x0a   \
 RowLayout {\x0d\x0a  \
    Layout.margi\
ns: 10\x0d\x0a      La\
yout.alignment: \
Qt.AlignHCenter\x0d\
\x0a      Label { t\
ext: 'Sub-Theme:\
 ' }\x0d\x0a      Comb\
oBox {\x0d\x0a        \
id: subTheme\x0d\x0a  \
      model: ['D\
ark', 'Light']\x0d\x0a\
        Layout.f\
illWidth: true\x0d\x0a\
        enabled:\
 true\x0d\x0a      }\x0d\x0a\
    }\x0d\x0a    RowLa\
yout {\x0d\x0a      pr\
operty var mater\
ialColors: [\x0d\x0a  \
      'Red', 'Pi\
nk', 'Purple', '\
DeepPurple', 'In\
digo', 'Blue',\x0d\x0a\
        'LightBl\
ue', 'Cyan', 'Te\
al', 'Green', 'L\
ightGreen', 'Lim\
e',\x0d\x0a        'Ye\
llow', 'Amber', \
'Orange', 'DeepO\
range', 'Brown',\
 'Grey',\x0d\x0a      \
  'BlueGrey'\x0d\x0a  \
    ]\x0d\x0a      Lay\
out.margins: 10\x0d\
\x0a      Layout.al\
ignment: Qt.Alig\
nHCenter\x0d\x0a\x0d\x0a    \
  Label { text: \
'Primary' }\x0d\x0a   \
   ComboBox {\x0d\x0a \
       id: prima\
ryColor\x0d\x0a       \
 Layout.fillWidt\
h: true\x0d\x0a       \
 enabled: true\x0d\x0a\
        model: p\
arent.materialCo\
lors\x0d\x0a        cu\
rrentIndex: 6\x0d\x0a \
     }\x0d\x0a\x0d\x0a      \
Label { text: 'A\
ccent' }\x0d\x0a      \
ComboBox {\x0d\x0a    \
    id: accentCo\
lor\x0d\x0a        Lay\
out.fillWidth: t\
rue\x0d\x0a        ena\
bled: true\x0d\x0a    \
    model: paren\
t.materialColors\
\x0d\x0a        curren\
tIndex: 7\x0d\x0a     \
 }\x0d\x0a    }\x0d\x0a  }\x0d\x0a\
}\
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
\x00\x00\x00h\
i\
mport QtQuick.Co\
ntrols 2.4\x0d\x0a\x0d\x0aBu\
tton {\x0d\x0a  flat: \
true\x0d\x0a  backgrou\
nd.anchors.fill:\
 this\x0d\x0a  spacing\
: 40\x0d\x0a}\
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
\x00\x00\x003\
[\
Controls]\x0d\x0aStyle\
=Material\x0d\x0aFallb\
ackStyle=Default\
\x0d\x0a\
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
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x0b\
\x09\xf8\xd2<\
\x00C\
\x00e\x00l\x00l\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x11\
\x03S\x87\xdc\
\x00S\
\x00i\x00d\x00e\x00N\x00a\x00v\x00B\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\
\x00\x12\
\x08\xbdU\xfc\
\x00L\
\x00a\x00r\x00g\x00e\x00C\x00h\x00a\x00r\x00t\x00V\x00i\x00e\x00w\x00.\x00q\x00m\
\x00l\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
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
\x00\x00\x00\x1e\x00\x02\x00\x00\x00\x05\x00\x00\x00\x07\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x00\xde\x00\x00\x00\x00\x00\x01\x00\x00A\xdb\
\x00\x00\x01L\x00\x00\x00\x00\x00\x01\x00\x00C\xd5\
\x00\x00\x01\x10\x00\x00\x00\x00\x00\x01\x00\x00B\xa6\
\x00\x00\x00\x5c\x00\x00\x00\x00\x00\x01\x00\x00@D\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\xae\x00\x00\x00\x00\x00\x01\x00\x00A\xa4\
\x00\x00\x00\x84\x00\x00\x00\x00\x00\x01\x00\x00@\xb0\
\x00\x00\x00@\x00\x00\x00\x00\x00\x01\x00\x00?\x96\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
