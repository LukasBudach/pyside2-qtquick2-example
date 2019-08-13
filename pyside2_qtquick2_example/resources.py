# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Di Aug 13 14:30:59 2019
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
\x00\x00L!\
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
  visible: true\x0d\
\x0a  minimumHeight\
: 700\x0d\x0a  minimum\
Width: 1600\x0d\x0a  M\
aterial.theme: M\
aterial[subTheme\
.currentText]\x0d\x0a \
 Material.accent\
: Material[accen\
tColor.currentTe\
xt]\x0d\x0a  Material.\
primary: Materia\
l[primaryColor.c\
urrentText]\x0d\x0a  m\
enuBar: MenuBar \
{\x0d\x0a    Menu {\x0d\x0a \
     title: '&Fi\
le'\x0d\x0a      Actio\
n { text: '&New.\
..' }\x0d\x0a      Act\
ion { text: '&Op\
en...' }\x0d\x0a      \
Action { text: '\
&Save' }\x0d\x0a      \
Action { text: '\
Save &As...' }\x0d\x0a\
      MenuSepara\
tor {}\x0d\x0a      Ac\
tion { text: '&Q\
uit' }\x0d\x0a    }\x0d\x0a \
   Menu {\x0d\x0a     \
 title: '&Edit'\x0d\
\x0a      Action { \
text: 'Cu&t' }\x0d\x0a\
      Action { t\
ext: '&Copy' }\x0d\x0a\
      Action { t\
ext: '&Paste' }\x0d\
\x0a    }\x0d\x0a    Menu\
 {\x0d\x0a      title:\
 '&Help'\x0d\x0a      \
Action { text: '\
&About' }\x0d\x0a    }\
\x0d\x0a  }\x0d\x0a  header:\
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
PyQt5 QtQuick2 E\
xample'\x0d\x0a       \
 elide: Label.El\
ideRight\x0d\x0a      \
  horizontalAlig\
nment: Qt.AlignH\
Center\x0d\x0a        \
verticalAlignmen\
t: Qt.AlignVCent\
er\x0d\x0a        Layo\
ut.fillWidth: tr\
ue\x0d\x0a      }\x0d\x0a   \
   ToolButton { \
text: 'Action 1'\
 }\x0d\x0a      ToolBu\
tton { text: 'Ac\
tion 2' }\x0d\x0a     \
 ToolSeparator {\
}\x0d\x0a      ToolBut\
ton { text: 'Act\
ion 3' }\x0d\x0a      \
ToolButton { tex\
t: 'Action 4' }\x0d\
\x0a      ToolButto\
n {\x0d\x0a        ico\
n.source: '../im\
ages/baseline-mo\
re_vert-24px.svg\
'\x0d\x0a        onCli\
cked: menu.open(\
)\x0d\x0a        Menu \
{\x0d\x0a          id:\
 menu\x0d\x0a         \
 y: parent.heigh\
t\x0d\x0a          Men\
uItem { text: 'N\
ew...' }\x0d\x0a      \
    MenuItem { t\
ext: 'Open...' }\
\x0d\x0a          Menu\
Item { text: 'Sa\
ve' }\x0d\x0a        }\
\x0d\x0a      }\x0d\x0a    }\
\x0d\x0a  }\x0d\x0a  Drawer \
{\x0d\x0a    id: sideN\
av\x0d\x0a    width: 2\
00\x0d\x0a    height: \
parent.height\x0d\x0a \
   ColumnLayout \
{\x0d\x0a      width: \
parent.width\x0d\x0a  \
    Label {\x0d\x0a   \
       text: 'Dr\
awer'\x0d\x0a         \
 horizontalAlign\
ment: Text.Align\
HCenter\x0d\x0a       \
   verticalAlign\
ment: Text.Align\
VCenter\x0d\x0a       \
   font.pixelSiz\
e: 20\x0d\x0a         \
 Layout.fillWidt\
h: true\x0d\x0a      }\
\x0d\x0a      Repeater\
 {\x0d\x0a        mode\
l: 5\x0d\x0a        Si\
deNavButton {\x0d\x0a \
         icon.so\
urce: '../images\
/baseline-catego\
ry-24px.svg'\x0d\x0a  \
        text: 'L\
