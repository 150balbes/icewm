# -*- mode: rpm-spec; coding: utf-8 -*-
%define realname icewm
%define alt altlinux
%def_with menu

Name: icex
Version: 1.3.12
Release: alt2.1

Summary: X11 Window Manager
Group: Graphical desktop/Icewm
License: LGPLv2
Url: http://www.icewm.org
Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Provides: %realname = %version-%release
#Provides: %realname-light = %version-%release
#Requires: design-%realname >= 1.0-alt6
#Obsoletes: %realname-light < %version-%release

Source0: %name.tar
Source1: %alt/%realname.menu
Source2: %alt/%realname.menu-method
Source3: %alt/%realname-16.png
Source4: %alt/%realname-32.png
Source5: %alt/%realname-48.png

Source7: %alt/IceWM.xpm
Source8: %alt/%realname.wmsession
Source9: %alt/README.ALT
Source10: %alt/%realname.desktop

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Sat Apr 11 2015
BuildRequires: OpenSP cmake gcc-c++ libSM-devel libXext-devel libXft-devel
BuildRequires: libXinerama-devel libXrandr-devel libalsa-devel libesd-devel
BuildRequires: libgdk-pixbuf-devel libsndfile-devel linuxdoc-tools perl-parent

%if_without menu
BuildPreReq: desktop-file-utils
%endif

Conflicts: icewm-githubmod icewm-x-githubmod

%description
 Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.
 This release is based on alternative source, based on a community fork
maintained on Github https://github.com/bbidulock/icewm

Recommends: iftop, mutt

%package theme-default
Group: Graphical desktop/Icewm
Summary: Extra themes for icewm default
Summary(ru_RU.UTF-8): Дефолтные темы для IceWM
###Requires: %name > 1.3.11
AutoReq: no
BuildArch: noarch

%description theme-default
Extra themes for icewm default
%description -l ru_RU.UTF-8 theme-default
Темы для IceWM по умолчанию.


%prep
%setup -n %name

%build
%cmake	-DCFGDIR=%_sysconfdir/%realname -DPREFIX=%_prefix \
	-DLIBDIR=%_datadir/%realname -DCONFIG_GUIEVENTS=on  \
	-DICESOUND="ALSA,OSS,ESound"
pushd BUILD
%make_build
popd

%install
pushd BUILD
%makeinstall_std
popd

%if_with menu
mkdir -p %buildroot%_menudir
install -m 644 %SOURCE1 %buildroot%_menudir/%realname
%endif
mkdir -p %buildroot%_sysconfdir/menu-methods
install -m 755 %SOURCE2 %buildroot%_sysconfdir/menu-methods/%realname

install -pD -m644 %SOURCE3 %buildroot%_miconsdir/%realname.png
install -pD -m644 %SOURCE4 %buildroot%_niconsdir/%realname.png
install -pD -m644 %SOURCE5 %buildroot%_liconsdir/%realname.png
install -pD -m644 %SOURCE7 %buildroot%_pixmapsdir/IceWM.xpm
install -pD -m644 %SOURCE8 %buildroot%_sysconfdir/X11/wmsession.d/04IceWM
install -m644 %SOURCE9 README.ALT

mkdir -p %buildroot%_sysconfdir/%realname

%if_without menu
desktop-file-install --vendor alt --dir %buildroot%_desktopdir %SOURCE10
%endif

%find_lang  %realname

# remove unpackaged files
rm -f %buildroot/%_bindir/%realname-set-gnomewm
rm -rf %buildroot/%_datadir/doc/%realname
rm -rf %buildroot/%_datadir/xsessions

%files -f %realname.lang
%dir %_sysconfdir/%realname
%dir %_sysconfdir/%realname/logout_d
%dir %_sysconfdir/%realname/shutdown_d
%dir %_sysconfdir/%realname/reboot_d
%dir %_sysconfdir/%realname/restart_d
%dir %_sysconfdir/%realname/startup_d
%_sysconfdir/%realname/logout_d
%_sysconfdir/%realname/shutdown_d
%_sysconfdir/%realname/reboot_d
%_sysconfdir/%realname/restart_d
%_sysconfdir/%realname/startup_d
%config(noreplace) %_sysconfdir/menu-methods/*
%_sysconfdir/X11/wmsession.d/*
%_bindir/*
%_datadir/%realname/themes/default/*
%_datadir/%realname/icons
%_datadir/%realname/ledclock
%_datadir/%realname/mailbox
%_datadir/%realname/taskbar
%_datadir/%realname/keys
%_datadir/%realname/menu
%_datadir/%realname/preferences
%_datadir/%realname/programs
%_datadir/%realname/toolbar
%_datadir/%realname/winoptions
%_sysconfdir/%realname/icewm_logout
%_sysconfdir/%realname/icewm_shutdown
%_sysconfdir/%realname/icewm_reboot
%_sysconfdir/%realname/icewm_restart
%_sysconfdir/%realname/icewm_startup
%if_with menu
%_menudir/*
%else
%_desktopdir/*
%endif
%_niconsdir/*
%_miconsdir/*
%_liconsdir/*
%_pixmapsdir/*
%_man1dir/*

%doc AUTHORS NEWS README.ALT README.md BUILD/doc/*.html

%files theme-default
%_datadir/%realname/themes/Infadel2
%_datadir/%realname/themes/gtk2
%_datadir/%realname/themes/metal2
%_datadir/%realname/themes/motif
%_datadir/%realname/themes/nice
%_datadir/%realname/themes/nice2
%_datadir/%realname/themes/warp3
%_datadir/%realname/themes/warp4
%_datadir/%realname/themes/win95
%_datadir/%realname/themes/yellowmotif
%_datadir/%realname/themes/icedesert

%changelog
* Mon Dec 19 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.12-alt2.1
- add default theme background

* Mon Dec 19 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.12-alt2
- Supports settings on and off tray and background

* Mon Dec 18 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.12-alt1.1
- dell icewm-session

* Mon Dec 18 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.12-alt1
- edit default theme

* Mon Dec 13 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt10.3
- move script

* Mon Dec 11 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt10.2
- add defaults themes icedesert

* Mon Dec 10 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt10.1
- edit fdomenu.cc

* Mon Dec 09 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt10
- edit default settings

* Mon Dec 05 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt9.1
- edit background

* Mon Dec 05 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt9
- new version

* Mon Nov 28 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt8.1
- edit libdir
- delete icewm-session
- add script icewm_logout icewm_reboot icewm_restart icewm_shutdowun icewm_startup

* Mon Nov 22 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt6
- added Obsoletes

* Mon Oct 05 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt3
- added Obsoletes
- added README.ALT
- fixed Url

* Tue Sep 22 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.11-alt1
- 1.3.11 release

* Sun Jul 05 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.10-alt1
- 1.3.10 release
- updated reboot/shutdown commands for use with systemd and sysvinit
- extended strong control of startup sequence in icewm-session

* Mon May 04 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt4.git960629d
- added forgotten requires to design-icewm

* Thu Apr 30 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt3.git960629d
- git snapshot 960629d
- old changelog cut off to separate file
- added conflict to icewm-light

* Tue Apr 14 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt2.gite97394f
- added support fd.o-style icons

* Tue Apr 14 2015 Dmitriy Khanzhin <jinn@altlinux.org> 1.3.9-alt1.gite97394f
- initial build for altlinux
