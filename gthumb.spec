Summary:	An image viewer and browser for GNOME
Summary(pl.UTF-8):	Przeglądarka obrazków dla GNOME
Name:		gthumb
Version:	2.10.4
Release:	1
License:	GPL v2
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/gthumb/2.10/%{name}-%{version}.tar.bz2
# Source0-md5:	090b0cd29cfbcd50c77b4f645472ac38
Patch0:		%{name}-desktop.patch
URL:		http://gthumb.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.18.0
BuildRequires:	ORBit2-devel >= 1:2.14.7
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.18.0
BuildRequires:	gnome-vfs2-devel >= 2.18.1
BuildRequires:	gtk+2-devel >= 2:2.10.13
BuildRequires:	gtkunique >= 0.9.1
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libexif-devel >= 1:0.6.13
BuildRequires:	libglade2-devel >= 1:2.6.1
BuildRequires:	libgnomeprintui-devel >= 2.18.0
BuildRequires:	libgnomeui-devel >= 2.18.1
BuildRequires:	libgphoto2-devel >= 2.2.1
BuildRequires:	libiptcdata-devel >= 0.2.1
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-devel >= 0.0.2
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.29
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
BuildRequires:	sed >= 4.0
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gtk+2 >= 2:2.10.13
Requires:	hicolor-icon-theme
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

%prep
%setup -q
%patch0 -p1

%build
%{__gnome_doc_common}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-scrollkeeper \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libgthumb.{a,la}
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.{a,la}
rm -rf $RPM_BUILD_ROOT%{_datadir}/application-registry

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gthumb.schemas
%scrollkeeper_update_post
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gthumb.schemas

%postun
%scrollkeeper_update_postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.so
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/%{name}.desktop
