Summary:	An image viewer and browser for GNOME
Summary(pl):	Przegl±darka obrazków dla GNOME
Name:		gthumb
Version:	2.6.2
Release:	2
License:	GPL
Vendor:		GNOME
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/gthumb/2.6/%{name}-%{version}.tar.bz2
# Source0-md5:	9fcf3a1f71cf4f90b4b259f5bf198c50
URL:		http://gthumb.sourceforge.net/
BuildRequires:	GConf2-devel
BuildRequires:	ORBit2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-common >= 2.8.0-2
BuildRequires:	gnome-vfs2-devel >= 2.6.0
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool >= 0.21
BuildRequires:	libexif-devel >= 1:0.6.9
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	libgnomeprintui-devel >= 2.6.0
BuildRequires:	libgnomeui-devel >= 2.6.0
BuildRequires:	libgphoto2-devel >= 2.1.3
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.0
Requires(post,postun):	scrollkeeper
Requires(post):	GConf2
Requires:	libbonobo >= 2.6.0
Requires:	gtk+2 >= 2:2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images,
view slideshows, set your desktop background, and more.

%description -l pl
gThumb pozwala na przegl±danie twardego dysku z pokazywaniem
miniaturek plików z obrazkami. Pozwala tak¿e ogl±daæ pojedyncze pliki
(w tym animacje GIF), dodawaæ komentarze do obrazków, uk³adaæ obrazki
w katalogi, drukowaæ obrazki, ogl±daæ slajdy, ustawiaæ t³o biurka itd.

%prep
%setup -q
sed -i -e 's/^Categories=Application;/Categories=GTK;GNOME;/' \
	data/gthumb.desktop.in

%build
cp /usr/share/gnome-common/data/omf.make .
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/%{name}/modules/*.{a,la}
rm $RPM_BUILD_ROOT%{_libdir}/%{name}/*.{a,la}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
/usr/bin/scrollkeeper-update
%gconf_schema_install
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%postun
umask 022
/usr/bin/scrollkeeper-update
[ ! -x /usr/bin/update-desktop-database ] || /usr/bin/update-desktop-database >/dev/null 2>&1 ||:

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}-image-viewer
%attr(755,root,root) %{_libdir}/%{name}-catalog-view
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%attr(755,root,root) %{_libdir}/%{name}/lib*.so
%attr(755,root,root) %{_libdir}/%{name}/modules/*.so
%{_libdir}/bonobo/servers/*.server
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/%{name}
%{_datadir}/application-registry/%{name}.applications
%{_mandir}/man1/%{name}.1*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_pixmapsdir}/%{name}.png
%{_desktopdir}/%{name}.desktop
