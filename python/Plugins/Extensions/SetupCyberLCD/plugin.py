# -*- coding: UTF-8 -*-

# Plugin - Setup CyberLCD
# Developer - Sirius
# Homepage - http://www.gisclub.Tv
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Components.Label import Label
from Components.Language import language
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection
from Tools.Directories import fileExists, resolveFilename, SCOPE_PLUGINS, SCOPE_SKIN_IMAGE, SCOPE_LANGUAGE
from Tools.LoadPixmap import LoadPixmap
from skin import parseColor, parseFont
from os import system, environ
from enigma import addFont
import os, gettext, urllib

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("SetupCyberLCD", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/SetupCyberLCD/locale"))

addFont("/usr/share/enigma2/CyberLCD/fonts/Neuropol.ttf", "SkinTitles", 100, 1)
addFont("/usr/share/enigma2/CyberLCD/fonts/LedCounter.ttf", "SkinIndication", 100, 1)
addFont("/usr/share/enigma2/CyberLCD/fonts/Roboto-Regular.ttf", "SkinGlobal", 100, 1)

def _(txt):
	t = gettext.dgettext("SetupCyberLCD", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

def SearchReplaceWrite(skinPartSearchAndReplace, source, target):
	inFile = open(source, "r")
	file_lines = inFile.readlines()
	inFile.close()
	outFile =  open(target, "w")
	for skinLine in file_lines:
		for item in skinPartSearchAndReplace:
			skinLine = skinLine.replace(item[0], item[1])
		outFile.writelines(skinLine)
	outFile.close()  

colorsetting = [
	("0", _("Standart")),
	("1", _("Expert"))]

styletransparent = [
	("0", _("0%")),
	("1", _("10%")),
	("2", _("20%")),
	("3", _("30%")),
	("4", _("40%")),
	("5", _("50%")),
	("6", _("60%")),
	("7", _("70%")),
	("8", _("80%")),
	("9", _("90%"))]

stylecolor = [
	("0000000", _("Black")),
	("0000080", _("Navy")),
	("00000ff", _("Blue")),
	("0800080", _("Purple")),
	("0008000", _("Green")),
	("000ff00", _("Lime")),
	("0008080", _("Teal")),
	("000ffff", _("Cyan")),
	("0800000", _("Maroon")),
	("0ff0000", _("Red")),
	("0ff00ff", _("Magenta")),
	("0808000", _("Olive")),
	("0ffa500", _("Orange")),
	("0ffd700", _("Gold")),
	("0696969", _("DimGray")),
	("0808080", _("Gray")),
	("0a9a9a9", _("DarkGray")),
	("0c0c0c0", _("Silver")),
	("0f5f5f5", _("WhiteSmoke")),
	("0ffffff", _("White"))]

stylefullcolor = [
	("0000000", _("Black")),
	("02f4f4f", _("DarkSlateGray")),
	("0708090", _("SlateGray")),
	("0778899", _("LightSlateGray")),
	("0696969", _("DimGray")),
	("0808080", _("Gray")),
	("0a9a9a9", _("DarkGray")),
	("0c0c0c0", _("Silver")),
	("0d3d3d3", _("LightGray")),
	("0dcdcdc", _("Gainsboro")),

	("0191970", _("MidnightBlue")),
	("0000080", _("Navy")),
	("000008b", _("DarkBlue")),
	("00000cd", _("MediumBlue")),
	("00000ff", _("Blue")),
	("04169e1", _("RoyalBlue")),
	("04682b4", _("SteelBlue")),
	("06495ed", _("CornflowerBlue")),
	("01e90ff", _("DodgerBlue")),
	("000bfff", _("DeepSkyBlue")),
	("05f9ea0", _("CadetBlue")),
	("087cefa", _("LightSkyBlue")),
	("087ceeb", _("SkyBlue")),
	("0add8e6", _("LightBlue")),
	("0b0e0e6", _("PowderBlue")),
	("0b0c4de", _("LightSteelBlue")),
	("000ced1", _("DarkTurquoise")),
	("048d1cc", _("MediumTurquoise")),
	("040e0d0", _("Turquoise")),
	("000ffff", _("Cyan")),
	("0afeeee", _("PaleTurquoise")),
	("0e0ffff", _("LightCyan")),

	("0800080", _("Purple")),
	("08b008b", _("DarkMagenta")),
	("09932cc", _("DarkOrchid")),
	("09400d3", _("DarkViolet")),
	("08a2be2", _("BlueViolet")),
	("04b0082", _("Indigo")),
	("0483d8b", _("DarkSlateBlue")),
	("06a5acd", _("SlateBlue")),
	("07b68ee", _("MediumSlateBlue")),
	("09370db", _("MediumPurple")),
	("0ba55d3", _("MediumOrchid")),
	("0db7093", _("PaleVioletRed")),
	("0ffb6c1", _("LightPink")),
	("0da70d6", _("Orchid")),
	("0ee82ee", _("Violet")),
	("0ffc0cb", _("Pink")),
	("0dda0dd", _("Plum")),
	("0d8bfd8", _("Thistle")),
	("0e6e6fa", _("Lavender")),

	("0006400", _("DarkGreen")),
	("0008000", _("Green")),
	("0228b22", _("ForestGreen")),
	("0008080", _("Teal")),
	("0008b8b", _("DarkCyan")),
	("0556b2f", _("DarkOliveGreen")),
	("02e8b57", _("SeaGreen")),
	("03cb371", _("MediumSeaGreen")),
	("020b2aa", _("LightSeaGreen")),
	("08fbc8f", _("DarkSeaGreen")),
	("0808000", _("Olive")),
	("06b8e23", _("OliveDrab")),
	("066cdaa", _("MediumAquamarine")),
	("07fffd4", _("Aquamarine")),
	("000fa9a", _("MediumSpringGreen")),
	("000ff7f", _("SpringGreen")),
	("090ee90", _("LightGreen")),
	("098fb98", _("PaleGreen")),
	("032cd32", _("LimeGreen")),
	("000ff00", _("Lime")),
	("07cfc00", _("LawnGreen")),
	("07fff00", _("Chartreuse")),
	("0adff2f", _("GreenYellow")),
	("09acd32", _("YellowGreen")),

	("0800000", _("Maroon")),
	("08b0000", _("DarkRed")),
	("0a52a2a", _("Brown")),
	("0b22222", _("FireBrick")),
	("0ff0000", _("Red")),
	("0ff4500", _("OrangeRed")),
	("0ff6347", _("Tomato")),
	("0dc143c", _("Crimson")),
	("0c71585", _("MediumVioletRed")),
	("0ff1493", _("DeepPink")),
	("0ff00ff", _("Magenta")),
	("0ff69b4", _("HotPink")),
	("08b4513", _("SaddleBrown")),
	("0a0522d", _("Sienna")),
	("0cd5c5c", _("IndianRed")),
	("0f08080", _("LightCoral")),
	("0fa8072", _("Salmon")),
	("0e9967a", _("DarkSalmon")),
	("0ffa07a", _("LightSalmon")),
	("0bc8f8f", _("RosyBrown")),
	("0f4a460", _("SandyBrown")),
	("0deb887", _("BurlyWood")),
	("0d2b48c", _("Tan")),
	("0ffdead", _("NavajoWhite")),
	("0f5deb3", _("Wheat")),
	("0ffe4c4", _("Bisque")),
	("0ffdab9", _("PeachPuff")),
	("0ffebcd", _("BlanchedAlmond")),
	("0fff8dc", _("Cornsilk")),

	("0d2691e", _("Chocolate")),
	("0ff7f50", _("Coral")),
	("0cd853f", _("Peru")),
	("0b8860b", _("DarkGoldenrod")),
	("0daa520", _("Goldenrod")),
	("0ff8c00", _("DarkOrange")),
	("0ffa500", _("Orange")),
	("0ffd700", _("Gold")),
	("0ffff00", _("Yellow")),
	("0bdb76b", _("DarkKhaki")),
	("0f0e68c", _("Khaki")),
	("0eee8aa", _("PaleGoldenrod")),
	("0ffe4b5", _("Moccasin")),
	("0ffefd5", _("PapayaWhip")),
	("0fafad2", _("LightGoldenrodYellow")),
	("0fffacd", _("LemonChiffon")),
	("0ffffe0", _("LightYellow")),

	("0ffe4e1", _("MistyRose")),
	("0fff0f5", _("LavenderBlush")),
	("0faf0e6", _("Linen")),
	("0faebd7", _("AntiqueWhite")),
	("0fdf5e6", _("OldLace")),
	("0fff5ee", _("Seashell")),
	("0f5f5dc", _("Beige")),
	("0fffaf0", _("FloralWhite")),
	("0fffff0", _("Ivory")),
	("0f5f5f5", _("WhiteSmoke")),
	("0f8f8ff", _("GhostWhite")),
	("0f0f8ff", _("AliceBlue")),
	("0f0ffff", _("Azure")),
	("0f5fffa", _("MintCream")),
	("0f0fff0", _("Honeydew")),
	("0fffafa", _("Snow")),
	("0ffffff", _("White"))]

device = [
	("uno4k", _("Uno4k")),
	("solo4k", _("Duo4k/Solo4k")),
	("ultimo4k", _("Ultimo4k"))]

fonts = [
	("Roboto-Regular", _("Regular")),
	("Roboto-Medium", _("Medium")),
	("Roboto-Bold", _("Bold")),
	("Roboto-Italic", _("Italic")),
	("Roboto-MediumItalic", _("MediumItalic")),
	("Roboto-BoldItalic", _("BoldItalic"))]

progressmode = [
	("TemplatesDisplayProgressLayerStandard", _("Standard")),
	("TemplatesDisplayProgressLayerImproved", _("Improved"))]

widgetinfobar = [
	("TemplatesInfoBarDisplayName", _("Name")),
	("TemplatesInfoBarDisplayPicon", _("Picon")),
	("TemplatesInfoBarDisplayClock", _("Clock"))]

widgetmovieinfobar = [
	("TemplatesMovieInfoBarDisplayName", _("Name")),
	("TemplatesMovieInfoBarDisplayClock", _("Clock"))]

widgetchannelselection = [
	("TemplatesChannelSelectionDisplayName", _("Name")),
	("TemplatesChannelSelectionDisplayPicon", _("Picon")),
	("TemplatesChannelSelectionDisplayClock", _("Clock"))]

widgetradioselection = [
	("TemplatesRadioSelectionDisplayName", _("Name")),
	("TemplatesRadioSelectionDisplayClock", _("Clock"))]

widgetepgselection = [
	("TemplatesEPGSelectionDisplayName", _("Name")),
	("TemplatesEPGSelectionDisplayPicon", _("Picon")),
	("TemplatesEPGSelectionDisplayClock", _("Clock"))]

if not fileExists("/usr/lib/enigma2/python/Components/Converter/MSNWeather2.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/AnimatedWeatherPixmap.py"):
	widgetstandby = [
		("TemplatesStandbyDisplayClock", _("Clock"))]
else:
	widgetstandby = [
		("TemplatesStandbyDisplayClock", _("Clock")),
		("TemplatesStandbyDisplayWeatherMSN", _("Weather MSN")),
		("TemplatesStandbyDisplayWeatherMSNAnimated", _("Animated Weather MSN"))]

config.skin.cyberlcd = ConfigSubsection()

config.skin.cyberlcd.device = ConfigSelection(default="Duo4k/Solo4k", choices = device)

config.skin.cyberlcd.fonts = ConfigSelection(default="Roboto-Regular", choices = fonts)

config.skin.cyberlcd.colorsetting = ConfigSelection(default="0", choices = colorsetting)

if config.skin.cyberlcd.colorsetting.value == "0":
	config.skin.cyberlcd.colorbackground1 = ConfigSelection(default="0000000", choices = stylecolor)
	config.skin.cyberlcd.colorbackground4 = ConfigSelection(default="000ffff", choices = stylecolor)

	config.skin.cyberlcd.colorforeground1 = ConfigSelection(default="0ffd700", choices = stylecolor)
	config.skin.cyberlcd.colorforeground2 = ConfigSelection(default="0f5f5f5", choices = stylecolor)
	config.skin.cyberlcd.colorforeground3 = ConfigSelection(default="0a9a9a9", choices = stylecolor)
	config.skin.cyberlcd.colorforeground4 = ConfigSelection(default="000ffff", choices = stylecolor)
else:
	config.skin.cyberlcd.colorbackground1 = ConfigSelection(default="0000000", choices = stylefullcolor)
	config.skin.cyberlcd.colorbackground4 = ConfigSelection(default="000ffff", choices = stylefullcolor)

	config.skin.cyberlcd.colorforeground1 = ConfigSelection(default="0ffd700", choices = stylefullcolor)
	config.skin.cyberlcd.colorforeground2 = ConfigSelection(default="0f5f5f5", choices = stylefullcolor)
	config.skin.cyberlcd.colorforeground3 = ConfigSelection(default="0a9a9a9", choices = stylefullcolor)
	config.skin.cyberlcd.colorforeground4 = ConfigSelection(default="000ffff", choices = stylefullcolor)

config.skin.cyberlcd.backgroundtransparent = ConfigSelection(default="5", choices = styletransparent)
config.skin.cyberlcd.foregroundtransparent = ConfigSelection(default="0", choices = styletransparent)

config.skin.cyberlcd.progressmode = ConfigSelection(default="TemplatesDisplayProgressLayerStandard", choices = progressmode)

config.skin.cyberlcd.widgetinfobar = ConfigSelection(default="TemplatesInfoBarDisplayName", choices = widgetinfobar)

config.skin.cyberlcd.widgetmovieinfobar = ConfigSelection(default="TemplatesMovieInfoBarDisplayName", choices = widgetmovieinfobar)

config.skin.cyberlcd.widgetchannelselection = ConfigSelection(default="TemplatesChannelSelectionDisplayName", choices = widgetchannelselection)

config.skin.cyberlcd.widgetradioselection = ConfigSelection(default="TemplatesRadioSelectionDisplayName", choices = widgetradioselection)

config.skin.cyberlcd.widgetepgselection = ConfigSelection(default="TemplatesEPGSelectionDisplayName", choices = widgetepgselection)

config.skin.cyberlcd.widgetstandby = ConfigSelection(default="TemplatesStandbyDisplayClock", choices = widgetstandby)

SKIN_CYBERLCD = """
	<!-- Setup CyberLCD -->
		<screen name="SetupCyberLCD" position="0,0" size="1920,1080" title=" " flags="wfNoBorder" backgroundColor="transparent">

	<!-- Menu Layer -->
		<eLabel position="0,88" size="1920,54" backgroundColor="#50ffffff" zPosition="-14" />
		<eLabel position="0,90" size="1920,50" backgroundColor="#50000000" zPosition="-13" />
		<eLabel position="0,888" size="1920,104" backgroundColor="#50ffffff" zPosition="-14" />
		<eLabel position="0,890" size="1920,100" backgroundColor="#50000000" zPosition="-13" />
		<eLabel position="98,867" size="234,146" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="100,869" size="230,142" backgroundColor="#50696969" zPosition="-11" />
		<eLabel position="78,188" size="1004,659" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="80,190" size="1000,655" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="0,188" size="80,659" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="0,190" size="80,655" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="10,200" size="70,635" backgroundColor="#50696969" zPosition="-10" />
		<eLabel text="C" position="10,205" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="Y" position="10,275" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="B" position="10,345" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="E" position="10,415" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="R" position="10,485" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="L" position="10,625" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="C" position="10,695" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="D" position="10,765" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<widget source="Title" render="Label" position="80,96" size="1500,44" font="SkinTitles; 40" foregroundColor="#10ffd700" backgroundColor="#50000000" halign="left" transparent="1" />
		<widget name="config" position="90,200" size="980,635" scrollbarMode="showNever" itemHeight="35" font="SkinGlobal; 25" backgroundColor="#50000000" backgroundColorSelected="#50696969" transparent="1" />
		<widget name="info_com" position="340,895" size="1000,60" font="SkinGlobal; 25" foregroundColor="#10a9a9a9" backgroundColor="#50000000" halign="left" valign="top" transparent="1" />
		<widget name="info_sk" position="340,960" size="1000,30" font="SkinGlobal; 25" foregroundColor="#10a9a9a9" backgroundColor="#50000000" halign="left" valign="center" transparent="1" />

	<!-- Preview Layer -->
		<eLabel position="1098,363" size="742,484" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1100,365" size="740,480" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="1110,375" size="720,460" backgroundColor="#ffffffff" zPosition="-10" />
		<eLabel position="1840,363" size="80,484" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1840,365" size="80,480" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="1840,375" size="70,460" backgroundColor="#50696969" zPosition="-10" />

		<widget name="bgcolor1a" position="1120,385" size="700,440" backgroundColor="background" zPosition="-3" />
		<widget name="bgcolor4a" position="1120,750" size="700,20" backgroundColor="background" zPosition="-2" />

		<widget name="fgcolor1a" position="1120,400" size="700,35" font="SkinTitles; 35" halign="center" backgroundColor="background" transparent="1" />
		<widget name="fgcolor2a" position="1120,670" size="700,25" font="SkinGlobal; 25" halign="center" backgroundColor="background" transparent="1" />
		<widget name="fgcolor3a" position="1120,710" size="700,25" font="SkinGlobal; 25" halign="center" backgroundColor="background" transparent="1" />
		<widget name="fgcolor4a" position="1120,775" size="700,35" font="SkinIndication; 35" halign="center" backgroundColor="background" transparent="1" />

	<!-- Buttons Layer -->
		<eLabel position="1368,867" size="454,146" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1370,869" size="450,142" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="1375,875" size="390,130" backgroundColor="#50696969" zPosition="-10" />
		<ePixmap pixmap="CyberLCD/buttons/button_key_red.png" position="1773,885" size="40,20" alphatest="on" />
		<ePixmap pixmap="CyberLCD/buttons/button_key_green.png" position="1773,915" size="40,20" alphatest="on" />
		<ePixmap pixmap="CyberLCD/buttons/button_key_yellow.png" position="1773,945" size="40,20" alphatest="on" />
		<ePixmap pixmap="CyberLCD/buttons/button_key_blue.png" position="1773,975" size="40,20" alphatest="on" />
		<widget source="key_red" render="Label" position="1380,884" size="380,22" font="SkinTitles; 22" halign="right" valign="center" foregroundColor="#10f5f5f5" backgroundColor="#50696969" transparent="1" />
		<widget source="key_green" render="Label" position="1380,914" size="380,22" font="SkinTitles; 22" halign="right" valign="center" foregroundColor="#10f5f5f5" backgroundColor="#50696969" transparent="1" />
		<widget source="key_yellow" render="Label" position="1380,944" size="380,22" font="SkinTitles; 22" halign="right" valign="center" foregroundColor="#10f5f5f5" backgroundColor="#50696969" transparent="1" />
		<widget source="key_blue" render="Label" position="1380,974" size="380,22" font="SkinTitles; 22" halign="right" valign="center" foregroundColor="#10f5f5f5" backgroundColor="#50696969" transparent="1" />

	<!-- Clock Layer -->
		<eLabel position="1618,63" size="204,104" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1620,65" size="200,100" backgroundColor="#50696969" zPosition="-11" />
		<widget source="global.CurrentTime" render="Label" position="1615,95" size="90,50" font="SkinIndication; 50" foregroundColor="#10ffd700" backgroundColor="#50000000" halign="right" transparent="1">
			<convert type="ClockToText">Format:%H</convert>
		</widget>
		<eLabel text=":" position="1710,95" size="20,50" font="SkinIndication; 50" foregroundColor="#10ffd700" backgroundColor="#50000000" halign="center" transparent="1" zPosition="-1" />
		<widget source="global.CurrentTime" render="Label" position="1735,95" size="90,50" font="SkinIndication; 50" foregroundColor="#10ffd700" backgroundColor="#50000000" halign="left" transparent="1">
			<convert type="ClockToText">Format:%M</convert>
		</widget>
		<widget source="global.CurrentTime" render="Label" position="1620,70" size="200,25" font="SkinTitles; 20" foregroundColor="#10f5f5f5" backgroundColor="#50696969" halign="center" transparent="1">
			<convert type="ClockToText">Format:%A</convert>
		</widget>
		<widget source="global.CurrentTime" render="Label" position="1620,140" size="200,25" font="SkinTitles; 22" foregroundColor="#10f5f5f5" backgroundColor="#50696969" halign="center" transparent="1">
			<convert type="ClockToText">Format:%d.%m.%Y</convert>
		</widget>
	</screen>"""

class SetupCyberLCD(ConfigListScreen, Screen):
	def __init__(self, session):

		Screen.__init__(self, session)
		self.session = session
		self.skin = SKIN_CYBERLCD

		ConfigListScreen.__init__(self, self.list(), session = session)

		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "DirectionActions", "EPGSelectActions"],
		{
			"ok": self.save,
			"cancel": self.exit,
			"left": self.keyLeft,
			"right": self.keyRight,
			"down": self.keyDown,
			"up": self.keyUp,
			"red": self.exit,
			"green": self.save,
			"yellow": self.default,
			"blue": self.download,
			"info": self.about
		}, -1)

		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("Save"))
		self["key_yellow"] = StaticText(_("Default"))
		self["key_blue"] = StaticText(_("Update CyberLCD"))
		self["Title"] = StaticText(_("Setup CyberLCD"))

		self["bgcolor1a"] = Label(_(" "))
		self["bgcolor4a"] = Label(_(" "))

		self["fgcolor1a"] = Label(_(" "))
		self["fgcolor2a"] = Label(_(" "))
		self["fgcolor3a"] = Label(_(" "))
		self["fgcolor4a"] = Label(_(" "))

		self["info_sk"] = Label(_(" "))
		self["info_com"] = Label(_(" "))

		self.infosk()
		self.infocom()

		self.onLayoutFinish.append(self.previewSkin)

	def list(self):
		list = []
		sep = "-"
		char = 40
		tab = " "*10
		section = _("Devise")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Your devise:"), config.skin.cyberlcd.device))
		section = _("Fonts")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Fonts:"), config.skin.cyberlcd.fonts))
		section = _("Style")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Color setting:"), config.skin.cyberlcd.colorsetting))

		list.append(getConfigListEntry(_("Background color:"), config.skin.cyberlcd.colorbackground1))
		list.append(getConfigListEntry(_("Progress color:"), config.skin.cyberlcd.colorbackground4))

		list.append(getConfigListEntry(_("Title text color:"), config.skin.cyberlcd.colorforeground1))
		list.append(getConfigListEntry(_("Main text color:"), config.skin.cyberlcd.colorforeground2))
		list.append(getConfigListEntry(_("Additional text color:"), config.skin.cyberlcd.colorforeground3))
		list.append(getConfigListEntry(_("Indication text color:"), config.skin.cyberlcd.colorforeground4))

		list.append(getConfigListEntry(_("Background transparent:"), config.skin.cyberlcd.backgroundtransparent))
		list.append(getConfigListEntry(_("Text transparent:"), config.skin.cyberlcd.foregroundtransparent))
		section = _("Progress")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Progress mode:"), config.skin.cyberlcd.progressmode))
		section = _("Infobar")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Widget in infobar:"), config.skin.cyberlcd.widgetinfobar))
		section = _("Movie Infobar")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Widget in movieinfobar:"), config.skin.cyberlcd.widgetmovieinfobar))
		section = _("Channel Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Widget in channel selection:"), config.skin.cyberlcd.widgetchannelselection))
		section = _("Radio Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Widget in radio selection:"), config.skin.cyberlcd.widgetradioselection))
		section = _("EPG Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Widget in EPG selection:"), config.skin.cyberlcd.widgetepgselection))
		section = _("Standby")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Widget in standby:"), config.skin.cyberlcd.widgetstandby))
		return list

	def keyLeft(self):
		ConfigListScreen.keyLeft(self)
		self.previewSkin()

	def keyRight(self):
		ConfigListScreen.keyRight(self)
		self.previewSkin()

	def keyDown(self):
		self["config"].instance.moveSelection(self["config"].instance.moveDown)
		self.previewSkin()

	def keyUp(self):
		self["config"].instance.moveSelection(self["config"].instance.moveUp)
		self.previewSkin()

	def previewSkin(self):
		self.bgtext = "..."
		self.fgtext = "Skin CyberLCD"
		self.fglogo = "CyberLCD"
		self.bgColor1 = "#0%s" % config.skin.cyberlcd.colorbackground1.value
		self.bgColor4 = "#0%s" % config.skin.cyberlcd.colorbackground4.value

		self.fgColor1 = "#0%s" % config.skin.cyberlcd.colorforeground1.value
		self.fgColor2 = "#0%s" % config.skin.cyberlcd.colorforeground2.value
		self.fgColor3 = "#0%s" % config.skin.cyberlcd.colorforeground3.value
		self.fgColor4 = "#0%s" % config.skin.cyberlcd.colorforeground4.value

	# Background
		self["bgcolor1a"].setText(_(self.bgtext))
		self["bgcolor1a"].instance.setBackgroundColor(parseColor(self.bgColor1))
		self["bgcolor1a"].instance.setForegroundColor(parseColor(self.bgColor1))
	# Progress
		self["bgcolor4a"].setText(_(self.bgtext))
		self["bgcolor4a"].instance.setBackgroundColor(parseColor(self.bgColor4))
		self["bgcolor4a"].instance.setForegroundColor(parseColor(self.bgColor4))
	# Title
		self["fgcolor1a"].setText(_(self.fgtext))
		self["fgcolor1a"].instance.setForegroundColor(parseColor(self.fgColor1))
	# Font 1
		self["fgcolor2a"].setText(_(self.fgtext))
		self["fgcolor2a"].instance.setForegroundColor(parseColor(self.fgColor2))
	# Font 2
		self["fgcolor3a"].setText(_(self.fgtext))
		self["fgcolor3a"].instance.setForegroundColor(parseColor(self.fgColor3))
	# Indication
		self["fgcolor4a"].setText(_(self.fgtext))
		self["fgcolor4a"].instance.setForegroundColor(parseColor(self.fgColor4))

	def infosk(self):
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/"
		version = ""
		try:
			for text in open("%sSetupCyberLCD/version" % (pluginpath)).readlines()[1]:
				version += text
			self["info_sk"].setText(version)
			return version
		except:
			return ""

	def infocom(self):
		try:
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberLCD/version","/tmp/version")
		except:
			pass

		if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/WeatherMSN/plugin.pyo")\
			and not fileExists("/usr/lib/enigma2/python/Components/Converter/MSNWeather2.py"):
			self["info_com"] = Label(_("No install components skin !!! \nPress blue button to install !!!"))
		elif not fileExists("/usr/lib/enigma2/python/Components/Converter/AlwaysTrue.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py"):
			self["info_com"] = Label(_("No install components skin !!! \nPress blue button to install !!!"))
		else:
			version = ""
			try:
				for text in open("/tmp/version").readlines()[3]:
					version += text
				self["info_com"].setText(version)
				return version
			except:
				return ""

	def createSkin(self):
		try:
	# user skin
			skin_user = []
	# color`s
			skin_user.append(["#50000000", "#" + config.skin.cyberlcd.backgroundtransparent.value + config.skin.cyberlcd.colorbackground1.value])
			skin_user.append(["#5000ffff", "#" + config.skin.cyberlcd.foregroundtransparent.value + config.skin.cyberlcd.colorbackground4.value])
			skin_user.append(["#10ffd700", "#" + config.skin.cyberlcd.foregroundtransparent.value + config.skin.cyberlcd.colorforeground1.value])
			skin_user.append(["#10f5f5f5", "#" + config.skin.cyberlcd.foregroundtransparent.value + config.skin.cyberlcd.colorforeground2.value])
			skin_user.append(["#10a9a9a9", "#" + config.skin.cyberlcd.foregroundtransparent.value + config.skin.cyberlcd.colorforeground3.value])
			skin_user.append(["#1000ffff", "#" + config.skin.cyberlcd.foregroundtransparent.value + config.skin.cyberlcd.colorforeground4.value])
	# clock
			if not fileExists("/usr/lib/enigma2/python/Components/Converter/AlwaysTrue.py"):
				skin_user.append(["TemplatesDisplayClockDefault","TemplatesDisplayClock"])
				skin_user.append(["TemplatesStandbyDisplayClockDefault","TemplatesStandbyDisplayClock"])
			else:
				skin_user.append(["TemplatesDisplayClockStyle","TemplatesDisplayClock"])
				skin_user.append(["TemplatesStandbyDisplayClockStyle","TemplatesStandbyDisplayClock"])
	# fonts
			skin_user.append(["Roboto-Regular", config.skin.cyberlcd.fonts.value])
	# progress
			skin_user.append([config.skin.cyberlcd.progressmode.value, "TemplatesDisplayProgressLayer"])
	# widget infobar
			skin_user.append([config.skin.cyberlcd.widgetinfobar.value, "TemplatesInfoBarDisplay"])
	# widget movie infobar
			skin_user.append([config.skin.cyberlcd.widgetmovieinfobar.value, "TemplatesMovieInfoBarDisplay"])
	# widget channel selection
			skin_user.append([config.skin.cyberlcd.widgetchannelselection.value, "TemplatesChannelSelectionDisplay"])
	# widget radio selection
			skin_user.append([config.skin.cyberlcd.widgetradioselection.value, "TemplatesRadioSelectionDisplay"])
	# widget epg selection
			skin_user.append([config.skin.cyberlcd.widgetepgselection.value, "TemplatesEPGSelectionDisplay"])
	# widget standby
			skin_user.append([config.skin.cyberlcd.widgetstandby.value, "TemplatesStandbyDisplay"])

			SearchReplaceWrite(skin_user, "/usr/share/enigma2/CyberLCD/skin_default.xml", "/etc/enigma2/skin_user.xml")
		except:
			self.default()
	# end
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def install(self):
		skinpath = "/usr/share/enigma2/"
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/"
		componentspath = "/usr/lib/enigma2/python/Components/"
		if fileExists("/tmp/version")\
			and fileExists("/tmp/plugin.py")\
			and fileExists("/tmp/ruSetupCyberLCD.mo")\
			and fileExists("/tmp/deSetupCyberLCD.mo")\
			and fileExists("/tmp/skin_solo4k.xml")\
			and fileExists("/tmp/skin_uno4k.xml")\
			and fileExists("/tmp/skin_ultimo4k.xml")\
			and fileExists("/tmp/AlwaysTrue.py")\
			and fileExists("/tmp/AnimatedWeatherPixmap.py")\
			and fileExists("/tmp/PiconUni.py"):
			os.system("cp /tmp/version %sSetupCyberLCD/version" % (pluginpath))
	# install plugin
			os.system("cp /tmp/plugin.py %sSetupCyberLCD/plugin.py" % (pluginpath))
			os.system("cp /tmp/ruSetupCyberLCD.mo %sSetupCyberLCD/locale/ru/LC_MESSAGES/SetupCyberLCD.mo" % (pluginpath))
			os.system("cp /tmp/deSetupCyberLCD.mo %sSetupCyberLCD/locale/de/LC_MESSAGES/SetupCyberLCD.mo" % (pluginpath))
	# install skin
			os.system("cp /tmp/skin_default.xml %sCyberLCD/skin_default.xml" % (skinpath))
			os.system("cp /tmp/skin_solo4k.xml %sCyberLCD/skin_solo4k.xml" % (skinpath))
			os.system("cp /tmp/skin_uno4k.xml %sCyberLCD/skin_uno4k.xml" % (skinpath))
			os.system("cp /tmp/skin_ultimo4k.xml %sCyberLCD/skin_ultimo4k.xml" % (skinpath))
	# install converter
			os.system("cp /tmp/AlwaysTrue.py %sConverter/AlwaysTrue.py" % (componentspath))
			os.system("cp %sWeatherMSN/components/MSNWeather2.py %sConverter/MSNWeather2.py" % (pluginpath, componentspath))
	# install renderer
			os.system("cp /tmp/AnimatedWeatherPixmap.py %sRenderer/AnimatedWeatherPixmap.py" % (componentspath))
			os.system("cp /tmp/PiconUni.py %sRenderer/PiconUni.py" % (componentspath))
	# end
			self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)
		else:
			self.default()

	def download(self):
		try:
	# download plugin
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberLCD/plugin.py","/tmp/plugin.py")
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberLCD/locale/ru/LC_MESSAGES/SetupCyberLCD.mo","/tmp/ruSetupCyberLCD.mo")
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberLCD/locale/de/LC_MESSAGES/SetupCyberLCD.mo","/tmp/deSetupCyberLCD.mo")
	# download skin
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberLCD/skin_default.xml","/tmp/skin_default.xml")
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberLCD/skin_solo4k.xml","/tmp/skin_solo4k.xml")
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberLCD/skin_uno4k.xml","/tmp/skin_uno4k.xml")
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberLCD/skin_ultimo4k.xml","/tmp/skin_ultimo4k.xml")
	# download converter
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/AlwaysTrue.py","/tmp/AlwaysTrue.py")
	# download renderer
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/AnimatedWeatherPixmap.py","/tmp/AnimatedWeatherPixmap.py")
			urllib.urlretrieve ("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/PiconUni.py","/tmp/PiconUni.py")
	# end
			self.install()
		except:
			pass

	def setDefault(self, configItem):
		configItem.setValue(configItem.default)

	def save(self):
		for x in self["config"].list:
			if len(x) > 1:
				x[1].save()
		os.system("cp /usr/share/enigma2/CyberLCD/skin_%s.xml /usr/share/enigma2/CyberLCD/skin_default.xml" % (config.skin.cyberlcd.device.value))
		self.createSkin()

	def default(self):
		for x in self["config"].list:
			if len(x) > 1:
				self.setDefault(x[1])
				x[1].save()
		os.system("rm -f /etc/enigma2/skin_user.xml")
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def exit(self):
		for x in self["config"].list:
			if len(x) > 1:
				x[1].cancel()
		self.close()

	def restart(self, answer):
		if answer is True:
			self.session.open(TryQuitMainloop, 3)

	def about(self):
		self.session.open(MessageBox, _("Skin CyberLCD\nDeveloper: Sirius0103 \nHomepage: www.gisclub.tv \nGithub: www.github.com/Sirius0103 \n\nDonate:\nVISA 4276 4000 5465 0552"), MessageBox.TYPE_INFO)

def main(session, **kwargs):
	session.open(SetupCyberLCD)

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Setup CyberLCD"),
	description=_("Setup skin CyberLCD"),
	where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU],
	icon="plugin.png",
	fnc=main)
