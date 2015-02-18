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
Requires: coreutils
Requires: findutils
Requires: gawk
Requires: grep
Requires: gzip
Requires: net-tools
Requires: sed
Requires: simta
Requires: util-linux
BuildRequires: setup

%description
These scripts are used by admins to deal with simta.

%prep
%setup

%install
install -m 0755 -d %{buildroot}%{_sbindir} %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/cron.d
install -m 0644 40simta.cron %{buildroot}%{_sysconfdir}/cron.d/40simta
install -m 0755 simqclean %{buildroot}%{_sbindir}/simqclean
install -m 0755 simtamaint %{buildroot}%{_sbindir}/simtamaint
install -m 0755 simqc %{buildroot}%{_bindir}/simqc
install -m 0755 simqgrep %{buildroot}%{_bindir}/simqgrep
install -m 0755 simtrans %{buildroot}%{_bindir}/simtrans

%files
%defattr(-,root,root,-)
%{_sysconfdir}/cron.d/40simta
%{_sbindir}/simqclean
%{_sbindir}/simtamaint
%{_bindir}/simqc
%{_bindir}/simqgrep
%{_bindir}/simtrans

%changelog
* %(date "+%a %b %d %Y") (Automated RPM build) - %{version}-%{release}
- See git log for actual changes.
