#
%define		_snap	20060601
Summary:	MLT++
Summary(pl):	MLT++
Name:		mlt++
Version:	0.2.2
Release:	0.%{_snap}.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	06ad73cbc6f8ce4a076b86fb83cca0eb
URL:		http://www.dennedy.org/mlt/twiki/bin/view/MLT/WebHome
BuildRequires:	mlt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLT is an open source multimedia framework, designed and developed for
television broadcasting. It provides a toolkit for broadcasters, video
editors, media players, transcoders, web streamers and many more types
of applications. The functionality of the system is provided via an
assortment of ready to use tools, xml authoring components, and an
extendible plug-in based API.

#%description -l pl

%package devel
Summary:	Header files for MLT++
Summary(pl):	Pliki nag³ówkowe dla MLT++
Group:		Development/Libraries

%description devel
Header files for MLT++

#%description devel -l pl

%prep
%setup -q -n %{name}

%build
%configure
%{__make}
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/*.so*

%files devel
%defattr(644,root,root,755)
%{_includedir}/mlt++*
