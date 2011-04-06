Summary: System to user tools
Name: s2u
Version: 0.9.2
Release: %mkrel 2
URL: http://www.mandrivalinux.com/
Source0: %{name}-%{version}.tar.bz2
Patch0: s2u-0.9.2-new-libnotify.patch
License: GPLv2+
Group: Graphical desktop/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: dbus-glib-devel
BuildRequires: gtk+2-devel
BuildRequires: libnotify-devel >= 0.7
Requires: dbus
Requires: initscripts >= 7.06-52mdk

%description
Use dbus to communicate between from the system to the users.

%prep
%setup -q
%apply_patches

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags}"

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


