## SetupNeutronHD
## Coded by Sirius
##
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.Sources.StaticText import StaticText
from Components.Language import language
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection, ConfigText, ConfigInteger
from Tools.Directories import fileExists
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_SKIN_IMAGE, SCOPE_LANGUAGE
from os import environ
from os import system
import gettext
import os

lang = language.getLanguage()
environ["LANGUAGE"] = lang[:2]
gettext.bindtextdomain("enigma2", resolveFilename(SCOPE_LANGUAGE))
gettext.textdomain("enigma2")
gettext.bindtextdomain("SetupNeutronHD", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/SetupNeutronHD/locale"))

def _(txt):
	t = gettext.dgettext("SetupNeutronHD", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

config.skin.neutron = ConfigSubsection()
config.skin.neutron.style = ConfigSelection(default="grey", choices = [
	("white", _("white")),
	("grey", _("grey")),
	("yellow", _("yellow")),
	("red", _("red")),
	("green", _("green")),
	("aqua", _("aqua")),
	("skyblue", _("skyblue")),
	("purple", _("purple")),
	("blue", _("blue"))])
config.skin.neutron.numberchannel = ConfigSelection(default="TemplatesInfoBarNumber-1", choices = [
	("TemplatesInfoBarNumber-1", _("no")),
	("TemplatesInfoBarNumber-2", _("yes"))])
config.skin.neutron.styleinfobar = ConfigSelection(default="TemplatesInfoBarTvPicon", choices = [
	("TemplatesInfoBarTvPicon", _("default")),
	("TemplatesInfoBarTvPiconProv", _("picon provider")),
	("TemplatesInfoBarTvPiconSat", _("picon sattelite")),
	("TemplatesInfoBarTvPiconProvSat", _("picon provider, picon sattelite")),
	("TemplatesInfoBarTvPiconTuner", _("tuner")),
	("TemplatesInfoBarTvPiconProvTuner", _("picon provider, tuner")),
	("TemplatesInfoBarTvPiconSatTuner", _("picon sattelite, tuner")),
	("TemplatesInfoBarTvPiconProvSatTuner", _("picon provider, picon sattelite, tuner")),
	("TemplatesInfoBarTvPiconAnalogTuner", _("analog tuner")),
	("TemplatesInfoBarTvPiconProvAnalogTuner", _("picon provider, analog tuner")),
	("TemplatesInfoBarTvPiconSatAnalogTuner", _("picon sattelite, analog tuner")),
	("TemplatesInfoBarTvPiconProvSatAnalogTuner", _("picon provider, picon sattelite, analog tuner"))])
config.skin.neutron.technicalinfobar = ConfigSelection(default="TemplatesInfoBarTechnical-1", choices = [
	("TemplatesInfoBarTechnical-1", _("no")),
	("TemplatesInfoBarTechnical-2", _("pid")),
	("TemplatesInfoBarTechnical-3", _("ecm, caids")),
	("TemplatesInfoBarTechnical-4", _("crypt, ecm, camd"))])
config.skin.neutron.stylesecondinfobar = ConfigSelection(default="TemplatesInfoBarTvPicon", choices = [
	("TemplatesInfoBarTvPicon", _("default")),
	("TemplatesInfoBarTvPiconProv", _("picon provider")),
	("TemplatesInfoBarTvPiconSat", _("picon sattelite")),
	("TemplatesInfoBarTvPiconProvSat", _("picon provider, picon sattelite")),
	("TemplatesInfoBarTvPiconTuner", _("tuner")),
	("TemplatesInfoBarTvPiconProvTuner", _("picon provider, tuner")),
	("TemplatesInfoBarTvPiconSatTuner", _("picon sattelite, tuner")),
	("TemplatesInfoBarTvPiconProvSatTuner", _("picon provider, picon sattelite, tuner")),
	("TemplatesInfoBarTvPiconAnalogTuner", _("analog tuner")),
	("TemplatesInfoBarTvPiconProvAnalogTuner", _("picon provider, analog tuner")),
	("TemplatesInfoBarTvPiconSatAnalogTuner", _("picon sattelite, analog tuner")),
	("TemplatesInfoBarTvPiconProvSatAnalogTuner", _("picon provider, picon sattelite, analog tuner"))])
config.skin.neutron.technicalsecondinfobar = ConfigSelection(default="TemplatesInfoBarTechnical-1", choices = [
	("TemplatesInfoBarTechnical-1", _("no")),
	("TemplatesInfoBarTechnical-2", _("pid")),
	("TemplatesInfoBarTechnical-3", _("ecm, caids")),
	("TemplatesInfoBarTechnical-4", _("crypt, ecm, camd"))])
config.skin.neutron.ecmepgpanel = ConfigSelection(default="TemplatesInfoBarECM-EPG-5", choices = [
	("TemplatesInfoBarECM-EPG-1", _("no")),
	("TemplatesInfoBarECM-EPG-2", _("ecm centre")),
	("TemplatesInfoBarECM-EPG-3", _("ecm right")),
	("TemplatesInfoBarECM-EPG-4", _("ecm left")),
	("TemplatesInfoBarECM-EPG-5", _("epg centre")),
	("TemplatesInfoBarECM-EPG-6", _("epg right")),
	("TemplatesInfoBarECM-EPG-7", _("epg left")),
	("TemplatesInfoBarECM-EPG-8", _("ecm centre, epg centre")),
	("TemplatesInfoBarECM-EPG-9", _("ecm right, epg left")),
	("TemplatesInfoBarECM-EPG-10", _("ecm left, epg right"))])
config.skin.neutron.epgchannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoEPG-1", choices = [
	("TemplatesChannelSelectionInfoEPG-1", _("no")),
	("TemplatesChannelSelectionInfoEPG-2", _("now")),
	("TemplatesChannelSelectionInfoEPG-3", _("now, next")),
	("TemplatesChannelSelectionInfoEPG-4", _("9 programs"))])
