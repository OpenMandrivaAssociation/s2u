Summary:	System to user tools
Name:		s2u
Version:	0.9.2
Release:	18
URL:		http://www.mandrivalinux.com/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		s2u-0.9.2-new-libnotify.patch
License:	GPLv2+
Group:		Graphical desktop/Other
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libnotify)
Requires:	dbus

%description
Use dbus to communicate between from the system to the users.

%prep
%setup -q
%autopatch -p1

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

%install
%make_install

%files
%doc ChangeLog README AUTHORS LICENSE
%_bindir/s2u
%_sysconfdir/X11/xinit.d/s2u
%_sysconfdir/sysconfig/network-scripts/hostname.d/s2u
%config(noreplace) %_sysconfdir/dbus-1/system.d/*.conf
