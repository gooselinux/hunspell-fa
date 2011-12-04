Name: hunspell-fa
Summary: Farsi hunspell dictionaries
%define upstreamid 20070116
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Group: Applications/Text
Source: ftp://ftp.gnu.org/gnu/aspell/dict/fa/aspell6-fa-0.11-0.tar.bz2
URL: http://aspell.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPL+
BuildArch: noarch
BuildRequires: aspell, hunspell-devel

Requires: hunspell

%description
Farsi hunspell dictionaries.

%prep
%setup -q -n aspell6-fa-0.11-0

%build
export LANG=fa_IR.utf8
preunzip -d *.cwl
cat *.wl > farsi.wordlist
wordlist2hunspell farsi.wordlist fa_IR

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING Copyright doc/README doc/ChangeLog
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20070116-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20070116-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20070116-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 20 2008 Caolan McNamara <caolanm@redhat.com> - 0.20070116-1
- initial version
