# -*- coding: UTF-8 -*-
## SetupTechnoHD
## Coded by Sirius
##
from Plugins.Plugin import PluginDescriptor
from Screens.Screen import Screen
from Screens.MessageBox import MessageBox
from Screens.Standby import TryQuitMainloop
from Components.ActionMap import ActionMap
from Components.Language import language
from Components.Sources.StaticText import StaticText
from Components.ConfigList import ConfigListScreen
from Components.config import config, ConfigYesNo, ConfigSubsection, getConfigListEntry, ConfigSelection
from Tools.Directories import fileExists
from Tools.LoadPixmap import LoadPixmap
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_SKIN_IMAGE, SCOPE_LANGUAGE
from os import system, environ
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

textcolor = [
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
	("#00400080", _("purple"))]
style = [
	("white", _("white")),
	("grey", _("grey")),
	("yellow", _("yellow")),
	("red", _("red")),
	("green", _("green")),
	("purple", _("purple")),
	("blue", _("blue"))]
numberchannel = [
	("TemplatesNumberCh-1", _("no")),
	("TemplatesNumberCh-2", _("yes"))]
ecmepgpanel = [
	("TemplatesInfoBarECM-EPG-1", _("no")),
	("TemplatesInfoBarECM-EPG-2", _("ecm centre")),
	("TemplatesInfoBarECM-EPG-3", _("ecm right")),
	("TemplatesInfoBarECM-EPG-4", _("ecm left")),
	("TemplatesInfoBarECM-EPG-5", _("epg centre")),
	("TemplatesInfoBarECM-EPG-6", _("epg right")),
	("TemplatesInfoBarECM-EPG-7", _("epg left")),
	("TemplatesInfoBarECM-EPG-8", _("ecm centre, epg centre")),
	("TemplatesInfoBarECM-EPG-9", _("ecm right, epg left")),
	("TemplatesInfoBarECM-EPG-10", _("ecm left, epg right"))]
epgchannelselection = [
	("TemplatesChannelSelectionInfoEPG-1", _("no")),
	("TemplatesChannelSelectionInfoEPG-2", _("now")),
	("TemplatesChannelSelectionInfoEPG-3", _("now, next")),
	("TemplatesChannelSelectionInfoEPG-4", _("10 programs"))]
infochannelselection = [
	("TemplatesChannelSelectionInfoChannel-1", _("no")),
	("TemplatesChannelSelectionInfoChannel-2", _("picons")),
	("TemplatesChannelSelectionInfoChannel-3", _("picons, channel info"))]
clockpanel = [
	("Clock-1", _("no")),
	("Clock-2", _("12:00")),
	("Clock-3", _("saturday, 01 january 12:00")),
	("Clock-4", _("saturday, 01.01.2010 12:00"))]
dish = [
	("Dish-1", _("on left")),
	("Dish-2", _("on right"))]
scrollbarmode = [
	("showNever", _("no")),
	("showOnDemand", _("yes"))]
fonts = [
	("LiberationSans-Regular", _("regular")),
	("LiberationSans-Bold", _("bold")),
	("LiberationSans-Italic", _("italic")),
	("LiberationSans-BoldItalic", _("bolditalic"))]

if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/TMBD/plugin.pyo")\
	and fileExists("/usr/lib/enigma2/python/Components/Renderer/RatingTmbd.py")\
	and fileExists("/usr/lib/enigma2/python/Components/Renderer/CoverTmbd.py"):
	coverinfopanel = [
	("TemplatesInfoBarInfoMovie-Cover-1", _("no")),
	("TemplatesInfoBarInfoMovie-Cover-2", _("poster right")),
	("TemplatesInfoBarInfoMovie-Cover-3", _("poster left")),
	("TemplatesInfoBarInfoMovie-Cover-4", _("description right")),
	("TemplatesInfoBarInfoMovie-Cover-5", _("description left")),
	("TemplatesInfoBarInfoMovie-Cover-6", _("poster left, description right")),
	("TemplatesInfoBarInfoMovie-Cover-7", _("poster right, description left"))]
	infomovieselection = [
	("TemplatesMovieSelectionInfoMovie-1", _("no")),
	("TemplatesMovieSelectionInfoMovie-2", _("standard")),
	("TemplatesMovieSelectionInfoMovie-3", _("TMDB plugin PIG")),
	("TemplatesMovieSelectionInfoMovie-4", _("TMDB plugin noPIG"))]