ist ' + index\x0d\x0a \
         Layout.\
fillWidth: true\x0d\
\x0a        }\x0d\x0a    \
  }\x0d\x0a    }\x0d\x0a  }\x0d\
\x0a  Pane {\x0d\x0a    p\
adding: 10\x0d\x0a    \
anchors.fill: pa\
rent\x0d\x0a    GridLa\
yout {\x0d\x0a      an\
chors.fill: pare\
nt\x0d\x0a      flow: \
GridLayout.TopTo\
Bottom\x0d\x0a      ro\
ws: 2\x0d\x0a      Cel\
lBox {\x0d\x0a        \
title: 'Buttons'\
\x0d\x0a        Column\
Layout {\x0d\x0a      \
    anchors.fill\
: parent\x0d\x0a      \
    Button {\x0d\x0a  \
          text: \
'Button'\x0d\x0a      \
      Layout.fil\
lWidth: true\x0d\x0a  \
          onClic\
ked: normalPopup\
.open()\x0d\x0a       \
   }\x0d\x0a          \
Button {\x0d\x0a      \
      text: 'Fla\
t'\x0d\x0a            \
Layout.fillWidth\
: true\x0d\x0a        \
    flat: true\x0d\x0a\
            onCl\
icked: modalPopu\
p.open()\x0d\x0a      \
    }\x0d\x0a         \
 Button {\x0d\x0a     \
       text: 'Hi\
ghlighted'\x0d\x0a    \
        Layout.f\
illWidth: true\x0d\x0a\
            high\
lighted: true\x0d\x0a \
           onCli\
cked: dialog.ope\
n()\x0d\x0a          }\
\x0d\x0a          Roun\
dButton {\x0d\x0a     \
       text: '+'\
\x0d\x0a            La\
yout.alignment: \
Qt.AlignHCenter\x0d\
\x0a          }\x0d\x0a  \
      }\x0d\x0a      }\
\x0d\x0a      CellBox \
{\x0d\x0a        title\
: 'Radio Buttons\
'\x0d\x0a        Colum\
nLayout {\x0d\x0a     \
     anchors.fil\
l: parent\x0d\x0a     \
     RadioButton\
 { text: 'Radio \
Button 1'; check\
ed: true }\x0d\x0a    \
      RadioButto\
n { text: 'Radio\
 Button 2' }\x0d\x0a  \
        RadioBut\
ton { text: 'Rad\
io Button 3' }\x0d\x0a\
          RadioB\
utton { text: 'R\
adio Button 4' }\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a      Cell\
Box {\x0d\x0a        t\
itle: 'Check Box\
es'\x0d\x0a        Col\
umnLayout {\x0d\x0a   \
       anchors.f\
ill: parent\x0d\x0a   \
       Switch { \
Layout.alignment\
: Qt.AlignHCente\
r }\x0d\x0a          B\
uttonGroup {\x0d\x0a  \
          id: ch\
ildGroup\x0d\x0a      \
      exclusive:\
 false\x0d\x0a        \
    checkState: \
parentBox.checkS\
tate\x0d\x0a          \
}\x0d\x0a          Che\
ckBox {\x0d\x0a       \
     id: parentB\
ox\x0d\x0a            \
text: 'Parent'\x0d\x0a\
            chec\
kState: childGro\
up.checkState\x0d\x0a \
         }\x0d\x0a    \
      CheckBox {\
\x0d\x0a            ch\
ecked: true\x0d\x0a   \
         text: '\
Child 1'\x0d\x0a      \
      leftPaddin\
g: indicator.wid\
th\x0d\x0a            \
ButtonGroup.grou\
p: childGroup\x0d\x0a \
         }\x0d\x0a    \
      CheckBox {\
\x0d\x0a            te\
xt: 'Child 2'\x0d\x0a \
           leftP\
adding: indicato\
r.width\x0d\x0a       \
     ButtonGroup\
.group: childGro\
up\x0d\x0a          }\x0d\
\x0a        }\x0d\x0a    \
  }\x0d\x0a      CellB\
ox {\x0d\x0a        ti\
tle: 'Progress I\
ndicators'\x0d\x0a    \
    ColumnLayout\
 {\x0d\x0a          an\
chors.fill: pare\
nt\x0d\x0a          Bu\
syIndicator {\x0d\x0a \
           runni\
ng: true\x0d\x0a      \
      Layout.ali\
gnment: Qt.Align\
HCenter\x0d\x0a       \
     ToolTip.vis\
ible: hovered\x0d\x0a \
           ToolT\
ip.text: 'Busy I\
ndicator'\x0d\x0a     \
     }\x0d\x0a        \
  DelayButton {\x0d\
\x0a            tex\
t: 'Delay Button\
'\x0d\x0a            d\
elay: 3000\x0d\x0a    \
        Layout.f\
illWidth: true\x0d\x0a\
          }\x0d\x0a   \
       ProgressB\
ar { value: 0.6;\
 Layout.fillWidt\
h: true }\x0d\x0a     \
     ProgressBar\
 { indeterminate\
: true; Layout.f\
illWidth: true }\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a      Cell\
Box {\x0d\x0a         \
 title: 'ComboBo\
