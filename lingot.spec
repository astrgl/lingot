Summary:    A musical instrument tuner
Name:       lingot
Version:    1.1.1
Release:    1
URL:        http://savannah.nongnu.org/projects/%{name}
Source0:     http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:     lingot-0.9.1-mdv-format-security.patch
License:    GPLv2
Group:      Sound
BuildRequires: gtk2-devel
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: intltool
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, it can now be used
to tune other instruments.

It looks like an analogue tuner, with a gauge indicating the relative shift to
a certain note, found automatically as the closest note to the estimated
frequency.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_docdir}
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README THANKS
%{_bindir}/%name
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/%{name}
