%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	CBC
Summary:	Crypt::CBC perl module
Summary(pl):	Modu³ perla Crypt::CBC
Name:		perl-Crypt-CBC
Version:	2.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::CBC - perl implementation of the CBC (cryptographic cipher block
chaining mode).

%description -l pl
Crypt::CBC - implementacja CBC (cryptographic cipher block chaining
mode) dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz eg
%{perl_sitelib}/Crypt/CBC.pm
%{_mandir}/man3/*
