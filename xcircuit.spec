# TODO:
# - Rs (X at least...)
Summary:	Drawing electrical circuit schematic diagrams and related figure
Summary(pl):	Rysowanie schematów elektronicznych i zbli¿onych diagramów
Name:		xcircuit
Version:	3.2.21
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://bach.ece.jhu.edu/~tim/programs/xcircuit/archive/%{name}-%{version}.tgz
# Source0-md5:	a0d7794477241be9a9ffa82176c57470
Source1:	%{name}.desktop
URL:		http://bach.ece.jhu.edu/~tim/programs/xcircuit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xcircuitdir	%{_prefix}/lib/%{name}-3.2

%description
XCircuit is a UNIX/X11 program for drawing publishable-quality
electrical circuit schematic diagrams and related figures, and
producing circuit netlists through schematic capture. XCircuit regards
circuits as inherently hierarchical, and writes both hierarchical
PostScript output and hierarchical SPICE netlists. Circuit components
are saved in and retrieved from libraries which are fully editable.
XCircuit does not separate artistic expression from circuit drawing;
it maintains flexiblity in style without compromising the power of
schematic capture.

%description -l pl
XCircuit to program dla systemu UNIX/X11 do rysowania w jako¶ci
nadaj±cej siê do publikacji ró¿nych schematów elektronicznych i
zbli¿onych diagramów oraz tworzenia list po³±czeñ poprzez odczytanie
schematu. XCurcuit traktuje obwody jako nieod³±cznie hierarchiczne i
zapisuje zarówno hierarchiczne wyj¶cie w PostScripcie, jak i
hierarchiczne listy po³±czeñ SPICE. Sk³adniki obwodów s± zapisywane i
odczytywane z bibliotek, które s± w pe³ni modyfikowalne. XCircuit nie
oddziela wyra¿enia artystycznego od rysowania obwodów; zachowuje
elastyczno¶æ w stylu bez kompromisów kosztem mo¿liwo¶ci odczytu
schematu.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
%{__make} install-man \
	DESTDIR=$RPM_BUILD_ROOT \

install lib/pixmaps/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO examples
%attr(755,root,root) %{_bindir}/*
%dir %{_xcircuitdir}
%attr(755,root,root) %{_xcircuitdir}/*.so
%attr(755,root,root) %{_xcircuitdir}/*.tcl
%{_xcircuitdir}/*.lps
#%{_xcircuitdir}/*.script
%{_xcircuitdir}/*.pro
%dir %{_xcircuitdir}/app-defaults
%{_xcircuitdir}/app-defaults/XCircuit
%dir %{_xcircuitdir}/fonts
%{_xcircuitdir}/fonts/*.lps
%{_xcircuitdir}/fonts/*.xfe
%dir %{_xcircuitdir}/pixmaps
%{_xcircuitdir}/pixmaps/*.xpm
%{_xcircuitdir}/pixmaps/*.xbm
%{_pixmapsdir}/*
%{_mandir}/man1/*.1*
%{_desktopdir}/%{name}.desktop
