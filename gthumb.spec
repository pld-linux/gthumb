Summary:	An image viewer and browser for GNOME
Summary(pl):	Przegl±darka obrazków dla GNOME
Name:		gthumb
Version:	2.1.1
Release:	1
License:	GPL
Vendor:		GNOME
Group:		X11/Applications/Graphics
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.1/%{name}-%{version}.tar.bz2
URL:		http://gthumb.sourceforge.net/
BuildRequires:	bonobo-activation-devel >= 2.1.0
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libbonobo-devel >= 2.2.0
BuildRequires:	libbonoboui-devel >= 2.2.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnome-devel >= 2.2.0
BuildRequires:	libgnomeprint-devel >= 2.2.0
BuildRequires:	libgnomeprintui-devel >= 2.2.0
BuildRequires:	libgnomeui-devel >= 2.2.0
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel >= 2.4.0
Requires(post):	GConf2
Requires(post):	scrollkeeper
Requires:	bonobo-activation >= 2.2.0
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

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/modules/*.{a,la}
rm $RPM_BUILD_ROOT/%{_libdir}/*.{a,la}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/gthumb
%attr(755,root,root) %{_libdir}/libgthumb.so
%{_libexecdir}/gthumb-image-viewer
%{_libexecdir}/gthumb-catalog-view
%{_libdir}/%{name}
%{_desktopdir}/gthumb.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gthumb
%{_datadir}/application-registry/gthumb.applications
%{_libdir}/bonobo/servers/*.server
%{_pixmapsdir}/gthumb.png
%{_mandir}/man1/gthumb.1*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/gthumb.schemas
