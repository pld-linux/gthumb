Summary:	An image viewer and browser for GNOME
Summary(pl.UTF-8):	Przeglądarka obrazków dla GNOME
Name:		gthumb
Version:	2.12.1
Release:	2
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gthumb/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	a89be18a9e6f7f9d65cef56f34eb3022
URL:		http://gthumb.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.20.0
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	brasero-devel >= 2.28.0
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.10.0
BuildRequires:	docbook-dtd412-xml
BuildRequires:	exiv2-devel >= 0.18
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.20.0
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libgnome-keyring-devel >= 2.28.0
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-devel >= 0.0.8
BuildRequires:	libpng-devel
BuildRequires:	libsoup-gnome-devel >= 2.26.0
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.1.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gtk+2 >= 2:2.20.0
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
Requires:	gtk+2-devel >= 2:2.20.0

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
	--disable-scrollkeeper \
	--disable-schemas-install \
	--disable-silent-rules \
	--enable-openraw
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/extensions/*.{a,la}

%find_lang %{name} --with-gnome --with-omf --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gthumb.schemas
%gconf_schema_install gthumb-comments.schemas
%gconf_schema_install gthumb-gstreamer.schemas
%gconf_schema_install gthumb-image-viewer.schemas
%gconf_schema_install gthumb-importer.schemas
%gconf_schema_install gthumb-picasaweb.schemas
%gconf_schema_install gthumb-pixbuf-savers.schemas
%gconf_schema_install gthumb-slideshow.schemas
%gconf_schema_install gthumb_convert_format.schemas
%gconf_schema_install gthumb_crop_options.schemas
%gconf_schema_install gthumb_image_print.schemas
%gconf_schema_install gthumb_photo_importer.schemas
%gconf_schema_install gthumb_rename_series.schemas
%gconf_schema_install gthumb_resize_images.schemas
%gconf_schema_install gthumb_resize_options.schemas
%gconf_schema_install gthumb_webalbums.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gthumb.schemas
%gconf_schema_uninstall gthumb-comments.schemas
%gconf_schema_uninstall gthumb-gstreamer.schemas
%gconf_schema_uninstall gthumb-image-viewer.schemas
%gconf_schema_uninstall gthumb-importer.schemas
%gconf_schema_uninstall gthumb-picasaweb.schemas
%gconf_schema_uninstall gthumb-pixbuf-savers.schemas
%gconf_schema_uninstall gthumb-slideshow.schemas
%gconf_schema_uninstall gthumb_convert_format.schemas
%gconf_schema_uninstall gthumb_crop_options.schemas
%gconf_schema_uninstall gthumb_image_print.schemas
%gconf_schema_uninstall gthumb_photo_importer.schemas
%gconf_schema_uninstall gthumb_rename_series.schemas
%gconf_schema_uninstall gthumb_resize_images.schemas
%gconf_schema_uninstall gthumb_resize_options.schemas
%gconf_schema_uninstall gthumb_webalbums.schemas

%postun
%scrollkeeper_update_postun
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
%{_sysconfdir}/gconf/schemas/gthumb.schemas
%{_sysconfdir}/gconf/schemas/gthumb-comments.schemas
%{_sysconfdir}/gconf/schemas/gthumb-gstreamer.schemas
%{_sysconfdir}/gconf/schemas/gthumb-image-viewer.schemas
%{_sysconfdir}/gconf/schemas/gthumb-importer.schemas
%{_sysconfdir}/gconf/schemas/gthumb-picasaweb.schemas
%{_sysconfdir}/gconf/schemas/gthumb-pixbuf-savers.schemas
%{_sysconfdir}/gconf/schemas/gthumb-slideshow.schemas
%{_sysconfdir}/gconf/schemas/gthumb_convert_format.schemas
%{_sysconfdir}/gconf/schemas/gthumb_crop_options.schemas
%{_sysconfdir}/gconf/schemas/gthumb_image_print.schemas
%{_sysconfdir}/gconf/schemas/gthumb_photo_importer.schemas
%{_sysconfdir}/gconf/schemas/gthumb_rename_series.schemas
%{_sysconfdir}/gconf/schemas/gthumb_resize_images.schemas
%{_sysconfdir}/gconf/schemas/gthumb_resize_options.schemas
%{_sysconfdir}/gconf/schemas/gthumb_webalbums.schemas
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_desktopdir}/gthumb.desktop
%{_desktopdir}/gthumb-import.desktop

%files devel
%defattr(644,root,root,755)
%{_aclocaldir}/gthumb.m4
%{_includedir}/gthumb-*
%{_pkgconfigdir}/gthumb-*.pc
