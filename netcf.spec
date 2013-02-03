# TODO: enhance pld_interfaces patch, including PLDifing netcf-transaction (or disabling it)
#  maybe create drv_pld.c?
Summary:	netcf - a cross-platform network configuration library
Summary(pl.UTF-8):	netcf - wieloplatformowa biblioteka do konfiguracji sieci
Name:		netcf
Version:	0.2.3
Release:	2
License:	GPL v2
Group:		Administration/System
Source0:	https://fedorahosted.org/released/netcf/%{name}-%{version}.tar.gz
# Source0-md5:	bee292470b06201b59af0fad473a1b65
Patch0:		%{name}-pld_interfaces.patch
URL:		https://fedorahosted.org/netcf/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	augeas-devel >= 0.5.0
BuildRequires:	libnl-devel >= 3.2
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-devel
Requires:	augeas >= 0.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
netcf is a cross-platform network configuration library.

%description -l pl.UTF-8
netcf to wieloplatformowa biblioteka do konfiguracji sieci.

%package libs
Summary:	Netcf library
Summary(pl.UTF-8):	Biblioteka netcf
Group:		Libraries
Requires:	augeas-libs >= 0.5.0

%description libs
This package contains the netcf shared library.

%description libs -l pl.UTF-8
Ten pakiet zawiera bibliotekę współdzieloną netcf.

%package devel
Summary:	Netcf development files
Summary(pl.UTF-8):	Pliki programistyczne netcf
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	augeas-devel >= 0.5.0
Requires:	libxml2-devel >= 2.0
Requires:	libxslt-devel

%description devel
This package contains the include files used to develop using netcf
APIs.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkow służące do programowania z użyciem
API netcf.

%package static
Summary:	The netcf static library
Summary(pl.UTF-8):	Statyczna biblioteka netcf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the netcf static library.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczną bibliotekę netcf.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I gnulib/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-driver=redhat

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ncftool
%attr(754,root,root) /etc/rc.d/init.d/netcf-transaction
%{_datadir}/netcf   
%{_mandir}/man1/ncftool.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetcf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetcf.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetcf.so
%{_libdir}/libnetcf.la
%{_includedir}/netcf.h
%{_pkgconfigdir}/netcf.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetcf.a
