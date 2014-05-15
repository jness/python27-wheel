%define __python /usr/bin/python%{pybasever}
# sitelib for noarch packages
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pyver 27
%define pybasever 2.7

Name:           python%{pyver}-wheel
Version:        0.23.0
Release:        1.ius%{?dist}
Summary:        A built-package format for Python.

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/wheel
Source0:        http://pypi.python.org/packages/source/w/wheel/wheel-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python%{pyver}-devel, python%{pyver}-setuptools
Requires:       python%{pyver}-setuptools, python%{pyver}-pip

%description
A wheel is a ZIP-format archive with a specially formatted filename and the .whl extension.
It is designed to contain all the files for a PEP 376 compatible install in a way that is
very close to the on-disk format. Many packages will be properly installed with only the
"Unpack" step (simply extracting the file onto sys.path), and the unpacked archive preserves
enough information to "Spread" (copy data and scripts to their final locations) at any later time.

%prep
%setup -q -n wheel-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO LICENSE.txt MANIFEST.in CHANGES.txt
%{_bindir}/egg2wheel
%{_bindir}/wininst2wheel
# For noarch packages: sitelib
%{python_sitelib}/*
%attr(755,root,root) %{_bindir}/wheel*