config.skin.neutron.infochannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoChannel-1", choices = [
	("TemplatesChannelSelectionInfoChannel-1", _("no")),
	("TemplatesChannelSelectionInfoChannel-2", _("picons")),
	("TemplatesChannelSelectionInfoChannel-3", _("channel info")),
	("TemplatesChannelSelectionInfoChannel-4", _("picon channel, channel info")),
	("TemplatesChannelSelectionInfoChannel-5", _("picon channel, picon provider, channel info")),
	("TemplatesChannelSelectionInfoChannel-6", _("picon channel, picon provider, picon sattelite, channel info"))])
config.skin.neutron.coverinfopanel = ConfigSelection(default="TemplatesInfoBarInfoMovie-Cover-1", choices = [
	("TemplatesInfoBarInfoMovie-Cover-1", _("no")),
	("TemplatesInfoBarInfoMovie-Cover-2", _("poster (support TMDB plugin)")),
	("TemplatesInfoBarInfoMovie-Cover-3", _("poster, description (support TMDB plugin)"))])
config.skin.neutron.infomovieselection = ConfigSelection(default="TemplatesMovieSelectionInfoMovie-1", choices = [
	("TemplatesMovieSelectionInfoMovie-1", _("no")),
	("TemplatesMovieSelectionInfoMovie-2", _("standard")),
	("TemplatesMovieSelectionInfoMovie-3", _("support TMDB plugin"))])
config.skin.neutron.clockpanel = ConfigSelection(default="TemplatesClock-1", choices = [
	("TemplatesClock-1", _("no")),
	("TemplatesClock-2", _("12:00")),
	("TemplatesClock-3", _("saturday, 01 january 12:00")),
	("TemplatesClock-4", _("saturday, 01.01.2010 12:00"))])
