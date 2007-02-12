#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CBC
Summary:	Crypt::CBC - encrypt data with Cipher Block Chaining mode
Summary(pl.UTF-8):   Crypt::CBC - szyfrowanie danych w trybie Cipher Block Chaining
Name:		perl-Crypt-CBC
Version:	2.19
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9e611ce8984d1d2f14cd038e62b50064
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Crypt-CBC/
BuildRequires:	perl-Digest-MD5 >= 2.00
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-Blowfish_PP
BuildRequires:	perl-Crypt-CAST5
BuildRequires:	perl-Crypt-IDEA
BuildRequires:	perl-Crypt-Rijndael
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a Perl-only implementation of the cryptographic cipher
block chaining mode (CBC). In combination with a block cipher such as
DES or IDEA, you can encrypt and decrypt messages of arbitrarily long
length. The encrypted messages are compatible with the encryption
format used by SSLeay.

%description -l pl.UTF-8
Ten moduł jest czysto perlową implementacją szyfrowania w trybie CBC
(Cipher Block Chaining). W połączeniu z szyfrem blokowym, takim jak
DES lub IDEA, pozwala szyfrować i deszyfrować wiadomości o dowolnej
długości. Zaszyfrowane wiadomości są kompatybilne z formatem używanym
przez SSLeay.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Crypt/CBC.pm
%{_mandir}/man3/*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
