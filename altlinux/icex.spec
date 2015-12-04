# -*- mode: rpm-spec; coding: utf-8 -*-
%define realname icewm
%define alt altlinux
%def_with menu
%define gitrev .gitd490895

Name: %realname
Version: 1.3.11
Release: alt8.1

Summary: X11 Window Manager
Group: Graphical desktop/Icewm
License: LGPLv2
Url: http://www.icewm.org
Packager: Oleg Ivanov <Leo-sp150@yandex.ru>

Provides: %realname = %version-%release
Provides: %realname-light = %version-%release
Requires: design-%realname >= 1.0-alt6
Obsoletes: %realname-light < %version-%release

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

Source12: %alt/icewm-old-changelog
Source13: %alt/icewm_logout
Source14: %alt/icewm_shutdown
Source15: %alt/icewm_reboot
Source16: %alt/icewm_restart
Source17: %alt/icewm_startup

BuildRequires(pre): rpm-macros-cmake
# Automatically added by buildreq on Sat Apr 11 2015
BuildRequires: OpenSP cmake gcc-c++ libSM-devel libXext-devel libXft-devel
BuildRequires: libXinerama-devel libXrandr-devel libalsa-devel libesd-devel
BuildRequires: libgdk-pixbuf-devel libsndfile-devel linuxdoc-tools perl-parent

%if_without menu
BuildPreReq: desktop-file-utils
%endif

Conflicts: icewm-githubmod

%description
 Window Manager for X Window System. Can emulate the look of Windows'95, OS/2
Warp 3,4, Motif or the Java Metal GUI. Tries to take the best features of the
above systems. Features multiple workspaces, opaque move/resize, task bar,
window list, mailbox status, digital clock. Fast and small.
 This release is based on alternative source, based on a community fork
maintained on Github https://github.com/bbidulock/icewm

Recommends: iftop, mutt

%prep
%setup -n %name

%build
%cmake	-DCFGDIR=%_sysconfdir/X11/%realname -DPREFIX=%_prefix \
	-DLIBDIR=%_x11x11dir/%realname -DCONFIG_GUIEVENTS=on  \
	-DICESOUND="ALSA,OSS,ESound"
pushd BUILD
%make_build
popd

%install
pushd BUILD
%makeinstall_std
popd
cp %buildroot%_x11x11dir/%realname/preferences %buildroot%_x11x11dir/%realname/preferences

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
install -m644 %SOURCE12 icewm-old-changelog.bz2

mkdir -p %buildroot%_sysconfdir/X11/%realname

mkdir -p %buildroot%_sysconfdir/X11/%realname/startup.d
mkdir -p %buildroot%_sysconfdir/X11/%realname/logout.d
mkdir -p %buildroot%_sysconfdir/X11/%realname/shutdown.d
mkdir -p %buildroot%_sysconfdir/X11/%realname/reboot.d
mkdir -p %buildroot%_sysconfdir/X11/%realname/restart.d

install -m 755 %SOURCE13 %buildroot%_sysconfdir/X11/%realname/icewm_logout
install -m 755 %SOURCE14 %buildroot%_sysconfdir/X11/%realname/icewm_shutdown
install -m 755 %SOURCE15 %buildroot%_sysconfdir/X11/%realname/icewm_reboot
install -m 755 %SOURCE16 %buildroot%_sysconfdir/X11/%realname/icewm_restart
install -m 755 %SOURCE17 %buildroot%_sysconfdir/X11/%realname/icewm_startup

%if_without menu
desktop-file-install --vendor alt --dir %buildroot%_desktopdir %SOURCE10
%endif

%find_lang  %realname

# remove unpackaged files
rm -f %buildroot/%_bindir/%realname-set-gnomewm
rm -rf %buildroot/%_datadir/doc/%realname
rm -rf %buildroot/%_datadir/xsessions

%files -f %realname.lang
%dir %_sysconfdir/X11/%realname
%config(noreplace) %_sysconfdir/menu-methods/*
%_sysconfdir/X11/wmsession.d/*
%_bindir/*
%dir %_x11x11dir/%realname
%_x11x11dir/%realname/icons
%_x11x11dir/%realname/ledclock
%_x11x11dir/%realname/mailbox
%_x11x11dir/%realname/taskbar
%_x11x11dir/%realname/keys
%_x11x11dir/%realname/menu
%_x11x11dir/%realname/preferences
%_x11x11dir/%realname/programs
%_x11x11dir/%realname/toolbar
%_x11x11dir/%realname/winoptions
%dir %_sysconfdir/X11/%realname/startup.d
%dir %_sysconfdir/X11/%realname/logout.d
%dir %_sysconfdir/X11/%realname/shutdown.d
%dir %_sysconfdir/X11/%realname/reboot.d
%dir %_sysconfdir/X11/%realname/restart.d
%config(noreplace) %_sysconfdir/X11/%realname/icewm_logout
%config(noreplace) %_sysconfdir/X11/%realname/icewm_shutdown
%config(noreplace) %_sysconfdir/X11/%realname/icewm_reboot
%config(noreplace) %_sysconfdir/X11/%realname/icewm_restart
%config(noreplace) %_sysconfdir/X11/%realname/icewm_startup
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

%doc AUTHORS NEWS README.ALT README.md BUILD/doc/*.html icewm-old-changelog.bz2

%changelog
* Mon Nov 28 2015 Oleg Ivanov <Leo-sp150@yandex.ru> 1.3.11-alt8.1
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
