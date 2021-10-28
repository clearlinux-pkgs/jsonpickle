#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jsonpickle
Version  : 2.0.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/62/8a/84864798c5ef120e3a5b5cf08d8c231fa4499b53d465488563c4cb901f2f/jsonpickle-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/8a/84864798c5ef120e3a5b5cf08d8c231fa4499b53d465488563c4cb901f2f/jsonpickle-2.0.0.tar.gz
Summary  : Python library for serializing any arbitrary object graph into JSON
Group    : Development/Tools
License  : BSD-3-Clause
Requires: jsonpickle-license = %{version}-%{release}
Requires: jsonpickle-python = %{version}-%{release}
Requires: jsonpickle-python3 = %{version}-%{release}
Requires: importlib_metadata
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools_scm-python
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/jsonpickle.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/jsonpickle.svg
:target: `PyPI link`_

%package license
Summary: license components for the jsonpickle package.
Group: Default

%description license
license components for the jsonpickle package.


%package python
Summary: python components for the jsonpickle package.
Group: Default
Requires: jsonpickle-python3 = %{version}-%{release}

%description python
python components for the jsonpickle package.


%package python3
Summary: python3 components for the jsonpickle package.
Group: Default
Requires: python3-core
Provides: pypi(jsonpickle)

%description python3
python3 components for the jsonpickle package.


%prep
%setup -q -n jsonpickle-2.0.0
cd %{_builddir}/jsonpickle-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612800657
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jsonpickle
cp %{_builddir}/jsonpickle-2.0.0/LICENSE %{buildroot}/usr/share/package-licenses/jsonpickle/d168b004e2b3920a6a893cae9f6e7923c4e8470e
cp %{_builddir}/jsonpickle-2.0.0/jsonpickleJS/LICENSE %{buildroot}/usr/share/package-licenses/jsonpickle/502b8fa73760ceab2e36965b01ec88535e230a33
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jsonpickle/502b8fa73760ceab2e36965b01ec88535e230a33
/usr/share/package-licenses/jsonpickle/d168b004e2b3920a6a893cae9f6e7923c4e8470e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
