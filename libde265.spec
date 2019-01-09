%define major 0
%define libname %mklibname de265_ %{major}
%define devname %mklibname de265 -d

Summary:	Open h.265 video codec implementation
Name:		libde265
Version:	1.0.3
Release:	1
Group:		System/Libraries
License:	LGPLv2 and GPLv2
URL:		https://github.com/strukturag/libde265
Source0:	https://github.com/strukturag/libde265/archive/master/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x265)

%description
libde265 is an open source implementation of the h.265 video codec. It is
written from scratch and has a plain C API to enable a simple integration
into other software.

libde265 supports WPP and tile-based multithreading and includes SSE
optimizations. The decoder includes all features of the Main profile and
correctly decodes almost all conformance streams.

%package -n %{libname}
Summary:	Library files for %{name}
Group:		System/Libraries

%description -n %{libname}
The %{libname} package contains the libraries for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	de265-devel = %{EVRD}

%description -n %{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install
find %{buildroot} -name '*.*a' -delete

%files
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*%{name}*.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}/
%{_libdir}/*%{name}*.so
%{_libdir}/pkgconfig/libde265.pc

