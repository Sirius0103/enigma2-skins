## SetuptechnonoHD
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
gettext.bindtextdomain("SetupTechnoHD", "%s%s" % (resolveFilename(SCOPE_PLUGINS), "Extensions/SetupTechnoHD/locale"))

def _(txt):
	t = gettext.dgettext("SetupTechnoHD", txt)
	if t == txt:
		t = gettext.gettext(txt)
	return t

config.skin.techno = ConfigSubsection()
config.skin.techno.style = ConfigSelection(default="grey", choices = [
	("white", _("white")),
	("grey", _("grey")),
	("yellow", _("yellow")),
	("red", _("red")),
	("green", _("green")),
	("purple", _("purple")),
	("blue", _("blue"))])
config.skin.techno.numberchannel = ConfigSelection(default="TemplatesNumberCh-1", choices = [
	("TemplatesNumberCh-1", _("no")),
	("TemplatesNumberCh-2", _("yes"))])
config.skin.techno.ecmepgpanel = ConfigSelection(default="TemplatesInfoBarECM-EPG-5", choices = [
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
config.skin.techno.epgchannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoEPG-2", choices = [
	("TemplatesChannelSelectionInfoEPG-1", _("no")),
	("TemplatesChannelSelectionInfoEPG-2", _("now")),
	("TemplatesChannelSelectionInfoEPG-3", _("now, next")),
	("TemplatesChannelSelectionInfoEPG-4", _("10 programs"))])
config.skin.techno.infochannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoChannel-1", choices = [
	("TemplatesChannelSelectionInfoChannel-1", _("no")),
	("TemplatesChannelSelectionInfoChannel-2", _("picons")),
	("TemplatesChannelSelectionInfoChannel-3", _("picons, channel info"))])
config.skin.techno.coverinfopanel = ConfigSelection(default="TemplatesInfoBarInfoMovie-Cover-1", choices = [
	("TemplatesInfoBarInfoMovie-Cover-1", _("no")),
	("TemplatesInfoBarInfoMovie-Cover-2", _("poster right (support TMDB plugin)")),
	("TemplatesInfoBarInfoMovie-Cover-3", _("poster left (support TMDB plugin)")),
	("TemplatesInfoBarInfoMovie-Cover-4", _("description right (support TMDB plugin)")),
	("TemplatesInfoBarInfoMovie-Cover-5", _("description left (support TMDB plugin)")),
	("TemplatesInfoBarInfoMovie-Cover-6", _("poster left, description right (support TMDB plugin)")),
	("TemplatesInfoBarInfoMovie-Cover-7", _("poster right, description left (support TMDB plugin)"))])
config.skin.techno.infomovieselection = ConfigSelection(default="TemplatesMovieSelectionInfoMovie-2", choices = [
	("TemplatesMovieSelectionInfoMovie-1", _("no")),
	("TemplatesMovieSelectionInfoMovie-2", _("standard")),
	("TemplatesMovieSelectionInfoMovie-3", _("support TMDB plugin"))])
config.skin.techno.clockpanel = ConfigSelection(default="Clock-1", choices = [
	("Clock-1", _("no")),
	("Clock-2", _("12:00")),
	("Clock-3", _("saturday, 01 january 12:00")),
	("Clock-4", _("saturday, 01.01.2010 12:00"))])
config.skin.techno.dish = ConfigSelection(default="Dish-1", choices = [
	("Dish-1", _("on left")),
	("Dish-2", _("on right"))])
config.skin.techno.scrollbarmode = ConfigSelection(default="showNever", choices = [
	("showNever", _("no")),
	("showOnDemand", _("yes"))])
config.skin.techno.fonts = ConfigSelection(default="LiberationSans-Regular", choices = [
	("LiberationSans-Regular", _("regular")),
	("LiberationSans-Bold", _("bold")),
	("LiberationSans-Italic", _("italic")),
	("LiberationSans-BoldItalic", _("bolditalic"))])
