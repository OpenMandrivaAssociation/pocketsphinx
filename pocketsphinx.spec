%define name pocketsphinx
%define devel %mklibname %{name} -d
%define libs %mklibname %{name}
%define python %mklibname %{name}-python

Name: %{name}
Version: 0.6.1
Release: %mkrel 2
Summary: Real-time speech recognition
Group: Sound
License: BSD and LGPLv2+
URL: http://www.pocketsphinx.org/
Source: http://downloads.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires: pkgconfig, python-setuptools, sphinxbase-devel
Requires: sphinxbase
BuildRequires: sphinxbase sphinxbase-devel


%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%package -n %{devel}
Summary: Header files for developing with pocketsphinx
Group: Development/C
Requires: lib%{name} = %{version}-%{release}, pkgconfig
Requires: sphinxbase-devel
Provides: %{name}-devel = %{version}-%{release}

%description -n %{devel}
Header files for developing with pocketsphinx.

%package -n %{libs}
Summary: Shared libraries for pocketsphinx executables
Group: System/Libraries
Provides: %{name}-libs = %{version}-%{release}
Provides: lib%{name} = %{version}-%{release}

%description -n %{libs}
Shared libraries for pocketsphinx executables.

%package -n %{python}
Summary: Python interface to pocketsphinx
Group: Development/Python
Requires: lib%{name} = %{version}-%{release}
Provides: %{name}-python = %{version}-%{release}

%description -n %{python}
Python interface to pocketsphinx.

%package gstreamer
Summary: Gstreamer plugin for pocketsphinx
Group: Sound
Requires: lib%{name} = %{version}-%{release}
BuildRequires: libgstreamer-devel, libgstreamer-plugins-base-devel
Provides: %{name}-gstreamer = %{version}-%{release}

%description gstreamer
Gstreamer plugin for pocketsphinx.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --disable-dependency-tracking --disable-static
%make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{python_sitearch}
%makeinstall
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/*.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%if %{mdkversion} <= 200900
%post -n %{libs} -p /sbin/ldconfig
%postun -n %{libs} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/pocketsphinx
%{_mandir}/man1/*

%files -n %{devel}
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/libpocketsphinx.so
%{_libdir}/libpocketsphinx.la
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/gstreamer-0.10/libgstpocketsphinx.la

%files -n %{libs}
%defattr(-,root,root,-)
%{_libdir}/libpocketsphinx.so.*

%files -n %{python}
%defattr(-,root,root,-)
%py_platsitedir/*

%files gstreamer
%defattr(-,root,root,-)
%{_libdir}/gstreamer-0.10/libgstpocketsphinx.so
