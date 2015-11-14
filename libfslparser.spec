#
# spec file for package libfslcodec
#
# Copyright (c) 2015 Josua Mayer <privacy@not.given>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

%define blobpkg_name libfslparser-4.0.7
%define blobpkg_md5 d1d0a2cff6cec3f157934034021ccf87

Name: libfslparser
Version: 4.0.7
Release: 1
License: Unknown
Group: Productivity/Multimedia/Other
Summary: Multimedia container implementations for i.MX SoCs
Source: %{name}-%{version}.tar.gz
Source1: %{blobpkg_name}.bin
BuildRequires: pkg-config autoconf automake libtool

%description
Provides Multimedia Container implementations for use on i.MX SoCs

%package devel
Group: Development/Languages/C and C++
Summary: Development files for Freescale codecs
%description devel
Provides development files to build against the multimedia container implementations provided by Freescale.

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%prep
%setup -q
cp %{SOURCE1} ./
chmod +x %{blobpkg_name}.bin
./fetch.sh %{blobpkg_name}.bin %{blobpkg_md5}
./%{blobpkg_name}.bin --auto-accept --force

%build
cd %{blobpkg_name}
NOCONFIGURE=1 ./autogen.sh
%configure \
%ifarch armv7hl
--enable-fhw \
%endif
%{_nop}

make %{?_smp_mflags}
cd ..

%install
cd %{blobpkg_name}
%makeinstall
cd ..

%files
%defattr(-,root,root)
%dir /usr/lib/imx-mm
%dir /usr/lib/imx-mm/parser
/usr/lib/*.so.*
/usr/lib/imx-mm/parser/*.so.*
/usr/share/doc/libfslparser

%files devel
%defattr(-,root,root)
/usr/include/imx-mm
/usr/lib/pkgconfig/*.pc
/usr/lib/*.so
/usr/lib/imx-mm/parser/*.so

%changelog
