Summary:	An image viewer and browser for GNOME
Summary(pl):	Przegl±darka obrazków dla GNOME
Name:		gthumb
Version:	1.104
Release:	0.1
License:	GPL
Vendor:		GNOME
Group:		X11/Applications/Graphics
Source0:	%{name}-%{version}.tar.gz
URL:		http://gthumb.sourceforge.net/
BuildRequires:	bonobo-activation-devel >= 1.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeprint-devel >= 1.110
BuildRequires:	libgnomeprintui-devel >= 1.110
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README COPYING
%attr(755,root,root) %{_bindir}/gthumb
%{_libexecdir}/gthumb-image-viewer
%{_libexecdir}/gthumb-catalog-view
%{_datadir}/applications/gthumb.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%dir %{_datadir}/gthumb
%{_datadir}/gthumb/glade/*.glade2
%{_datadir}/gthumb/icons/*.xpm
%{_datadir}/application-registry/gthumb.applications
%{_libdir}/bonobo/servers/*.server
%{_pixmapsdir}/gthumb.png
%{_mandir}/man1/gthumb.1*
%doc %{_datadir}/gnome/help/gthumb
