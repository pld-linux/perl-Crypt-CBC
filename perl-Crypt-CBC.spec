#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	CBC
Summary:	Crypt::CBC - encrypt data with Cipher Block Chaining mode
Summary(pl):	Crypt::CBC - szyfrowanie danych w trybie Cipher Block Chaining
Name:		perl-Crypt-CBC
Version:	2.12
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	27842b8ab627681b4a322610ea6184b5
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Digest-MD5 >= 2.00
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
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

%description -l pl
Ten modu³ jest czysto perlow± implementacj± szyfrowania w trybie
CBC (Cipher Block Chaining). W po³±czeniu z szyfrem blokowym, takim
jak DES lub IDEA, pozwala szyfrowaæ i deszyfrowaæ wiadomo¶ci o
dowolnej d³ugo¶ci. Zaszyfrowane wiadomo¶ci s± kompatybilne z formatem
u¿ywanym przez SSLeay.

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
