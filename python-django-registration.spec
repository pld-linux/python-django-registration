%define		projectname	django-registration
%define		module		registration
Summary:	Simple, portable, generic user-registration application for Django projects
Summary(pl.UTF-8):	Prosta i przenośna aplikacja do rejestrowania użytkowników w projektach Django
Name:		python-django-registration
Version:	0.6
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://%{projectname}.googlecode.com/files/%{projectname}-%{version}.tar.gz
# Source0-md5:	70c24a498443ebefac04b850762fe927
URL:		http://django-registration.googlecode.com/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#%pyrequires_eq	python-libs
%pyrequires_eq	python-modules
Requires:	python-django >= 1.0
Obsoletes:		python-django_registration < 0.6-2
Provides:		python-django_registration = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{projectname}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
