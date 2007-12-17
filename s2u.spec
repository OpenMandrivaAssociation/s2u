Summary: System to user tools
Name: s2u
Version: 0.8
Release: %mkrel 1
URL: http://www.mandrivalinux.com/
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/Other
BuildRequires: dbus-glib-devel
BuildRequires: gtk+2-devel
Requires: dbus
Requires: initscripts >= 7.06-52mdk

%description
Use dbus to communicate between from the system to the users.

%prep
%setup -q

%build
%make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README AUTHORS LICENSE
%_bindir/s2u
%_sysconfdir/X11/xinit.d/s2u
%_sysconfdir/sysconfig/network-scripts/hostname.d/s2u
%config(noreplace) %_sysconfdir/dbus-1/system.d/*.conf

# MAKE THE CHANGES IN SVN: NO PATCH OR SOURCE ALLOWED