xes'\x0d\x0a          \
ColumnLayout {\x0d\x0a\
              an\
chors.fill: pare\
nt\x0d\x0a            \
  ComboBox {\x0d\x0a  \
              mo\
del: ['Normal', \
'Second', 'Third\
']\x0d\x0a            \
    Layout.fillW\
idth: true\x0d\x0a    \
          }\x0d\x0a   \
           Combo\
Box {\x0d\x0a         \
       model: ['\
Flat', 'Second',\
 'Third']\x0d\x0a     \
           Layou\
t.fillWidth: tru\
e\x0d\x0a             \
   flat: true\x0d\x0a \
             }\x0d\x0a\
              Co\
mboBox {\x0d\x0a      \
          model:\
 ['Editable', 'S\
econd', 'Third']\
\x0d\x0a              \
  Layout.fillWid\
th: true\x0d\x0a      \
          editab\
le: true\x0d\x0a      \
        }\x0d\x0a     \
         ComboBo\
x {\x0d\x0a           \
       model: 10\
\x0d\x0a              \
    editable: tr\
ue\x0d\x0a            \
      validator:\
 IntValidator { \
top: 9; bottom: \
0 }\x0d\x0a           \
       Layout.fi\
llWidth: true\x0d\x0a \
             }\x0d\x0a\
          }\x0d\x0a   \
   }\x0d\x0a      Cell\
Box {\x0d\x0a        t\
itle: 'Range Con\
trollers'\x0d\x0a     \
   ColumnLayout \
{\x0d\x0a          anc\
hors.fill: paren\
t\x0d\x0a          Dia\
l {\x0d\x0a           \
 id: dial\x0d\x0a     \
       scale: 0.\
8\x0d\x0a            L\
ayout.alignment:\
 Qt.AlignHCenter\
\x0d\x0a            To\
olTip {\x0d\x0a       \
       parent: d\
ial.handle\x0d\x0a    \
          visibl\
e: dial.pressed\x0d\
\x0a              t\
ext: dial.value.\
toFixed(2)\x0d\x0a    \
        }\x0d\x0a     \
     }\x0d\x0a        \
  RangeSlider {\x0d\
\x0a            fir\
st.value: 0.25; \
second.value: 0.\
75; Layout.fillW\
idth: true\x0d\x0a    \
        ToolTip.\
visible: hovered\
\x0d\x0a            To\
olTip.text: 'Ran\
ge Slider'\x0d\x0a    \
      }\x0d\x0a       \
   Slider {\x0d\x0a   \
         id: sli\
der\x0d\x0a           \
 Layout.fillWidt\
h: true\x0d\x0a       \
     ToolTip {\x0d\x0a\
              pa\
rent: slider.han\
dle\x0d\x0a           \
   visible: slid\
er.pressed\x0d\x0a    \
          text: \
slider.value.toF\
ixed(2)\x0d\x0a       \
     }\x0d\x0a        \
  }\x0d\x0a        }\x0d\x0a\
      }\x0d\x0a      C\
ellBox {\x0d\x0a      \
  title: 'Spin B\