else:
	coverinfopanel = [
	("TemplatesInfoBarInfoMovie-Cover-1", _("no"))]
	infomovieselection = [
	("TemplatesMovieSelectionInfoMovie-1", _("no")),
	("TemplatesMovieSelectionInfoMovie-2", _("standard"))]

config.skin.techno = ConfigSubsection()
config.skin.techno.style = ConfigSelection(default="grey", choices = style)
config.skin.techno.numberchannel = ConfigSelection(default="TemplatesNumberCh-1", choices = numberchannel)
config.skin.techno.ecmepgpanel = ConfigSelection(default="TemplatesInfoBarECM-EPG-5", choices = ecmepgpanel)
config.skin.techno.epgchannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoEPG-1", choices = epgchannelselection)
config.skin.techno.infochannelselection = ConfigSelection(default="TemplatesChannelSelectionInfoChannel-1", choices = infochannelselection)
config.skin.techno.coverinfopanel = ConfigSelection(default="TemplatesInfoBarInfoMovie-Cover-1", choices = coverinfopanel)
config.skin.techno.infomovieselection = ConfigSelection(default="TemplatesMovieSelectionInfoMovie-1", choices = infomovieselection)
config.skin.techno.clockpanel = ConfigSelection(default="Clock-1", choices = clockpanel)
config.skin.techno.dish = ConfigSelection(default="Dish-1", choices = dish)
config.skin.techno.scrollbarmode = ConfigSelection(default="showNever", choices = scrollbarmode)
config.skin.techno.fonts = ConfigSelection(default="LiberationSans-Regular", choices = fonts)
config.skin.techno.titlecolor = ConfigSelection(default="#00ffcc33", choices = textcolor)
config.skin.techno.textcolor = ConfigSelection(default="#00f4f4f4", choices = textcolor)
config.skin.techno.avtextcolor = ConfigSelection(default="#008f8f8f", choices = textcolor)
config.skin.techno.textcurcolor = ConfigSelection(default="#000099ff", choices = textcolor)
config.skin.techno.progresscolor = ConfigSelection(default="yellow", choices = style)

