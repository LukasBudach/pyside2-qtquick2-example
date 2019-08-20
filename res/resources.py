# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Tue Aug 20 11:05:56 2019
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
\x00\x00\x17}\
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
1.0\x0d\x0a\x0d\x0aimport \x22c\
omponents\x22\x0d\x0aimpo\
rt \x22pages\x22\x0d\x0a\x0d\x0aAp\
plicationWindow \
{\x0d\x0a    id: mainW\
indow\x0d\x0a    title\
: \x22My amazing ne\
ural network app\
\x22\x0d\x0a    visible: \
true\x0d\x0a    minimu\
mHeight: 900\x0d\x0a  \
  minimumWidth: \
1600\x0d\x0a    Materi\
al.theme: Materi\
al[subTheme.curr\
entText]\x0d\x0a    Ma\
terial.accent: M\
aterial[accentCo\
lor.currentText]\
\x0d\x0a    Material.p\
rimary: Material\
[primaryColor.cu\
rrentText]\x0d\x0a\x0d\x0a  \
  signal console\
reemitted(string\
 log)\x0d\x0a\x0d\x0a    Com\
ponent.onComplet\
ed: {\x0d\x0a        c\
ontrol_bridge.lo\
g_event.connect(\
mainWindow.conso\
lereemitted)\x0d\x0a  \
  }\x0d\x0a\x0d\x0a    onCon\
solereemitted: {\
\x0d\x0a        consol\
eTextfield.appen\
d(log)\x0d\x0a    }\x0d\x0a\x0d\
\x0a\x0d\x0a    header: T\
oolBar {\x0d\x0a      \
  RowLayout {\x0d\x0a \
           ancho\
rs.fill: parent\x0d\
\x0a            Too\
lButton {\x0d\x0a     \
       icon.sour\
ce: \x22../images/b\
aseline-menu-24p\
x.svg\x22\x0d\x0a        \
    onClicked: s\
ideNav.open()\x0d\x0a \
           }\x0d\x0a  \
          Label \
{\x0d\x0a             \
   text: \x22Neural\
 network control\
 panel\x22\x0d\x0a       \
         elide: \
Label.ElideRight\
\x0d\x0a              \
  horizontalAlig\
nment: Qt.AlignH\
Center\x0d\x0a        \
        vertical\
Alignment: Qt.Al\
ignVCenter\x0d\x0a    \
            Layo\
ut.fillWidth: tr\
ue\x0d\x0a            \
}\x0d\x0a            T\
oolButton {\x0d\x0a   \
             tex\
t: \x22Start Traini\
ng\x22\x0d\x0a           \
     id: btn_sta\
rtTraining\x0d\x0a    \
            onCl\
icked: () => {\x0d\x0a\
                \
    btn_startTra\
ining.enabled = \
false\x0d\x0a         \
           contr\
ol_bridge.start_\
simulation()\x0d\x0a  \
              }\x0d\
\x0a            }\x0d\x0a\
            Tool\
Button { text: \x22\
Pause Training\x22 \
}\x0d\x0a            T\
oolSeparator {}\x0d\
\x0a            Too\
lButton {\x0d\x0a     \
           icon.\
source: \x22../imag\
es/baseline-more\
_vert-24px.svg\x22\x0d\
\x0a               \
 onClicked: menu\
.open()\x0d\x0a       \
         Menu {\x0d\
\x0a               \
     id: menu\x0d\x0a \
                \
   y: parent.hei\
ght\x0d\x0a           \
         MenuIte\
m { text: \x22New..\
.\x22 }\x0d\x0a          \
          MenuIt\
em { text: \x22Open\
...\x22 }\x0d\x0a        \
            Menu\
Item { text: \x22Sa\
ve\x22 }\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a       \
 }\x0d\x0a    }\x0d\x0a    D\
rawer {\x0d\x0a       \
 id: sideNav\x0d\x0a  \
      width: 200\
\x0d\x0a        height\
: parent.height\x0d\
\x0a        ColumnL\
ayout {\x0d\x0a       \
     width: pare\
nt.width\x0d\x0a      \
      Label {\x0d\x0a \
               t\
ext: \x22Drawer\x22\x0d\x0a \
               h\
orizontalAlignme\
nt: Text.AlignHC\
enter\x0d\x0a         \
       verticalA\
lignment: Text.A\
lignVCenter\x0d\x0a   \
             fon\
t.pixelSize: 20\x0d\
\x0a               \
 Layout.fillWidt\
h: true\x0d\x0a       \
     }\x0d\x0a        \
    Repeater {\x0d\x0a\
                \
model: 5\x0d\x0a      \
          SideNa\
vButton {\x0d\x0a     \
               i\
con.source: \x22../\
images/baseline-\
category-24px.sv\
g\x22\x0d\x0a            \
        text: \x22L\
ist \x22 + index\x0d\x0a \
                \
   Layout.fillWi\
dth: true\x0d\x0a     \
           }\x0d\x0a  \
          }\x0d\x0a   \
     }\x0d\x0a    }\x0d\x0a \
   Pane {\x0d\x0a     \
   id: body\x0d\x0a   \
     padding: 10\
\x0d\x0a        anchor\
s.fill: parent\x0d\x0a\
        ColumnLa\
yout {\x0d\x0a        \
    anchors.fill\
: parent\x0d\x0a      \
      NoteBook {\
\x0d\x0a              \
  Preprocess {}\x0d\
\x0a               \
 Train {}\x0d\x0a     \
           Predi\
ct {}\x0d\x0a         \
   }\x0d\x0a\x0d\x0a        \
    CellBox {\x0d\x0a \
               L\
ayout.preferredH\
eight: 100;\x0d\x0a   \
             tit\
le: \x22Console Out\
put\x22\x0d\x0a          \
      ScrollView\
 {\x0d\x0a            \
        anchors.\
fill: parent\x0d\x0a  \
                \
  TextArea {\x0d\x0a  \
                \
      anchors.fi\
ll: parent\x0d\x0a    \
                \
    id: consoleT\
extfield\x0d\x0a      \
                \
  placeholderTex\
t: \x22Console outp\
ut...\x22\x0d\x0a        \
                \
selectByMouse: t\
rue\x0d\x0a           \
             per\
sistentSelection\
: true\x0d\x0a        \
                \
readOnly: true\x0d\x0a\
                \
    }\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a       \
 }\x0d\x0a    }\x0d\x0a\x0d\x0a   \
 /**************\
****************\
****************\
************\x0d\x0a  \
  Footer\x0d\x0a    **\
****************\
****************\
****************\
********/\x0d\x0a    f\
ooter: RowLayout\
 {\x0d\x0a        widt\
h: parent.width\x0d\
\x0a        RowLayo\
ut {\x0d\x0a          \
  Layout.margins\
: 10\x0d\x0a          \
  Layout.alignme\
nt: Qt.AlignHCen\
ter\x0d\x0a           \
 Label { text: \x22\
Theme customizat\
ion: \x22 }\x0d\x0a      \
      Label {\x0d\x0a \
               i\
d: qtquick2Theme\
s\x0d\x0a             \
   objectName: \x22\
qtquick2Themes\x22\x0d\
\x0a               \
 Layout.fillWidt\
h: true\x0d\x0a       \
     }\x0d\x0a        \
}\x0d\x0a        RowLa\
yout {\x0d\x0a        \
    Layout.margi\
ns: 10\x0d\x0a        \
    Layout.align\
ment: Qt.AlignHC\
enter\x0d\x0a         \
   Label { text:\
 \x22QtQuick Charts\
 Themes: \x22 }\x0d\x0a  \
          ComboB\
ox {\x0d\x0a          \
      id: qtquic\
kChartsThemes\x0d\x0a \
               m\
odel: [\x0d\x0a       \
             \x22Ch\
artThemeLight\x22, \
\x22ChartThemeBlueC\
erulean\x22,\x0d\x0a     \
               \x22\
ChartThemeDark\x22,\
 \x22ChartThemeBrow\
nSand\x22,\x0d\x0a       \
             \x22Ch\
artThemeBlueNcs\x22\
, \x22ChartThemeHig\
hContrast\x22,\x0d\x0a   \
                \
 \x22ChartThemeBlue\
Icy\x22, \x22ChartThem\
eQt\x22\x0d\x0a          \
      ]\x0d\x0a       \
         Layout.\
fillWidth: true\x0d\
\x0a               \
 currentIndex: 2\
\x0d\x0a            }\x0d\
\x0a        }\x0d\x0a    \
    RowLayout {\x0d\
\x0a            Lay\
out.margins: 10\x0d\
\x0a            Lay\
out.alignment: Q\
t.AlignHCenter\x0d\x0a\
            Labe\
l { text: \x22Sub-T\
heme: \x22 }\x0d\x0a     \
       ComboBox \
{\x0d\x0a             \
   id: subTheme\x0d\
\x0a               \
 model: [\x22Dark\x22,\
 \x22Light\x22]\x0d\x0a     \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
   enabled: true\
\x0d\x0a            }\x0d\
\x0a        }\x0d\x0a    \
    RowLayout {\x0d\
\x0a            pro\
perty var materi\
alColors: [\x0d\x0a   \
             \x22Re\
d\x22, \x22Pink\x22, \x22Pur\
ple\x22, \x22DeepPurpl\
e\x22, \x22Indigo\x22, \x22B\
lue\x22,\x0d\x0a         \
       \x22LightBlu\
e\x22, \x22Cyan\x22, \x22Tea\
l\x22, \x22Green\x22, \x22Li\
ghtGreen\x22, \x22Lime\
\x22,\x0d\x0a            \
    \x22Yellow\x22, \x22A\
mber\x22, \x22Orange\x22,\
 \x22DeepOrange\x22, \x22\
Brown\x22, \x22Grey\x22,\x0d\
\x0a               \
 \x22BlueGrey\x22\x0d\x0a   \
         ]\x0d\x0a    \
        Layout.m\
argins: 10\x0d\x0a    \
        Layout.a\
lignment: Qt.Ali\
gnHCenter\x0d\x0a\x0d\x0a   \
         Label {\
 text: \x22Primary\x22\
 }\x0d\x0a            \
ComboBox {\x0d\x0a    \
            id: \
primaryColor\x0d\x0a  \
              La\
yout.fillWidth: \
true\x0d\x0a          \
      enabled: t\
rue\x0d\x0a           \
     model: pare\
nt.materialColor\
s\x0d\x0a             \
   currentIndex:\
 6\x0d\x0a            \
}\x0d\x0a\x0d\x0a           \
 Label { text: \x22\
Accent\x22 }\x0d\x0a     \
       ComboBox \
{\x0d\x0a             \
   id: accentCol\
or\x0d\x0a            \
    Layout.fillW\
idth: true\x0d\x0a    \
            enab\
led: true\x0d\x0a     \
           model\
: parent.materia\
lColors\x0d\x0a       \
         current\
Index: 7\x0d\x0a      \
      }\x0d\x0a       \
 }\x0d\x0a    }\x0d\x0a}\
\x00\x00\x003\
[\
Controls]\x0d\x0aStyle\
=Material\x0d\x0aFallb\
ackStyle=Default\
\x0d\x0a\
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
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
\x00\x0a\
\x07j\x093\
\x00c\
\x00o\x00m\x00p\x00o\x00n\x00e\x00n\x00t\x00s\
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
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x03\x00\x00\x00\x07\
\x00\x00\x00\x18\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x00*\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\x5c\x00\x00\x00\x00\x00\x01\x00\x00\x00\xcb\
\x00\x00\x00\x96\x00\x00\x00\x00\x00\x01\x00\x00\x01\xc4\
\x00\x00\x01\x18\x00\x02\x00\x00\x00\x03\x00\x00\x00\x0a\
\x00\x00\x00\xd2\x00\x00\x00\x00\x00\x01\x00\x00\x02\xf3\
\x00\x00\x00\xe8\x00\x00\x00\x00\x00\x01\x00\x00\x1at\
\x00\x00\x01\x5c\x00\x00\x00\x00\x00\x01\x00\x00\x1b\x9f\
\x00\x00\x012\x00\x00\x00\x00\x00\x01\x00\x00\x1a\xab\
\x00\x00\x01\x84\x00\x00\x00\x00\x00\x01\x00\x00\x1c\x0b\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
