Name: kaboom
Version: 1.1.2
Release: %mkrel 2
Summary: The Debian KDE settings migration tool
License: GPL
Url: http://pkg-kde.alioth.debian.org/kaboom.html
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

