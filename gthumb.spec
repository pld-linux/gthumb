# TODO: turn on webservices support - it requires gtk-webkit3 >= 1.10 and json-glib >= 0.15 (unstable?)
#
Summary:	An image viewer and browser for GNOME
Summary(pl.UTF-8):	Przeglądarka obrazków dla GNOME
Name:		gthumb
Version:	3.2.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gthumb/3.2/%{name}-%{version}.tar.xz
# Source0-md5:	c4d85caae04ab6382e3597b07828590e
URL:		http://gthumb.sourceforge.net/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	bison
BuildRequires:	brasero-devel >= 3.2.0
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 1.0.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.34.0
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gsettings-desktop-schemas-devel
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libchamplain-devel >= 0.12
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-devel >= 0.0.8
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 2.34.0
BuildRequires:	libsecret-devel >= 0.11
BuildRequires:	libsoup-gnome-devel >= 2.36.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libwebp-devel >= 0.2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz >= 1:4.999.7
BuildRequires:	yelp-tools
BuildRequires:	zlib-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	glib2 >= 1:2.34.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	gsettings-desktop-schemas
Requires:	gtk+3 >= 3.4.0
Requires:	hicolor-icon-theme
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
Requires:	gtk+3-devel >= 3.4.0

%description devel
This package provides header files for developing gThumb extensions.

%description devel -l pl.UTF-8
Ten pakiet dostarcza pliki nagłówkowe potrzebne do rozwijania
rozszerzeń gThumb.

%prep
%setup -q

sed -i -e 's#sr@Latn#sr@latin#' po/LINGUAS
mv -f po/sr@{Latn,latin}.po

%build
%{__gnome_doc_common}
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules \
	--enable-libopenraw
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/*.{a,la}

%find_lang %{name} --with-gnome --all-name

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/extensions
%attr(755,root,root) %{_libdir}/%{name}/extensions/*.so
%{_libdir}/%{name}/extensions/*.extension
%{_datadir}/%{name}
%{_datadir}/GConf/gsettings/gthumb.convert
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/glib-2.0/schemas/*.enums.xml
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_desktopdir}/gthumb.desktop
%{_desktopdir}/gthumb-import.desktop
%{_mandir}/man1/gthumb.1*

%files devel
%defattr(644,root,root,755)
%{_aclocaldir}/gthumb.m4
%{_includedir}/gthumb-*
%{_pkgconfigdir}/gthumb-*.pc
