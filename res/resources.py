# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Di Aug 13 20:52:55 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
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
\x00\x007\x04\
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
  title: 'My ama\
zing neural netw\
ork app'\x0d\x0a  visi\
ble: true\x0d\x0a  min\
imumHeight: 900\x0d\
\x0a  minimumWidth:\
 1600\x0d\x0a  Materia\
l.theme: Materia\
l[subTheme.curre\
ntText]\x0d\x0a  Mater\
ial.accent: Mate\
rial[accentColor\
.currentText]\x0d\x0a \
 Material.primar\
y: Material[prim\
aryColor.current\
Text]\x0d\x0a  header:\
 ToolBar {\x0d\x0a    \
RowLayout {\x0d\x0a   \
   anchors.fill:\
 parent\x0d\x0a      T\
oolButton {\x0d\x0a   \
     icon.source\
: '../images/bas\
eline-menu-24px.\
svg'\x0d\x0a        on\
Clicked: sideNav\
.open()\x0d\x0a      }\
\x0d\x0a      Label {\x0d\
\x0a        text: '\
Neural network c\
ontrol panel'\x0d\x0a \
       elide: La\
bel.ElideRight\x0d\x0a\
        horizont\
alAlignment: Qt.\
AlignHCenter\x0d\x0a  \
      verticalAl\
ignment: Qt.Alig\
nVCenter\x0d\x0a      \
  Layout.fillWid\
th: true\x0d\x0a      \
}\x0d\x0a      ToolBut\
ton { text: 'Sta\
rt Training' }\x0d\x0a\
      ToolButton\
 { text: 'Pause \
Training' }\x0d\x0a   \
   ToolSeparator\
 {}\x0d\x0a      ToolB\
utton {\x0d\x0a       \
 icon.source: '.\
./images/baselin\
e-more_vert-24px\
.svg'\x0d\x0a        o\
nClicked: menu.o\
pen()\x0d\x0a        M\
enu {\x0d\x0a         \
 id: menu\x0d\x0a     \
     y: parent.h\
eight\x0d\x0a         \
 MenuItem { text\
: 'New...' }\x0d\x0a  \
        MenuItem\
 { text: 'Open..\
.' }\x0d\x0a          \
MenuItem { text:\
 'Save' }\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a \
   }\x0d\x0a  }\x0d\x0a  Dra\
wer {\x0d\x0a    id: s\
ideNav\x0d\x0a    widt\
h: 200\x0d\x0a    heig\
ht: parent.heigh\
t\x0d\x0a    ColumnLay\
out {\x0d\x0a      wid\
th: parent.width\
\x0d\x0a      Label {\x0d\
\x0a          text:\
 'Drawer'\x0d\x0a     \
     horizontalA\
lignment: Text.A\
lignHCenter\x0d\x0a   \
       verticalA\
lignment: Text.A\
lignVCenter\x0d\x0a   \
       font.pixe\
lSize: 20\x0d\x0a     \
     Layout.fill\
Width: true\x0d\x0a   \
   }\x0d\x0a      Repe\
ater {\x0d\x0a        \
model: 5\x0d\x0a      \
  SideNavButton \
{\x0d\x0a          ico\
n.source: '../im\
ages/baseline-ca\
tegory-24px.svg'\
\x0d\x0a          text\
: 'List ' + inde\
x\x0d\x0a          Lay\
out.fillWidth: t\
rue\x0d\x0a        }\x0d\x0a\
      }\x0d\x0a    }\x0d\x0a\
  }\x0d\x0a  Pane {\x0d\x0a \
   padding: 10\x0d\x0a\
    anchors.fill\
: parent\x0d\x0a    Gr\
idLayout {\x0d\x0a    \
  anchors.fill: \
parent\x0d\x0a      fl\
ow: GridLayout.T\
opToBottom\x0d\x0a    \
  rows: 3\x0d\x0a\x0d\x0a   \
   CellBox {\x0d\x0a  \
      title: 'Da\
tasets'\x0d\x0a       \
 GridLayout {\x0d\x0a \
           ancho\
rs.fill: parent\x0d\
\x0a            col\
umns: 3\x0d\x0a       \
     Label {\x0d\x0a  \
              te\
xt: 'Train Datas\
et'\x0d\x0a           \
     Layout.alig\
nment: Qt.AlignH\
Center\x0d\x0a        \
    }\x0d\x0a         \
   TextField {\x0d\x0a\
                \
width: parent.wi\
dth\x0d\x0a           \
     placeholder\
Text: 'Train Dat\
a goes here...'\x0d\
\x0a               \
 selectByMouse: \
true\x0d\x0a          \
  }\x0d\x0a           \
 RoundButton {\x0d\x0a\
                \
text: '...'\x0d\x0a   \
             Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
            }\x0d\x0a\x0d\
\x0a            Lab\
el {\x0d\x0a          \
      text: 'Tes\
t Dataset'\x0d\x0a    \
            Layo\
ut.alignment: Qt\
.AlignHCenter\x0d\x0a \
           }\x0d\x0a  \
          TextFi\
eld {\x0d\x0a         \
       width: pa\
rent.width\x0d\x0a    \
            plac\
eholderText: 'Te\
st Data goes her\
e...'\x0d\x0a         \
       selectByM\
ouse: true\x0d\x0a    \
        }\x0d\x0a     \
       RoundButt\
on {\x0d\x0a          \
      text: '...\
'\x0d\x0a             \
   Layout.alignm\
ent: Qt.AlignHCe\
nter\x0d\x0a          \
  }\x0d\x0a        }\x0d\x0a\
      }\x0d\x0a\x0d\x0a     \
 CellBox {\x0d\x0a    \
    title: 'Netw\
ork Settings'\x0d\x0a \
       GridLayou\
t {\x0d\x0a           \
 anchors.fill: p\
arent\x0d\x0a         \
   columns: 2\x0d\x0a \
           Label\
 {\x0d\x0a            \
    text: 'Total\
 Training Epochs\
'\x0d\x0a             \
   Layout.alignm\
ent: Qt.AlignHCe\
nter\x0d\x0a          \
  }\x0d\x0a           \
 SpinBox {\x0d\x0a    \
            id: \
totalEpochs\x0d\x0a   \
             edi\
table: true\x0d\x0a   \
             val\
ue: 10\x0d\x0a        \
        from: 1\x0d\
\x0a               \
 to: 999999\x0d\x0a   \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
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
ut'\x0d\x0a        Col\
umn {\x0d\x0a         \
 // ScrollView w\
ill not work if \
we use ColumnLay\
out as\x0d\x0a        \
  // ColumnLayou\
t always measure\
s its size depen\
ding on its\x0d\x0a   \
       // conten\
ts.\x0d\x0a          a\
nchors.fill: par\
ent\x0d\x0a          s\
pacing: 10\x0d\x0a    \
      ScrollView\
 {\x0d\x0a            \
width: parent.wi\
dth\x0d\x0a           \
 height: 150\x0d\x0a  \
          TextAr\
ea {\x0d\x0a          \
    text: 'Multi\
-line text edito\
r...\x5cnThis is a \
new line.'\x0d\x0a    \
          select\
ByMouse: true\x0d\x0a \
             per\
sistentSelection\
: true\x0d\x0a        \
      readOnly: \
true\x0d\x0a          \
  }\x0d\x0a          }\
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
         text: '\
6'\x0d\x0a            \
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
 text: 'Train Ac\
curacy'\x0d\x0a       \
         }\x0d\x0a    \
            Labe\
l {\x0d\x0a           \
         text: '\
100%'\x0d\x0a         \
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
.03'\x0d\x0a          \
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
'95.4%'\x0d\x0a       \
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
      text: 'Tes\
t Loss'\x0d\x0a       \
         }\x0d\x0a    \
            Labe\
l {\x0d\x0a           \
         text: '\
0.05'\x0d\x0a         \
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
    text: 'mAP'\x0d\
\x0a               \
 }\x0d\x0a            \
    Label {\x0d\x0a   \
                \
 text: '90%'\x0d\x0a  \
                \
  horizontalAlig\
nment: Text.Alig\
nRight\x0d\x0a        \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
    }\x0d\x0a\x0d\x0a       \
         Label {\
\x0d\x0a              \
      Layout.fil\
lWidth: true\x0d\x0a  \
                \
  horizontalAlig\
nment: Text.Alig\
nLeft\x0d\x0a         \
           text:\
 'mIoU'\x0d\x0a       \
         }\x0d\x0a    \
            Labe\
l {\x0d\x0a           \
         text: '\
92%'\x0d\x0a          \
          horizo\
ntalAlignment: T\
ext.AlignRight\x0d\x0a\
                \
    Layout.fillW\
idth: true\x0d\x0a    \
            }\x0d\x0a\x0d\
\x0a              }\
\x0d\x0a\x0d\x0a            \
  GridLayout {\x0d\x0a\
                \
  Layout.alignme\
nt: Qt.AlignBott\
om\x0d\x0a            \
      columns: 2\
\x0d\x0a\x0d\x0a            \
      Label {\x0d\x0a \
                \
     Layout.fill\
Width: true\x0d\x0a   \
                \
   horizontalAli\
gnment: Text.Ali\
gnLeft\x0d\x0a        \
              te\
xt: 'Epoch Progr\
ess: '\x0d\x0a        \
          }\x0d\x0a   \
               L\
abel {\x0d\x0a        \
              te\
xt: '60%'\x0d\x0a     \
                \
 horizontalAlign\
ment: Text.Align\
Right\x0d\x0a         \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
       }\x0d\x0a      \
            Prog\
ressBar {\x0d\x0a     \
                \
 Layout.fillWidt\
h: true\x0d\x0a       \
               L\
ayout.columnSpan\
: 2\x0d\x0a           \
           value\
: 0.6;\x0d\x0a        \
          }\x0d\x0a   \
           }\x0d\x0a  \
        }\x0d\x0a     \
 }\x0d\x0a\x0d\x0a      /***\
****************\
****************\
****************\
*******\x0d\x0a      G\
raphs\x0d\x0a      ***\
****************\
****************\
****************\
*******/\x0d\x0a      \
CellBox {\x0d\x0a     \
   Layout.rowSpa\
n: 3; Layout.min\
imumWidth: 700\x0d\x0a\
        Layout.p\
referredWidth: h\
eight // Keep th\
e ratio right!\x0d\x0a\
        TabBar {\
\x0d\x0a          id: \
bar\x0d\x0a          w\
idth: parent.wid\
th\x0d\x0a          Ta\
bButton { text: \
'Test Loss' }\x0d\x0a \
         TabButt\
on { text: 'Accu\
racies' }\x0d\x0a     \
   }\x0d\x0a        St\
ackLayout {\x0d\x0a   \
       width: pa\
rent.width\x0d\x0a    \
      height: pa\
rent.height - y\x0d\
\x0a          ancho\
rs.top: bar.bott\
om\x0d\x0a          cu\
rrentIndex: bar.\
currentIndex\x0d\x0a  \
        LargeCha\
rtView {\x0d\x0a      \
      ValueAxis \
{\x0d\x0a             \
 id: valueAxisLo\
ssSeries\x0d\x0a      \
        min: 0\x0d\x0a\
              ma\
x: 5\x0d\x0a          \
    tickCount: 6\
\x0d\x0a              \
labelFormat: '%.\
0f'\x0d\x0a           \
 }\x0d\x0a\x0d\x0a          \
  SplineSeries {\
\x0d\x0a              \
name: 'Test Loss\
'\x0d\x0a             \
 axisX: valueAxi\
sLossSeries\x0d\x0a   \
           XYPoi\
nt { x: 0; y: 0 \
}\x0d\x0a             \
 XYPoint { x: 1;\
 y: 2.67 }\x0d\x0a    \
          XYPoin\
t { x: 2; y: 1.3\
4 }\x0d\x0a           \
   XYPoint { x: \
3; y: 0.51 }\x0d\x0a  \
            XYPo\
int { x: 4; y: 0\
.21 }\x0d\x0a         \
     XYPoint { x\
: 5; y: 0.05 }\x0d\x0a\
            }\x0d\x0a \
         }\x0d\x0a\x0d\x0a  \
        LargeCha\
rtView {\x0d\x0a      \
      ValueAxis \
{\x0d\x0a             \
 id: valueAxisSp\
lineSeries\x0d\x0a    \
          min: 0\
\x0d\x0a              \
max: 5\x0d\x0a        \
      tickCount:\
 6\x0d\x0a            \
  labelFormat: '\
%.0f'\x0d\x0a         \
   }\x0d\x0a\x0d\x0a        \
    SplineSeries\
 {\x0d\x0a            \
  name: 'Test Ac\
c.'\x0d\x0a           \
   axisX: valueA\
xisSplineSeries\x0d\
\x0a              X\
YPoint { x: 0; y\
: 0 }\x0d\x0a         \
     XYPoint { x\
: 1; y: 0.5 }\x0d\x0a \
             XYP\
oint { x: 2; y: \
0.75 }\x0d\x0a        \
      XYPoint { \
x: 3; y: 0.87 }\x0d\
\x0a              X\
YPoint { x: 4; y\
: 0.92 }\x0d\x0a      \
        XYPoint \
{ x: 5; y: 0.95 \
}\x0d\x0a            }\
\x0d\x0a            Sp\
lineSeries {\x0d\x0a  \
            name\
: 'mAP'\x0d\x0a       \
       axisX: va\
lueAxisSplineSer\
ies\x0d\x0a           \
   XYPoint { x: \
0; y: 0 }\x0d\x0a     \
         XYPoint\
 { x: 1; y: 0.45\
 }\x0d\x0a            \
  XYPoint { x: 2\
; y: 0.80 }\x0d\x0a   \
           XYPoi\
nt { x: 3; y: 0.\
78 }\x0d\x0a          \
    XYPoint { x:\
 4; y: 0.85 }\x0d\x0a \
             XYP\
oint { x: 5; y: \
0.90 }\x0d\x0a        \
    }\x0d\x0a         \
   SplineSeries \
{\x0d\x0a             \
 name: 'mIoU'\x0d\x0a \
             axi\
sX: valueAxisSpl\
ineSeries\x0d\x0a     \
         XYPoint\
 { x: 0; y: 0 }\x0d\
\x0a              X\
YPoint { x: 1; y\
: 0.43 }\x0d\x0a      \
        XYPoint \
{ x: 2; y: 0.68 \
}\x0d\x0a             \
 XYPoint { x: 3;\
 y: 0.84 }\x0d\x0a    \
          XYPoin\
t { x: 4; y: 0.9\
0 }\x0d\x0a           \
   XYPoint { x: \
5; y: 0.92 }\x0d\x0a  \
          }\x0d\x0a   \
       }\x0d\x0a      \
  }\x0d\x0a      }\x0d\x0a\x0d\x0a\
      /*********\
****************\
****************\
****************\
*\x0d\x0a      Pop-Ups\
\x0d\x0a      ********\
****************\
****************\
****************\
**/\x0d\x0a      Popup\
 {\x0d\x0a        id: \
normalPopup\x0d\x0a   \
     ColumnLayou\
t {\x0d\x0a          a\
nchors.fill: par\
ent\x0d\x0a          L\
abel { text: 'No\
rmal Popup' }\x0d\x0a \
         CheckBo\
x { text: 'E-mai\
l' }\x0d\x0a          \
CheckBox { text:\
 'Calendar' }\x0d\x0a \
         CheckBo\
x { text: 'Conta\
cts' }\x0d\x0a        \
}\x0d\x0a      }\x0d\x0a    \
  Popup {\x0d\x0a     \
   id: modalPopu\
p\x0d\x0a        modal\
: true\x0d\x0a        \
ColumnLayout {\x0d\x0a\
          anchor\
s.fill: parent\x0d\x0a\
          Label \
{ text: 'Modal P\
opup' }\x0d\x0a       \
   CheckBox { te\
xt: 'E-mail' }\x0d\x0a\
          CheckB\
ox { text: 'Cale\
ndar' }\x0d\x0a       \
   CheckBox { te\
xt: 'Contacts' }\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a      Dial\
og {\x0d\x0a        id\
: dialog\x0d\x0a      \
  title: 'Dialog\
'\x0d\x0a        Label\
 { text: 'The st\
andard dialog.' \
}\x0d\x0a        foote\
r: DialogButtonB\
ox {\x0d\x0a          \
standardButtons:\
 DialogButtonBox\
.Ok | DialogButt\
onBox.Cancel\x0d\x0a  \
      }\x0d\x0a      }\
\x0d\x0a    }\x0d\x0a  }\x0d\x0a\x0d\x0a\
  /*************\
****************\
****************\
*************\x0d\x0a \
 Footer\x0d\x0a  *****\
****************\
****************\
****************\
*****/\x0d\x0a  footer\
: RowLayout {\x0d\x0a \
   width: parent\
.width\x0d\x0a    RowL\
ayout {\x0d\x0a      L\
ayout.margins: 1\
0\x0d\x0a      Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a    \
  Label { text: \
'Theme customiza\
tion: ' }\x0d\x0a     \
 Label {\x0d\x0a      \
  id: qtquick2Th\
emes\x0d\x0a        ob\
jectName: 'qtqui\
ck2Themes'\x0d\x0a    \
    Layout.fillW\
idth: true\x0d\x0a    \
  }\x0d\x0a    }\x0d\x0a    \
RowLayout {\x0d\x0a   \
   Layout.margin\
s: 10\x0d\x0a      Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
      Label { te\
xt: 'QtQuick Cha\
rts Themes: ' }\x0d\
\x0a      ComboBox \
{\x0d\x0a        id: q\
tquickChartsThem\
es\x0d\x0a        mode\
l: [\x0d\x0a          \
'ChartThemeLight\
', 'ChartThemeBl\
ueCerulean',\x0d\x0a  \
        'ChartTh\
emeDark', 'Chart\
ThemeBrownSand',\
\x0d\x0a          'Cha\
rtThemeBlueNcs',\
 'ChartThemeHigh\
Contrast',\x0d\x0a    \
      'ChartThem\
eBlueIcy', 'Char\
tThemeQt'\x0d\x0a     \
   ]\x0d\x0a        La\
yout.fillWidth: \
true\x0d\x0a        cu\
rrentIndex: 2\x0d\x0a \
     }\x0d\x0a    }\x0d\x0a \
   RowLayout {\x0d\x0a\
      Layout.mar\
gins: 10\x0d\x0a      \
Layout.alignment\
: Qt.AlignHCente\
r\x0d\x0a      Label {\
 text: 'Sub-Them\
e: ' }\x0d\x0a      Co\
mboBox {\x0d\x0a      \
  id: subTheme\x0d\x0a\
        model: [\
'Dark', 'Light']\
\x0d\x0a        Layout\
.fillWidth: true\
\x0d\x0a        enable\
d: true\x0d\x0a      }\
\x0d\x0a    }\x0d\x0a    Row\
Layout {\x0d\x0a      \
property var mat\
erialColors: [\x0d\x0a\
        'Red', '\
Pink', 'Purple',\
 'DeepPurple', '\
Indigo', 'Blue',\
\x0d\x0a        'Light\
Blue', 'Cyan', '\
Teal', 'Green', \
'LightGreen', 'L\
ime',\x0d\x0a        '\
Yellow', 'Amber'\
, 'Orange', 'Dee\
pOrange', 'Brown\
', 'Grey',\x0d\x0a    \
    'BlueGrey'\x0d\x0a\
      ]\x0d\x0a      L\
ayout.margins: 1\
0\x0d\x0a      Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a\x0d\x0a  \
    Label { text\
: 'Primary' }\x0d\x0a \
     ComboBox {\x0d\
\x0a        id: pri\
maryColor\x0d\x0a     \
   Layout.fillWi\
dth: true\x0d\x0a     \
   enabled: true\
\x0d\x0a        model:\
 parent.material\
Colors\x0d\x0a        \
currentIndex: 6\x0d\
\x0a      }\x0d\x0a\x0d\x0a    \
  Label { text: \
'Accent' }\x0d\x0a    \
  ComboBox {\x0d\x0a  \
      id: accent\
Color\x0d\x0a        L\
ayout.fillWidth:\
 true\x0d\x0a        e\
nabled: true\x0d\x0a  \
      model: par\
ent.materialColo\
rs\x0d\x0a        curr\
entIndex: 7\x0d\x0a   \
   }\x0d\x0a    }\x0d\x0a  }\
\x0d\x0a}\
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
\x00\x11\
\x03S\x87\xdc\
\x00S\
\x00i\x00d\x00e\x00N\x00a\x00v\x00B\x00u\x00t\x00t\x00o\x00n\x00.\x00q\x00m\x00l\
\
\x00\x0b\
\x09\xf8\xd2<\
\x00C\
\x00e\x00l\x00l\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
\x00\x12\
\x08\xbdU\xfc\
\x00L\
\x00a\x00r\x00g\x00e\x00C\x00h\x00a\x00r\x00t\x00V\x00i\x00e\x00w\x00.\x00q\x00m\
\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x04\x00\x00\x00\x07\
\x00\x00\x00\x18\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x98\x00\x00\x00\x00\x00\x01\x00\x00\x01\xfa\
\x00\x00\x00\x5c\x00\x00\x00\x00\x00\x01\x00\x00\x00\xcb\
\x00\x00\x00\xd2\x00\x00\x00\x00\x00\x01\x00\x00\x02\xf3\
\x00\x00\x01@\x00\x00\x00\x00\x00\x01\x00\x00\x05\x01\
\x00\x00\x01\x16\x00\x00\x00\x00\x00\x01\x00\x00\x04\x0d\
\x00\x00\x00\xfa\x00\x00\x00\x00\x00\x01\x00\x00\x03_\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