oxes'\x0d\x0a        C\
olumnLayout {\x0d\x0a \
         anchors\
.fill: parent\x0d\x0a \
         SpinBox\
 { value: 50; ed\
itable: true; La\
yout.fillWidth: \
true }\x0d\x0a        \
  SpinBox {\x0d\x0a   \
         from: 0\
\x0d\x0a            to\
: items.length -\
 1\x0d\x0a            \
value: 1 // 'Med\
ium'\x0d\x0a          \
  property var i\
tems: ['Small', \
'Medium', 'Large\
']\x0d\x0a            \
validator: RegEx\
pValidator {\x0d\x0a  \
            regE\
xp: new RegExp('\
(Small|Medium|La\
rge)', 'i')\x0d\x0a   \
         }\x0d\x0a    \
        textFrom\
Value: function(\
value) {\x0d\x0a      \
        return i\
tems[value];\x0d\x0a  \
          }\x0d\x0a   \
         valueFr\
omText: function\
(text) {\x0d\x0a      \
        for (var\
 i = 0; i < item\
s.length; ++i)\x0d\x0a\
                \
if (items[i].toL\
owerCase().index\
Of(text.toLowerC\
ase()) === 0)\x0d\x0a \
                \
 return i\x0d\x0a     \
         return \
sb.value\x0d\x0a      \
      }\x0d\x0a       \
     Layout.fill\
Width: true\x0d\x0a   \
       }\x0d\x0a      \
    SpinBox {\x0d\x0a \
           id: d\
oubleSpinbox\x0d\x0a  \
          editab\
le: true\x0d\x0a      \
      from: 0\x0d\x0a \
           value\
: 110\x0d\x0a         \
   to: 100 * 100\
\x0d\x0a            st\
epSize: 100\x0d\x0a   \
         propert\
y int decimals: \
2\x0d\x0a            p\
roperty real rea\
lValue: value / \
100\x0d\x0a           \
 validator: Doub\
leValidator {\x0d\x0a \
             bot\
tom: Math.min(do\
ubleSpinbox.from\
, doubleSpinbox.\
to)\x0d\x0a           \
   top:  Math.ma\
x(doubleSpinbox.\
from, doubleSpin\
box.to)\x0d\x0a       \
     }\x0d\x0a        \
    textFromValu\
e: function(valu\
e, locale) {\x0d\x0a  \
            retu\
rn Number(value \
/ 100).toLocaleS\
tring(locale, 'f\
', doubleSpinbox\
.decimals)\x0d\x0a    \
        }\x0d\x0a     \
       valueFrom\
Text: function(t\
ext, locale) {\x0d\x0a\
              re\
turn Number.from\
LocaleString(loc\
ale, text) * 100\
\x0d\x0a            }\x0d\
\x0a            Lay\
out.fillWidth: t\
rue\x0d\x0a          }\
\x0d\x0a        }\x0d\x0a   \
   }\x0d\x0a      Cell\
Box {\x0d\x0a        t\
itle: 'Text Inpu\
ts'\x0d\x0a        Col\
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
      TextField \
{\x0d\x0a            w\
idth: parent.wid\
th\x0d\x0a            \
placeholderText:\
 'Enter somethin\
g here...'\x0d\x0a    \
        selectBy\
Mouse: true\x0d\x0a   \
       }\x0d\x0a      \
    TextField {\x0d\
\x0a            wid\
th: parent.width\
\x0d\x0a            te\
xt: 'read only'\x0d\
\x0a            rea\
dOnly: true\x0d\x0a   \
       }\x0d\x0a      \
    ScrollView {\
\x0d\x0a            wi\
dth: parent.widt\
h\x0d\x0a            h\
eight: parent.he\
ight - y\x0d\x0a      \
      TextArea {\
\x0d\x0a              \
placeholderText:\
 'Multi-line tex\
t editor...'\x0d\x0a  \
            sele\
ctByMouse: true\x0d\
\x0a              p\
ersistentSelecti\
on: true\x0d\x0a      \
      }\x0d\x0a       \
   }\x0d\x0a        }\x0d\
