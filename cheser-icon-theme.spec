Summary:	Mix of different Tango-style icons for GNOME 3.8 and Xfce 4.10.
Name:		cheser-icon-theme
Version:	3.8.0
Release:	1
License:	GPL
Group:		Themes
Source0:	https://dl.dropbox.com/u/9335585/Icons/%{name}-%{version}.tar.gz
# Source0-md5:	0e86e06e37bb4f2850bee7ed1226c4f0
BuildRequires:	/usr/bin/gtk-update-icon-cache
BuildArch:	noarch
Requires:	gnome-icon-theme
Provides:	xdg-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mix of different Tango-style icons for GNOME 3.8 and Xfce 4.10.
Based on GNOME and Xfce icons. Used Mist, Tango, Tangerine, Sonar icon
themes; icons from Ubuntu, Fedora, OpenSuse.

%prep
%setup -q

%build

%install
install -d $RPM_BUILD_ROOT%{_iconsdir}

cp -ar Cheser $RPM_BUILD_ROOT%{_iconsdir}

gtk-update-icon-cache -ft $RPM_BUILD_ROOT%{_iconsdir}/Cheser

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_iconsdir}/Cheser

