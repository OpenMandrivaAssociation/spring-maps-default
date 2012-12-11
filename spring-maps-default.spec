
%define name	spring-maps-default
%define version	1.0
%define rel	2

Summary:	Default maps for Spring
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Group:		Games/Strategy
URL:		http://taspring.clan-sy.com/
# Maps listed in spring/installer/sections/maps.nsh.
Source:		http://buildbot.no-ip.org/~yokozar/apt/pool/main/s/spring-maps-default/%{name}_%{version}.tar.gz
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-root
Requires:	spring
Conflicts:	spring-data < 0.75
BuildArch:	noarch

%description
Default maps for Spring.

%prep
%setup -q

%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_gamesdatadir}/spring/maps
install -m644 *.sd7 %{buildroot}%{_gamesdatadir}/spring/maps

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc debian/changelog debian/copyright
%{_gamesdatadir}/spring/maps/*.sd7


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0-2mdv2010.0
+ Revision: 434079
- rebuild

* Sat Jan 05 2008 Anssi Hannula <anssi@mandriva.org> 1.0-1mdv2008.1
+ Revision: 145684
- initial Mandriva release

