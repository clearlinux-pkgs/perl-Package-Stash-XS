#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-Stash-XS
Version  : 0.28
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/D/DO/DOY/Package-Stash-XS-0.28.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DO/DOY/Package-Stash-XS-0.28.tar.gz
Summary  : 'faster and more correct implementation of the Package::Stash API'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Package-Stash-XS-lib = %{version}-%{release}
Requires: perl-Package-Stash-XS-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Package-Stash-XS,
version 0.28:
faster and more correct implementation of the Package::Stash API

%package dev
Summary: dev components for the perl-Package-Stash-XS package.
Group: Development
Requires: perl-Package-Stash-XS-lib = %{version}-%{release}
Provides: perl-Package-Stash-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-Package-Stash-XS package.


%package lib
Summary: lib components for the perl-Package-Stash-XS package.
Group: Libraries
Requires: perl-Package-Stash-XS-license = %{version}-%{release}

%description lib
lib components for the perl-Package-Stash-XS package.


%package license
Summary: license components for the perl-Package-Stash-XS package.
Group: Default

%description license
license components for the perl-Package-Stash-XS package.


%prep
%setup -q -n Package-Stash-XS-0.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Package-Stash-XS
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Package-Stash-XS/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Package/Stash/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::Stash::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Package/Stash/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Package-Stash-XS/LICENSE
