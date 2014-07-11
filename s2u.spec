Summary:	System to user tools
Name:		s2u
Version:	0.9.2
Release:	10
URL:		http://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		s2u-0.9.2-new-libnotify.patch
License:	GPLv2+
Group:		Graphical desktop/Other
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libnotify)
Requires:	dbus
Requires:	initscripts >= 7.06-52mdk

%description
Use dbus to communicate between from the system to the users.

%prep
%setup -q
%apply_patches

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std

%files
%doc ChangeLog README AUTHORS LICENSE
%_bindir/s2u
%_sysconfdir/X11/xinit.d/s2u
%_sysconfdir/sysconfig/network-scripts/hostname.d/s2u
%config(noreplace) %_sysconfdir/dbus-1/system.d/*.conf

# MAKE THE CHANGES IN SVN: NO PATCH OR SOURCE ALLOWED




%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Wed Apr 06 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.2-2mdv2011.0
+ Revision: 650899
- patch for libnotify 0.7
- update license

* Thu Feb 17 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.9.2-1
+ Revision: 638185
- New version: 0.9.2

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-3mdv2011.0
+ Revision: 607481
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-2mdv2010.1
+ Revision: 523956
- rebuilt for 2010.1

* Tue Aug 18 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.9.1-1mdv2010.0
+ Revision: 417796
- 0.9.1
- implemented generic user notifications (for netprofile and other applications)

* Tue Mar 24 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.9-2mdv2009.1
+ Revision: 360788
- fixed libnotify requires on x86_64 arch

* Tue Mar 24 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.9-1mdv2009.1
+ Revision: 360776
- Requiring libnotify-devel to get both libnotify1-devel and lib64notify1-devel.
- 0.9
 - Added support for MSEC notifications.
 - Merged Patch0.

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8-3mdv2009.1
+ Revision: 317586
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.8-2mdv2009.0
+ Revision: 225344
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1mdv2008.1-current
+ Revision: 126919
- kill re-definition of %%buildroot on Pixel's request


* Tue Feb 20 2007 Frederic Crozat <fcrozat@mandriva.com> 0.8-1mdv2007.0
+ Revision: 123110
- Release 0.8
- svn cleanup
- rename xinit.d script and don't call s2u in debug mode
- Import s2u

* Sat Aug 05 2006 Frederic Crozat <fcrozat@mandriva.com> 0.7-3mdv2007.0
- Fix buildrequires

* Wed Aug 02 2006 Frederic Crozat <fcrozat@mandriva.com> 0.7-2mdv2007.0
- Rebuild with latest dbus

* Tue May 30 2006 Frederic Crozat <fcrozat@mandriva.com> 0.7-1mdv2007.0
- Fix for modular xorg
- Fix crash when parsing cookie fails

* Fri Jan 27 2006 Frederic Lepied <flepied@mandriva.com> 0.6-1mdk
- switch to Mandriva
- log actions by default
- mkrel

* Wed Jan 25 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5-5mdk
- Rebuild for latest dbus

* Sat Oct 29 2005 Frederic Crozat <fcrozat@mandriva.com> 0.5-4mdk
- Rebuild with new dbus

* Wed Mar 09 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-3mdk 
- add new signal to start update-menus if requested by system
- remove dbus-x11 requires

* Tue Mar 08 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-2mdk 
- connect to X server, so s2u exits when X exits

* Mon Mar 07 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.5-1mdk 
- Release 0.5 :
 no longer use session bus, use system bus instead (fix Mdk bug #13166)

* Tue Oct 19 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.4-1mdk
- lib64 fixes

* Thu Aug 26 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.3-1mdk
- don't put noreplace on these scripts
- changes in cvs
- use $DISPLAY in temp filename

* Thu Aug 26 2004 Götz Waschk <waschk@linux-mandrake.com> 0.2-2mdk
- mark config files
- fix file list
- drop prefix
- fix buildrequires

* Thu Aug 19 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.2-1mdk
- add a require on dbus
- put temporary file in /tmp instead of /var/tmp and use a naming
  which includes the user name

* Wed Aug 04 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.1-2mdk
- fix buildrequires

* Sun Aug 01 2004 Frederic Lepied <flepied@mandrakesoft.com> 0.1-1mdk
- monitor hostname change

