Name:    symlinks
Version: 1.4
Release: 23
Summary: Scan or change symbolic links
License: Copyright only
URL:     http://ibiblio.org/pub/Linux/utils/file/
Source0: http://ibiblio.org/pub/Linux/utils/file/%{name}-%{version}.tar.gz
Source1: symlinks-LICENSE.txt

BuildRequires: gcc

Patch1: symlinks-coverity-readlink.patch
Patch2: symlinks-coverity-overrun-dynamic.patch

%description
Scans directories for symbolic links, and identifies dangling,
relative, absolute, messy, and other_fs links.  Can optionally
change absolute links to relative within a given filesystem.

%prep
%autosetup -p1 -n %{name}-%{version}
cp %{SOURCE1} .

%build
%make_build CFLAGS="%{optflags} %{build_ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man8
install -m 755 symlinks $RPM_BUILD_ROOT%{_bindir}
install -m 644 symlinks.8 $RPM_BUILD_ROOT%{_mandir}/man8

%check

%pre

%preun

%post

%postun

%files
%doc symlinks-LICENSE.txt
%{_bindir}/symlinks
%{_mandir}/man8/symlinks.8*


%changelog
* Sat Sep 21 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.4-23
- Modify spec error information

 Sat Sep 07 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.4-22
- Package init
