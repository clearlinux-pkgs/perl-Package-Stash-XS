#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Package-Stash-XS
Version  : 0.29
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Package-Stash-XS-0.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Package-Stash-XS-0.29.tar.gz
Summary  : 'faster and more correct implementation of the Package::Stash API'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Package-Stash-XS-license = %{version}-%{release}
Requires: perl-Package-Stash-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Package-Stash-XS,
version 0.29:
faster and more correct implementation of the Package::Stash API

%package dev
Summary: dev components for the perl-Package-Stash-XS package.
Group: Development
Provides: perl-Package-Stash-XS-devel = %{version}-%{release}
Requires: perl-Package-Stash-XS = %{version}-%{release}

%description dev
dev components for the perl-Package-Stash-XS package.


%package license
Summary: license components for the perl-Package-Stash-XS package.
Group: Default

%description license
license components for the perl-Package-Stash-XS package.


%package perl
Summary: perl components for the perl-Package-Stash-XS package.
Group: Default
Requires: perl-Package-Stash-XS = %{version}-%{release}

%description perl
perl components for the perl-Package-Stash-XS package.


%prep
%setup -q -n Package-Stash-XS-0.29
cd %{_builddir}/Package-Stash-XS-0.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Package-Stash-XS
cp %{_builddir}/Package-Stash-XS-0.29/LICENSE %{buildroot}/usr/share/package-licenses/perl-Package-Stash-XS/86fe74a925805c9016a91b52d3efab8705c51e94
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Package::Stash::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Package-Stash-XS/86fe74a925805c9016a91b52d3efab8705c51e94

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/Package/Stash/XS.pm
/usr/lib/perl5/vendor_perl/5.30.3/x86_64-linux-thread-multi/auto/Package/Stash/XS/XS.so
