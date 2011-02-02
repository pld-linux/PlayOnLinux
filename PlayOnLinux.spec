Summary:	GUI for managing Windows and DOS programs under linux
Name:		PlayOnLinux
Version:	3.8.8
Release:	0.2
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://www.playonlinux.com/script_files/PlayOnLinux/%{version}/%{name}_%{version}.tar.gz
# Source0-md5:	1bc12abd0a3d2426ea35e6887e9d3bd5
Source1:	%{name}.desktop
URL:		http://www.playonlinux.com/en/
Requires:	python-wxPython
Requires:	wine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PlayOnLinux is a piece of sofware which allows you to easily install
and use numerous games and apps designed to run with Microsoft®
Windows.

%prep
%setup -q -n playonlinux

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir}}
cp -r * $RPM_BUILD_ROOT%{_datadir}/%{name}
install %SOURCE1 $RPM_BUILD_ROOT%{_desktopdir}
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/{CHANGELOG,LICENCE}

for exec in playonlinux*; do
(cat << EOF
#!/bin/bash
%{_datadir}/%{name}/$exec $@

EOF
) > $RPM_BUILD_ROOT%{_bindir}/$exec
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/playonlinux*
%attr(755,root,root) %{_datadir}/%{name}/playonlinux*
%{_datadir}/%{name}/bash
%{_datadir}/%{name}/etc
%{_datadir}/%{name}/lang
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/python
%{_datadir}/%{name}/themes
%{_desktopdir}/%{name}.desktop