config.skin.neutron.otherinfobar = ConfigSelection(default="TemplatesInfoBarOther-1", choices = [
	("TemplatesInfoBarOther-1", _("no")),
	("TemplatesInfoBarOther-2", _("rambler weather")),
	("TemplatesInfoBarOther-3", _("msn weather")),
	("TemplatesInfoBarOther-4", _("msn weather full")),
	("TemplatesInfoBarOther-5", _("calendar (support Calendar plugin)")),
	("TemplatesInfoBarOther-6", _("rambler weather, calendar (support Calendar plugin)")),
	("TemplatesInfoBarOther-7", _("msn weather, calendar (support Calendar plugin)")),
	("TemplatesInfoBarOther-8", _("msn weather full, calendar (support Calendar plugin)"))])
config.skin.neutron.dish = ConfigSelection(default="Dish-2", choices = [
	("Dish-1", _("on left")),
	("Dish-2", _("on right"))])
config.skin.neutron.scrollbarmode = ConfigSelection(default="showNever", choices = [
	("showNever", _("no")),
	("showOnDemand", _("yes"))])
config.skin.neutron.fonts = ConfigSelection(default="Roboto-Regular", choices = [
	("Roboto-Regular", _("regular")),
	("Roboto-Medium", _("medium")),
	("Roboto-Bold", _("bold")),
	("Roboto-Italic", _("italic")),
	("Roboto-MediumItalic", _("mediumitalic")),
	("Roboto-BoldItalic", _("bolditalic"))])
config.skin.neutron.titlecolor = ConfigSelection(default="#00ffcc33", choices = [
	("#00f4f4f4", _("white")),
	("#00c0c0c0", _("lightgrey")),
	("#008f8f8f", _("grey")),
	("#00555555", _("darkgrey")),
	("#00ffff55", _("yellow")),
	("#00ffcc33", _("gold")),
	("#00ff80ff", _("pink")),
	("#00ff8000", _("orange")),
	("#00ff0000", _("red")),
	("#00800000", _("maroon")),
	("#00804000", _("brown")),
	("#0000ffff", _("aqua")),
	("#0080ff00", _("lime")),
	("#0000ff00", _("green")),
	("#00008000", _("darkgreen")),
	("#000099ff", _("skyblue")),
	("#000000ff", _("blue")),
	("#00000080", _("darkblue")),
	("#008080ff", _("glaucous")),
	("#00400080", _("purple"))])
config.skin.neutron.textcolor = ConfigSelection(default="#00f4f4f4", choices = [
	("#00f4f4f4", _("white")),
	("#00c0c0c0", _("lightgrey")),
	("#008f8f8f", _("grey")),
	("#00555555", _("darkgrey")),
	("#00ffff55", _("yellow")),
	("#00ffcc33", _("gold")),
	("#00ff80ff", _("pink")),
	("#00ff8000", _("orange")),
	("#00ff0000", _("red")),
	("#00800000", _("maroon")),
	("#00804000", _("brown")),
	("#0000ffff", _("aqua")),
	("#0080ff00", _("lime")),
	("#0000ff00", _("green")),
	("#00008000", _("darkgreen")),
	("#000099ff", _("skyblue")),
	("#000000ff", _("blue")),
	("#00000080", _("darkblue")),
	("#008080ff", _("glaucous")),
	("#00400080", _("purple"))])
config.skin.neutron.avtextcolor = ConfigSelection(default="#008f8f8f", choices = [
	("#00f4f4f4", _("white")),
	("#00c0c0c0", _("lightgrey")),
	("#008f8f8f", _("grey")),
	("#00555555", _("darkgrey")),
	("#00ffff55", _("yellow")),
	("#00ffcc33", _("gold")),
	("#00ff80ff", _("pink")),
	("#00ff8000", _("orange")),
	("#00ff0000", _("red")),
	("#00800000", _("maroon")),
	("#00804000", _("brown")),
	("#0000ffff", _("aqua")),
	("#0080ff00", _("lime")),
	("#0000ff00", _("green")),
	("#00008000", _("darkgreen")),
	("#000099ff", _("skyblue")),
	("#000000ff", _("blue")),
	("#00000080", _("darkblue")),
	("#008080ff", _("glaucous")),
	("#00400080", _("purple"))])
