Summary:	An image viewer and browser for GNOME.
Name:		gthumb
Version:	1.104
Release:	0.1
License:	GPL
Vendor:		GNOME
URL:		http://gthumb.sourceforge.net/
Group:		Applications/Multimedia
######		Unknown group!
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	libpng-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	libgnome-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	libglade2-devel >= 2.0.0
BuildRequires:	libgnomeprint-devel >= 1.110
BuildRequires:	libgnomeprintui-devel >= 1.110
BuildRequires:	bonobo-activation-devel >= 1.0.0
BuildRequires:	libbonobo-devel >= 2.0.0
BuildRequires:	libbonoboui-devel >= 2.0.0

%description
gThumb lets you browse your hard disk, showing you thumbnails of image
files. It also lets you view single files (including GIF animations),
add comments to images, organize images in catalogs, print images,
view slideshows, set your desktop background, and more.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gthumb
%{_libexecdir}/gthumb-image-viewer
%{_libexecdir}/gthumb-catalog-view
%{_datadir}/applications/gthumb.desktop
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/gthumb/glade/*.glade2
%{_datadir}/gthumb/icons/*.xpm
%{_datadir}/locale/*/LC_MESSAGES/gthumb-2.0.mo
%{_datadir}/application-registry/gthumb.applications
%{_libdir}/bonobo/servers/*.server
%{_datadir}/pixmaps/gthumb.png
%doc AUTHORS NEWS README COPYING
%doc %{_mandir}/man1/gthumb.1*
%doc %{_datadir}/gnome/help/gthumb
