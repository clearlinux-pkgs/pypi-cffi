#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cffi
Version  : 1.15.1
Release  : 119
URL      : https://files.pythonhosted.org/packages/2b/a8/050ab4f0c3d4c1b8aaa805f70e26e84d0e27004907c5b8ecc1d31815f92a/cffi-1.15.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/a8/050ab4f0c3d4c1b8aaa805f70e26e84d0e27004907c5b8ecc1d31815f92a/cffi-1.15.1.tar.gz
Summary  : Foreign Function Interface for Python calling C code.
Group    : Development/Tools
License  : MIT
Requires: pypi-cffi-filemap = %{version}-%{release}
Requires: pypi-cffi-lib = %{version}-%{release}
Requires: pypi-cffi-license = %{version}-%{release}
Requires: pypi-cffi-python = %{version}-%{release}
Requires: pypi-cffi-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libffi-dev
BuildRequires : pkgconfig(libffi)
BuildRequires : pypi(pycparser)

%description
CFFI
====
Foreign Function Interface for Python calling C code.
Please see the [Documentation](http://cffi.readthedocs.org/) or uncompiled
in the doc/ subdirectory.

%package filemap
Summary: filemap components for the pypi-cffi package.
Group: Default

%description filemap
filemap components for the pypi-cffi package.


%package lib
Summary: lib components for the pypi-cffi package.
Group: Libraries
Requires: pypi-cffi-license = %{version}-%{release}
Requires: pypi-cffi-filemap = %{version}-%{release}

%description lib
lib components for the pypi-cffi package.


%package license
Summary: license components for the pypi-cffi package.
Group: Default

%description license
license components for the pypi-cffi package.


%package python
Summary: python components for the pypi-cffi package.
Group: Default
Requires: pypi-cffi-python3 = %{version}-%{release}

%description python
python components for the pypi-cffi package.


%package python3
Summary: python3 components for the pypi-cffi package.
Group: Default
Requires: pypi-cffi-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(cffi)
Requires: pypi(pycparser)

%description python3
python3 components for the pypi-cffi package.


%prep
%setup -q -n cffi-1.15.1
cd %{_builddir}/cffi-1.15.1
pushd ..
cp -a cffi-1.15.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656621160
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cffi
cp %{_builddir}/cffi-1.15.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cffi/65e8b9015ffb0747c23370a3d3af2a796c64780e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-cffi

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cffi/65e8b9015ffb0747c23370a3d3af2a796c64780e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
