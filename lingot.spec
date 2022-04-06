%define	major	0
%define	libname	%mklibname lingot %{major}
%define	devname	%mklibname -d lingot

Summary:	A musical instrument tuner
Name:		lingot
Version:	1.1.1
Release:	1
License:	GPLv2+
Group:		Sound
Url:			https://www.nongnu.org/lingot/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	intltool >= 0.23
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libpulse-simple)
Conflicts:	%{name} <= 0.9.1

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, it can now be
used to tune other instruments.
It looks like an analogue tuner, with a gauge indicating the relative shift to
a certain note, found automatically as the closest note to the estimated
frequency.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README README.config
%{_bindir}/%{name}
%{_datadir}/applications/org.nongnu.%{name}.desktop
%{_datadir}/metainfo/org.nongnu.%{name}.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/org.nongnu.%{name}.svg
%{_mandir}/man1/%{name}.1*

#-----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library used by %{name}
Group:		System/Libraries

%description  -n %{libname}
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, it can now be
used to tune other instruments.
This package contains the main library used by %{name}.

%files    -n %{libname}
%doc COPYING
%{_libdir}/liblingot.so.%{major}*

#-----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{libname}
Group:		Development/C

%description  -n %{devname}
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, it can now be
used to tune other instruments.
This package contains the files needed to build against %{libname}.

%files    -n %{devname}
%doc COPYING
%{_includedir}/%{name}/lingot-*.h
%{_libdir}/liblingot.so
%{_libdir}/pkgconfig/%{name}.pc

#-----------------------------------------------------------------------------

%prep
%setup -q


%build
%configure	--with-alsa \
				--with-fftw \
				--with-jack \
				--with-pulseaudio
%make


%install
%makeinstall_std

# Drop docs: we pick them with our macro
rm -rf %{buildroot}%{_docdir}

%find_lang %{name}
