#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v3
# autospec commit: c1050fe
#
Name     : php-json_post
Version  : 1.1.0
Release  : 67
URL      : https://pecl.php.net/get/json_post-1.1.0.tgz
Source0  : https://pecl.php.net/get/json_post-1.1.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-json_post-lib = %{version}-%{release}
Requires: php-json_post-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : perl(Getopt::Long)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# ext-json_post
[![Build Status](https://github.com/m6w6/ext-json_post/workflows/ci/badge.svg?branch=master)](https://github.com/m6w6/ext-json_post/actions?query=branch%3Amaster+workflow%3Aci)
[![codecov](https://codecov.io/gh/m6w6/ext-json_post/branch/master/graph/badge.svg?token=Nku9tz8EMj)](https://codecov.io/gh/m6w6/ext-json_post)

%package lib
Summary: lib components for the php-json_post package.
Group: Libraries
Requires: php-json_post-license = %{version}-%{release}

%description lib
lib components for the php-json_post package.


%package license
Summary: license components for the php-json_post package.
Group: Default

%description license
license components for the php-json_post package.


%prep
%setup -q -n json_post-1.1.0
cd %{_builddir}/json_post-1.1.0
pushd ..
cp -a json_post-1.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-json_post
cp %{_builddir}/json_post-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-json_post/a8e63d3d3705690cf7268d26d3c29d78e6b497d9 || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20230831/json_post.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-json_post/a8e63d3d3705690cf7268d26d3c29d78e6b497d9
