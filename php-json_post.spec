#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-json_post
Version  : 1.0.1
Release  : 6
URL      : https://pecl.php.net//get/json_post-1.0.1.tgz
Source0  : https://pecl.php.net//get/json_post-1.0.1.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: php-json_post-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
No detailed description available

%package lib
Summary: lib components for the php-json_post package.
Group: Libraries

%description lib
lib components for the php-json_post package.


%prep
%setup -q -n json_post-1.0.1
cd %{_builddir}/json_post-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/json_post.so
