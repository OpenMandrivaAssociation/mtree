%define debug_package %{nil}

Name:    mtree
Version: 2.7
Release: 8
Summary: Map a directory hierarchy
License: BSD
Group:   System/Base
Url:     http://www-db.deis.unibo.it/Mtree/
Source:  %{name}-%{version}.cvs.tar.bz2
Patch:   mtree-3.1-owl-linux.patch
Patch2:  %{name}-%{version}.cvs-alt-getlogin.patch
Patch3:  mtree-3.1-owl-fixes.patch

BuildRequires: openssl-devel

%description
The utility %name compares the file hierarchy rooted in the current
directory against a specification read from the standard input.
Messages are written to the standard output for any files whose
characteristics do not match the specification, or which are
missing from either the file hierarchy or the specification.

%prep
%setup -q -n %{name}-%{version}.cvs
%patch -p1
%patch2 -p1
%patch3 -p1

%build
make -C usr.sbin/%{name}

%install
install -p -m755 -D usr.sbin/%{name}/%{name} %{buildroot}%{_sbindir}/%{name}
install -p -m644 -D usr.sbin/%{name}/%{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8

%files
%{_sbindir}/*
%{_mandir}/man?/*
