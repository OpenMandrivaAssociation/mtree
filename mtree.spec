Name: mtree
Version: 2.7
Release: %mkrel 6

Summary: Map a directory hierarchy
License: BSD
Group: System/Base
Url: http://www-db.deis.unibo.it/Mtree/
Source: %name-%{version}.cvs.tar.bz2
Patch: mtree-3.1-owl-linux.patch
Patch2: %name-%{version}.cvs-alt-getlogin.patch
Patch3: mtree-3.1-owl-fixes.patch

BuildRequires: openssl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The utility %name compares the file hierarchy rooted in the current
directory against a specification read from the standard input.
Messages are written to the standard output for any files whose
characteristics do not match the specification, or which are
missing from either the file hierarchy or the specification.

%prep
%setup -q -n %name-%{version}.cvs
%patch -p1
%patch2 -p1
%patch3 -p1

%build
make -C usr.sbin/%name

%install
rm -rf $RPM_BUILD_ROOT
install -p -m755 -D usr.sbin/%name/%name $RPM_BUILD_ROOT%_sbindir/%name
install -p -m644 -D usr.sbin/%name/%name.8 $RPM_BUILD_ROOT%_mandir/man8/%name.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_sbindir/*
%_mandir/man?/*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.7-6mdv2011.0
+ Revision: 612950
- the mass rebuild of 2010.1 packages

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 2.7-5mdv2010.1
+ Revision: 536599
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.7-4mdv2010.0
+ Revision: 430114
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.7-3mdv2009.0
+ Revision: 253068
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 21 2007 Jérôme Soyer <saispo@mandriva.org> 2.7-1mdv2008.1
+ Revision: 110893
- import mtree


