Name: x11-font-adobe-100dpi
Version: 1.0.4
Release: 2
Summary: Xorg X11 font adobe-100dpi
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-adobe-100dpi-%{version}.tar.xz
License: MIT-like
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font adobe-100dpi.

%prep
%autosetup -p1 -n font-adobe-100dpi-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/100dpi

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/100dpi/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/100dpi/fonts.scale

%post
mkfontscale %{_datadir}/fonts/100dpi
mkfontdir %{_datadir}/fonts/100dpi

%postun
mkfontscale %{_datadir}/fonts/100dpi
mkfontdir %{_datadir}/fonts/100dpi

%files
%doc COPYING
%{_datadir}/fonts/100dpi/cour*.pcf.gz
%{_datadir}/fonts/100dpi/helv*
%{_datadir}/fonts/100dpi/ncen*
%{_datadir}/fonts/100dpi/symb*
%{_datadir}/fonts/100dpi/tim*
