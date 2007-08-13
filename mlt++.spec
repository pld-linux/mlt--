Summary:	MLT++ - C++ binding to MLT
Summary(pl.UTF-8):	MLT++ - wiązanie C++ do MLT
Name:		mlt++
Version:	0.2.2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sourceforge/mlt/%{name}-%{version}.tar.gz
# Source0-md5:	7f00c36c54d09d6159641e65955fcad7
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

%description -l pl.UTF-8
MLT to szkielet multimedialny o otwartych źródłach zaprojektowany i
rozwijany do nadawania telewizji. Udostępnia zestaw narzędzi dla
nadawców, edytory obrazu, odtwarzacze mediów, transkodery, narzędzia
do udostępniania strumieni przez WWW i wiele innych rodzajów
aplikacji. Funkcjonalność systemu jest zapewniona poprzez asortyment
gotowych do użycia narzędzi, komponentów do tworzenia XML-a i
rozszerzalne API oparte na wtyczkach.

%package devel
Summary:	Header files for MLT++
Summary(pl.UTF-8):	Pliki nagłówkowe dla MLT++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for MLT++.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla MLT++.

%prep
%setup -q 

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
