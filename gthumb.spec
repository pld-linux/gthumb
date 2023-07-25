Summary:	An image viewer and browser for GNOME
Summary(pl.UTF-8):	Przeglądarka obrazków dla GNOME
Name:		gthumb
Version:	3.12.2
Release:	5
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	https://download.gnome.org/sources/gthumb/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	6bb8246244cdd87c8f041a1e86e144b1
Patch0:		%{name}-libraw.patch
Patch1:		exiv2-0.28.patch
URL:		https://wiki.gnome.org/Apps/Gthumb
BuildRequires:	AppStream-devel >= 0.14.6
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	brasero-devel >= 3.2.0
BuildRequires:	clutter-devel >= 1.12.0
BuildRequires:	clutter-gtk-devel >= 1.0.0
BuildRequires:	colord-devel >= 1.3
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	flex
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.54.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.16
# webkit2gtk-4.0 or webkit2-3.0; libsoup3 is not supported yet
BuildRequires:	gtk-webkit4-devel >= 1.10.0
BuildRequires:	json-glib-devel >= 0.16
BuildRequires:	lcms2-devel >= 2.6
BuildRequires:	libchamplain-devel >= 0.12
BuildRequires:	libheif-devel >= 1.11
BuildRequires:	libjpeg-devel
BuildRequires:	libjxl-devel >= 0.3.0
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel >= 0.14
BuildRequires:	librsvg-devel >= 2.34.0
BuildRequires:	libsecret-devel >= 0.11
BuildRequires:	libsoup-devel >= 2.42
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libwebp-devel >= 0.2.0
BuildRequires:	meson >= 0.43
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz >= 1:4.999.7
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.54.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	brasero-libs >= 3.2.0
Requires:	clutter >= 1.12.0
Requires:	colord >= 1.3
Requires:	exiv2-libs >= 0.21
Requires:	glib2 >= 1:2.54.0
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.16
Requires:	gtk-webkit4 >= 1.10.0
Requires:	hicolor-icon-theme
Requires:	json-glib >= 0.16
Requires:	lcms2 >= 2.6
Requires:	libchamplain >= 0.12
Requires:	libjxl >= 0.3.0
Requires:	librsvg >= 2.34.0
Requires:	libsecret >= 0.11
Requires:	libsoup >= 2.42
Requires:	libwebp >= 0.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images,
view slideshows, set your desktop background, and more.

%description -l pl.UTF-8
gThumb pozwala na przeglądanie twardego dysku z pokazywaniem
miniaturek plików z obrazkami. Pozwala także oglądać pojedyncze pliki
(w tym animacje GIF), dodawać komentarze do obrazków, układać obrazki
w katalogi, drukować obrazki, oglądać slajdy, ustawiać tło biurka itd.

%package devel
Summary:	gThumb development files
Summary(pl.UTF-8):	Pliki programistyczne gThumb
Group:		X11/Development/Libraries
Requires:	gtk+3-devel >= 3.16

%description devel
This package provides header files for developing gThumb extensions.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki nagłówkowe potrzebne do rozwijania
rozszerzeń gThumb.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%meson build \
	-Dlibchamplain=true

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/gthumb
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/extensions
%attr(755,root,root) %{_libdir}/%{name}/extensions/*.so
%{_libdir}/%{name}/extensions/*.extension
%{_datadir}/%{name}
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gthumb.*.gschema.xml
%{_datadir}/metainfo/org.gnome.gThumb.appdata.xml
%{_desktopdir}/org.gnome.gThumb.desktop
%{_desktopdir}/org.gnome.gThumb.Import.desktop
%{_iconsdir}/hicolor/*x*/apps/org.gnome.gThumb.png
# XXX: wrong dir
%{_iconsdir}/hicolor/16x16/apps/org.gnome.gThumb-symbolic.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.gThumb.svg
%{_mandir}/man1/gthumb.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gthumb
%{_pkgconfigdir}/gthumb.pc
%{_aclocaldir}/gthumb.m4