config.skin.neutron.textcurcolor = ConfigSelection(default="#00ffcc33", choices = [
	("#00f4f4f4", _("white")),
	("#00c0c0c0", _("lightgrey")),
	("#008f8f8f", _("grey")),
	("#00555555", _("darkgrey")),
	("#00ffff55", _("yellow")),
	("#00ffcc33", _("gold")),
	("#00ff80ff", _("pink")),
	("#00ff8000", _("orange")),
	("#00ff0000", _("red")),
	("#00800000", _("maroon")),
	("#00804000", _("brown")),
	("#0000ffff", _("aqua")),
	("#0080ff00", _("lime")),
	("#0000ff00", _("green")),
	("#00008000", _("darkgreen")),
	("#000099ff", _("skyblue")),
	("#000000ff", _("blue")),
	("#00000080", _("darkblue")),
	("#008080ff", _("glaucous")),
	("#00400080", _("purple"))])
config.skin.neutron.progresscolor = ConfigSelection(default="gold", choices = [
	("white", _("white")),
	("yellow", _("yellow")),
	("gold", _("gold")),
	("pink", _("pink")),
	("orange", _("orange")),
	("red", _("red")),
	("maroon", _("maroon")),
	("brown", _("brown")),
	("aqua", _("aqua")),
	("lime", _("lime")),
	("green", _("green")),
	("darkgreen", _("darkgreen")),
	("skyblue", _("skyblue")),
	("blue", _("blue")),
	("darkblue", _("darkblue")),
	("glaucous", _("glaucous")),
	("purple", _("purple"))])