\x0a      }\x0d\x0a      \
CellBox {\x0d\x0a     \
   Layout.rowSpa\
n: 2; Layout.min\
imumWidth: 700\x0d\x0a\
        title: '\
Tabs'\x0d\x0a        L\
ayout.preferredW\
idth: height // \
Keep the ratio r\
ight!\x0d\x0a        T\
abBar {\x0d\x0a       \
   id: bar\x0d\x0a    \
      width: par\
ent.width\x0d\x0a     \
     TabButton {\
 text: 'Area' }\x0d\
\x0a          TabBu\
tton { text: 'Ba\
r' }\x0d\x0a          \
TabButton { text\
: 'Box' }\x0d\x0a     \
     TabButton {\
 text: 'Candlest\
ick' }\x0d\x0a        \
  TabButton { te\
xt: 'Polar' }\x0d\x0a \
         TabButt\
on { text: 'Scat\
ter' }\x0d\x0a        \
  TabButton { te\
xt: 'Spine' }\x0d\x0a \
         TabButt\
on { text: 'Pie'\
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
{\x0d\x0a            /\
/ Define x-axis \
to be used with \
the series inste\
ad of default on\
e\x0d\x0a            V\
alueAxis {\x0d\x0a    \
          id: va\
lueAxisAreaSerie\
s\x0d\x0a             \
 min: 2000\x0d\x0a    \
          max: 2\
011\x0d\x0a           \
   tickCount: 12\
\x0d\x0a              \
labelFormat: '%.\
0f'\x0d\x0a           \
 }\x0d\x0a            \
AreaSeries {\x0d\x0a  \
            name\
: 'The U.S.'\x0d\x0a  \
            axis\
X: valueAxisArea\
Series\x0d\x0a        \
      upperSerie\
s: LineSeries {\x0d\
\x0a               \
 XYPoint { x: 20\
00; y: 3 }\x0d\x0a    \
            XYPo\
int { x: 2001; y\
: 2 }\x0d\x0a         \
       XYPoint {\
 x: 2002; y: 1 }\
\x0d\x0a              \
  XYPoint { x: 2\
003; y: 2 }\x0d\x0a   \
             XYP\
oint { x: 2004; \
y: 1 }\x0d\x0a        \
        XYPoint \
{ x: 2005; y: 1 \
}\x0d\x0a             \
   XYPoint { x: \
2006; y: 0 }\x0d\x0a  \
              XY\
Point { x: 2007;\
 y: 3 }\x0d\x0a       \
         XYPoint\
 { x: 2008; y: 4\
 }\x0d\x0a            \
    XYPoint { x:\
 2009; y: 1 }\x0d\x0a \
               X\
YPoint { x: 2010\
; y: 0 }\x0d\x0a      \
          XYPoin\
t { x: 2011; y: \
1 }\x0d\x0a           \
   }\x0d\x0a          \
  }\x0d\x0a           \
 AreaSeries {\x0d\x0a \
             nam\
e: 'Russian'\x0d\x0a  \
            axis\
X: valueAxisArea\
Series\x0d\x0a        \
      upperSerie\
s: LineSeries {\x0d\
\x0a               \
 XYPoint { x: 20\
00; y: 1 }\x0d\x0a    \
            XYPo\
int { x: 2001; y\
: 1 }\x0d\x0a         \
       XYPoint {\
 x: 2002; y: 1 }\
\x0d\x0a              \
  XYPoint { x: 2\
003; y: 1 }\x0d\x0a   \
             XYP\
oint { x: 2004; \
y: 1 }\x0d\x0a        \
        XYPoint \
{ x: 2005; y: 0 \
}\x0d\x0a             \
   XYPoint { x: \
2006; y: 1 }\x0d\x0a  \
              XY\
Point { x: 2007;\
 y: 1 }\x0d\x0a       \
         XYPoint\
 { x: 2008; y: 4\
 }\x0d\x0a            \
    XYPoint { x:\
 2009; y: 3 }\x0d\x0a \
               X\
YPoint { x: 2010\
; y: 2 }\x0d\x0a      \
          XYPoin\
t { x: 2011; y: \
1 }\x0d\x0a           \
   }\x0d\x0a          \
  }\x0d\x0a           \
 AreaSeries {\x0d\x0a \
             nam\
e: 'Taiwan'\x0d\x0a   \
           axisX\
: valueAxisAreaS\
eries\x0d\x0a         \
     upperSeries\
: LineSeries {\x0d\x0a\
                \
XYPoint { x: 200\
0; y: 2 }\x0d\x0a     \
           XYPoi\
nt { x: 2001; y:\
 1 }\x0d\x0a          \
      XYPoint { \
x: 2002; y: 0 }\x0d\
\x0a               \
 XYPoint { x: 20\
03; y: 3 }\x0d\x0a    \
            XYPo\
int { x: 2004; y\
: 0 }\x0d\x0a         \
       XYPoint {\
 x: 2005; y: 0 }\
\x0d\x0a              \
  XYPoint { x: 2\
006; y: 1 }\x0d\x0a   \
             XYP\
oint { x: 2007; \
y: 1 }\x0d\x0a        \
        XYPoint \
{ x: 2008; y: 0 \
}\x0d\x0a             \
   XYPoint { x: \
2009; y: 2 }\x0d\x0a  \
              XY\
Point { x: 2010;\
 y: 2 }\x0d\x0a       \
         XYPoint\
 { x: 2011; y: 1\
 }\x0d\x0a            \
  }\x0d\x0a           \
 }\x0d\x0a          }\x0d\
\x0a          Large\
ChartView {\x0d\x0a   \
         BarSeri\
es {\x0d\x0a          \
    axisX: BarCa\
tegoryAxis {\x0d\x0a  \
              ca\
tegories: ['2007\
', '2008', '2009\
', '2010', '2011\
', '2012' ]\x0d\x0a   \
           }\x0d\x0a  \
            BarS\
et { label: 'Bob\
'; values: [2, 2\
, 3, 4, 5, 6] }\x0d\
\x0a              B\
arSet { label: '\
Susan'; values: \
[5, 1, 2, 4, 1, \
7] }\x0d\x0a          \
    BarSet { lab\
el: 'James'; val\
ues: [3, 5, 8, 1\
3, 5, 8] }\x0d\x0a    \
        }\x0d\x0a     \
     }\x0d\x0a        \
  LargeChartView\
 {\x0d\x0a            \
BoxPlotSeries {\x0d\
\x0a              n\
ame: 'Income'\x0d\x0a \
             Box\
Set { label: 'Ja\
n'; values: [3, \
4, 5.1, 6.2, 8.5\
] }\x0d\x0a           \
   BoxSet { labe\
l: 'Feb'; values\
: [5, 6, 7.5, 8.\
6, 11.8] }\x0d\x0a    \
          BoxSet\
 { label: 'Mar';\
 values: [3.2, 5\
, 5.7, 8, 9.2] }\
\x0d\x0a              \
BoxSet { label: \
'Apr'; values: [\
3.8, 5, 6.4, 7, \
8] }\x0d\x0a          \
    BoxSet { lab\
el: 'May'; value\
s: [4, 5, 5.2, 6\
, 7] }\x0d\x0a        \
    }\x0d\x0a         \
   BoxPlotSeries\
 {\x0d\x0a            \
  name: 'Tax'\x0d\x0a \
             Box\
Set { label: 'Ja\
n'; values: [1.2\
, 2.1, 3.2, 3.4,\
 5.5] }\x0d\x0a       \
       BoxSet { \
label: 'Feb'; va\
lues: [2, 2.2, 2\
.9, 3.6, 6.8] }\x0d\
\x0a              B\
oxSet { label: '\
Mar'; values: [1\
.2, 2.2, 2.7, 3.\
9, 5.2] }\x0d\x0a     \
         BoxSet \
{ label: 'Apr'; \
values: [1.8, 2,\
 2.2, 3, 3.2] }\x0d\
\x0a              B\
oxSet { label: '\
May'; values: [2\
, 1.9, 2.2, 3, 4\
] }\x0d\x0a           \
 }\x0d\x0a          }\x0d\
\x0a          Large\
ChartView {\x0d\x0a   \
         Candles\
tickSeries {\x0d\x0a  \
            name\
: 'Acme Ltd.'\x0d\x0a \
             inc\
reasingColor: 'g\
reen'\x0d\x0a         \
     decreasingC\
olor: 'red'\x0d\x0a   \
           Candl\
estickSet { time\
stamp: 143570880\
0000; open: 690;\
 high: 694; low:\
 599; close: 660\
 }\x0d\x0a            \
  CandlestickSet\
 { timestamp: 14\
35795200000; ope\
n: 669; high: 66\
9; low: 669; clo\
se: 669 }\x0d\x0a     \
         Candles\
tickSet { timest\
amp: 14361408000\
00; open: 485; h\
igh: 623; low: 4\
85; close: 600 }\
\x0d\x0a              \
CandlestickSet {\
 timestamp: 1436\
227200000; open:\
 589; high: 615;\
 low: 377; close\
: 569 }\x0d\x0a       \
       Candlesti\
ckSet { timestam\
p: 1436313600000\
; open: 464; hig\
h: 464; low: 254\
; close: 254 }\x0d\x0a\
            }\x0d\x0a \
         }\x0d\x0a    \
      PolarChart\
View {\x0d\x0a        \
    animationOpt\
ions: ChartView.\
SeriesAnimations\
\x0d\x0a            le\
gend.visible: fa\
lse\x0d\x0a           \
 antialiasing: t\
rue\x0d\x0a           \
 theme: ChartVie\
w[qtquickChartsT\
hemes.currentTex\
t]\x0d\x0a            \
ValueAxis {\x0d\x0a   \
           id: a\
xisAngular\x0d\x0a    \
          min: 0\
\x0d\x0a              \
max: 20\x0d\x0a       \
       tickCount\
: 9\x0d\x0a           \
 }\x0d\x0a            \
ValueAxis {\x0d\x0a   \
           id: a\
xisRadial\x0d\x0a     \
         min: -0\
.5\x0d\x0a            \
  max: 1.5\x0d\x0a    \
        }\x0d\x0a     \
       SplineSer\
ies {\x0d\x0a         \
     id: series1\
\x0d\x0a              \
axisAngular: axi\
sAngular\x0d\x0a      \
        axisRadi\
al: axisRadial\x0d\x0a\
              po\
intsVisible: tru\
e\x0d\x0a            }\
\x0d\x0a            Sc\
atterSeries {\x0d\x0a \
             id:\
 series2\x0d\x0a      \
        axisAngu\
lar: axisAngular\
\x0d\x0a              \
axisRadial: axis\
Radial\x0d\x0a        \
      markerSize\
: 10\x0d\x0a          \
  }\x0d\x0a          }\
\x0d\x0a          // A\
dd data dynamica\
lly to the serie\
s\x0d\x0a          Com\
ponent.onComplet\
ed: {\x0d\x0a         \
   for (var i = \
0; i <= 20; i++)\
 {\x0d\x0a            \
  series1.append\
(i, Math.random(\
));\x0d\x0a           \
   series2.appen\
d(i, Math.random\
());\x0d\x0a          \
  }\x0d\x0a          }\
\x0d\x0a          Larg\
eChartView {\x0d\x0a  \
          Scatte\
rSeries {\x0d\x0a     \
         name: '\
Scatter1'\x0d\x0a     \
         XYPoint\
 { x: 0.51; y: 1\
.5 }\x0d\x0a          \
    XYPoint { x:\
 0.56; y: 1.6 }\x0d\
\x0a              X\
YPoint { x: 0.57\
; y: 1.55 }\x0d\x0a   \
           XYPoi\
nt { x: 0.85; y:\
 1.8 }\x0d\x0a        \
      XYPoint { \
x: 0.96; y: 1.6 \
}\x0d\x0a             \
 XYPoint { x: 0.\
12; y: 1.3 }\x0d\x0a  \
            XYPo\
int { x: 0.52; y\
: 2.1 }\x0d\x0a       \
     }\x0d\x0a        \
    ScatterSerie\
s {\x0d\x0a           \
   name: 'Scatte\
r2'\x0d\x0a           \
   XYPoint { x: \
0.4; y: 1.5 }\x0d\x0a \
             XYP\
oint { x: 0.9; y\
: 1.6 }\x0d\x0a       \
       XYPoint {\
 x: 0.7; y: 1.55\
 }\x0d\x0a            \
  XYPoint { x: 0\
.8; y: 1.8 }\x0d\x0a  \
            XYPo\
int { x: 0.5; y:\
 1.6 }\x0d\x0a        \
      XYPoint { \
x: 0.1; y: 1.3 }\
\x0d\x0a              \
XYPoint { x: 0.6\
; y: 2.1 }\x0d\x0a    \
        }\x0d\x0a     \
     }\x0d\x0a        \
  LargeChartView\
 {\x0d\x0a            \
SplineSeries {\x0d\x0a\
              na\
me: 'BPM'\x0d\x0a     \
         XYPoint\
 { x: 0; y: 0.0 \
}\x0d\x0a             \
 XYPoint { x: 1.\
1; y: 5.2 }\x0d\x0a   \
           XYPoi\
nt { x: 1.9; y: \
2.4 }\x0d\x0a         \
     XYPoint { x\
: 2.1; y: 2.1 }\x0d\
\x0a              X\
YPoint { x: 2.9;\
 y: 2.6 }\x0d\x0a     \
         XYPoint\
 { x: 3.4; y: 2.\
3 }\x0d\x0a           \
   XYPoint { x: \
4.1; y: 3.1 }\x0d\x0a \
           }\x0d\x0a  \
        }\x0d\x0a     \
     LargeChartV\
iew {\x0d\x0a         \
   PieSeries {\x0d\x0a\
              Pi\
eSlice { label: \
'eaten'; value: \
74.7 }\x0d\x0a        \
      PieSlice {\
 label: 'not yet\
 eaten'; value: \
5.1 }\x0d\x0a         \
     PieSlice { \
label: 'wut?'; v\
alue: 20.2; expl\
oded: true }\x0d\x0a  \
          }\x0d\x0a   \
       }\x0d\x0a      \
  }\x0d\x0a      }\x0d\x0a  \
    Popup {\x0d\x0a   \
     id: normalP\
opup\x0d\x0a        Co\
lumnLayout {\x0d\x0a  \
        anchors.\
fill: parent\x0d\x0a  \
        Label { \
text: 'Normal Po\
pup' }\x0d\x0a        \
  CheckBox { tex\
t: 'E-mail' }\x0d\x0a \
         CheckBo\
x { text: 'Calen\
dar' }\x0d\x0a        \
  CheckBox { tex\
t: 'Contacts' }\x0d\
\x0a        }\x0d\x0a    \
  }\x0d\x0a      Popup\
 {\x0d\x0a        id: \
modalPopup\x0d\x0a    \
    modal: true\x0d\
\x0a        ColumnL\
ayout {\x0d\x0a       \
   anchors.fill:\
 parent\x0d\x0a       \
   Label { text:\
 'Modal Popup' }\
\x0d\x0a          Chec\
kBox { text: 'E-\
mail' }\x0d\x0a       \
   CheckBox { te\
xt: 'Calendar' }\
\x0d\x0a          Chec\
kBox { text: 'Co\
ntacts' }\x0d\x0a     \
   }\x0d\x0a      }\x0d\x0a \
     Dialog {\x0d\x0a \
       id: dialo\
g\x0d\x0a        title\
: 'Dialog'\x0d\x0a    \
    Label { text\
: 'The standard \
dialog.' }\x0d\x0a    \
    footer: Dial\
ogButtonBox {\x0d\x0a \
         standar\
dButtons: Dialog\
ButtonBox.Ok | D\
ialogButtonBox.C\
ancel\x0d\x0a        }\
\x0d\x0a      }\x0d\x0a    }\
\x0d\x0a  }\x0d\x0a  footer:\
 RowLayout {\x0d\x0a  \
  width: parent.\
width\x0d\x0a    RowLa\
yout {\x0d\x0a      La\
yout.margins: 10\
\x0d\x0a      Layout.a\
lignment: Qt.Ali\
gnHCenter\x0d\x0a     \
 Label { text: '\
QtQuick Charts T\
hemes: ' }\x0d\x0a    \
  ComboBox {\x0d\x0a  \
      id: qtquic\
kChartsThemes\x0d\x0a \
       model: [\x0d\
\x0a          'Char\
tThemeLight', 'C\
hartThemeBlueCer\
ulean',\x0d\x0a       \
   'ChartThemeDa\
rk', 'ChartTheme\
BrownSand',\x0d\x0a   \
       'ChartThe\
meBlueNcs', 'Cha\
rtThemeHighContr\
ast',\x0d\x0a         \
 'ChartThemeBlue\
Icy', 'ChartThem\
eQt'\x0d\x0a        ]\x0d\
\x0a        Layout.\
fillWidth: true\x0d\
\x0a      }\x0d\x0a    }\x0d\
\x0a    RowLayout {\
\x0d\x0a      Layout.m\
argins: 10\x0d\x0a    \
  Layout.alignme\
nt: Qt.AlignHCen\
ter\x0d\x0a      Label\
 { text: 'QtQuic\
k 2 Themes: ' }\x0d\
\x0a      Label {\x0d\x0a\
        id: qtqu\
ick2Themes\x0d\x0a    \
    objectName: \
'qtquick2Themes'\
\x0d\x0a        Layout\
.fillWidth: true\
\x0d\x0a      }\x0d\x0a    }\
\x0d\x0a    RowLayout \
{\x0d\x0a      Layout.\
margins: 10\x0d\x0a   \
   Layout.alignm\
ent: Qt.AlignHCe\
nter\x0d\x0a      Labe\
l { text: 'Sub-T\
heme: ' }\x0d\x0a     \
 ComboBox {\x0d\x0a   \
     id: subThem\
e\x0d\x0a        model\
: ['Light', 'Dar\
k']\x0d\x0a        Lay\
out.fillWidth: t\
rue\x0d\x0a        ena\
bled: true\x0d\x0a    \
  }\x0d\x0a    }\x0d\x0a    \
RowLayout {\x0d\x0a   \
   property var \
materialColors: \
[\x0d\x0a        'Red'\
, 'Pink', 'Purpl\
e', 'DeepPurple'\
, 'Indigo', 'Blu\
e',\x0d\x0a        'Li\
ghtBlue', 'Cyan'\
, 'Teal', 'Green\
', 'LightGreen',\
 'Lime',\x0d\x0a      \
  'Yello', 'Ambe\
r', 'Orange', 'D\
eepOrange', 'Bro\
wn', 'Grey',\x0d\x0a  \
      'BlueGrey'\
\x0d\x0a      ]\x0d\x0a     \
 Layout.margins:\
 10\x0d\x0a      Layou\
t.alignment: Qt.\
AlignHCenter\x0d\x0a  \
    Label { text\
: 'Colors: ' }\x0d\x0a\
      Label { te\
xt: 'Accent' }\x0d\x0a\
      ComboBox {\
\x0d\x0a        id: ac\
centColor\x0d\x0a     \
   Layout.fillWi\
dth: true\x0d\x0a     \
   enabled: true\
\x0d\x0a        model:\
 {\x0d\x0a          re\
turn parent.mate\
rialColors\x0d\x0a    \
    }\x0d\x0a      }\x0d\x0a\
      Label { te\
xt: 'Primary' }\x0d\
\x0a      ComboBox \
{\x0d\x0a        id: p\
rimaryColor\x0d\x0a   \
     Layout.fill\
Width: true\x0d\x0a   \
     enabled: tr\
ue\x0d\x0a        mode\
l: parent.materi\
alColors\x0d\x0a      \
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
"

qt_resource_name = b"\
\x00\x18\
\x05\x0dd\x85\
\x00p\
\x00y\x00s\x00i\x00d\x00e\x002\x00_\x00q\x00t\x00q\x00u\x00i\x00c\x00k\x002\x00_\
\x00e\x00x\x00a\x00m\x00p\x00l\x00e\
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
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x0b\
\x09\xf8\xd2<\
\x00C\
\x00e\x00l\x00l\x00B\x00o\x00x\x00.\x00q\x00m\x00l\
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
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x02\
\x00\x00\x00H\x00\x02\x00\x00\x00\x04\x00\x00\x00\x07\
\x00\x00\x006\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\
\x00\x00\x01\x12\x00\x00\x00\x00\x00\x01\x00\x00O,\
\x00\x00\x00\xd8\x00\x00\x00\x00\x00\x01\x00\x00N3\
\x00\x00\x01D\x00\x00\x00\x00\x00\x01\x00\x00O\xf7\
\x00\x00\x00~\x00\x00\x00\x00\x00\x01\x00\x00\x00\xf4\
\x00\x00\x00\xa6\x00\x00\x00\x00\x00\x01\x00\x00\x01`\
\x00\x00\x00T\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00\xbc\x00\x00\x00\x00\x00\x01\x00\x00M\x85\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
