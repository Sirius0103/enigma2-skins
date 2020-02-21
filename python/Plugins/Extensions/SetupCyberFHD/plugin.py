# -*- coding: UTF-8 -*-

# Plugin - Setup CyberFHD
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

import urllib
import os, gettext
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
from urllib import urlretrieve
from os import system, environ
from enigma import addFont

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("SetupCyberFHD", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/SetupCyberFHD/locale"))

addFont("/usr/share/enigma2/CyberFHD/fonts/Neuropol.ttf", "SkinTitles", 100, 1)
addFont("/usr/share/enigma2/CyberFHD/fonts/LedCounter.ttf", "SkinIndication", 100, 1)
addFont("/usr/share/enigma2/CyberFHD/fonts/Roboto-Regular.ttf", "SkinGlobal", 100, 1)

def _(txt):
	t = gettext.dgettext("SetupCyberFHD", txt)
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

fonts = [
	("Roboto-Regular", _("Regular")),
	("Roboto-Medium", _("Medium")),
	("Roboto-Bold", _("Bold")),
	("Roboto-Italic", _("Italic")),
	("Roboto-MediumItalic", _("MediumItalic")),
	("Roboto-BoldItalic", _("BoldItalic"))]

cornerbackground2 = [
	("CornerBackground2Standard", _("Standard")),
	("CornerBackground2Improved", _("Improved"))]

cornerbackground3 = [
	("CornerBackground3Standard", _("Standard")),
	("CornerBackground3Improved", _("Improved"))]

progressmode = [
	("ProgressLayerStandard", _("Standard")),
	("ProgressLayerImproved", _("Improved"))]

scrollbarmode = [
	("showNever", _("No")),
	("showOnDemand", _("Yes"))]

epgpanelinfobar = [
	("TemplatesInfoBarTvInfoEPGDefault", _("No")),
	("TemplatesInfoBarTvInfoEPGNow", _("Now")),
	("TemplatesInfoBarTvInfoEPGNxt", _("Now, Next"))]

bouquetchannelselection = [
	("TemplatesChannelSelectionTvBouquetDefault", _("No")),
	("TemplatesChannelSelectionTvBouquetStyle", _("Yes"))]

bouquetradiochannelselection = [
	("TemplatesChannelSelectionRadioBouquetDefault", _("No")),
	("TemplatesChannelSelectionRadioBouquetStyle", _("Yes"))]

if not fileExists("/usr/lib/enigma2/python/Components/Converter/CaidInfo2.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Converter/CamdInfo3.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Converter/EventName2.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Converter/FrontendInfo2.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Converter/ModuleControl.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceName2.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceInfoEX.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/Watches.py"):
	numberchannel = [
		("TemplatesInfoBarTvNumberDefault", _("No"))]
	tunerpanelinfobar = [
		("TemplatesInfoBarTvTunerStyle", _("Yes")),
		("TemplatesInfoBarTvTunerDigital", _("Digital"))]
	cryptedpanelinfobar = [
		("TemplatesInfoBarTvInfoCryptedDefault", _("No"))]
	infopanelinfobar = [
		("TemplatesInfoBarTvInfoPanelDefault", _("No"))]
	cipanelinfobar = [
		("TemplatesInfoBarTvInfoPanelCIDefault", _("No"))]
	piconchannelselection = [
		("TemplatesChannelSelectionTvPiconDefault", _("No"))]
	channelpanelchannelselection = [
		("TemplatesChannelSelectionTvInfoChannelDefault", _("No"))]
	epgpanelchannelselection = [
		("TemplatesChannelSelectionTvInfoEPGDefault", _("No")),
		("TemplatesChannelSelectionTvInfoEPGNow", _("Now"))]
else:
	numberchannel = [
		("TemplatesInfoBarTvNumberDefault", _("No")),
		("TemplatesInfoBarTvNumberStyle", _("Yes"))]
	tunerpanelinfobar = [
		("TemplatesInfoBarTvTunerDefault", _("No")),
		("TemplatesInfoBarTvTunerStyle", _("Yes")),
		("TemplatesInfoBarTvTunerDigital", _("Digital")),
		("TemplatesInfoBarTvTunerAnalog", _("Analog"))]
	cryptedpanelinfobar = [
		("TemplatesInfoBarTvInfoCryptedDefault", _("No")),
		("TemplatesInfoBarTvInfoCryptedStyle", _("Style")),
		("TemplatesInfoBarTvInfoCryptedImproved", _("Improved"))]
	infopanelinfobar = [
		("TemplatesInfoBarTvInfoPanelDefault", _("No")),
		("TemplatesInfoBarTvInfoPanelNIM", _("NIM")),
		("TemplatesInfoBarTvInfoPanelECM", _("ECM")),
		("TemplatesInfoBarTvInfoPanelPID", _("PID"))]
	cipanelinfobar = [
		("TemplatesInfoBarTvInfoPanelCIDefault", _("No")),
		("TemplatesInfoBarTvInfoPanelCIStyle", _("Yes"))]
	piconchannelselection = [
		("TemplatesChannelSelectionTvPiconDefault", _("No")),
		("TemplatesChannelSelectionTvPiconStyle", _("Yes"))]
	channelpanelchannelselection = [
		("TemplatesChannelSelectionTvInfoChannelDefault", _("No")),
		("TemplatesChannelSelectionTvInfoChannelStyle", _("Yes"))]
	epgpanelchannelselection = [
		("TemplatesChannelSelectionTvInfoEPGDefault", _("No")),
		("TemplatesChannelSelectionTvInfoEPGNow", _("Now")),
		("TemplatesChannelSelectionTvInfoEPGNxt", _("Now, Next")),
		("TemplatesChannelSelectionTvInfoEPGNowPrograms", _("Now, 5 Programs")),
		("TemplatesChannelSelectionTvInfoEPGPrograms", _("10 Programs"))]

if not fileExists("/usr/lib/enigma2/python/Components/Converter/MSNWeather2.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/AnimatedWeatherPixmap.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/AnimatedMoonPixmap.py"):
	weatherpanelinfobar = [
		("TemplatesInfoBarTvInfoWeatherDefault", _("No"))]
	weatherpanelmovieinfobar = [
		("TemplatesInfoBarMediaInfoWeatherDefault", _("No"))]
else:
	weatherpanelinfobar = [
		("TemplatesInfoBarTvInfoWeatherDefault", _("No")),
		("TemplatesInfoBarTvInfoWeatherMSN", _("MSN")),
		("TemplatesInfoBarTvInfoWeatherMSNAnimated", _("Animated MSN")),
		("TemplatesInfoBarTvInfoWeatherMSNMoon", _("MSN & Moon")),
		("TemplatesInfoBarTvInfoWeatherMSNAnimatedMoon", _("Animated MSN & Moon"))]
	weatherpanelmovieinfobar = [
		("TemplatesInfoBarMediaInfoWeatherDefault", _("No")),
		("TemplatesInfoBarMediaInfoWeatherMSN", _("MSN")),
		("TemplatesInfoBarMediaInfoWeatherMSNAnimated", _("Animated MSN")),
		("TemplatesInfoBarMediaInfoWeatherMSNMoon", _("MSN & Moon")),
		("TemplatesInfoBarMediaInfoWeatherMSNAnimatedMoon", _("Animated MSN & Moon"))]

if not fileExists("/usr/lib/enigma2/python/Components/Converter/MovieInfo2.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/MovieCover.py")\
	or not fileExists("/usr/lib/enigma2/python/Components/Renderer/MovieRating.py"):
	covermovieinfobar = [
		("TemplatesInfoBarMediaCoverDefault", _("No"))]
	infopanelmovieinfobar = [
		("TemplatesInfoBarMediaInfoPanelDefault", _("No"))]
	panelmovieselection = [
		("TemplatesMovieSelectionDescriptionDefault", _("No")),
		("TemplatesMovieSelectionDescriptionShort", _("Short Description")),
		("TemplatesMovieSelectionDescriptionMeta", _("Meta Description"))]
else:
	covermovieinfobar = [
		("TemplatesInfoBarMediaCoverDefault", _("No")),
		("TemplatesInfoBarMediaCoverStyle", _("Yes"))]
	infopanelmovieinfobar = [
		("TemplatesInfoBarMediaInfoPanelDefault", _("No")),
		("TemplatesInfoBarMediaInfoPanelStyle", _("Description"))]
	panelmovieselection = [
		("TemplatesMovieSelectionDescriptionDefault", _("No")),
		("TemplatesMovieSelectionDescriptionShort", _("Short Description")),
		("TemplatesMovieSelectionDescriptionMeta", _("Meta Description")),
		("TemplatesMovieSelectionDescriptionFull", _("Full Description")),
		("TemplatesMovieSelectionDescriptionMovie", _("Movie Description"))]

config.skin.cyberfhd = ConfigSubsection()
config.skin.cyberfhd.fonts = ConfigSelection(default="Roboto-Regular", choices = fonts)

config.skin.cyberfhd.colorsetting = ConfigSelection(default="0", choices = colorsetting)

if config.skin.cyberfhd.colorsetting.value == "0":
	config.skin.cyberfhd.colorbackground1 = ConfigSelection(default="0000000", choices = stylecolor)
	config.skin.cyberfhd.colorbackground2 = ConfigSelection(default="0696969", choices = stylecolor)
	config.skin.cyberfhd.colorbackground3 = ConfigSelection(default="0ffffff", choices = stylecolor)
	config.skin.cyberfhd.colorbackground4 = ConfigSelection(default="000ffff", choices = stylecolor)
	config.skin.cyberfhd.colorbackground5 = ConfigSelection(default="0696969", choices = stylecolor)

	config.skin.cyberfhd.colorforeground1 = ConfigSelection(default="0ffd700", choices = stylecolor)
	config.skin.cyberfhd.colorforeground2 = ConfigSelection(default="0f5f5f5", choices = stylecolor)
	config.skin.cyberfhd.colorforeground3 = ConfigSelection(default="0a9a9a9", choices = stylecolor)
	config.skin.cyberfhd.colorforeground4 = ConfigSelection(default="000ffff", choices = stylecolor)
	config.skin.cyberfhd.colorforeground5 = ConfigSelection(default="0ffffff", choices = stylecolor)
else:
	config.skin.cyberfhd.colorbackground1 = ConfigSelection(default="0000000", choices = stylefullcolor)
	config.skin.cyberfhd.colorbackground2 = ConfigSelection(default="0696969", choices = stylefullcolor)
	config.skin.cyberfhd.colorbackground3 = ConfigSelection(default="0ffffff", choices = stylefullcolor)
	config.skin.cyberfhd.colorbackground4 = ConfigSelection(default="000ffff", choices = stylefullcolor)
	config.skin.cyberfhd.colorbackground5 = ConfigSelection(default="0696969", choices = stylefullcolor)

	config.skin.cyberfhd.colorforeground1 = ConfigSelection(default="0ffd700", choices = stylefullcolor)
	config.skin.cyberfhd.colorforeground2 = ConfigSelection(default="0f5f5f5", choices = stylefullcolor)
	config.skin.cyberfhd.colorforeground3 = ConfigSelection(default="0a9a9a9", choices = stylefullcolor)
	config.skin.cyberfhd.colorforeground4 = ConfigSelection(default="000ffff", choices = stylefullcolor)
	config.skin.cyberfhd.colorforeground5 = ConfigSelection(default="0ffffff", choices = stylefullcolor)

config.skin.cyberfhd.cornerbackground2 = ConfigSelection(default="CornerBackground2Standard", choices = cornerbackground2)
config.skin.cyberfhd.cornerbackground3 = ConfigSelection(default="CornerBackground3Standard", choices = cornerbackground3)

config.skin.cyberfhd.backgroundtransparent = ConfigSelection(default="5", choices = styletransparent)
config.skin.cyberfhd.foregroundtransparent = ConfigSelection(default="0", choices = styletransparent)

config.skin.cyberfhd.numberchannel = ConfigSelection(default="TemplatesInfoBarTvNumberDefault", choices = numberchannel)
config.skin.cyberfhd.tunerpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvTunerStyle", choices = tunerpanelinfobar)
config.skin.cyberfhd.epgpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoEPGDefault", choices = epgpanelinfobar)
config.skin.cyberfhd.cryptedpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoCryptedDefault", choices = cryptedpanelinfobar)
config.skin.cyberfhd.infopanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoPanelDefault", choices = infopanelinfobar)
config.skin.cyberfhd.cipanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoPanelCIDefault", choices = cipanelinfobar)
config.skin.cyberfhd.weatherpanelinfobar = ConfigSelection(default="TemplatesInfoBarTvInfoWeatherDefault", choices = weatherpanelinfobar)

config.skin.cyberfhd.covermovieinfobar = ConfigSelection(default="TemplatesInfoBarMediaCoverDefault", choices = covermovieinfobar)
config.skin.cyberfhd.infopanelmovieinfobar = ConfigSelection(default="TemplatesInfoBarMediaInfoPanelDefault", choices = infopanelmovieinfobar)
config.skin.cyberfhd.weatherpanelmovieinfobar = ConfigSelection(default="TemplatesInfoBarMediaInfoWeatherDefault", choices = weatherpanelmovieinfobar)

config.skin.cyberfhd.progressmode = ConfigSelection(default="ProgressLayerStandard", choices = progressmode)
config.skin.cyberfhd.scrollbarmode = ConfigSelection(default="showNever", choices = scrollbarmode)

config.skin.cyberfhd.bouquetchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvBouquetDefault", choices = bouquetchannelselection)
config.skin.cyberfhd.piconchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvPiconDefault", choices = piconchannelselection)
config.skin.cyberfhd.channelpanelchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvInfoChannelDefault", choices = channelpanelchannelselection)
config.skin.cyberfhd.epgpanelchannelselection = ConfigSelection(default="TemplatesChannelSelectionTvInfoEPGNow", choices = epgpanelchannelselection)

config.skin.cyberfhd.bouquetradiochannelselection = ConfigSelection(default="TemplatesChannelSelectionRadioBouquetDefault", choices = bouquetradiochannelselection)

config.skin.cyberfhd.panelmovieselection = ConfigSelection(default="TemplatesMovieSelectionDescriptionShort", choices = panelmovieselection)

SKIN_CYBERFHD = """
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
		<eLabel text="C" position="10,205" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="Y" position="10,275" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="B" position="10,345" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="E" position="10,415" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="R" position="10,485" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="F" position="10,625" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
		<eLabel text="H" position="10,695" size="70,70" font="SkinTitles; 70" foregroundColor="color5" backgroundColor="#50696969" halign="center" valign="center" transparent="1" zPosition="-9" />
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

		<widget name="fgcolor1a" position="1120,413" size="300,25" font="SkinTitles; 25" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor1b" position="1120,490" size="380,20" font="SkinGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor2a" position="1120,460" size="380,20" font="SkinGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor2b" position="1120,520" size="380,20" font="SkinGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor2c" position="1120,751" size="700,20" font="SkinGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor3a" position="1120,779" size="700,20" font="SkinGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor3b" position="1525,595" size="300,140" font="SkinGlobal; 15" halign="left" backgroundColor="background" transparent="1" />
		<widget name="fgcolor4a" position="1520,413" size="300,25" font="SkinIndication; 25" halign="right" backgroundColor="background" transparent="1" />
		<widget name="fgcolor5a" position="1525,685" size="300,50" font="SkinTitles; 40" halign="center" backgroundColor="background" transparent="1" />

	<!-- Buttons Layer -->
		<eLabel position="1368,867" size="454,146" backgroundColor="#50ffffff" zPosition="-12" />
		<eLabel position="1370,869" size="450,142" backgroundColor="#50000000" zPosition="-11" />
		<eLabel position="1375,875" size="390,130" backgroundColor="#50696969" zPosition="-10" />
		<ePixmap pixmap="CyberFHD/buttons/button_key_red.png" position="1773,885" size="40,20" alphatest="on" />
		<ePixmap pixmap="CyberFHD/buttons/button_key_green.png" position="1773,915" size="40,20" alphatest="on" />
		<ePixmap pixmap="CyberFHD/buttons/button_key_yellow.png" position="1773,945" size="40,20" alphatest="on" />
		<ePixmap pixmap="CyberFHD/buttons/button_key_blue.png" position="1773,975" size="40,20" alphatest="on" />
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

class SetupCyberFHD(ConfigListScreen, Screen):
	def __init__(self, session):

		Screen.__init__(self, session)
		self.session = session
		self.skin = SKIN_CYBERFHD

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
		self["key_blue"] = StaticText(_("Update CyberFHD"))
		self["Title"] = StaticText(_("Setup CyberFHD"))

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

		self["info_sk"] = Label(_(" "))
		self["info_com"] = Label(_(" "))

		self.onLayoutFinish.append(self.previewSkin)

	def list(self):
		list = []
		sep = "-"
		char = 40
		tab = " "*10
		section = _("Fonts")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Fonts:"), config.skin.cyberfhd.fonts))
		section = _("Style")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Color setting:"), config.skin.cyberfhd.colorsetting))

		list.append(getConfigListEntry(_("Background 1 color:"), config.skin.cyberfhd.colorbackground1))
		list.append(getConfigListEntry(_("Background 2 color:"), config.skin.cyberfhd.colorbackground2))
		list.append(getConfigListEntry(_("Background 3 color:"), config.skin.cyberfhd.colorbackground3))

		list.append(getConfigListEntry(_("Background 2 corner:"), config.skin.cyberfhd.cornerbackground2))
		list.append(getConfigListEntry(_("Background 3 corner:"), config.skin.cyberfhd.cornerbackground3))

		list.append(getConfigListEntry(_("Progress color:"), config.skin.cyberfhd.colorbackground4))
		list.append(getConfigListEntry(_("Cursor color:"), config.skin.cyberfhd.colorbackground5))

		list.append(getConfigListEntry(_("Title text color:"), config.skin.cyberfhd.colorforeground1))
		list.append(getConfigListEntry(_("Main text color:"), config.skin.cyberfhd.colorforeground2))
		list.append(getConfigListEntry(_("Additional text color:"), config.skin.cyberfhd.colorforeground3))
		list.append(getConfigListEntry(_("Indication text color:"), config.skin.cyberfhd.colorforeground4))
		list.append(getConfigListEntry(_("Icon`s color:"), config.skin.cyberfhd.colorforeground5))

		list.append(getConfigListEntry(_("Background transparent:"), config.skin.cyberfhd.backgroundtransparent))
		list.append(getConfigListEntry(_("Text transparent:"), config.skin.cyberfhd.foregroundtransparent))
		section = _("Infobar")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Channel number in infobar:"), config.skin.cyberfhd.numberchannel))
		list.append(getConfigListEntry(_("Tuner panel in infobar:"), config.skin.cyberfhd.tunerpanelinfobar))
		list.append(getConfigListEntry(_("EPG panel in secondinfobar:"), config.skin.cyberfhd.epgpanelinfobar))
		list.append(getConfigListEntry(_("Crypted panel in secondinfobar:"), config.skin.cyberfhd.cryptedpanelinfobar))
		list.append(getConfigListEntry(_("Info panel in secondinfobar:"), config.skin.cyberfhd.infopanelinfobar))
		list.append(getConfigListEntry(_("Show CI in info panel:"), config.skin.cyberfhd.cipanelinfobar))
		list.append(getConfigListEntry(_("Weather panel in secondinfobar:"), config.skin.cyberfhd.weatherpanelinfobar))
		section = _("Movie Infobar")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Poster in movieinfobar:"), config.skin.cyberfhd.covermovieinfobar))
		list.append(getConfigListEntry(_("Info panel in movieinfobar:"), config.skin.cyberfhd.infopanelmovieinfobar))
		list.append(getConfigListEntry(_("Weather panel in movieinfobar:"), config.skin.cyberfhd.weatherpanelmovieinfobar))
		section = _("Menu")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Progress mode:"), config.skin.cyberfhd.progressmode))
		list.append(getConfigListEntry(_("Scrollbar in menu:"), config.skin.cyberfhd.scrollbarmode))
		section = _("Channel Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Userbouquet name in channel selection:"), config.skin.cyberfhd.bouquetchannelselection))
		list.append(getConfigListEntry(_("Picon panel in channel selection:"), config.skin.cyberfhd.piconchannelselection))
		list.append(getConfigListEntry(_("Channel info panel in channel selection:"), config.skin.cyberfhd.channelpanelchannelselection))
		list.append(getConfigListEntry(_("EPG panel in channel selection:"), config.skin.cyberfhd.epgpanelchannelselection))

		section = _("Radio Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Userbouquet name in radio channel selection:"), config.skin.cyberfhd.bouquetradiochannelselection))
		section = _("Movie Selection")
		list.append(getConfigListEntry(sep*(char-(len(section))/2) + tab + section + tab + sep*(char-(len(section))/2)))
		list.append(getConfigListEntry(_("Description panel in movie selection:"), config.skin.cyberfhd.panelmovieselection))
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
		self.fgtext = "Skin CyberFHD"
		self.fglogo = "CyberFHD"
		self.bgColor1 = "#0%s" % config.skin.cyberfhd.colorbackground1.value
		self.bgColor2 = "#0%s" % config.skin.cyberfhd.colorbackground2.value
		self.bgColor3 = "#0%s" % config.skin.cyberfhd.colorbackground3.value
		self.bgColor4 = "#0%s" % config.skin.cyberfhd.colorbackground4.value
		self.bgColor5 = "#0%s" % config.skin.cyberfhd.colorbackground5.value

		self.fgColor1 = "#0%s" % config.skin.cyberfhd.colorforeground1.value
		self.fgColor2 = "#0%s" % config.skin.cyberfhd.colorforeground2.value
		self.fgColor3 = "#0%s" % config.skin.cyberfhd.colorforeground3.value
		self.fgColor4 = "#0%s" % config.skin.cyberfhd.colorforeground4.value
		self.fgColor5 = "#0%s" % config.skin.cyberfhd.colorforeground5.value

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

		self.version()
		self.infosk()

	def version(self):
		urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberFHD/version","/tmp/version")
		self.infocom()

	def infocom(self):
		version = ""
		if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/WeatherMSN/plugin.pyo")\
			and not fileExists("/usr/lib/enigma2/python/Components/Converter/MSNWeather2.py"):
			self["info_com"] = Label(_("No install components skin !!! \nPress blue button to install !!!"))
		elif not fileExists("/usr/lib/enigma2/python/Components/Converter/AlwaysTrue.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/AC3DownMixStatus.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/CaidInfo2.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/CamdInfo3.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/EventName2.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/FrontendInfo2.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/ModuleControl.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/MovieInfo2.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/ProgressDiskSpaceInfo.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceInfoEX.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceName2.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Converter/TunerBar.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/AnimatedWeatherPixmap.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/AnimatedMoonPixmap.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/MovieCover.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/MovieRating.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/RendVolumeTextP.py")\
			or not fileExists("/usr/lib/enigma2/python/Components/Renderer/Watches.py"):
			self["info_com"] = Label(_("No install components skin !!! \nPress blue button to install !!!"))
		else:
			for text in open("/tmp/version").readlines()[3]:
				version += text
			self["info_com"].setText(version)
			return version

	def infosk(self):
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/"
		version = ""
		try:
			for text in open("%sSetupCyberFHD/version" % (pluginpath)).readlines()[1]:
				version += text
			self["info_sk"].setText(version)
			return version
		except:
			return ""

	def createSkin(self):
		try:
	# user skin
			skin_user = skin_templates_user = []
	# color`s
			skin_user.append(["#50000000", "#" + config.skin.cyberfhd.backgroundtransparent.value + config.skin.cyberfhd.colorbackground1.value])
			skin_user.append(["#50696969", "#" + config.skin.cyberfhd.backgroundtransparent.value + config.skin.cyberfhd.colorbackground2.value])
			skin_user.append(["#50ffffff", "#" + config.skin.cyberfhd.backgroundtransparent.value + config.skin.cyberfhd.colorbackground3.value])
			skin_user.append(["#5000ffff", "#" + config.skin.cyberfhd.foregroundtransparent.value + config.skin.cyberfhd.colorbackground4.value])
			skin_user.append(["#60696969", "#" + config.skin.cyberfhd.backgroundtransparent.value + config.skin.cyberfhd.colorbackground5.value])
			skin_user.append(["#10ffd700", "#" + config.skin.cyberfhd.foregroundtransparent.value + config.skin.cyberfhd.colorforeground1.value])
			skin_user.append(["#10f5f5f5", "#" + config.skin.cyberfhd.foregroundtransparent.value + config.skin.cyberfhd.colorforeground2.value])
			skin_user.append(["#10a9a9a9", "#" + config.skin.cyberfhd.foregroundtransparent.value + config.skin.cyberfhd.colorforeground3.value])
			skin_user.append(["#1000ffff", "#" + config.skin.cyberfhd.foregroundtransparent.value + config.skin.cyberfhd.colorforeground4.value])
			skin_user.append(["#10ffffff", "#" + config.skin.cyberfhd.backgroundtransparent.value + config.skin.cyberfhd.colorforeground5.value])
	# clock
			if not fileExists("/usr/lib/enigma2/python/Components/Converter/AlwaysTrue.py"):
				skin_templates_user.append(["TemplatesClockDefault","TemplatesClock"])
			else:
				skin_templates_user.append(["TemplatesClockStyle","TemplatesClock"])
	# indication
			if not fileExists("/usr/lib/enigma2/python/Components/Converter/AC3DownMixStatus.py")\
				or not fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceInfoEX.py"):
				skin_templates_user.append(["TemplatesInfoBarTvIndicationDefault","TemplatesInfoBarTvIndication"])
				skin_templates_user.append(["TemplatesInfoBarMediaIndicationDefault","TemplatesInfoBarMediaIndication"])
				skin_templates_user.append(["TemplatesInfoBarRadioIndicationDefault","TemplatesInfoBarRadioIndication"])
			else:
				skin_templates_user.append(["TemplatesInfoBarTvIndicationStyle","TemplatesInfoBarTvIndication"])
				skin_templates_user.append(["TemplatesInfoBarMediaIndicationStyle","TemplatesInfoBarMediaIndication"])
				skin_templates_user.append(["TemplatesInfoBarRadioIndicationStyle","TemplatesInfoBarRadioIndication"])
	# fonts
			skin_user.append(["Roboto-Regular", config.skin.cyberfhd.fonts.value])
	# corner
			skin_templates_user.append([config.skin.cyberfhd.cornerbackground2.value, "CornerBackground2"])
			skin_templates_user.append([config.skin.cyberfhd.cornerbackground3.value, "CornerBackground3"])
	# scrollbar
			skin_user.append(["showNever", config.skin.cyberfhd.scrollbarmode.value])
	# number channel
			skin_templates_user.append([config.skin.cyberfhd.numberchannel.value, "TemplatesInfoBarTvNumber"])
	# tuner panel
			skin_templates_user.append([config.skin.cyberfhd.tunerpanelinfobar.value, "TemplatesInfoBarTvTuner"])
	# epg panel
			skin_templates_user.append([config.skin.cyberfhd.epgpanelinfobar.value, "TemplatesInfoBarTvInfoEPG"])
	# crypted panel
			skin_templates_user.append([config.skin.cyberfhd.cryptedpanelinfobar.value, "TemplatesInfoBarTvInfoCrypted"])
	# info panel
			skin_templates_user.append([config.skin.cyberfhd.infopanelinfobar.value, "TemplatesInfoBarTvInfoPanel"])
	# ci panel
			skin_templates_user.append([config.skin.cyberfhd.cipanelinfobar.value, "TemplatesInfoBarTvInfoPanelCI"])
	# weather panel
			skin_templates_user.append([config.skin.cyberfhd.weatherpanelinfobar.value, "TemplatesInfoBarTvInfoWeather"])
			skin_templates_user.append([config.skin.cyberfhd.weatherpanelmovieinfobar.value, "TemplatesInfoBarMediaInfoWeather"])
	# cover panel
			skin_templates_user.append([config.skin.cyberfhd.covermovieinfobar.value, "TemplatesInfoBarMediaCover"])
	# info panel
			skin_templates_user.append([config.skin.cyberfhd.infopanelmovieinfobar.value, "TemplatesInfoBarMediaInfoPanel"])
	# progress
			skin_templates_user.append([config.skin.cyberfhd.progressmode.value, "ProgressLayer"])
	# bouquet
			skin_templates_user.append([config.skin.cyberfhd.bouquetchannelselection.value, "TemplatesChannelSelectionTvBouquet"])
			skin_templates_user.append([config.skin.cyberfhd.bouquetchannelselection.value +"Full", "TemplatesChannelSelectionTvBouquetFull"])
	# picon panel
			skin_templates_user.append([config.skin.cyberfhd.piconchannelselection.value, "TemplatesChannelSelectionTvPicon"])
	# epg panel
			skin_templates_user.append([config.skin.cyberfhd.epgpanelchannelselection.value, "TemplatesChannelSelectionTvInfoEPG"])
	# channel panel
			skin_templates_user.append([config.skin.cyberfhd.channelpanelchannelselection.value, "TemplatesChannelSelectionTvInfoChannel"])
	# bouquet
			skin_templates_user.append([config.skin.cyberfhd.bouquetradiochannelselection.value, "TemplatesChannelSelectionRadioBouquet"])
	# description panel
			skin_templates_user.append([config.skin.cyberfhd.panelmovieselection.value, "TemplatesMovieSelectionDescription"])

			SearchReplaceWrite(skin_user, "/usr/share/enigma2/CyberFHD/skin_style.xml", "/usr/share/enigma2/CyberFHD/skin.xml")
			SearchReplaceWrite(skin_templates_user, "/usr/share/enigma2/CyberFHD/skin_templates_style.xml", "/usr/share/enigma2/CyberFHD/skin_templates.xml")
		except:
			self.default()
	# end
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def install(self):
		skinpath = "/usr/share/enigma2/"
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/"
		componentspath = "/usr/lib/enigma2/python/Components/"
		if fileExists ("/tmp/version"\
			and "/tmp/plugin.py"\
			and "/tmp/ruSetupCyberFHD.mo"\
			and "/tmp/deSetupCyberFHD.mo"\
			and "/tmp/skin.xml"\
			and "/tmp/skin_style.xml"\
			and "/tmp/skin_templates.xml"\
			and "/tmp/skin_templates_style.xml"\
			and "/tmp/skin_extra.xml"\
			and "/tmp/AlwaysTrue.py"\
			and "/tmp/AC3DownMixStatus.py"\
			and "/tmp/CaidInfo2.py"\
			and "/tmp/CamdInfo3.py"\
			and "/tmp/EventName2.py"\
			and "/tmp/FrontendInfo2.py"\
			and "/tmp/ModuleControl.py"\
			and "/tmp/MovieInfo2.py"\
			and "/tmp/ProgressDiskSpaceInfo.py"\
			and "/tmp/ServiceInfoEX.py"\
			and "/tmp/ServiceName2.py"\
			and "/tmp/TunerBar.py"\
			and "/tmp/AnimatedWeatherPixmap.py"\
			and "/tmp/AnimatedMoonPixmap.py"\
			and "/tmp/MovieCover.py"\
			and "/tmp/MovieRating.py"\
			and "/tmp/PiconUni.py"\
			and "/tmp/RendVolumeTextP.py"\
			and "/tmp/Watches.py"):
			os.system("cp /tmp/version %sSetupCyberFHD/version" % (pluginpath))
	# install plugin
			os.system("cp /tmp/plugin.py %sSetupCyberFHD/plugin.py" % (pluginpath))
			os.system("cp /tmp/ruSetupCyberFHD.mo %sSetupCyberFHD/locale/ru/LC_MESSAGES/SetupCyberFHD.mo" % (pluginpath))
			os.system("cp /tmp/deSetupCyberFHD.mo %sSetupCyberFHD/locale/de/LC_MESSAGES/SetupCyberFHD.mo" % (pluginpath))
	# install skin
			os.system("cp /tmp/skin.xml %sCyberFHD/skin.xml" % (skinpath))
			os.system("cp /tmp/skin_style.xml %sCyberFHD/skin_style.xml" % (skinpath))
			os.system("cp /tmp/skin_templates.xml %sCyberFHD/skin_templates.xml" % (skinpath))
			os.system("cp /tmp/skin_templates_style.xml %sCyberFHD/skin_templates_style.xml" % (skinpath))
			os.system("cp /tmp/skin_extra.xml %sCyberFHD/skin_extra.xml" % (skinpath))
	# install converter
			os.system("cp /tmp/AlwaysTrue.py %sConverter/AlwaysTrue.py" % (componentspath))
			os.system("cp /tmp/AC3DownMixStatus.py %sConverter/AC3DownMixStatus.py" % (componentspath))
			os.system("cp /tmp/CaidInfo2.py %sConverter/CaidInfo2.py" % (componentspath))
			os.system("cp /tmp/CamdInfo3.py %sConverter/CamdInfo3.py" % (componentspath))
			os.system("cp /tmp/EventName2.py %sConverter/EventName2.py" % (componentspath))
			os.system("cp /tmp/FrontendInfo2.py %sConverter/FrontendInfo2.py" % (componentspath))
			os.system("cp /tmp/ModuleControl.py %sConverter/ModuleControl.py" % (componentspath))
			os.system("cp /tmp/MovieInfo2.py %sConverter/MovieInfo2.py" % (componentspath))
			os.system("cp /tmp/ProgressDiskSpaceInfo.py %sConverter/ProgressDiskSpaceInfo.py" % (componentspath))
			os.system("cp /tmp/ServiceInfoEX.py %sConverter/ServiceInfoEX.py" % (componentspath))
			os.system("cp /tmp/ServiceName2.py %sConverter/ServiceName2.py" % (componentspath))
			os.system("cp /tmp/TunerBar.py %sConverter/TunerBar.py" % (componentspath))
			os.system("cp %sWeatherMSN/components/MSNWeather2.py %sConverter/MSNWeather2.py" % (pluginpath, componentspath))
	# install renderer
			os.system("cp /tmp/AnimatedWeatherPixmap.py %sRenderer/AnimatedWeatherPixmap.py" % (componentspath))
			os.system("cp /tmp/AnimatedMoonPixmap.py %sRenderer/AnimatedMoonPixmap.py" % (componentspath))
			os.system("cp /tmp/MovieCover.py %sRenderer/MovieCover.py" % (componentspath))
			os.system("cp /tmp/MovieRating.py %sRenderer/MovieRating.py" % (componentspath))
			os.system("cp /tmp/PiconUni.py %sRenderer/PiconUni.py" % (componentspath))
			os.system("cp /tmp/RendVolumeTextP.py %sRenderer/RendVolumeTextP.py" % (componentspath))
			os.system("cp /tmp/Watches.py %sRenderer/Watches.py" % (componentspath))
	# end
			self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)
		else:
			self.download()

	def download(self):
		try:
	# download plugin
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberFHD/plugin.py","/tmp/plugin.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberFHD/locale/ru/LC_MESSAGES/SetupCyberFHD.mo","/tmp/ruSetupCyberFHD.mo")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/python/Plugins/Extensions/SetupCyberFHD/locale/de/LC_MESSAGES/SetupCyberFHD.mo","/tmp/deSetupCyberFHD.mo")
	# download skin
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberFHD/skin.xml","/tmp/skin.xml")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberFHD/skin_style.xml","/tmp/skin_style.xml")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberFHD/skin_templates.xml","/tmp/skin_templates.xml")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberFHD/skin_templates_style.xml","/tmp/skin_templates_style.xml")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-skins/master/share/enigma2/CyberFHD/skin_extra.xml","/tmp/skin_extra.xml")
	# download converter
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/AlwaysTrue.py","/tmp/AlwaysTrue.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/AC3DownMixStatus.py","/tmp/AC3DownMixStatus.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/CaidInfo2.py","/tmp/CaidInfo2.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/CamdInfo3.py","/tmp/CamdInfo3.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/EventName2.py","/tmp/EventName2.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/FrontendInfo2.py","/tmp/FrontendInfo2.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/ModuleControl.py","/tmp/ModuleControl.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/MovieInfo2.py","/tmp/MovieInfo2.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/ProgressDiskSpaceInfo.py","/tmp/ProgressDiskSpaceInfo.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/ServiceInfoEX.py","/tmp/ServiceInfoEX.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/ServiceName2.py","/tmp/ServiceName2.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Converter/TunerBar.py","/tmp/TunerBar.py")
	# download renderer
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/AnimatedWeatherPixmap.py","/tmp/AnimatedWeatherPixmap.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/AnimatedMoonPixmap.py","/tmp/AnimatedMoonPixmap.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/MovieCover.py","/tmp/MovieCover.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/MovieRating.py","/tmp/MovieRating.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/PiconUni.py","/tmp/PiconUni.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/RendVolumeTextP.py","/tmp/RendVolumeTextP.py")
			urllib.urlretrieve("https://raw.githubusercontent.com/Sirius0103/enigma2-components/master/python/Components/Renderer/Watches.py","/tmp/Watches.py")
	# end
			self.install()
		except:
			self.session.open(MessageBox,(_("Download failed, check your internet connection !!!")), MessageBox.TYPE_INFO, timeout = 10)

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
			config.skin.primary_skin.value = "CyberFHD/skin.xml"
			config.skin.primary_skin.save()
			self.session.open(TryQuitMainloop, 3)

	def about(self):
		self.session.open(MessageBox, _("Skin CyberFHD\nDeveloper: Sirius0103 \nHomepage: www.gisclub.tv \nGithub: www.github.com/Sirius0103 \n\nDonate: \nR460680746216 \nZ395874509364 \nE284580190260"), MessageBox.TYPE_INFO)

def main(session, **kwargs):
	session.open(SetupCyberFHD)

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Setup CyberFHD"),
	description=_("Setup skin CyberFHD"),
	where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU],
	icon="plugin.png",
	fnc=main)
