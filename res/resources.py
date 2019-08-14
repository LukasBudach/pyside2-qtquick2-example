# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Mi Aug 14 15:56:11 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
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
\x00\x00:!\
i\
mport QtQuick 2.\
13\x0d\x0aimport QtQui\
ck.Layouts 1.11\x0d\
\x0aimport QtQuick.\
Controls 2.4\x0d\x0aim\
port QtQuick.Con\
trols.Material 2\
.4\x0d\x0aimport QtCha\
rts 2.2\x0d\x0a\x0d\x0aAppli\
cationWindow {\x0d\x0a\
  id: mainWindow\
\x0d\x0a  title: 'My a\
mazing neural ne\
twork app'\x0d\x0a  vi\
sible: true\x0d\x0a  m\
inimumHeight: 90\
0\x0d\x0a  minimumWidt\
h: 1600\x0d\x0a  Mater\
ial.theme: Mater\
ial[subTheme.cur\
rentText]\x0d\x0a  Mat\
erial.accent: Ma\
terial[accentCol\
or.currentText]\x0d\
\x0a  Material.prim\
ary: Material[pr\
imaryColor.curre\
ntText]\x0d\x0a\x0d\x0a  sig\
nal lossreemitte\
d(int epoch, dou\
ble loss)\x0d\x0a  sig\
nal consolereemi\
tted(string log)\
\x0d\x0a\x0d\x0a  Component.\
onCompleted: {\x0d\x0a\
      control_br\
idge.epoch_done.\
connect(mainWind\
ow.lossreemitted\
)\x0d\x0a      control\
_bridge.log_even\
t.connect(mainWi\
ndow.consolereem\
itted)\x0d\x0a  }\x0d\x0a  o\
nLossreemitted: \
{\x0d\x0a      yAxisLo\
ssSeries.max = M\
ath.max(yAxisLos\
sSeries.max, los\
s)\x0d\x0a      yAxisL\
ossSeries.min = \
Math.min(yAxisLo\
ssSeries.min, lo\
ss)\x0d\x0a      lossS\
eries.append(epo\
ch, loss)\x0d\x0a  }\x0d\x0a\
  onConsolereemi\
tted: {\x0d\x0a      c\
onsoleTextfield.\
append(log)\x0d\x0a  }\
\x0d\x0a\x0d\x0a  header: To\
olBar {\x0d\x0a    Row\
Layout {\x0d\x0a      \
anchors.fill: pa\
rent\x0d\x0a      Tool\
Button {\x0d\x0a      \
  icon.source: '\
../images/baseli\
ne-menu-24px.svg\
'\x0d\x0a        onCli\
cked: sideNav.op\
en()\x0d\x0a      }\x0d\x0a \
     Label {\x0d\x0a  \
      text: 'Neu\
ral network cont\
rol panel'\x0d\x0a    \
    elide: Label\
.ElideRight\x0d\x0a   \
     horizontalA\
lignment: Qt.Ali\
gnHCenter\x0d\x0a     \
   verticalAlign\
ment: Qt.AlignVC\
enter\x0d\x0a        L\
ayout.fillWidth:\
 true\x0d\x0a      }\x0d\x0a\
      ToolButton\
 {\x0d\x0a        text\
: 'Start Trainin\
g'\x0d\x0a        id: \
btn_startTrainin\
g\x0d\x0a        onCli\
cked: () => {\x0d\x0a \
           btn_s\
tartTraining.ena\
bled = false\x0d\x0a  \
          contro\
l_bridge.start_s\
imulation()\x0d\x0a   \
     }\x0d\x0a      }\x0d\
\x0a      ToolButto\
n { text: 'Pause\
 Training' }\x0d\x0a  \
    ToolSeparato\
r {}\x0d\x0a      Tool\
Button {\x0d\x0a      \
  icon.source: '\
../images/baseli\
ne-more_vert-24p\
x.svg'\x0d\x0a        \
onClicked: menu.\
open()\x0d\x0a        \
Menu {\x0d\x0a        \
  id: menu\x0d\x0a    \
      y: parent.\
height\x0d\x0a        \
  MenuItem { tex\
t: 'New...' }\x0d\x0a \
         MenuIte\
m { text: 'Open.\
..' }\x0d\x0a         \
 MenuItem { text\
: 'Save' }\x0d\x0a    \
    }\x0d\x0a      }\x0d\x0a\
    }\x0d\x0a  }\x0d\x0a  Dr\
awer {\x0d\x0a    id: \
sideNav\x0d\x0a    wid\
th: 200\x0d\x0a    hei\
ght: parent.heig\
ht\x0d\x0a    ColumnLa\
yout {\x0d\x0a      wi\
dth: parent.widt\
h\x0d\x0a      Label {\
\x0d\x0a          text\
: 'Drawer'\x0d\x0a    \
      horizontal\
Alignment: Text.\
AlignHCenter\x0d\x0a  \
        vertical\
Alignment: Text.\
AlignVCenter\x0d\x0a  \
        font.pix\
elSize: 20\x0d\x0a    \
      Layout.fil\
lWidth: true\x0d\x0a  \
    }\x0d\x0a      Rep\
eater {\x0d\x0a       \
 model: 5\x0d\x0a     \
   SideNavButton\
 {\x0d\x0a          ic\
on.source: '../i\
mages/baseline-c\
ategory-24px.svg\
'\x0d\x0a          tex\
t: 'List ' + ind\
ex\x0d\x0a          La\
yout.fillWidth: \
true\x0d\x0a        }\x0d\
\x0a      }\x0d\x0a    }\x0d\
\x0a  }\x0d\x0a  Pane {\x0d\x0a\
    padding: 10\x0d\
\x0a    anchors.fil\
l: parent\x0d\x0a    G\
ridLayout {\x0d\x0a   \
   anchors.fill:\
 parent\x0d\x0a      f\
low: GridLayout.\
TopToBottom\x0d\x0a   \
   rows: 3\x0d\x0a\x0d\x0a  \
    CellBox {\x0d\x0a \
       title: 'D\
atasets'\x0d\x0a      \
  GridLayout {\x0d\x0a\
            anch\
ors.fill: parent\
\x0d\x0a            co\
lumns: 3\x0d\x0a      \
      Label {\x0d\x0a \
               t\
ext: 'Train Data\
set'\x0d\x0a          \
      Layout.ali\
gnment: Qt.Align\
HCenter\x0d\x0a       \
     }\x0d\x0a        \
    TextField {\x0d\
\x0a               \
 width: parent.w\
idth\x0d\x0a          \
      placeholde\
rText: 'Train Da\
ta goes here...'\
\x0d\x0a              \
  selectByMouse:\
 true\x0d\x0a         \
   }\x0d\x0a          \
  RoundButton {\x0d\
\x0a               \
 text: '...'\x0d\x0a  \
              La\
yout.alignment: \
Qt.AlignHCenter\x0d\
\x0a            }\x0d\x0a\
\x0d\x0a            La\
bel {\x0d\x0a         \
       text: 'Te\
st Dataset'\x0d\x0a   \
             Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
            }\x0d\x0a \
           TextF\
ield {\x0d\x0a        \
        width: p\
arent.width\x0d\x0a   \
             pla\
ceholderText: 'T\
est Data goes he\
re...'\x0d\x0a        \
        selectBy\
Mouse: true\x0d\x0a   \
         }\x0d\x0a    \
        RoundBut\
ton {\x0d\x0a         \
       text: '..\
.'\x0d\x0a            \
    Layout.align\
ment: Qt.AlignHC\
enter\x0d\x0a         \
   }\x0d\x0a        }\x0d\
\x0a      }\x0d\x0a\x0d\x0a    \
  CellBox {\x0d\x0a   \
     title: 'Net\
work Settings'\x0d\x0a\
        GridLayo\
ut {\x0d\x0a          \
  anchors.fill: \
parent\x0d\x0a        \
    columns: 2\x0d\x0a\
            Labe\
l {\x0d\x0a           \
     text: 'Tota\
l Training Epoch\
s'\x0d\x0a            \
    Layout.align\
ment: Qt.AlignHC\
enter\x0d\x0a         \
   }\x0d\x0a          \
  SpinBox {\x0d\x0a   \
             id:\
 totalEpochs\x0d\x0a  \
              ed\
itable: true\x0d\x0a  \
              va\
lue: settings_br\
idge.epochs\x0d\x0a   \
             fro\
m: 1\x0d\x0a          \
      to: 999999\
\x0d\x0a              \
  Layout.fillWid\
th: true\x0d\x0a      \
          onValu\
eChanged: settin\
gs_bridge.epochs\
 = value\x0d\x0a      \
          Compon\
ent.onCompleted:\
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
"

qt_resource_name = b"\
\x00\x03\
\x00\x00x\xc3\
\x00r\
\x00e\x00s\
\x00\x03\
\x00\x00x<\
\x00q\
\x00m\x00l\
\x00\x06\
\x07\x03}\xc3\
\x00i\
\x00m\x00a\x00g\x00e\x00s\
\x00\x1a\
\x0b\xaf\xda'\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00c\x00a\x00t\x00e\x00g\x00o\x00r\x00y\
\x00-\x002\x004\x00p\x00x\x00.\x00s\x00v\x00g\
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
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x0b\
\x09\xf8\xd2<\
\x00C\
\x00e\x00l\x00l\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x04\x00\x00\x00\x07\
\x00\x00\x00\x18\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x00d\x00\x00\x00\x00\x00\x01\x00\x00\x00\xf9\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x96\x00\x00\x00\x00\x00\x01\x00\x00\x01\xc4\
\x00\x00\x00\xfc\x00\x00\x00\x00\x00\x01\x00\x00\x03\xe7\
\x00\x00\x01$\x00\x00\x00\x00\x00\x01\x00\x00\x04S\
\x00\x00\x00\xd2\x00\x00\x00\x00\x00\x01\x00\x00\x02\xf3\
\x00\x00\x01:\x00\x00\x00\x00\x00\x01\x00\x00>x\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
