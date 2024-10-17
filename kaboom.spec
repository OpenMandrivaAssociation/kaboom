Name: kaboom
Version: 1.1.2
Release: 3
Summary: The Debian KDE settings migration tool
License: GPL
Url: https://pkg-kde.alioth.debian.org/kaboom.html
Group: Graphical desktop/KDE
Source0: http://ftp.de.debian.org/debian/pool/main/k/kaboom/%{name}_%{version}.tar.gz 
Source1: CMakeLists.txt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: qt4-devel
BuildRequires: cmake

%description
The Debian KDE settings migration tool.

%files
%defattr(-,root,root,-)
%{qt4bin}/*
%_datadir/kaboom

#-----------------------------------------------------------------

%prep
%setup -q 
cp %{SOURCE1} .

%build
%cmake_qt4

%make

%install
rm -rf %buildroot

%makeinstall_std -C build

%clean
rm -rf %buildroot



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2mdv2011.0
+ Revision: 619874
- the mass rebuild of 2010.0 packages

* Thu Oct 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1.1.2-1mdv2010.0
+ Revision: 452272
- imported package kaboom

