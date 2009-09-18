#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Event-Random
Summary:	DateTime::Event::Random - DateTime extension for creating random datetimes
Summary(pl.UTF-8):	DateTime::Event::Random - rozszerzenie DateTime do tworzenia dat losowych
Name:		perl-DateTime-Event-Random
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1ce3995c36791bf9dabc8ea3b97f4451
URL:		http://search.cpan.org/dist/DateTime-Event-Random/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-DateTime
BuildRequires:	perl-DateTime-Set >= 0.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides convenience methods that let you easily create
DateTime::Set, DateTime, or DateTime::Duration objects with random
values.

%description -l pl.UTF-8
Ten moduł udostępnia metody udogadniające pozwalające łatwo tworzyć
obiekty DateTime::Set, DateTime i DateTime::Duration zawierające
wartości losowe.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%{perl_vendorlib}/DateTime/Event/*.pm
%{_mandir}/man3/*
