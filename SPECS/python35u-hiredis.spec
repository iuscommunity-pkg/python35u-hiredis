%global ius_suffix 35u

Name:           python%{ius_suffix}-hiredis
Version:        0.2.0
Release:        1.ius%{?dist}
Summary:        Python wrapper for hiredis
License:        BSD
URL:            https://github.com/redis/hiredis-py
Source0:        https://pypi.python.org/packages/source/h/hiredis/hiredis-%{version}.tar.gz
BuildRequires:  python%{ius_suffix}-devel
BuildRequires:  python%{ius_suffix}-setuptools


%description
Python extension that wraps protocol parsing code in hiredis. It primarily
speeds up parsing of multi bulk replies.


%prep
%setup -q -n hiredis-%{version}


%build
%{__python35u} setup.py build


%install
%{__python35u} setup.py install --optimize 1 --skip-build --root %{buildroot}


%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%{python35u_sitearch}/hiredis*


%changelog
* Fri Apr 15 2016 Carl George <carl.george@rackspace.com> - 0.2.0-1.ius
- Initial package