class SetupNeutronHD(ConfigListScreen, Screen):
	skin = """
	<!-- Setup NeutronHD -->
	<screen name="SetupNeutronHD" position="0,0" size="1280,720" title=" " flags="wfNoBorder" backgroundColor="transparent">
		<ePixmap position="30,25" size="700,600" pixmap="Neutron_hd/style/greymenu_1.png" alphatest="on" zPosition="-1" />
		<ePixmap position="center,575" size="1280,150" pixmap="Neutron_hd/style/menubar_1.png" alphatest="off" zPosition="-2" />
		<ePixmap position="20,635" size="80,80" pixmap="Neutron_hd/menu/setting.png" alphatest="blend" />
		<widget source="Title" render="Label" position="30,25" size="700,36" font="Regular; 30" foregroundColor="#00ffcc33" backgroundColor="background" halign="center" transparent="1" borderWidth="2" />
		<widget name="config" position="45,70" size="670,540" scrollbarMode="showOnDemand" selectionPixmap="Neutron_hd/style/greysel.png" transparent="1" />
		<widget source="version_sk" render="Label" position="110,690" size="150,22" font="Regular; 18" foregroundColor="#008f8f8f" backgroundColor="background" halign="left" valign="center" transparent="1" />
		<widget source="vinfo_sk" render="Label" position="260,690" size="80,22" font="Regular; 18" foregroundColor="#008f8f8f" backgroundColor="background" halign="left" valign="center" transparent="1" />
		<widget source="key_red" render="Label" position="750,615" size="400,25" font="Regular; 22" halign="right" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" />
		<widget source="key_green" render="Label" position="750,640" size="400,25" font="Regular; 22" halign="right" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" />
		<widget source="key_blue" render="Label" position="750,690" size="400,25" font="Regular; 22" halign="right" valign="center" foregroundColor="#00f4f4f4" backgroundColor="background" transparent="1" />
		<ePixmap pixmap="Neutron_hd/buttons/key_epg.png" position="1210,668" size="40,20" alphatest="blend" />
		<ePixmap pixmap="Neutron_hd/buttons/key_red.png" position="1160,616" size="40,20" alphatest="on" />
		<ePixmap pixmap="Neutron_hd/buttons/key_green.png" position="1160,642" size="40,20" alphatest="on" />
		<ePixmap pixmap="Neutron_hd/buttons/key_yellow.png" position="1160,668" size="40,20" alphatest="on" />
		<ePixmap pixmap="Neutron_hd/buttons/key_blue.png" position="1160,694" size="40,20" alphatest="on" />
	</screen>"""

	def __init__(self, session):

		Screen.__init__(self, session)
		self.session = session

		list = []
		list.append(getConfigListEntry(_("Style skins:"), config.skin.neutron.style))
		list.append(getConfigListEntry(_("Channel number in infobars:"), config.skin.neutron.numberchannel))
		list.append(getConfigListEntry(_("Widgets infobar:"), config.skin.neutron.styleinfobar))
		list.append(getConfigListEntry(_("Additional widget infobar:"), config.skin.neutron.technicalinfobar))
		list.append(getConfigListEntry(_("Widgets secondinfobar:"), config.skin.neutron.stylesecondinfobar))
		list.append(getConfigListEntry(_("Additional widget secondinfobar:"), config.skin.neutron.technicalsecondinfobar))
		list.append(getConfigListEntry(_("ECM, EPG panel in secondinfobar:"), config.skin.neutron.ecmepgpanel))
		list.append(getConfigListEntry(_("Panel EPG in channel selection:"), config.skin.neutron.epgchannelselection))
		list.append(getConfigListEntry(_("Additional widgets in channel selection:"), config.skin.neutron.infochannelselection))
		list.append(getConfigListEntry(_("Widget mediainfobar:"), config.skin.neutron.coverinfopanel))
		list.append(getConfigListEntry(_("Panel description in movie selection:"), config.skin.neutron.infomovieselection))
		list.append(getConfigListEntry(_("Clock in menu, infobars:"), config.skin.neutron.clockpanel))
		list.append(getConfigListEntry(_("Other widget in infobars:"), config.skin.neutron.otherinfobar))
		list.append(getConfigListEntry(_("Position dish:"), config.skin.neutron.dish))
		list.append(getConfigListEntry(_("Scrollbar in menu:"), config.skin.neutron.scrollbarmode))
		list.append(getConfigListEntry(_("Fonts:"), config.skin.neutron.fonts))
		list.append(getConfigListEntry(_("Title text color:"), config.skin.neutron.titlecolor))
		list.append(getConfigListEntry(_("Menu text color:"), config.skin.neutron.textcolor))
		list.append(getConfigListEntry(_("Additional text color:"), config.skin.neutron.avtextcolor))
		list.append(getConfigListEntry(_("Cursor text color:"), config.skin.neutron.textcurcolor))
		list.append(getConfigListEntry(_("Progress bar color:"), config.skin.neutron.progresscolor))
		ConfigListScreen.__init__(self, list)

		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "EPGSelectActions"],{"ok": self.save, "cancel": self.exit, "red": self.exit, "green": self.save, "blue": self.install, "info": self.about}, -1)
		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("Save"))
		self["key_blue"] = StaticText(_("Install components"))
		self["Title"] = StaticText(_("Setup NeutronHD"))
		self["version_sk"] = StaticText(_("Version skin:"))
		self["vinfo_sk"] = StaticText()
		self.infosk()

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
			if line.find("neutron-hd") > -1:
				package = 1
			if line.find("Version:") > -1 and package == 1:
				package = 0
				try:
					self["vinfo_sk"].text = line.split()[1]
				except:
					self["vinfo_sk"].text = " "
				break

	def save(self):
		skinpath = "/usr/share/enigma2/Neutron_hd/"
		pluginpath = "/usr/lib/enigma2/python/"
		style = config.skin.neutron.style.value
		numberchannel = config.skin.neutron.numberchannel.value
		styleinfobar = config.skin.neutron.styleinfobar.value
		technicalinfobar = config.skin.neutron.technicalinfobar.value
		otherinfobar = config.skin.neutron.otherinfobar.value
		stylesecondinfobar = config.skin.neutron.stylesecondinfobar.value
		technicalsecondinfobar = config.skin.neutron.technicalsecondinfobar.value
		ecmepgpanel = config.skin.neutron.ecmepgpanel.value
		epgchannelselection = config.skin.neutron.epgchannelselection.value
		infochannelselection = config.skin.neutron.infochannelselection.value
		coverinfopanel = config.skin.neutron.coverinfopanel.value
		infomovieselection = config.skin.neutron.infomovieselection.value
		clockpanel = config.skin.neutron.clockpanel.value
		dish = config.skin.neutron.dish.value
		fonts = config.skin.neutron.fonts.value
		scrollbarmode = config.skin.neutron.scrollbarmode.value
		titlecolor = config.skin.neutron.titlecolor.value
		textcolor = config.skin.neutron.textcolor.value
		avtextcolor = config.skin.neutron.avtextcolor.value
		textcurcolor = config.skin.neutron.textcurcolor.value
		progresscolor = config.skin.neutron.progresscolor.value
	# save config
		for x in self["config"].list:
			x[1].save()
		try:
	# default skin
			os.system("cp %sdefskin.xml %sskin.xml" % (skinpath, skinpath))
	# color`s text
			os.system("sed -i 's/#10ffcc33/%s/w' %sskin.xml" % (titlecolor, skinpath))
			os.system("sed -i 's/#10f4f4f4/%s/w' %sskin.xml" % (textcolor, skinpath))
			os.system("sed -i 's/#108f8f8f/%s/w' %sskin.xml" % (avtextcolor, skinpath))
			os.system("sed -i 's/#100099ff/%s/w' %sskin.xml" % (textcurcolor, skinpath))
	# fonts	
			os.system("sed -i 's/Roboto-Regular/%s/w' %sskin.xml" % (fonts, skinpath))
	# number channel
			os.system("sed -i 's/%s/TemplatesInfoBarNumber/w' %sskin.xml" % (numberchannel, skinpath))
	# widgets infobar
			os.system("sed -i 's/TemplatesInfoBarTvBar/%s/w' %sskin.xml" % (styleinfobar, skinpath))
	# additional infobar
			os.system("sed -i 's/TemplatesInfoBarTvTechnical/%s/w' %sskin.xml" % (technicalinfobar, skinpath))
	# widgets secondinfobar
			os.system("sed -i 's/TemplatesInfoBarTvSecondBar/%s/w' %sskin.xml" % (stylesecondinfobar, skinpath))
	# additional secondinfobar
			os.system("sed -i 's/TemplatesInfoBarTvSecondTechnical/%s/w' %sskin.xml" % (technicalsecondinfobar, skinpath))
	# ecm-epg panel
			os.system("sed -i 's/%s/TemplatesInfoBarECM-EPG/w' %sskin.xml" % (ecmepgpanel, skinpath))
	# epg channel selection
			os.system("sed -i 's/%s/TemplatesChannelSelectionInfoEPG/w' %sskin.xml" % (epgchannelselection, skinpath))
	# info channel selection
			os.system("sed -i 's/%s/TemplatesChannelSelectionInfoChannel/w' %sskin.xml" % (infochannelselection, skinpath))
	# cover info panel
			os.system("sed -i 's/%s/TemplatesInfoBarInfoMovie-Cover/w' %sskin.xml" % (coverinfopanel, skinpath))
	# info movie selection
			os.system("sed -i 's/%s/TemplatesMovieSelectionInfoMovie/w' %sskin.xml" % (infomovieselection, skinpath))
	# clock panel
			os.system("sed -i 's/%s/TemplatesClock/w' %sskin.xml" % (clockpanel, skinpath))
	# other widgets infobar
			os.system("sed -i 's/TemplatesInfoBarTvOther/%s/w' %sskin.xml" % (otherinfobar, skinpath))
	# dish
			os.system("sed -i 's/%s/Dish/w' %sskin.xml" % (dish, skinpath))
	# scrollbar
			os.system("sed -i 's/showNever/%s/w' %sskin.xml" % (scrollbarmode, skinpath))
	# style progress
			os.system("sed -i 's/goldprogress/%sprogress/w' %sskin.xml" % (progresscolor, skinpath))
	# style skin`s
			os.system("sed -i 's/greymenu/%smenu/w' %sskin.xml" % (style, skinpath))
			os.system("sed -i 's/greysel/%ssel/w' %sskin.xml" % (style, skinpath))
			os.system("sed -i 's/greybg/%sbg/w' %sskin.xml" % (style, skinpath))
	# end
		except:
			self.session.open(MessageBox, _("Error by processing !!!"), MessageBox.TYPE_ERROR)
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def install(self):
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/SetupNeutronHD/components/"
		componentspath = "/usr/lib/enigma2/python/Components/"
		try:
	# install converter
			os.system("cp %sAlwaysTrue.py %sConverter/AlwaysTrue.py" % (pluginpath, componentspath))
			os.system("cp %sCaidInfo2.py %sConverter/CaidInfo2.py" % (pluginpath, componentspath))
			os.system("cp %sCamdInfo3.py %sConverter/CamdInfo3.py" % (pluginpath, componentspath))
			os.system("cp %sConverterRotator.py %sConverter/ConverterRotator.py" % (pluginpath, componentspath))
			os.system("cp %sEventName2.py %sConverter/EventName2.py" % (pluginpath, componentspath))
			os.system("cp %sFrontendInfo2.py %sConverter/FrontendInfo2.py" % (pluginpath, componentspath))
			os.system("cp %sProgressDiskSpaceInfo.py %sConverter/ProgressDiskSpaceInfo.py" % (pluginpath, componentspath))
			os.system("cp %sRouteInfo.py %sConverter/RouteInfo.py" % (pluginpath, componentspath))
			os.system("cp %sRWeather.py %sConverter/RWeather.py" % (pluginpath, componentspath))
			os.system("cp %sMSNWeather.py %sConverter/MSNWeather.py" % (pluginpath, componentspath))
			os.system("cp %sServiceInfoEX.py %sConverter/ServiceInfoEX.py" % (pluginpath, componentspath))
			os.system("cp %sServiceName2.py %sConverter/ServiceName2.py" % (pluginpath, componentspath))
	# install renderer
			os.system("cp %sPiconUni.py %sRenderer/PiconUni.py" % (pluginpath, componentspath))
			os.system("cp %sRendVolumeText.py %sRenderer/RendVolumeText.py" % (pluginpath, componentspath))
			os.system("cp %sWatches.py %sRenderer/Watches.py" % (pluginpath, componentspath))
	# end
		except:
			self.session.open(MessageBox, _("Error by processing !!!"), MessageBox.TYPE_ERROR)
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def exit(self):
		for x in self["config"].list:
			x[1].cancel()
		self.close()

	def restart(self, answer):
		if answer is True:
			self.session.open(TryQuitMainloop, 3)

	def about(self):
		self.session.open(MessageBox, _("Skin NeutronHD\nDeveloper: Sirius0103 \nHomepage: www.gisclub.tv \n\nDonate:\nWMZ  Z395874509364\nWMR  R213063691482"), MessageBox.TYPE_INFO)

def main(session, **kwargs):
	session.open(SetupNeutronHD)

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Setup NeutronHD"),
	description=_("Setup skin NeutronHD"),
	where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU],
	icon="plugin.png",
	fnc=main)
