# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Tue Aug 20 13:45:42 2019
#      by: The Resource Compiler for PySide2 (Qt v5.13.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x003\
[\
Controls]\x0d\x0aStyle\
=Material\x0d\x0aFallb\
ackStyle=Default\
\x0d\x0a\
\x00\x00\x17\x92\
i\
mport QtQuick 2.\
13\x0d\x0aimport QtQui\
ck.Layouts 1.11\x0d\
\x0aimport QtQuick.\
Controls 2.4\x0d\x0aim\
port QtQuick.Con\
trols.Material 2\
.4\x0d\x0aimport QtQui\
ck.Dialogs 1.0\x0d\x0a\
import QtQuick.C\
ontrols.Styles 1\
.4\x0d\x0a\x0d\x0aimport \x22co\
mponents\x22\x0d\x0aimpor\
t \x22pages\x22\x0d\x0a\x0d\x0aApp\
licationWindow {\
\x0d\x0a    id: mainWi\
ndow\x0d\x0a    title:\
 \x22My amazing neu\
ral network app\x22\
\x0d\x0a    visible: t\
rue\x0d\x0a    minimum\
Height: 900\x0d\x0a   \
 minimumWidth: 1\
600\x0d\x0a    Materia\
l.theme: Materia\
l[subTheme.curre\
ntText]\x0d\x0a    Mat\
erial.accent: Ma\
terial[accentCol\
or.currentText]\x0d\
\x0a    Material.pr\
imary: Material[\
primaryColor.cur\
rentText]\x0d\x0a\x0d\x0a   \
 signal consoler\
eemitted(string \
log)\x0d\x0a\x0d\x0a    Comp\
onent.onComplete\
d: {\x0d\x0a        co\
nsole_stream.eve\
nt_logged.connec\
t(mainWindow.con\
solereemitted)\x0d\x0a\
    }\x0d\x0a\x0d\x0a    onC\
onsolereemitted:\
 {\x0d\x0a        cons\
oleTextfield.app\
end(log)\x0d\x0a    }\x0d\
\x0a\x0d\x0a\x0d\x0a    header:\
 ToolBar {\x0d\x0a    \
    RowLayout {\x0d\
\x0a            anc\
hors.fill: paren\
t\x0d\x0a            T\
oolButton {\x0d\x0a   \
         icon.so\
urce: \x22../images\
/baseline-menu-2\
4px.svg\x22\x0d\x0a      \
      onClicked:\
 sideNav.open()\x0d\
\x0a            }\x0d\x0a\
            Labe\
l {\x0d\x0a           \
     text: \x22Neur\
al network contr\
ol panel\x22\x0d\x0a     \
           elide\
: Label.ElideRig\
ht\x0d\x0a            \
    horizontalAl\
ignment: Qt.Alig\
nHCenter\x0d\x0a      \
          vertic\
alAlignment: Qt.\
AlignVCenter\x0d\x0a  \
              La\
yout.fillWidth: \
true\x0d\x0a          \
  }\x0d\x0a           \
 ToolButton {\x0d\x0a \
               t\
ext: \x22Start Trai\
ning\x22\x0d\x0a         \
       id: btn_s\
tartTraining\x0d\x0a  \
              on\
Clicked: () => {\
\x0d\x0a              \
      btn_startT\
raining.enabled \
= false\x0d\x0a       \
             con\
trol_bridge.star\
t_simulation()\x0d\x0a\
                \
}\x0d\x0a            }\
\x0d\x0a            To\
olButton { text:\
 \x22Pause Training\
\x22 }\x0d\x0a           \
 ToolSeparator {\
}\x0d\x0a            T\
oolButton {\x0d\x0a   \
             ico\
n.source: \x22../im\
ages/baseline-mo\
re_vert-24px.svg\
\x22\x0d\x0a             \
   onClicked: me\
nu.open()\x0d\x0a     \
           Menu \
{\x0d\x0a             \
       id: menu\x0d\
\x0a               \
     y: parent.h\
eight\x0d\x0a         \
           MenuI\
tem { text: \x22New\
...\x22 }\x0d\x0a        \
            Menu\
Item { text: \x22Op\
en...\x22 }\x0d\x0a      \
              Me\
nuItem { text: \x22\
Save\x22 }\x0d\x0a       \
         }\x0d\x0a    \
        }\x0d\x0a     \
   }\x0d\x0a    }\x0d\x0a   \
 Drawer {\x0d\x0a     \
   id: sideNav\x0d\x0a\
        width: 2\
00\x0d\x0a        heig\
ht: parent.heigh\
t\x0d\x0a        Colum\
nLayout {\x0d\x0a     \
       width: pa\
rent.width\x0d\x0a    \
        Label {\x0d\
\x0a               \
 text: \x22Drawer\x22\x0d\
\x0a               \
 horizontalAlign\
ment: Text.Align\
HCenter\x0d\x0a       \
         vertica\
lAlignment: Text\
.AlignVCenter\x0d\x0a \
               f\
ont.pixelSize: 2\
0\x0d\x0a             \
   Layout.fillWi\
dth: true\x0d\x0a     \
       }\x0d\x0a      \
      Repeater {\
\x0d\x0a              \
  model: 5\x0d\x0a    \
            Side\
NavButton {\x0d\x0a   \
                \
 icon.source: \x22.\
./images/baselin\
e-category-24px.\
svg\x22\x0d\x0a          \
          text: \
\x22List \x22 + index\x0d\
\x0a               \
     Layout.fill\
Width: true\x0d\x0a   \
             }\x0d\x0a\
            }\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a    Pane {\x0d\x0a   \
     id: body\x0d\x0a \
       padding: \
10\x0d\x0a        anch\
ors.fill: parent\
\x0d\x0a        Column\
Layout {\x0d\x0a      \
      anchors.fi\
ll: parent\x0d\x0a    \
        NoteBook\
 {\x0d\x0a            \
    Preprocess {\
}\x0d\x0a             \
   Train {}\x0d\x0a   \
             Pre\
dict {}\x0d\x0a       \
     }\x0d\x0a\x0d\x0a      \
      CellBox {\x0d\
\x0a               \
 Layout.preferre\
dHeight: 100;\x0d\x0a \
               t\
itle: \x22Console O\
utput\x22\x0d\x0a        \
        ScrollVi\
ew {\x0d\x0a          \
          anchor\
s.fill: parent\x0d\x0a\
                \
    TextArea {\x0d\x0a\
                \
        id: cons\
oleTextfield\x0d\x0a  \
                \
      placeholde\
rText: \x22Console \
output...\x22\x0d\x0a    \
                \
    selectByMous\
e: true\x0d\x0a       \
                \
 persistentSelec\
tion: true\x0d\x0a    \
                \
    readOnly: tr\
ue\x0d\x0a            \
            wrap\
Mode: Text.WordW\
rap\x0d\x0a           \
         }\x0d\x0a    \
            }\x0d\x0a \
           }\x0d\x0a  \
      }\x0d\x0a    }\x0d\x0a\
\x0d\x0a    /*********\
****************\
****************\
****************\
*\x0d\x0a    Footer\x0d\x0a \
   *************\
****************\
****************\
*************/\x0d\x0a\
    footer: RowL\
ayout {\x0d\x0a       \
 width: parent.w\
idth\x0d\x0a        Ro\
wLayout {\x0d\x0a     \
       Layout.ma\
rgins: 10\x0d\x0a     \
       Layout.al\
ignment: Qt.Alig\
nHCenter\x0d\x0a      \
      Label { te\
xt: \x22Theme custo\
mization: \x22 }\x0d\x0a \
           Label\
 {\x0d\x0a            \
    id: qtquick2\
Themes\x0d\x0a        \
        objectNa\
me: \x22qtquick2The\
mes\x22\x0d\x0a          \
      Layout.fil\
lWidth: true\x0d\x0a  \
          }\x0d\x0a   \
     }\x0d\x0a        \
RowLayout {\x0d\x0a   \
         Layout.\
margins: 10\x0d\x0a   \
         Layout.\
alignment: Qt.Al\
ignHCenter\x0d\x0a    \
        Label { \
text: \x22QtQuick C\
harts Themes: \x22 \
}\x0d\x0a            C\
omboBox {\x0d\x0a     \
           id: q\
tquickChartsThem\
es\x0d\x0a            \
    model: [\x0d\x0a  \
                \
  \x22ChartThemeLig\
ht\x22, \x22ChartTheme\
BlueCerulean\x22,\x0d\x0a\
                \
    \x22ChartThemeD\
ark\x22, \x22ChartThem\
eBrownSand\x22,\x0d\x0a  \
                \
  \x22ChartThemeBlu\
eNcs\x22, \x22ChartThe\
meHighContrast\x22,\
\x0d\x0a              \
      \x22ChartThem\
eBlueIcy\x22, \x22Char\
tThemeQt\x22\x0d\x0a     \
           ]\x0d\x0a  \
              La\
yout.fillWidth: \
true\x0d\x0a          \
      currentInd\
ex: 2\x0d\x0a         \
   }\x0d\x0a        }\x0d\
\x0a        RowLayo\
ut {\x0d\x0a          \
  Layout.margins\
: 10\x0d\x0a          \
  Layout.alignme\
nt: Qt.AlignHCen\
ter\x0d\x0a           \
 Label { text: \x22\
Sub-Theme: \x22 }\x0d\x0a\
            Comb\
oBox {\x0d\x0a        \
        id: subT\
heme\x0d\x0a          \
      model: [\x22D\
ark\x22, \x22Light\x22]\x0d\x0a\
                \
Layout.fillWidth\
: true\x0d\x0a        \
        enabled:\
 true\x0d\x0a         \
   }\x0d\x0a        }\x0d\
\x0a        RowLayo\
ut {\x0d\x0a          \
  property var m\
aterialColors: [\
\x0d\x0a              \
  \x22Red\x22, \x22Pink\x22,\
 \x22Purple\x22, \x22Deep\
Purple\x22, \x22Indigo\
\x22, \x22Blue\x22,\x0d\x0a    \
            \x22Lig\
htBlue\x22, \x22Cyan\x22,\
 \x22Teal\x22, \x22Green\x22\
, \x22LightGreen\x22, \
\x22Lime\x22,\x0d\x0a       \
         \x22Yellow\
\x22, \x22Amber\x22, \x22Ora\
nge\x22, \x22DeepOrang\
e\x22, \x22Brown\x22, \x22Gr\
ey\x22,\x0d\x0a          \
      \x22BlueGrey\x22\
\x0d\x0a            ]\x0d\
\x0a            Lay\
out.margins: 10\x0d\
\x0a            Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
\x0d\x0a            La\
bel { text: \x22Pri\
mary\x22 }\x0d\x0a       \
     ComboBox {\x0d\
\x0a               \
 id: primaryColo\
r\x0d\x0a             \
   Layout.fillWi\
dth: true\x0d\x0a     \
           enabl\
ed: true\x0d\x0a      \
          model:\
 parent.material\
Colors\x0d\x0a        \
        currentI\
ndex: 6\x0d\x0a       \
     }\x0d\x0a\x0d\x0a      \
      Label { te\
xt: \x22Accent\x22 }\x0d\x0a\
            Comb\
oBox {\x0d\x0a        \
        id: acce\
ntColor\x0d\x0a       \
         Layout.\
fillWidth: true\x0d\
\x0a               \
 enabled: true\x0d\x0a\
                \
model: parent.ma\
terialColors\x0d\x0a  \
              cu\
rrentIndex: 7\x0d\x0a \
           }\x0d\x0a  \
      }\x0d\x0a    }\x0d\x0a\
}\
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
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x0a\
\x07j\x093\
\x00c\
\x00o\x00m\x00p\x00o\x00n\x00e\x00n\x00t\x00s\
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
\x00\x0b\
\x09\xf8\xd2<\
\x00C\
\x00e\x00l\x00l\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
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
\x00\x1b\
\x0d\xe1;G\
\x00b\
\x00a\x00s\x00e\x00l\x00i\x00n\x00e\x00-\x00m\x00o\x00r\x00e\x00_\x00v\x00e\x00r\
\x00t\x00-\x002\x004\x00p\x00x\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x1e\x00\x02\x00\x00\x00\x03\x00\x00\x00\x07\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x00\xf8\x00\x00\x00\x00\x00\x01\x00\x00\x19\xdb\
\x00\x00\x01*\x00\x00\x00\x00\x00\x01\x00\x00\x1a\xa6\
\x00\x00\x01d\x00\x00\x00\x00\x00\x01\x00\x00\x1b\x9f\
\x00\x00\x00p\x00\x02\x00\x00\x00\x03\x00\x00\x00\x0a\
\x00\x00\x00Z\x00\x00\x00\x00\x00\x01\x00\x00\x007\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x8a\x00\x00\x00\x00\x00\x01\x00\x00\x17\xcd\
\x00\x00\x00\xb2\x00\x00\x00\x00\x00\x01\x00\x00\x189\
\x00\x00\x00\xdc\x00\x00\x00\x00\x00\x01\x00\x00\x19-\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
