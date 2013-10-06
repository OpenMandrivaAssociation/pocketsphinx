%define name	pocketsphinx

%define major	1
%define devname	%mklibname %{name} -d
%define libname	%mklibname %{name} %{major}

%define gstname	gstreamer0.10-%{name}

Name:		%{name}
Version:	0.8
Release:	1
Summary:	Real-time speech recognition
Group:		Sound
License:	BSD and LGPLv2+
URL:		http://www.pocketsphinx.org/
Source0:	https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/0.8/%{name}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	sphinxbase-devel

%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%package -n %{devname}
Summary:	Header files for developing with pocketsphinx
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files for developing with pocketsphinx.

%package -n %{libname}
Summary:	Shared libraries for pocketsphinx executables
Group:		System/Libraries

%description -n %{libname}
Shared libraries for pocketsphinx executables.

%package -n python-%{name}
Summary:	Python interface to pocketsphinx
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-%{name}
Python interface to pocketsphinx.

%package -n %{gstname}
Summary:	Gstreamer plugin for pocketsphinx
Group:		Sound
BuildRequires:	libgstreamer-devel
BuildRequires:	libgstreamer-plugins-base-devel
Requires:	%{name} = %{version}-%{release}

%description -n %{gstname}
Gstreamer plugin for pocketsphinx.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
%make LIBS="-lsphinxbase -lsphinxad -lm"

%install
mkdir -p %{buildroot}%{py_platsitedir}
%makeinstall_std

mkdir -p %{buildroot}%{_mandir}/man1
install -pm644 doc/*.1 %{buildroot}%{_mandir}/man1/

# we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;

%check
%make check

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/libpocketsphinx.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n python-%{name}
%{py_platsitedir}/*

%files -n %{gstname}
%{_libdir}/gstreamer-0.10/libgst%{name}.so

