%define		_snap	20060815
Summary:	MLT++ - C++ binding to MLT
Summary(pl):	MLT++ - wi±zanie C++ do MLT
Name:		mlt++
Version:	0.2.2
Release:	0.%{_snap}.1
License:	GPL
Group:		Libraries
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	d87399b0787ca88ae03a8939a23503f5
URL:		http://www.dennedy.org/mlt/twiki/bin/view/MLT/WebHome
BuildRequires:	mlt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MLT is an open source multimedia framework, designed and developed for
television broadcasting. It provides a toolkit for broadcasters, video
editors, media players, transcoders, web streamers and many more types
of applications. The functionality of the system is provided via an
assortment of ready to use tools, XML authoring components, and an
extendible plug-in based API.

%description -l pl
MLT to szkielet multimedialny o otwartych ¼ród³ach zaprojektowany i
rozwijany do nadawania telewizji. Udostêpnia zestaw narzêdzi dla
nadawców, edytory obrazu, odtwarzacze mediów, transkodery, narzêdzia
do udostêpniania strumieni przez WWW i wiele innych rodzajów
aplikacji. Funkcjonalno¶æ systemu jest zapewniona poprzez asortyment
gotowych do u¿ycia narzêdzi, komponentów do tworzenia XML-a i
rozszerzalne API oparte na wtyczkach.

%package devel
Summary:	Header files for MLT++
Summary(pl):	Pliki nag³ówkowe dla MLT++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MLT++.

%description devel -l pl
Pliki nag³ówkowe dla MLT++.

%prep
%setup -q -n %{name}

%build
%configure
%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

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
