%include	/usr/lib/rpm/macros.perl
Summary:	Crypt-CBC perl module
Summary(pl):	Modu³ perla Crypt-CBC
Name:		perl-Crypt-CBC
Version:	1.22
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/Crypt-CBC-%{version}.tar.gz
Patch:		perl-Crypt-CBC-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Digest-MD5
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-CBC - perl implementation of the CBC (cryptographic cipher block 
chaining mode).

%description -l pl
Crypt-CBC - implementacja CBC (cryptographic cipher block chaining mode)
dla perla.

%prep
%setup -q -n Crypt-CBC-%{version}
%patch -p1

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Crypt/CBC
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz eg

%{perl_sitelib}/Crypt/CBC.pm
%{perl_sitearch}/auto/Crypt/CBC

%{_mandir}/man3/*
