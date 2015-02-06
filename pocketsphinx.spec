%define major	1
%define devname	%mklibname %{name} -d
%define libname	%mklibname %{name} %{major}

%define gstname	gstreamer0.10-%{name}

Name:		pocketsphinx
Version:	0.8
Release:	2
Summary:	Real-time speech recognition
Group:		Sound
License:	BSD and LGPLv2+
URL:		http://cmusphinx.sourceforge.net/
Source0:	http://sourceforge.net/projects/cmusphinx/files/pocketsphinx/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(sphinxbase)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)

%description
PocketSphinx is a version of the open-source Sphinx-II speech recognition
system which is able to recognize speech in real-time.  While it may be
somewhat less accurate than the offline speech recognizers, it is lightweight
enough to run on handheld and embedded devices.

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Header files for developing with pocketsphinx
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files for developing with pocketsphinx.

%files -n %{devname}
%doc COPYING
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared libraries for pocketsphinx executables
Group:		System/Libraries

%description -n %{libname}
Shared libraries for pocketsphinx executables.

%files -n %{libname}
%doc COPYING
%{_libdir}/lib%{name}.so.%{major}*

#-----------------------------------------------------------------------------

%package -n python-%{name}
Summary:	Python interface to pocketsphinx
Group:		Development/Python
Requires:	%{name} = %{version}

%description -n python-%{name}
Python interface to pocketsphinx.

%files -n python-%{name}
%doc COPYING
%{py_platsitedir}/*

#-----------------------------------------------------------------------------

%package -n %{gstname}
Summary:	Gstreamer plugin for pocketsphinx
Group:		Sound
Requires:	%{name} = %{version}

%description -n %{gstname}
Gstreamer plugin for pocketsphinx.

%files -n %{gstname}
%doc COPYING
%{_libdir}/gstreamer-0.10/libgst%{name}.so

#-----------------------------------------------------------------------------

%prep
%setup -q


%build
%configure2_5x --disable-static
%make
#LIBS="-lsphinxbase -lsphinxad -lm"


%install
mkdir -p %{buildroot}%{python_sitearch}
%makeinstall_std

mkdir -p %{buildroot}%{_mandir}/man1
install -pm644 doc/*.1 %{buildroot}%{_mandir}/man1/

# we don't want these
find %{buildroot} -name "*.la" -exec rm -rf {} \;


%check
%make check


%changelog
* Wed Mar 26 2014 Giovanni Mariani <mc2374@mclink.it> 0.8-1
- New release 0.8
- Fixed URL and Source0 tags
- Added some docs to keep rpmlint happy