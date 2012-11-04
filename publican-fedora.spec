Summary:	Publican documentation template files for Fedora
Summary(pl.UTF-8):	Pliki szablonów dokumentacji Publicana dla Fedory
Name:		publican-fedora
Version:	2.0
Release:	1
License:	CC-BY-SA
Group:		Development/Libraries
Source0:	https://fedorahosted.org/releases/p/u/publican/%{name}-%{version}.tgz
# Source0-md5:	0492f961ac830898a6b763d9ef90a6a4
URL:		https://publican.fedorahosted.org
BuildRequires:	publican >= 2.0
Requires:	publican >= 2.0
Obsoletes:	documentation-devel-Fedora
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides common files and templates needed to build
documentation for Fedora with Publican.

%description -l pl.UTF-8
Ten pakiet udostępnia wspólne pliki oraz szablony wymagane do
budowania dokumentacji dla Fedory przy użyciu Publicana.

%prep
%setup -q

%build
publican build --formats=xml --langs=all --publish

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

publican install_brand --path=$RPM_BUILD_ROOT%{_datadir}/publican/Common_Content

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%{_datadir}/publican/Common_Content/fedora
