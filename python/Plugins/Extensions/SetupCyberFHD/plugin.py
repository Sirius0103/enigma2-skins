# -*- coding: UTF-8 -*-

# Plugin - Setup Cyber FHD
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
import gettext
import os

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("SetupCyberFHD", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/SetupCyberFHD/locale"))

addFont("/usr/share/enigma2/Cyber_fhd/fonts/Neuropol.ttf", "STitles", 100, 1)
addFont("/usr/share/enigma2/Cyber_fhd/fonts/LedCounter.ttf", "SIndication", 100, 1)
addFont("/usr/share/enigma2/Cyber_fhd/fonts/Roboto-Regular.ttf", "SGlobal", 100, 1)

def _(txt):
	t = gettext.dgettext("SetupCyberFHD", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

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
fonts = [
	("Roboto-Regular", _("Regular")),
	("Roboto-Medium", _("Medium")),
	("Roboto-Bold", _("Bold")),
	("Roboto-Italic", _("Italic")),
	("Roboto-MediumItalic", _("MediumItalic")),
	("Roboto-BoldItalic", _("BoldItalic"))]
numberchannel = [
	("TemplatesInfoBarTvNumberNo", _("No")),
	("TemplatesInfoBarTvNumberYes", _("Yes"))]
tunerpanelinfobar = [
	("TemplatesInfoBarTvTunerNo", _("No")),
	("TemplatesInfoBarTvTunerDigital", _("Digital")),
	("TemplatesInfoBarTvTunerAnalog", _("Analog"))]
epgpanelinfobar = [
	("TemplatesInfoBarTvInfoEPGNo", _("No")),
	("TemplatesInfoBarTvInfoEPGNow", _("Now")),
	("TemplatesInfoBarTvInfoEPGNext", _("Now, Next"))]
cryptedpanelinfobar = [
	("TemplatesInfoBarTvInfoCryptedNo", _("No")),
	("TemplatesInfoBarTvInfoCryptedYes", _("Yes"))]
infopanelinfobar = [
	("TemplatesInfoBarTvInfoPanelNo", _("No")),
#	("TemplatesInfoBarTvInfoPanelCI", _("CI")),
	("TemplatesInfoBarTvInfoPanelNIM", _("NIM")),
	("TemplatesInfoBarTvInfoPanelECM", _("ECM")),
	("TemplatesInfoBarTvInfoPanelPID", _("PID"))]
weatherpanelinfobar = [
	("TemplatesInfoBarTvInfoWeatherNo", _("No")),
	("TemplatesInfoBarTvInfoWeatherMSN", _("MSN"))]
progressmode = [
	("ProgressLayerStandard", _("Standard")),
	("ProgressLayerImproved", _("Improved"))]
scrollbarmode = [
	("showNever", _("No")),
	("showOnDemand", _("Yes"))]

buqetchannelselection = [
	("TemplatesChannelSelectionTvBuqetNo", _("No")),
	("TemplatesChannelSelectionTvBuqetYes", _("Yes"))]
piconchannelselection = [
	("TemplatesChannelSelectionTvPiconNo", _("No")),
	("TemplatesChannelSelectionTvPiconYes", _("Yes"))]
tunerpanelchannelselection = [
	("TemplatesChannelSelectionTvInfoTunerNo", _("No")),
	("TemplatesChannelSelectionTvInfoTunerYes", _("Yes"))]
epgpanelchannelselection = [
	("TemplatesChannelSelectionTvInfoEPGNo", _("No")),
	("TemplatesChannelSelectionTvInfoEPGNow", _("Now")),
	("TemplatesChannelSelectionTvInfoEPGNext", _("Now, Next")),
	("TemplatesChannelSelectionTvInfoEPGNowProgram", _("Now, 5 Programs")),
	("TemplatesChannelSelectionTvInfoEPGProgram", _("10 Programs"))]
buqetradiochannelselection = [
	("TemplatesChannelSelectionRadioBuqetNo", _("No")),
	("TemplatesChannelSelectionRadioBuqetYes", _("Yes"))]
panelmovieselection = [
	("TemplatesMovieSelectionDescriptionNo", _("No")),
	("TemplatesMovieSelectionDescriptionShort", _("Short Description")),
	("TemplatesMovieSelectionDescriptionFull", _("Full Description"))]

config.skin.cyber = ConfigSubsection()
config.skin.cyber.fonts = ConfigSelection(default="Roboto-Regular", choices = fonts)

config.skin.cyber.colorsetting = ConfigSelection(default="0", choices = colorsetting)

if config.skin.cyber.colorsetting.value == "0":
	config.skin.cyber.colorbackground1 = ConfigSelection(default="0000000", choices = stylecolor)
	config.skin.cyber.colorbackground2 = ConfigSelection(default="0696969", choices = stylecolor)
	config.skin.cyber.colorbackground3 = ConfigSelection(default="0ffffff", choices = stylecolor)
	config.skin.cyber.colorbackground4 = ConfigSelection(default="000ffff", choices = stylecolor)
	config.skin.cyber.colorbackground5 = ConfigSelection(default="0696969", choices = stylecolor)

	config.skin.cyber.colorforeground1 = ConfigSelection(default="0ffd700", choices = stylecolor)
	config.skin.cyber.colorforeground2 = ConfigSelection(default="0f5f5f5", choices = stylecolor)
	config.skin.cyber.colorforeground3 = ConfigSelection(default="0a9a9a9", choices = stylecolor)
	config.skin.cyber.colorforeground4 = ConfigSelection(default="000ffff", choices = stylecolor)
	config.skin.cyber.colorforeground5 = ConfigSelection(default="0ffffff", choices = stylecolor)
else:
	config.skin.cyber.colorbackground1 = ConfigSelection(default="0000000", choices = stylefullcolor)
	config.skin.cyber.colorbackground2 = ConfigSelection(default="0696969", choices = stylefullcolor)
	config.skin.cyber.colorbackground3 = ConfigSelection(default="0ffffff", choices = stylefullcolor)
	config.skin.cyber.colorbackground4 = ConfigSelection(default="000ffff", choices = stylefullcolor)
	config.skin.cyber.colorbackground5 = ConfigSelection(default="0696969", choices = stylefullcolor)

	config.skin.cyber.colorforeground1 = ConfigSelection(default="0ffd700", choices = stylefullcolor)
	config.skin.cyber.colorforeground2 = ConfigSelection(default="0f5f5f5", choices = stylefullcolor)
	config.skin.cyber.colorforeground3 = ConfigSelection(default="0a9a9a9", choices = stylefullcolor)
	config.skin.cyber.colorforeground4 = ConfigSelection(default="000ffff", choices = stylefullcolor)
	config.skin.cyber.colorforeground5 = ConfigSelection(default="0ffffff", choices = stylefullcolor)

config.skin.cyber.backgroundtransparent = ConfigSelection(default="5", choices = styletransparent)
config.skin.cyber.foregroundtransparent = ConfigSelection(default="0", choices = styletransparent)

config.skin.cyber.numberchannel = ConfigSelection(default="TemplatesInfoBarTvNumberNo", choices = numberchannel)
config.skin.cyber.tunerpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvTunerDigital", choices = tunerpanelinfobar)
config.skin.cyber.epgpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoEPGNo", choices = epgpanelinfobar)
config.skin.cyber.cryptedpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoCryptedNo", choices = cryptedpanelinfobar)
config.skin.cyber.infopanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoPanelNo", choices = infopanelinfobar)
config.skin.cyber.weatherpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoWeatherNo", choices = weatherpanelinfobar)

config.skin.cyber.progressmode = ConfigSelection(default="ProgressLayerStandard", choices = progressmode)
config.skin.cyber.scrollbarmode = ConfigSelection(default="showNever", choices = scrollbarmode)

config.skin.cyber.buqetchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvBuqetNo", choices = buqetchannelselection)
config.skin.cyber.piconchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvPiconNo", choices = piconchannelselection)
config.skin.cyber.tunerpanelchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvInfoTunerNo", choices = tunerpanelchannelselection)
config.skin.cyber.epgpanelchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvInfoEPGNow", choices = epgpanelchannelselection)

config.skin.cyber.buqetradiochannelselection = ConfigSelection(default="TemplatesChannelSelectionRadioBuqetNo", choices = buqetradiochannelselection)

config.skin.cyber.panelmovieselection = ConfigSelection(default="TemplatesMovieSelectionDescriptionShort", choices = panelmovieselection)

SKIN_CYBER = """
	<!-- Setup CyberFHD -->
		<screen name="SetupCyberFHD" position="0,0" size="1920,1080" title=" " flags="wfNoBorder" backgroundColor="transparent">

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
		<eLabel text="C" position="10,205" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="Y" position="10,275" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="B" position="10,345" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="E" position="10,415" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="R" position="10,485" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="F" position="10,625" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="H" position="10,695" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="D" position="10,765" size="70,70" font="STitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<widget source="Title" render="Label" position="80,96" size="1500,44" font="STitles; 40" foregroundColor="color1" backgroundColor="#50000000" halign="left" transparent="1" />
		<widget name="config" position="90,200" size="980,635" scrollbarMode="showNever" itemHeight="35" font="SGlobal; 25" backgroundColor="#50000000" backgroundColorSelected="#50696969" transparent="1" />

	<!-- Preview Layer -->
		<eLabel position="1098,363" size="742,484" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1100,365" size="740,480" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="1110,375" size="720,460" backgroundColor="#ffffffff" zPosition="-10" />
		<eLabel position="1840,363" size="80,484" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1840,365" size="80,480" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="1840,375" size="70,460" backgroundColor="#50696969" zPosition="-10" />

		<widget name="bgcolor1a" position="1110,410" size="720,30" backgroundColor="background" zPosition="-3" />
		<widget name="bgcolor1b" position="1110,750" size="720,50" backgroundColor="background" zPosition="-3" />
		<widget name="bgcolor1c" position="1110,450" size="400,290" backgroundColor="background" zPosition="-3" />
		<widget name="bgcolor2a" position="1520,590" size="310,150" backgroundColor="background" zPosition="-3" />
		<widget name="bgcolor3a" position="1110,409" size="720,32" backgroundColor="background" zPosition="-5" />
		<widget name="bgcolor3b" position="1110,749" size="720,52" backgroundColor="background" zPosition="-5" />
		<widget name="bgcolor3c" position="1110,449" size="401,292" backgroundColor="background" zPosition="-5" />
		<widget name="bgcolor3d" position="1519,589" size="311,152" backgroundColor="background" zPosition="-5" />
		<widget name="bgcolor4a" position="1120,772" size="700,5" backgroundColor="background" zPosition="-2" />
		<widget name="bgcolor5a" position="1110,490" size="400,20" backgroundColor="background" zPosition="-2" />

		<widget name="fgcolor1a" position="1120,413" size="300,25" font="STitles; 25" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor1b" position="1120,490" size="380,20" font="SGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor2a" position="1120,460" size="380,20" font="SGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor2b" position="1120,520" size="380,20" font="SGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor2c" position="1120,751" size="700,20" font="SGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor3a" position="1120,779" size="700,20" font="SGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor3b" position="1525,595" size="300,140" font="SGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor4a" position="1520,413" size="300,25" font="SIndication; 25" halign="right" backgroundColor="background" transparent="1" />
		<widget name="fgcolor5a" position="1525,685" size="300,50" font="STitles; 40" halign="center" backgroundColor="background" transparent="1" />

	<!-- Buttons Layer -->
		<eLabel position="1368,867" size="454,146" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1370,869" size="450,142" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="1375,875" size="390,130" backgroundColor="#50696969" zPosition="-10" />
		<ePixmap pixmap="Cyber_fhd/buttons/button_key_red.png" position="1773,885" size="40,20" alphatest="on" />
		<ePixmap pixmap="Cyber_fhd/buttons/button_key_green.png" position="1773,915" size="40,20" alphatest="on" />
		<ePixmap pixmap="Cyber_fhd/buttons/button_key_yellow.png" position="1773,945" size="40,20" alphatest="on" />
		<ePixmap pixmap="Cyber_fhd/buttons/button_key_blue.png" position="1773,975" size="40,20" alphatest="on" />
		<widget source="key_red" render="Label" position="1380,884" size="380,22" font="STitles; 22" halign="right" valign="center" foregroundColor="color2" backgroundColor="#50696969" transparent="1" />
		<widget source="key_green" render="Label" position="1380,914" size="380,22" font="STitles; 22" halign="right" valign="center" foregroundColor="color2" backgroundColor="#50696969" transparent="1" />

	<!-- Clock Layer -->
		<eLabel position="1618,63" size="204,104" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1620,65" size="200,100" backgroundColor="#50696969" zPosition="-11" />
		<widget source="global.CurrentTime" render="Label" position="1615,95" size="90,50" font="SIndication; 50" foregroundColor="color1" backgroundColor="#50000000" halign="right" transparent="1">
			<convert type="ClockToText">Format:%H</convert>
		</widget>
		<eLabel text=":" position="1710,95" size="20,50" font="SIndication; 50" foregroundColor="gray" backgroundColor="#50000000" halign="center" transparent="1" zPosition="-1" />
		<widget source="global.CurrentTime" render="FixedLabel" text=":" position="1710,95" size="20,50" font="SIndication; 50" foregroundColor="color1" backgroundColor="#50000000" halign="center" transparent="1">
			<convert type="AlwaysTrue">
			</convert>
			<convert type="ConditionalShowHide">Blink</convert>
		</widget>
		<widget source="global.CurrentTime" render="Label" position="1735,95" size="90,50" font="SIndication; 50" foregroundColor="color1" backgroundColor="#50000000" halign="left" transparent="1">
			<convert type="ClockToText">Format:%M</convert>
		</widget>
		<widget source="global.CurrentTime" render="Label" position="1620,70" size="200,25" font="STitles; 20" foregroundColor="color2" backgroundColor="#50696969" halign="center" transparent="1">
			<convert type="ClockToText">Format:%A</convert>
		</widget>
		<widget source="global.CurrentTime" render="Label" position="1620,140" size="200,25" font="STitles; 22" foregroundColor="color2" backgroundColor="#50696969" halign="center" transparent="1">
			<convert type="ClockToText">Format:%d.%m.%Y</convert>
		</widget>
	</screen>"""

class SetupCyberFHD(ConfigListScreen, Screen):
	def __init__(self, session):

		Screen.__init__(self, session)
		self.session = session
		self.skin = SKIN_CYBER

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
			"blue": self.install,
			"info": self.about
		}, -1)

		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("Save"))
		self["key_yellow"] = StaticText(_("Default"))
		self["key_blue"] = StaticText(_("Install components"))
		self["Title"] = StaticText(_("Setup Cyber FHD"))

		self["bgcolor1a"] = Label(_(" "))
		self["bgcolor1b"] = Label(_(" "))
		self["bgcolor1c"] = Label(_(" "))
		self["bgcolor2a"] = Label(_(" "))
		self["bgcolor3a"] = Label(_(" "))
		self["bgcolor3b"] = Label(_(" "))
		self["bgcolor3c"] = Label(_(" "))
		self["bgcolor3d"] = Label(_(" "))
		self["bgcolor4a"] = Label(_(" "))
		self["bgcolor5a"] = Label(_(" "))

		self["fgcolor1a"] = Label(_(" "))
		self["fgcolor1b"] = Label(_(" "))
		self["fgcolor2a"] = Label(_(" "))
		self["fgcolor2b"] = Label(_(" "))
		self["fgcolor2c"] = Label(_(" "))
		self["fgcolor3a"] = Label(_(" "))
		self["fgcolor3b"] = Label(_(" "))
		self["fgcolor4a"] = Label(_(" "))
		self["fgcolor5a"] = Label(_(" "))

		self["version_sk"] = StaticText(_("Version skin:"))
		self["info_sk"] = StaticText()
		self["info_com"] = StaticText()

		self.infosk()
		self.onLayoutFinish.append(self.previewSkin)

	def list(self):
		list = []
		sep = "-"
		char = 40
		tab = " "*10
		section = _("Fonts")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Fonts:"), config.skin.cyber.fonts))
		section = _("Style")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Color setting:"), config.skin.cyber.colorsetting))

		list.append(getConfigListEntry(_("Background 1 color:"), config.skin.cyber.colorbackground1))
		list.append(getConfigListEntry(_("Background 2 color:"), config.skin.cyber.colorbackground2))
		list.append(getConfigListEntry(_("Background 3 color:"), config.skin.cyber.colorbackground3))
		list.append(getConfigListEntry(_("Progress color:"), config.skin.cyber.colorbackground4))
		list.append(getConfigListEntry(_("Cursor color:"), config.skin.cyber.colorbackground5))

		list.append(getConfigListEntry(_("Title text color:"), config.skin.cyber.colorforeground1))
		list.append(getConfigListEntry(_("Main text color:"), config.skin.cyber.colorforeground2))
		list.append(getConfigListEntry(_("Additional text color:"), config.skin.cyber.colorforeground3))
		list.append(getConfigListEntry(_("Indication text color:"), config.skin.cyber.colorforeground4))
		list.append(getConfigListEntry(_("Icon`s color:"), config.skin.cyber.colorforeground5))

		list.append(getConfigListEntry(_("Background transparent:"), config.skin.cyber.backgroundtransparent))
		list.append(getConfigListEntry(_("Text transparent:"), config.skin.cyber.foregroundtransparent))
		section = _("Infobar")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Channel number in infobar:"), config.skin.cyber.numberchannel))
		list.append(getConfigListEntry(_("Tuner panel in infobar:"), config.skin.cyber.tunerpanelinfobar))
		list.append(getConfigListEntry(_("EPG panel in secondinfobar:"), config.skin.cyber.epgpanelinfobar))
		list.append(getConfigListEntry(_("Crypted panel in secondinfobar:"), config.skin.cyber.cryptedpanelinfobar))
		list.append(getConfigListEntry(_("Info panel in secondinfobar:"), config.skin.cyber.infopanelinfobar))
		list.append(getConfigListEntry(_("Weather panel in secondinfobar:"), config.skin.cyber.weatherpanelinfobar))
		section = _("Movie Infobar")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		section = _("Menu")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Progress mode:"), config.skin.cyber.progressmode))
		list.append(getConfigListEntry(_("Scrollbar in menu:"), config.skin.cyber.scrollbarmode))
		section = _("Channel Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Buqet name in channel selection:"), config.skin.cyber.buqetchannelselection))
		list.append(getConfigListEntry(_("Picon in channel selection:"), config.skin.cyber.piconchannelselection))
		list.append(getConfigListEntry(_("Tuner panel in channel selection:"), config.skin.cyber.tunerpanelchannelselection))
		list.append(getConfigListEntry(_("EPG panel in channel selection:"), config.skin.cyber.epgpanelchannelselection))

		section = _("Radio Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Buqet name in radio channel selection:"), config.skin.cyber.buqetradiochannelselection))
		section = _("Movie Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Description panel in movie selection:"), config.skin.cyber.panelmovieselection))
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
		self.fgtext = "Skin Cyber FHD"
		self.fglogo = "Cyber FHD"
		self.bgColor1 = "#0%s" % config.skin.cyber.colorbackground1.value
		self.bgColor2 = "#0%s" % config.skin.cyber.colorbackground2.value
		self.bgColor3 = "#0%s" % config.skin.cyber.colorbackground3.value
		self.bgColor4 = "#0%s" % config.skin.cyber.colorbackground4.value
		self.bgColor5 = "#0%s" % config.skin.cyber.colorbackground5.value

		self.fgColor1 = "#0%s" % config.skin.cyber.colorforeground1.value
		self.fgColor2 = "#0%s" % config.skin.cyber.colorforeground2.value
		self.fgColor3 = "#0%s" % config.skin.cyber.colorforeground3.value
		self.fgColor4 = "#0%s" % config.skin.cyber.colorforeground4.value
		self.fgColor5 = "#0%s" % config.skin.cyber.colorforeground5.value

		try:
		# Background 1
			self["bgcolor1a"].setText(_(self.bgtext))
			self["bgcolor1a"].instance.setBackgroundColor(parseColor(self.bgColor1))
			self["bgcolor1a"].instance.setForegroundColor(parseColor(self.bgColor1))
			self["bgcolor1b"].setText(_(self.bgtext))
			self["bgcolor1b"].instance.setBackgroundColor(parseColor(self.bgColor1))
			self["bgcolor1b"].instance.setForegroundColor(parseColor(self.bgColor1))
			self["bgcolor1c"].setText(_(self.bgtext))
			self["bgcolor1c"].instance.setBackgroundColor(parseColor(self.bgColor1))
			self["bgcolor1c"].instance.setForegroundColor(parseColor(self.bgColor1))
		# Background 2
			self["bgcolor2a"].setText(_(self.bgtext))
			self["bgcolor2a"].instance.setBackgroundColor(parseColor(self.bgColor2))
			self["bgcolor2a"].instance.setForegroundColor(parseColor(self.bgColor2))
		# Background 3
			self["bgcolor3a"].setText(_(self.bgtext))
			self["bgcolor3a"].instance.setBackgroundColor(parseColor(self.bgColor3))
			self["bgcolor3a"].instance.setForegroundColor(parseColor(self.bgColor3))
			self["bgcolor3b"].setText(_(self.bgtext))
			self["bgcolor3b"].instance.setBackgroundColor(parseColor(self.bgColor3))
			self["bgcolor3b"].instance.setForegroundColor(parseColor(self.bgColor3))
			self["bgcolor3c"].setText(_(self.bgtext))
			self["bgcolor3c"].instance.setBackgroundColor(parseColor(self.bgColor3))
			self["bgcolor3c"].instance.setForegroundColor(parseColor(self.bgColor3))
			self["bgcolor3d"].setText(_(self.bgtext))
			self["bgcolor3d"].instance.setBackgroundColor(parseColor(self.bgColor3))
			self["bgcolor3d"].instance.setForegroundColor(parseColor(self.bgColor3))
		# Progress
			self["bgcolor4a"].setText(_(self.bgtext))
			self["bgcolor4a"].instance.setBackgroundColor(parseColor(self.bgColor4))
			self["bgcolor4a"].instance.setForegroundColor(parseColor(self.bgColor4))
		# Cursor
			self["bgcolor5a"].setText(_(self.bgtext))
			self["bgcolor5a"].instance.setBackgroundColor(parseColor(self.bgColor5))
			self["bgcolor5a"].instance.setForegroundColor(parseColor(self.bgColor5))
		# Title
			self["fgcolor1a"].setText(_(self.fgtext))
			self["fgcolor1a"].instance.setForegroundColor(parseColor(self.fgColor1))
			self["fgcolor1b"].setText(_(self.fgtext))
			self["fgcolor1b"].instance.setForegroundColor(parseColor(self.fgColor1))
		# Font 1
			self["fgcolor2a"].setText(_(self.fgtext))
			self["fgcolor2a"].instance.setForegroundColor(parseColor(self.fgColor2))
			self["fgcolor2b"].setText(_(self.fgtext))
			self["fgcolor2b"].instance.setForegroundColor(parseColor(self.fgColor2))
			self["fgcolor2c"].setText(_(self.fgtext))
			self["fgcolor2c"].instance.setForegroundColor(parseColor(self.fgColor2))
		# Font 2
			self["fgcolor3a"].setText(_(self.fgtext))
			self["fgcolor3a"].instance.setForegroundColor(parseColor(self.fgColor3))
			self["fgcolor3b"].setText(_(self.fgtext))
			self["fgcolor3b"].instance.setForegroundColor(parseColor(self.fgColor3))
		# Indication
			self["fgcolor4a"].setText(_(self.fgtext))
			self["fgcolor4a"].instance.setForegroundColor(parseColor(self.fgColor4))
		# Icon
			self["fgcolor5a"].setText(_(self.fglogo))
			self["fgcolor5a"].instance.setForegroundColor(parseColor(self.fgColor5))
		except:
			pass

	def infosk(self):
		package = 0
		global status
		if fileExists("/usr/lib/opkg/status"):
			status = "/usr/lib/opkg/status"
		elif fileExists("/var/lib/opkg/status"):
			status = "/var/lib/opkg/status"
		elif fileExists("/var/opkg/status"):
			status = "/var/opkg/status"
		for line in open(status):
			if line.find("cyber-hd") > -1:
				package = 1
			if line.find("Version:") > -1 and package == 1:
				package = 0
				try:
					self["info_sk"].text = line.split()[1]
				except:
					self["info_sk"].text = " "
				break

	def createSkin(self):
		skinpath = "/usr/share/enigma2/Cyber_fhd/"

		try:
	# default skin
			os.system("cp %sskin_default.xml %sskin.xml" % (skinpath, skinpath))
			os.system("cp %sskin_templates_default.xml %sskin_templates.xml" % (skinpath, skinpath))
	# color`s
			os.system("sed -i 's/#50000000/#%s%s/w' %sskin.xml" % (config.skin.cyber.backgroundtransparent.value, config.skin.cyber.colorbackground1.value, skinpath))
			os.system("sed -i 's/#50696969/#%s%s/w' %sskin.xml" % (config.skin.cyber.backgroundtransparent.value, config.skin.cyber.colorbackground2.value, skinpath))
			os.system("sed -i 's/#50ffffff/#%s%s/w' %sskin.xml" % (config.skin.cyber.backgroundtransparent.value, config.skin.cyber.colorbackground3.value, skinpath))
			os.system("sed -i 's/#5000ffff/#%s%s/w' %sskin.xml" % (config.skin.cyber.foregroundtransparent.value, config.skin.cyber.colorbackground4.value, skinpath))
			os.system("sed -i 's/#60696969/#%s%s/w' %sskin.xml" % (config.skin.cyber.backgroundtransparent.value, config.skin.cyber.colorbackground5.value, skinpath))
			os.system("sed -i 's/#10ffd700/#%s%s/w' %sskin.xml" % (config.skin.cyber.foregroundtransparent.value, config.skin.cyber.colorforeground1.value, skinpath))
			os.system("sed -i 's/#10f5f5f5/#%s%s/w' %sskin.xml" % (config.skin.cyber.foregroundtransparent.value, config.skin.cyber.colorforeground2.value, skinpath))
			os.system("sed -i 's/#10a9a9a9/#%s%s/w' %sskin.xml" % (config.skin.cyber.foregroundtransparent.value, config.skin.cyber.colorforeground3.value, skinpath))
			os.system("sed -i 's/#1000ffff/#%s%s/w' %sskin.xml" % (config.skin.cyber.foregroundtransparent.value, config.skin.cyber.colorforeground4.value, skinpath))
			os.system("sed -i 's/#10ffffff/#%s%s/w' %sskin.xml" % (config.skin.cyber.backgroundtransparent.value, config.skin.cyber.colorforeground5.value, skinpath))
	# fonts	
			os.system("sed -i 's/Roboto-Regular/%s/w' %sskin.xml" % (config.skin.cyber.fonts.value, skinpath))
	# scrollbar
			os.system("sed -i 's/showNever/%s/w' %sskin.xml" % (config.skin.cyber.scrollbarmode.value, skinpath))
	# number channel
			os.system("sed -i 's/%s/TemplatesInfoBarTvNumber/w' %sskin_templates.xml" % (config.skin.cyber.numberchannel.value, skinpath))
	# tuner panel
			os.system("sed -i 's/%s/TemplatesInfoBarTvTuner/w' %sskin_templates.xml" % (config.skin.cyber.tunerpanelinfobar.value, skinpath))
	# epg panel
			os.system("sed -i 's/%s/TemplatesInfoBarTvInfoEPG/w' %sskin_templates.xml" % (config.skin.cyber.epgpanelinfobar.value, skinpath))
	# crypted panel
			os.system("sed -i 's/%s/TemplatesInfoBarTvInfoCrypted/w' %sskin_templates.xml" % (config.skin.cyber.cryptedpanelinfobar.value, skinpath))
	# info panel
			os.system("sed -i 's/%s/TemplatesInfoBarTvInfoPanel/w' %sskin_templates.xml" % (config.skin.cyber.infopanelinfobar.value, skinpath))
	# weather panel
			os.system("sed -i 's/%s/TemplatesInfoBarTvInfoWeather/w' %sskin_templates.xml" % (config.skin.cyber.weatherpanelinfobar.value, skinpath))
	# progress
			os.system("sed -i 's/%s/ProgressLayer/w' %sskin_templates.xml" % (config.skin.cyber.progressmode.value, skinpath))
	# buqet
			os.system("sed -i 's/%s/TemplatesChannelSelectionTvBuqet/w' %sskin_templates.xml" % (config.skin.cyber.buqetchannelselection.value, skinpath))
			os.system("sed -i 's/%sFull/TemplatesChannelSelectionTvBuqetFull/w' %sskin_templates.xml" % (config.skin.cyber.buqetchannelselection.value, skinpath))
	# picon panel
			os.system("sed -i 's/%s/TemplatesChannelSelectionTvPicon/w' %sskin_templates.xml" % (config.skin.cyber.piconchannelselection.value, skinpath))
	# tuner panel
			os.system("sed -i 's/%s/TemplatesChannelSelectionTvInfoEPG/w' %sskin_templates.xml" % (config.skin.cyber.tunerpanelchannelselection.value, skinpath))
	# epg panel
			os.system("sed -i 's/%s/TemplatesChannelSelectionTvInfoTuner/w' %sskin_templates.xml" % (config.skin.cyber.epgpanelchannelselection.value, skinpath))
	# buqet
			os.system("sed -i 's/%s/TemplatesChannelSelectionRadioBuqet/w' %sskin_templates.xml" % (config.skin.cyber.buqetradiochannelselection.value, skinpath))
	# description panel
			os.system("sed -i 's/%s/TemplatesMovieSelectionDescription/w' %sskin_templates.xml" % (config.skin.cyber.panelmovieselection.value, skinpath))
	# end
		except:
			self.session.open(MessageBox, _("Error by processing !!!"), MessageBox.TYPE_ERROR)
			os.system("cp %sskin_default.xml %sskin.xml" % (skinpath, skinpath))
			os.system("cp %sskin_templates_default.xml %sskin_templates.xml" % (skinpath, skinpath))
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def install(self):
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/"
		componentspath = "/usr/lib/enigma2/python/Components/"

		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def setDefault(self, configItem):
		configItem.setValue(configItem.default)

	def save(self):
		for x in self["config"].list:
			if len(x) > 1:
				x[1].save()
		self.createSkin()

	def default(self):
		for x in self["config"].list:
			if len(x) > 1:
				self.setDefault(x[1])
				x[1].save()
		self.createSkin()

	def exit(self):
		for x in self["config"].list:
			if len(x) > 1:
				x[1].cancel()
		self.close()

	def restart(self, answer):
		if answer is True:
			self.session.open(TryQuitMainloop, 3)

	def about(self):
		self.session.open(MessageBox, _("Skin CyberFHD\nDeveloper: Sirius0103 \nHomepage: www.gisclub.tv \n\nDonate:\nWMZ  Z395874509364\nWME  E284580190260\nWMR  R213063691482\nWMU  U658742613505"), MessageBox.TYPE_INFO)

def main(session, **kwargs):
	session.open(SetupCyberFHD)

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Setup CyberFHD"),
	description=_("Setup skin CyberFHD"),
	where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU],
	icon="plugin.png",
	fnc=main)
