#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-json_post
Version  : 1.1.0
Release  : 24
URL      : https://pecl.php.net/get/json_post-1.1.0.tgz
Source0  : https://pecl.php.net/get/json_post-1.1.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-json_post-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
# ext-json_post
[![Build Status](https://github.com/m6w6/ext-json_post/workflows/ci/badge.svg?branch=master)](https://github.com/m6w6/ext-json_post/actions?query=branch%3Amaster+workflow%3Aci)
[![codecov](https://codecov.io/gh/m6w6/ext-json_post/branch/master/graph/badge.svg?token=Nku9tz8EMj)](https://codecov.io/gh/m6w6/ext-json_post)

%package lib
Summary: lib components for the php-json_post package.
Group: Libraries

%description lib
lib components for the php-json_post package.


%prep
%setup -q -n json_post-1.1.0
cd %{_builddir}/json_post-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/json_post.so
