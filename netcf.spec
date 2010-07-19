Summary:	netcf is a cross-platform network configuration library
Summary(pl.UTF-8):	netcf to wieloplatformowa biblioteka do konfiguracji sieci
Name:		netcf
Version:	0.1.6
Release:	0.1
License:	GPLv2
Group:		Administration/System
Source0:	https://fedorahosted.org/released/netcf/%{name}-%{version}.tar.gz
# Source0-md5:	c19914d97b23be1837036d23cbdc6473
URL:		https://fedorahosted.org/netcf/
BuildRequires:	augeas-devel
BuildRequires:	libxslt-devel
BuildRequires:	libnl-devel
Requires:	augeas
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%package libs
Summary:	Netcf libraries
Summary(pl.UTF-8):	Biblioteki netcf
Group:		Libraries

%description libs
This package contains the netcf libraries.

%description libs -l pl.UTF-8
Ten pakiet zawiera biblioteki netcf.

%package devel
Summary:	Netcf development files
Summary(pl.UTF-8):	Pliki programistyczne netcf
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains the include files used to develop using netcf
APIs.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkow służące do programowania z użyciem
API netcf.

%package static
Summary:	The netcf static libraries
Summary(pl.UTF-8):	Statyczne biblioteki netcf
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the netcf static libraries.

%description static -l pl.UTF-8
Ten pakiet zawiera statyczne biblioteki netcf.

%prep
%setup -q

%build

%configure 

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
%attr(755,root,root)  %{_bindir}/ncftool
%{_datadir}/netcf   

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnetcf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnetcf.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libnetcf.la
%{_libdir}/libnetcf.so
%{_pkgconfigdir}/netcf.pc
%{_includedir}/netcf.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libnetcf.a
