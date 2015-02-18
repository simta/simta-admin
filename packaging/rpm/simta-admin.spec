Summary: Administrative scripts for simta
Name: simta-admin
Version: 1.1
Release: 1%{?dist}
License: BSD
Group: Applications/Internet
URL: https://github.com/simta
Source0: https://github.com/simta/simta-admin/archive/%{name}-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: bash >= 3.0
Requires: findutils
Requires: grep
Requires: gawk
Requires: gzip
Requires: coreutils
Requires: sed
BuildRequires: setup

%description
These scripts are used by admins to deal with simta.

%prep
%setup

%install
install -m 755 simqclean %{buildroot}%{_sbindir}/simqclean
install -m 755 simtamaint %{buildroot}%{_sbindir}/simtamaint
install -m 755 simqc %{buildroot}%{_bindir}/simqc
install -m 755 simqgrep %{buildroot}%{_bindir}/simqgrep
install -m 755 simtrans %{buildroot}%{_bindir}/simtrans

%files
%defattr(-,root,root,-)
%{_sbindir}/simqclean
%{_sbindir}/simtamaint
%{_bindir}/simqc
%{_bindir}/simqgrep
%{_bindir}/simtrans

%changelog
* %(date "+%a %b %d %Y") (Automated RPM build) - %{version}-%{release}
- See git log for actual changes.
