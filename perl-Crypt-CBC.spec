#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Crypt
%define		pnam	CBC
Summary:	Crypt::CBC - encrypt data with Cipher Block Chaining mode
Summary(pl.UTF-8):	Crypt::CBC - szyfrowanie danych w trybie Cipher Block Chaining
Name:		perl-Crypt-CBC
Version:	3.07
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ccd56523f2477df076ab7756825d1639
Patch0:		%{name}-paths.patch
URL:		https://metacpan.org/dist/Crypt-CBC
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Crypt-Blowfish
BuildRequires:	perl-Crypt-Blowfish_PP
BuildRequires:	perl-Crypt-DES
BuildRequires:	perl-Crypt-CAST5
BuildRequires:	perl-Crypt-Eksblowfish
BuildRequires:	perl-Crypt-IDEA
BuildRequires:	perl-Crypt-PBKDF2
BuildRequires:	perl-Crypt-Rijndael
BuildRequires:	perl-Crypt-URandom
# Crypt::Cipher::AES
BuildRequires:	perl-CryptX
BuildRequires:	perl-Digest-MD5 >= 2.00
BuildRequires:	perl-Digest-SHA
%ifarch %{x8664}
# if available
BuildRequires:	perl-Math-Int128
%endif
BuildRequires:	perl-Test-Simple
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
%patch -P0 -p1

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
%doc Changes SECURITY.md vulnerabilities.txt
%{perl_vendorlib}/Crypt/CBC.pm
%{perl_vendorlib}/Crypt/CBC
%{_mandir}/man3/Crypt::CBC.3pm*
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*
