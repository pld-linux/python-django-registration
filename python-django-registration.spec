%define		module	django-registration
Summary:	Simple, portable, generic user-registration application for Django projects
Summary(pl.UTF-8):	Prosta i przenośna aplikacja do rejestrowania użytkowników w projektach Django
Name:		python-%{module}
Version:	0.8
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	d3e785858e0040a6c3201acd43409b2e
URL:		https://bitbucket.org/ubernostrum/django-registration/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-django >= 1.3
Requires:	python-modules
Provides:	python-django_registration = %{version}-%{release}
Obsoletes:	python-django_registration < 0.6-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.3 or newer, but has no
other dependencies.

%prep
%setup -q -n %{module}-%{version}

rm -r docs/_build/html/.buildinfo

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/registration/tests

# Language files; not under %{_datadir}, need to be handled manually
for a in $RPM_BUILD_ROOT%{py_sitescriptdir}/registration/locale/[a-z]*; do
	# path file and lang
	p=${a#$RPM_BUILD_ROOT} l=${a##*/}
	echo "%lang($l) $p"
done >> %{name}.lang

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc LICENSE AUTHORS CHANGELOG README docs/*
%dir %{py_sitescriptdir}/registration
%{py_sitescriptdir}/registration/*.py[co]
%{py_sitescriptdir}/registration/backends
%{py_sitescriptdir}/registration/management
%dir %{py_sitescriptdir}/registration/locale
%{py_sitescriptdir}/django_registration-%{version}-py*.egg-info