class SetupTechnoHD(ConfigListScreen, Screen):
	skin = """
	<screen name="SetupTechnoHD" position="0,0" size="1280,720" title=" " flags="wfNoBorder">
		<ePixmap position="0,0" zPosition="-1" size="1280,720" pixmap="Techno_hd/style/greymenu_1.png" />
		<widget source="Title" render="Label" position="45,38" size="720,36" font="Regular; 30" halign="center" transparent="1" foregroundColor="#00ffcc33" backgroundColor="background" borderWidth="2" />
		<ePixmap position="775,450" zPosition="1" size="500,150" pixmap="Techno_hd/logo.png" alphatest="blend" />
		<widget name="config" position="50,95" size="710,540" scrollbarMode="showOnDemand" selectionPixmap="Techno_hd/style/greysel.png" transparent="1" />
		<widget source="version_sk" render="Label" position="930,615" size="200,22" font="Regular;20" halign="right" valign="center" backgroundColor="background" foregroundColor="#00f4f4f4" transparent="1" zPosition="2" />
		<widget source="info_sk" render="Label" position="1150,615" size="80,22" font="Regular;20" halign="left" valign="center" backgroundColor="background" foregroundColor="#008f8f8f" transparent="1" zPosition="2" />
		<widget source="info_com" render="Label" position="800,450" size="450,150" font="Regular;22" halign="center" valign="center" backgroundColor="background" foregroundColor="#008f8f8f" transparent="1" zPosition="2" />
		<widget source="key_red" render="Label" position="56,663" size="270,40" font="Regular; 22" halign="center" valign="top" backgroundColor="background" transparent="1" zPosition="3" foregroundColor="#00f4f4f4" borderWidth="1" />
		<widget source="key_green" render="Label" position="355,663" size="270,40" font="Regular; 22" halign="center" valign="top" backgroundColor="background" transparent="1" zPosition="3" foregroundColor="#00f4f4f4" borderWidth="1" />
		<widget source="key_blue" render="Label" position="951,663" size="270,40" font="Regular; 22" halign="center" valign="top" backgroundColor="background" transparent="1" zPosition="3" foregroundColor="#00f4f4f4" borderWidth="1" />
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

		self["actions"] = ActionMap(["OkCancelActions", "ColorActions", "EPGSelectActions"],{"ok": self.save, "cancel": self.exit, "red": self.exit, "green": self.save, "blue": self.install, "info": self.about}, -1)
		self["key_red"] = StaticText(_("Cancel"))
		self["key_green"] = StaticText(_("Save"))
		self["key_blue"] = StaticText(_("Install components"))
		self["Title"] = StaticText(_("Setup TechnoHD"))
		self["version_sk"] = StaticText(_("Version skin:"))
		self["info_sk"] = StaticText()
		self["info_com"] = StaticText()

		self.infosk()
		self.infocom()

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
					self["info_sk"].text = line.split()[1]
				except:
					self["info_sk"].text = " "
				break

	def infocom(self):
		if fileExists("/usr/lib/enigma2/python/Plugins/Extensions/TMBD/plugin.pyo")\
			and not fileExists("/usr/lib/enigma2/python/Components/Renderer/RatingTmbd.py")\
			and not fileExists("/usr/lib/enigma2/python/Components/Renderer/CoverTmbd.py"):
			self["info_com"] = StaticText(_("No install components TMBD !!!"))
		elif fileExists("/usr/lib/enigma2/python/Components/Converter/AlwaysTrue.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/CaidInfo2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/CamdInfo3.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ConverterRotator.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/EventName2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/FrontendInfo2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ProgressDiskSpaceInfo.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/RouteInfo.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/RWeather.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceInfoEX.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Converter/ServiceName2.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Renderer/PiconUni.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Renderer/RendVolumeText.py")\
			and fileExists("/usr/lib/enigma2/python/Components/Renderer/Watches.py"):
			self["info_com"] = StaticText(_(" "))
		else:
			self["info_com"] = StaticText(_("No install components !!! \nPress blue button to install !!!"))

	def save(self):
		skinpath = "/usr/share/enigma2/Techno_hd/"
	# save config
		for x in self["config"].list:
			x[1].save()
		try:
	# default skin
			os.system("cp %sdefskin.xml %sskin.xml" % (skinpath, skinpath))
	# color`s text
			os.system("sed -i 's/#10ffcc33/%s/w' %sskin.xml" % (config.skin.techno.titlecolor.value, skinpath))
			os.system("sed -i 's/#10f4f4f4/%s/w' %sskin.xml" % (config.skin.techno.textcolor.value, skinpath))
			os.system("sed -i 's/#108f8f8f/%s/w' %sskin.xml" % (config.skin.techno.avtextcolor.value, skinpath))
			os.system("sed -i 's/#100099ff/%s/w' %sskin.xml" % (config.skin.techno.textcurcolor.value, skinpath))
	# fonts	
			os.system("sed -i 's/LiberationSans-Regular/%s/w' %sskin.xml" % (config.skin.techno.fonts.value, skinpath))
	# number channel
			os.system("sed -i 's/%s/TemplatesNumberCh/w' %sskin.xml" % (config.skin.techno.numberchannel.value, skinpath))
	# ecm-epg panel
			os.system("sed -i 's/%s/TemplatesInfoBarECM-EPG/w' %sskin.xml" % (config.skin.techno.ecmepgpanel.value, skinpath))
	# epg channel selection
			os.system("sed -i 's/%s/TemplatesChannelSelectionInfoEPG/w' %sskin.xml" % (config.skin.techno.epgchannelselection.value, skinpath))
	# info channel selection
			os.system("sed -i 's/%s/TemplatesChannelSelectionInfoChannel/w' %sskin.xml" % (config.skin.techno.infochannelselection.value, skinpath))
	# cover info panel
			os.system("sed -i 's/%s/TemplatesInfoBarInfoMovie-Cover/w' %sskin.xml" % (config.skin.techno.coverinfopanel.value, skinpath))
	# info movie selection
			os.system("sed -i 's/%s/TemplatesMovieSelectionInfoMovie/w' %sskin.xml" % (config.skin.techno.infomovieselection.value, skinpath))
	# clock panel menu
			os.system("sed -i 's/%s/Clock/w' %sskin.xml" % (config.skin.techno.clockpanel.value, skinpath))
	# dish
			os.system("sed -i 's/%s/Dish/w' %sskin.xml" % (config.skin.techno.dish.value, skinpath))
	# scrollbar
			os.system("sed -i 's/showNever/%s/w' %sskin.xml" % (config.skin.techno.scrollbarmode.value, skinpath))
	# style progress
			os.system("sed -i 's/yellowprogress/%sprogress/w' %sskin.xml" % (config.skin.techno.progresscolor.value, skinpath))
			os.system("sed -i 's/yellowprogress_big/%sprogress_big/w' %sskin.xml" % (config.skin.techno.progresscolor.value, skinpath))
	# style skin`s
			os.system("sed -i 's/greyinfobar/%sinfobar/w' %sskin.xml" % (config.skin.techno.style.value, skinpath))
			os.system("sed -i 's/greymenu/%smenu/w' %sskin.xml" % (config.skin.techno.style.value, skinpath))
			os.system("sed -i 's/greysel/%ssel/w' %sskin.xml" % (config.skin.techno.style.value, skinpath))
			os.system("sed -i 's/greyvolume/%svolume/w' %sskin.xml" % (config.skin.techno.style.value, skinpath))
			os.system("sed -i 's/greydownload/%sdownload/w' %sskin.xml" % (config.skin.techno.style.value, skinpath))
	# end
		except:
			self.session.open(MessageBox, _("Error by processing !!!"), MessageBox.TYPE_ERROR)
		self.session.openWithCallback(self.restart, MessageBox,_("Do you want to restart the GUI now ?"), MessageBox.TYPE_YESNO)

	def install(self):
		pluginpath = "/usr/lib/enigma2/python/Plugins/Extensions/"
		componentspath = "/usr/lib/enigma2/python/Components/"
		try:
	# install converter
			os.system("cp %sSetupTechnoHD/components/AlwaysTrue.py %sConverter/AlwaysTrue.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/CaidInfo2.py %sConverter/CaidInfo2.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/CamdInfo3.py %sConverter/CamdInfo3.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/ConverterRotator.py %sConverter/ConverterRotator.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/EventName2.py %sConverter/EventName2.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/FrontendInfo2.py %sConverter/FrontendInfo2.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/ProgressDiskSpaceInfo.py %sConverter/ProgressDiskSpaceInfo.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/RouteInfo.py %sConverter/RouteInfo.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/ServiceInfoEX.py %sConverter/ServiceInfoEX.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/ServiceName2.py %sConverter/ServiceName2.py" % (pluginpath, componentspath))
	# install renderer
			os.system("cp %sSetupTechnoHD/components/PiconUni.py %sRenderer/PiconUni.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/RendVolumeText.py %sRenderer/RendVolumeText.py" % (pluginpath, componentspath))
			os.system("cp %sSetupTechnoHD/components/Watches.py %sRenderer/Watches.py" % (pluginpath, componentspath))
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
		self.session.open(MessageBox, _("Skin TechnoHD\nDeveloper: Sirius0103 \nHomepage: www.gisclub.tv \n\nDonate:\nWMZ  Z395874509364\nWME  E284580190260\nWMR  R213063691482\nWMU  U658742613505"), MessageBox.TYPE_INFO)

def main(session, **kwargs):
	session.open(SetupTechnoHD)

def Plugins(**kwargs):
	return PluginDescriptor(name=_("Setup TechnoHD"),
	description=_("Setup skin TechnoHD"),
	where = [PluginDescriptor.WHERE_PLUGINMENU, PluginDescriptor.WHERE_EXTENSIONSMENU],
	icon="plugin.png",
	fnc=main)
