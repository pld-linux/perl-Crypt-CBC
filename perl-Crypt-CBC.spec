%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CBC
Summary:	libxml-enno Perl module
Summary(cs):	Modul Crypt::CBC pro Perl
Summary(da):	Perlmodul Crypt::CBC
Summary(de):	Crypt::CBC Perl Modul
Summary(es):	Módulo de Perl Crypt::CBC
Summary(fr):	Module Perl Crypt::CBC
Summary(it):	Modulo di Perl Crypt::CBC
Summary(ja):	Crypt::CBC Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::CBC ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::CBC
Summary(pl):	Modu³ Perla Crypt::CBC
Summary(pt):	Módulo de Perl Crypt::CBC
Summary(pt_BR):	Módulo Perl Crypt::CBC
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::CBC
Summary(sv):	Crypt::CBC Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::CBC
Summary(zh_CN):	Crypt::CBC Perl Ä£¿é
Name:		perl-Crypt-CBC
Version:	2.05
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Digest-MD5 >= 2.00
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Crypt/CBC.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