config.skin.techno.titlecolor = ConfigSelection(default="#00ffcc33", choices = [
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
config.skin.techno.textcolor = ConfigSelection(default="#00f4f4f4", choices = [
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
config.skin.techno.avtextcolor = ConfigSelection(default="#008f8f8f", choices = [
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
config.skin.techno.textcurcolor = ConfigSelection(default="#000099ff", choices = [
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
config.skin.techno.progresscolor = ConfigSelection(default="yellow", choices = [
	("white", _("white")),
	("grey", _("grey")),
	("yellow", _("yellow")),
	("red", _("red")),
	("green", _("green")),
	("purple", _("purple")),
	("blue", _("blue"))])

class SetupTechnoHD(ConfigListScreen, Screen):
	skin = """
	<screen name="SetupTechnoHD" position="0,0" size="1280,720" title=" " flags="wfNoBorder">
		<ePixmap position="0,0" zPosition="-1" size="1280,720" pixmap="Techno_hd/style/greymenu_1.png" />
		<widget source="Title" render="Label" position="45,38" size="720,36" font="Regular; 30" halign="center" transparent="1" foregroundColor="#00ffcc33" backgroundColor="background" borderWidth="2" />
		<ePixmap position="775,450" zPosition="1" size="500,150" pixmap="Techno_hd/logo.png" alphatest="blend" />
		<widget name="config" position="50,95" size="710,540" scrollbarMode="showOnDemand" selectionPixmap="Techno_hd/style/greysel.png" transparent="1" />
		<widget source="version_sk" render="Label" position="930,585" size="200,22" font="Regular;20" halign="right" valign="center" backgroundColor="background" foregroundColor="#00f4f4f4" transparent="1" zPosition="2" />
		<widget source="vinfo_sk" render="Label" position="1150,585" size="80,22" font="Regular;20" halign="left" valign="center" backgroundColor="background" foregroundColor="#008f8f8f" transparent="1" zPosition="2" />
		<widget source="version_lib" render="Label" position="880,615" size="250,22" font="Regular;20" halign="right" valign="center" backgroundColor="background" foregroundColor="#00f4f4f4" transparent="1" zPosition="2" />
		<widget source="vinfo_lib" render="Label" position="1150,615" size="80,22" font="Regular;20" halign="left" valign="center" backgroundColor="background" foregroundColor="#008f8f8f" transparent="1" zPosition="2" />
		<widget source="key_red" render="Label" position="56,663" size="270,40" font="Regular; 22" halign="center" valign="top" backgroundColor="background" transparent="1" zPosition="3" foregroundColor="#00f4f4f4" borderWidth="1" />
		<widget source="key_green" render="Label" position="355,663" size="270,40" font="Regular; 22" halign="center" valign="top" backgroundColor="background" transparent="1" zPosition="3" foregroundColor="#00f4f4f4" borderWidth="1" />
		<ePixmap pixmap="Techno_hd/buttons/key_info.png" position="800,615" size="35,25" zPosition="2" alphatest="blend" />
		<widget source="session.VideoPicture" render="Pig" position="806,96" size="428,248" zPosition="3" backgroundColor="transparent" />
		<ePixmap position="51,651" size="281,16" pixmap="Techno_hd/buttons.png" alphatest="blend" zPosition="1" />
		<ePixmap position="350,651" size="281,16" pixmap="Techno_hd/buttons.png" alphatest="blend" zPosition="1" />
		<ePixmap position="648,651" size="281,16" pixmap="Techno_hd/buttons.png" alphatest="blend" zPosition="1" />
		<ePixmap position="946,651" size="281,16" pixmap="Techno_hd/buttons.png" alphatest="blend" zPosition="1" />
		<ePixmap pixmap="Techno_hd/buttons/red2.png" position="54,653" size="275,10" alphatest="on" zPosition="2" />
		<ePixmap pixmap="Techno_hd/buttons/green2.png" position="353,653" size="275,10" alphatest="on" zPosition="2" />
		<ePixmap pixmap="Techno_hd/buttons/yellow2.png" position="650,653" size="275,10" alphatest="on" zPosition="2" />
		<ePixmap pixmap="Techno_hd/buttons/blue2.png" position="949,653" size="275,10" alphatest="on" zPosition="2" />
	</screen>"""

	def __init__(self, session):

		Screen.__init__(self, session)
		self.session = session

		list = []
		list.append(getConfigListEntry(_("Style skin`s:"), config.skin.techno.style))
		list.append(getConfigListEntry(_("Channel number in infobars:"), config.skin.techno.numberchannel))
		list.append(getConfigListEntry(_("ECM, EPG panel in secondinfobar:"), config.skin.techno.ecmepgpanel))
		list.append(getConfigListEntry(_("Panel EPG in channel selection:"), config.skin.techno.epgchannelselection))
		list.append(getConfigListEntry(_("Additional widgets in channel selection:"), config.skin.techno.infochannelselection))
		list.append(getConfigListEntry(_("Widget mediainfobar:"), config.skin.techno.coverinfopanel))
		list.append(getConfigListEntry(_("Panel description in movie selection:"), config.skin.techno.infomovieselection))
		list.append(getConfigListEntry(_("Clock in menu, infobars:"), config.skin.techno.clockpanel))
		list.append(getConfigListEntry(_("Position dish:"), config.skin.techno.dish))
		list.append(getConfigListEntry(_("Scrollbar in menu:"), config.skin.techno.scrollbarmode))
		list.append(getConfigListEntry(_("Fonts:"), config.skin.techno.fonts))
		list.append(getConfigListEntry(_("Title text color:"), config.skin.techno.titlecolor))
		list.append(getConfigListEntry(_("Menu text color:"), config.skin.techno.textcolor))
		list.append(getConfigListEntry(_("Additional text color:"), config.skin.techno.avtextcolor))
		list.append(getConfigListEntry(_("Cursor text color:"), config.skin.techno.textcurcolor))
		list.append(getConfigListEntry(_("Progress bar color:"), config.skin.techno.progresscolor))
		ConfigListScreen.__init__(self, list)

		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "EPGSelectActions"],{"ok": self.save, "cancel": self.exit, "red": self.exit, "green": self.save, "info": self.about}, -1)
		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("Save"))
		self["Title"] = StaticText(_("Setup TechnoHD"))
		self["version_sk"] = StaticText(_("Version skin:"))
		self["version_lib"] = StaticText(_("Version library:"))
		self["vinfo_sk"] = StaticText()
		self["vinfo_lib"] = StaticText()
		self.infosk()
		self.infolib()

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
			if line.find("techno-hd") > -1:
				package = 1
			if line.find("Version:") > -1 and package == 1:
				package = 0
				try:
					self["vinfo_sk"].text = line.split()[1]
				except:
					self["vinfo_sk"].text = " "
				break

	def infolib(self):
		package = 0
		global status 
		if fileExists("/usr/lib/opkg/status"):
			status = "/usr/lib/opkg/status"
		elif fileExists("/var/lib/opkg/status"):
			status = "/var/lib/opkg/status"
		elif fileExists("/var/opkg/status"):
			status = "/var/opkg/status"
		for line in open(status):
			if line.find("gisclub-lib") > -1:
				package = 1
			if line.find("Version:") > -1 and package == 1:
				package = 0
				try:
					self["vinfo_lib"].text = line.split()[1]
				except:
					self["vinfo_lib"].text = " "
				break

	def save(self):
		skinpath = "/usr/share/enigma2/Techno_hd/"
		pluginpath = "/usr/lib/enigma2/python/"
		style = config.skin.techno.style.value
		clockpanel = config.skin.techno.clockpanel.value
		numberchannel = config.skin.techno.numberchannel.value
		ecmepgpanel = config.skin.techno.ecmepgpanel.value
		epgchannelselection = config.skin.techno.epgchannelselection.value
		infochannelselection = config.skin.techno.infochannelselection.value
		coverinfopanel = config.skin.techno.coverinfopanel.value
		infomovieselection = config.skin.techno.infomovieselection.value
		dish = config.skin.techno.dish.value
		fonts = config.skin.techno.fonts.value
		scrollbarmode = config.skin.techno.scrollbarmode.value
		titlecolor = config.skin.techno.titlecolor.value
		textcolor = config.skin.techno.textcolor.value
		avtextcolor = config.skin.techno.avtextcolor.value
		textcurcolor = config.skin.techno.textcurcolor.value
		progresscolor = config.skin.techno.progresscolor.value
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
			os.system("sed -i 's/LiberationSans-Regular/%s/w' %sskin.xml" % (fonts, skinpath))
	# number channel
			os.system("sed -i 's/%s/TemplatesNumberCh/w' %sskin.xml" % (numberchannel, skinpath))
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
	# clock panel menu
			os.system("sed -i 's/%s/Clock/w' %sskin.xml" % (clockpanel, skinpath))
	# dish
			os.system("sed -i 's/%s/Dish/w' %sskin.xml" % (dish, skinpath))
	# scrollbar
			os.system("sed -i 's/showNever/%s/w' %sskin.xml" % (scrollbarmode, skinpath))
	# style progress
			os.system("sed -i 's/yellowprogress/%sprogress/w' %sskin.xml" % (progresscolor, skinpath))
			os.system("sed -i 's/yellowprogress_big/%sprogress_big/w' %sskin.xml" % (progresscolor, skinpath))
	# style skin`s
			os.system("sed -i 's/greyinfobar/%sinfobar/w' %sskin.xml" % (style, skinpath))
			os.system("sed -i 's/greymenu/%smenu/w' %sskin.xml" % (style, skinpath))
			os.system("sed -i 's/greysel/%ssel/w' %sskin.xml" % (style, skinpath))
			os.system("sed -i 's/greyvolume/%svolume/w' %sskin.xml" % (style, skinpath))
			os.system("sed -i 's/greydownload/%sdownload/w' %sskin.xml" % (style, skinpath))
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
		self.session.open(MessageBox, _("Skin TechnoHD\nDeveloper: Sirius0103 \nHomepage: www.gisclub.tv \n\nDonate:\nWMZ  Z395874509364\nWMR  R213063691482"), MessageBox.TYPE_INFO)

def main(session, **kwargs):
	session.open(SetupTechnoHD)

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Setup TechnoHD"),
	description=_("Setup skin TechnoHD"),
	where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU],
	icon="plugin.png",
	fnc=main)
