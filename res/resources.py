# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Mi Aug 14 13:40:16 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x008\xc5\
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
Text]\x0d\x0a\x0d\x0a  heade\
r: ToolBar {\x0d\x0a  \
  RowLayout {\x0d\x0a \
     anchors.fil\
l: parent\x0d\x0a     \
 ToolButton {\x0d\x0a \
       icon.sour\
ce: '../images/b\
aseline-menu-24p\
x.svg'\x0d\x0a        \
onClicked: sideN\
av.open()\x0d\x0a     \
 }\x0d\x0a      Label \
{\x0d\x0a        text:\
 'Neural network\
 control panel'\x0d\
\x0a        elide: \
Label.ElideRight\
\x0d\x0a        horizo\
ntalAlignment: Q\
t.AlignHCenter\x0d\x0a\
        vertical\
Alignment: Qt.Al\
ignVCenter\x0d\x0a    \
    Layout.fillW\
idth: true\x0d\x0a    \
  }\x0d\x0a      ToolB\
utton {\x0d\x0a       \
 text: 'Start Tr\
aining'\x0d\x0a       \
 id: btn_startTr\
aining\x0d\x0a        \
onClicked: () =>\
 {\x0d\x0a            \
control_bridge.s\
tart_simulation(\
)\x0d\x0a            b\
tn_startTraining\
.enabled = false\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a      Tool\
Button { text: '\
Pause Training' \
}\x0d\x0a      ToolSep\
arator {}\x0d\x0a     \
 ToolButton {\x0d\x0a \
       icon.sour\
ce: '../images/b\
aseline-more_ver\
t-24px.svg'\x0d\x0a   \
     onClicked: \
menu.open()\x0d\x0a   \
     Menu {\x0d\x0a   \
       id: menu\x0d\
\x0a          y: pa\
rent.height\x0d\x0a   \
       MenuItem \
{ text: 'New...'\
 }\x0d\x0a          Me\
nuItem { text: '\
Open...' }\x0d\x0a    \
      MenuItem {\
 text: 'Save' }\x0d\
\x0a        }\x0d\x0a    \
  }\x0d\x0a    }\x0d\x0a  }\x0d\
\x0a  Drawer {\x0d\x0a   \
 id: sideNav\x0d\x0a  \
  width: 200\x0d\x0a  \
  height: parent\
.height\x0d\x0a    Col\
umnLayout {\x0d\x0a   \
   width: parent\
.width\x0d\x0a      La\
bel {\x0d\x0a         \
 text: 'Drawer'\x0d\
\x0a          horiz\
ontalAlignment: \
Text.AlignHCente\
r\x0d\x0a          ver\
ticalAlignment: \
Text.AlignVCente\
r\x0d\x0a          fon\
t.pixelSize: 20\x0d\
\x0a          Layou\
t.fillWidth: tru\
e\x0d\x0a      }\x0d\x0a    \
  Repeater {\x0d\x0a  \
      model: 5\x0d\x0a\
        SideNavB\
utton {\x0d\x0a       \
   icon.source: \
'../images/basel\
ine-category-24p\
x.svg'\x0d\x0a        \
  text: 'List ' \
+ index\x0d\x0a       \
   Layout.fillWi\
dth: true\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a \
   }\x0d\x0a  }\x0d\x0a  Pan\
e {\x0d\x0a    padding\
: 10\x0d\x0a    anchor\
s.fill: parent\x0d\x0a\
    GridLayout {\
\x0d\x0a      anchors.\
fill: parent\x0d\x0a  \
    flow: GridLa\
yout.TopToBottom\
\x0d\x0a      rows: 3\x0d\
\x0a\x0d\x0a      CellBox\
 {\x0d\x0a        titl\
e: 'Datasets'\x0d\x0a \
       GridLayou\
t {\x0d\x0a           \
 anchors.fill: p\
arent\x0d\x0a         \
   columns: 3\x0d\x0a \
           Label\
 {\x0d\x0a            \
    text: 'Train\
 Dataset'\x0d\x0a     \
           Layou\
t.alignment: Qt.\
AlignHCenter\x0d\x0a  \
          }\x0d\x0a   \
         TextFie\
ld {\x0d\x0a          \
      width: par\
ent.width\x0d\x0a     \
           place\
holderText: 'Tra\
in Data goes her\
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
  }\x0d\x0a\x0d\x0a         \
   Label {\x0d\x0a    \
            text\
: 'Test Dataset'\
\x0d\x0a              \
  Layout.alignme\
nt: Qt.AlignHCen\
ter\x0d\x0a           \
 }\x0d\x0a            \
TextField {\x0d\x0a   \
             wid\
th: parent.width\
\x0d\x0a              \
  placeholderTex\
t: 'Test Data go\
es here...'\x0d\x0a   \
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
        }\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a\x0d\
\x0a      CellBox {\
\x0d\x0a        title:\
 'Network Settin\
gs'\x0d\x0a        Gri\
dLayout {\x0d\x0a     \
       anchors.f\
ill: parent\x0d\x0a   \
         columns\
: 2\x0d\x0a           \
 Label {\x0d\x0a      \
          text: \
'Total Training \
Epochs'\x0d\x0a       \
         Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a    \
        }\x0d\x0a     \
       SpinBox {\
\x0d\x0a              \
  id: totalEpoch\
s\x0d\x0a             \
   editable: tru\
e\x0d\x0a             \
   value: settin\
gs_bridge.epochs\
\x0d\x0a              \
  from: 1\x0d\x0a     \
           to: 9\
99999\x0d\x0a         \
       Layout.fi\
llWidth: true\x0d\x0a \
               o\
nValueChanged: s\
ettings_bridge.e\
pochs = value\x0d\x0a \
               C\
omponent.onCompl\
eted: settings_b\
ridge.epochs = v\
alue\x0d\x0a          \
  }\x0d\x0a\x0d\x0a         \
   Label {\x0d\x0a    \
            text\
: 'Batch Size'\x0d\x0a\
                \
Layout.alignment\
: Qt.AlignHCente\
r\x0d\x0a            }\
\x0d\x0a            Sp\
inBox {\x0d\x0a       \
         editabl\
e: true\x0d\x0a       \
         value: \
32\x0d\x0a            \
    from: 2\x0d\x0a   \
             to:\
 2048\x0d\x0a         \
       Layout.fi\
llWidth: true\x0d\x0a \
           }\x0d\x0a\x0d\x0a\
            Labe\
l {\x0d\x0a           \
     text: 'Neig\
hborhood Size'\x0d\x0a\
                \
Layout.alignment\
: Qt.AlignHCente\
r\x0d\x0a            }\
\x0d\x0a            Sp\
inBox {\x0d\x0a       \
         editabl\
e: true\x0d\x0a       \
         value: \
2048\x0d\x0a          \
      from: 512\x0d\
\x0a               \
 to: 8192\x0d\x0a     \
           Layou\
t.fillWidth: tru\
e\x0d\x0a            }\
\x0d\x0a\x0d\x0a            \
Label {\x0d\x0a       \
         text: '\
Optimization Met\
ric'\x0d\x0a          \
      Layout.ali\
gnment: Qt.Align\
HCenter\x0d\x0a       \
     }\x0d\x0a        \
    SpinBox {\x0d\x0a \
               v\
alue: 100\x0d\x0a     \
           Layou\
t.fillWidth: tru\
e\x0d\x0a            }\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a\x0d\x0a      Ce\
llBox {\x0d\x0a       \
 Layout.columnSp\
an: 2; Layout.pr\
eferredHeight: 1\
00;\x0d\x0a        tit\
le: 'Console Out\
put'\x0d\x0a        Co\
lumn {\x0d\x0a        \
  // ScrollView \
will not work if\
 we use ColumnLa\
yout as\x0d\x0a       \
   // ColumnLayo\
ut always measur\
es its size depe\
nding on its\x0d\x0a  \
        // conte\
nts.\x0d\x0a          \
anchors.fill: pa\
rent\x0d\x0a          \
spacing: 10\x0d\x0a   \
       ScrollVie\
w {\x0d\x0a           \
 width: parent.w\
idth\x0d\x0a          \
  height: 150\x0d\x0a \
           TextA\
rea {\x0d\x0a         \
     text: 'Mult\
i-line text edit\
or...\x5cnThis is a\
 new line.'\x0d\x0a   \
           selec\
tByMouse: true\x0d\x0a\
              pe\
rsistentSelectio\
n: true\x0d\x0a       \
       readOnly:\
 true\x0d\x0a         \
   }\x0d\x0a          \
}\x0d\x0a        }\x0d\x0a  \
    }\x0d\x0a\x0d\x0a      C\
ellBox {\x0d\x0a      \
    Layout.rowSp\
an: 2\x0d\x0a         \
 title: 'Current\
 Info'\x0d\x0a        \
  ColumnLayout {\
\x0d\x0a              \
anchors.fill: pa\
rent\x0d\x0a\x0d\x0a        \
      GridLayout\
 {\x0d\x0a            \
    Layout.align\
ment: Qt.AlignTo\
p\x0d\x0a             \
   columns: 2\x0d\x0a\x0d\
\x0a               \
 Label {\x0d\x0a      \
              La\
yout.fillWidth: \
true\x0d\x0a          \
          horizo\
ntalAlignment: T\
ext.AlignLeft\x0d\x0a \
                \
   text: 'Curren\
t Epoch'\x0d\x0a      \
          }\x0d\x0a   \
             Lab\
el {\x0d\x0a          \
          text: \
epoch_bridge.epo\
ch\x0d\x0a            \
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
         text: e\
poch_bridge.trai\
n_acc\x0d\x0a         \
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
xt: epoch_bridge\
.progress\x0d\x0a     \
                \
 horizontalAlign\
ment: Text.Align\
Right\x0d\x0a         \
             Lay\
out.fillWidth: t\
rue\x0d\x0a           \
           id: p\
rogressLabel\x0d\x0a  \
                \
}\x0d\x0a             \
     ProgressBar\
 {\x0d\x0a            \
          Layout\
.fillWidth: true\
\x0d\x0a              \
        Layout.c\
olumnSpan: 2\x0d\x0a  \
                \
    value: epoch\
_bridge.progress\
 / 100;\x0d\x0a       \
           }\x0d\x0a  \
            }\x0d\x0a \
         }\x0d\x0a    \
  }\x0d\x0a\x0d\x0a      /**\
****************\
****************\
****************\
********\x0d\x0a      \
Graphs\x0d\x0a      **\
****************\
****************\
****************\
********/\x0d\x0a     \
 CellBox {\x0d\x0a    \
    Layout.rowSp\
an: 3; Layout.mi\
nimumWidth: 700\x0d\
\x0a        Layout.\
preferredWidth: \
height // Keep t\
he ratio right!\x0d\
\x0a        TabBar \
{\x0d\x0a          id:\
 bar\x0d\x0a          \
width: parent.wi\
dth\x0d\x0a          T\
abButton { text:\
 'Test Loss' }\x0d\x0a\
          TabBut\
ton { text: 'Acc\
uracies' }\x0d\x0a    \
    }\x0d\x0a        S\
tackLayout {\x0d\x0a  \
        width: p\
arent.width\x0d\x0a   \
       height: p\
arent.height - y\
\x0d\x0a          anch\
ors.top: bar.bot\
tom\x0d\x0a          c\
urrentIndex: bar\
.currentIndex\x0d\x0a \
         LargeCh\
artView {\x0d\x0a     \
       ValueAxis\
 {\x0d\x0a            \
  id: valueAxisL\
ossSeries\x0d\x0a     \
         min: 0\x0d\
\x0a              m\
ax: 5\x0d\x0a         \
     tickCount: \
6\x0d\x0a             \
 labelFormat: '%\
.0f'\x0d\x0a          \
  }\x0d\x0a\x0d\x0a         \
   SplineSeries \
{\x0d\x0a             \
 name: 'Test Los\
s'\x0d\x0a            \
  axisX: valueAx\
isLossSeries\x0d\x0a  \
            XYPo\
int { x: 0; y: 0\
 }\x0d\x0a            \
  XYPoint { x: 1\
; y: 2.67 }\x0d\x0a   \
           XYPoi\
nt { x: 2; y: 1.\
34 }\x0d\x0a          \
    XYPoint { x:\
 3; y: 0.51 }\x0d\x0a \
             XYP\
oint { x: 4; y: \
0.21 }\x0d\x0a        \
      XYPoint { \
x: 5; y: 0.05 }\x0d\
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
}\x0d\x0a    }\x0d\x0a  }\x0d\x0a\x0d\
\x0a  /************\
****************\
****************\
**************\x0d\x0a\
  Footer\x0d\x0a  ****\
****************\
****************\
****************\
******/\x0d\x0a  foote\
r: RowLayout {\x0d\x0a\
    width: paren\
t.width\x0d\x0a    Row\
Layout {\x0d\x0a      \
Layout.margins: \
10\x0d\x0a      Layout\
.alignment: Qt.A\
lignHCenter\x0d\x0a   \
   Label { text:\
 'Theme customiz\
ation: ' }\x0d\x0a    \
  Label {\x0d\x0a     \
   id: qtquick2T\
hemes\x0d\x0a        o\
bjectName: 'qtqu\
ick2Themes'\x0d\x0a   \
     Layout.fill\
Width: true\x0d\x0a   \
   }\x0d\x0a    }\x0d\x0a   \
 RowLayout {\x0d\x0a  \
    Layout.margi\
ns: 10\x0d\x0a      La\
yout.alignment: \
Qt.AlignHCenter\x0d\
\x0a      Label { t\
ext: 'QtQuick Ch\
arts Themes: ' }\
\x0d\x0a      ComboBox\
 {\x0d\x0a        id: \
qtquickChartsThe\
mes\x0d\x0a        mod\
el: [\x0d\x0a         \
 'ChartThemeLigh\
t', 'ChartThemeB\
lueCerulean',\x0d\x0a \
         'ChartT\
hemeDark', 'Char\
tThemeBrownSand'\
,\x0d\x0a          'Ch\
artThemeBlueNcs'\
, 'ChartThemeHig\
hContrast',\x0d\x0a   \
       'ChartThe\
meBlueIcy', 'Cha\
rtThemeQt'\x0d\x0a    \
    ]\x0d\x0a        L\
ayout.fillWidth:\
 true\x0d\x0a        c\
urrentIndex: 2\x0d\x0a\
      }\x0d\x0a    }\x0d\x0a\
    RowLayout {\x0d\
\x0a      Layout.ma\
rgins: 10\x0d\x0a     \
 Layout.alignmen\
t: Qt.AlignHCent\
er\x0d\x0a      Label \
{ text: 'Sub-The\
me: ' }\x0d\x0a      C\
omboBox {\x0d\x0a     \
   id: subTheme\x0d\
\x0a        model: \
['Dark', 'Light'\
]\x0d\x0a        Layou\
t.fillWidth: tru\
e\x0d\x0a        enabl\
ed: true\x0d\x0a      \
}\x0d\x0a    }\x0d\x0a    Ro\
wLayout {\x0d\x0a     \
 property var ma\
terialColors: [\x0d\
\x0a        'Red', \
'Pink', 'Purple'\
, 'DeepPurple', \
'Indigo', 'Blue'\
,\x0d\x0a        'Ligh\
tBlue', 'Cyan', \
'Teal', 'Green',\
 'LightGreen', '\
Lime',\x0d\x0a        \
'Yellow', 'Amber\
', 'Orange', 'De\
epOrange', 'Brow\
n', 'Grey',\x0d\x0a   \
     'BlueGrey'\x0d\
\x0a      ]\x0d\x0a      \
Layout.margins: \
10\x0d\x0a      Layout\
.alignment: Qt.A\
lignHCenter\x0d\x0a\x0d\x0a \
     Label { tex\
t: 'Primary' }\x0d\x0a\
      ComboBox {\
\x0d\x0a        id: pr\
imaryColor\x0d\x0a    \
    Layout.fillW\
idth: true\x0d\x0a    \
    enabled: tru\
e\x0d\x0a        model\
: parent.materia\
lColors\x0d\x0a       \
 currentIndex: 6\
\x0d\x0a      }\x0d\x0a\x0d\x0a   \
   Label { text:\
 'Accent' }\x0d\x0a   \
   ComboBox {\x0d\x0a \
       id: accen\
tColor\x0d\x0a        \
Layout.fillWidth\
: true\x0d\x0a        \
enabled: true\x0d\x0a \
       model: pa\
rent.materialCol\
ors\x0d\x0a        cur\
rentIndex: 7\x0d\x0a  \
    }\x0d\x0a    }\x0d\x0a  \
}\x0d\x0a}\
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
\x00\x16\
\x03d\xbe\x87\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00m\x00e\x00n\x00u\x00-\x002\x004\x00p\
\x00x\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x1e\x00\x02\x00\x00\x00\x04\x00\x00\x00\x07\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x01$\x00\x00\x00\x00\x00\x01\x00\x00<\xff\
\x00\x00\x00\xea\x00\x00\x00\x00\x00\x01\x00\x00<\x06\
\x00\x00\x00\xae\x00\x00\x00\x00\x00\x01\x00\x00:\xd7\
\x00\x00\x00@\x00\x00\x00\x00\x00\x01\x00\x008\xc9\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x84\x00\x00\x00\x00\x00\x01\x00\x009\xe3\
\x00\x00\x00h\x00\x00\x00\x00\x00\x01\x00\x0095\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
