# TODO:
# - Rs (X at least...)
Summary:	Drawing electrical circuit schematic diagrams and related figure
Summary(hu.UTF-8):	Elektromos áramkörök rajzolása
Summary(pl.UTF-8):	Rysowanie schematów elektronicznych i zbliżonych diagramów
Name:		xcircuit
Version:	3.8.38
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://opencircuitdesign.com/xcircuit/archive/%{name}-%{version}.tgz
# Source0-md5:	e749beb96374c89f84535d3e4629de7b
Source1:	%{name}.desktop
Source2:	http://opencircuitdesign.com/xcircuit/archive/tutorial.tar.gz
# Source2-md5:	16aaa9c90b0cc83f69c1837365817fe4
Patch1:		%{name}-not-a-string-literal.patch
URL:		http://opencircuitdesign.com/xcircuit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	tk-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _xcircuitdir    %{_libdir}/%{name}-3.8

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

%description -l hu.UTF-8
XCircuit egy UNIX/X11 program nyomdai minőségű elemktromos áramkörök
és hasonlók szedéséhe. Az XCircuit figyel a hierarchiára és a
PostScript kimenetnél és a SPICE listánál is megtartja. Az áramköri
komponensek könyvtárakba menti illetve tölti be, amelyek
szerkesztehtőek.

%description -l pl.UTF-8
XCircuit to program dla systemu UNIX/X11 do rysowania w jakości
nadającej się do publikacji różnych schematów elektronicznych i
zbliżonych diagramów oraz tworzenia list połączeń poprzez odczytanie
schematu. XCurcuit traktuje obwody jako nieodłącznie hierarchiczne i
zapisuje zarówno hierarchiczne wyjście w PostScripcie, jak i
hierarchiczne listy połączeń SPICE. Składniki obwodów są zapisywane i
odczytywane z bibliotek, które są w pełni modyfikowalne. XCircuit nie
oddziela wyrażenia artystycznego od rysowania obwodów; zachowuje
elastyczność w stylu bez kompromisów kosztem możliwości odczytu
schematu.

%package tutorial
Summary:	Tutorial to XCircuit
Summary(hu.UTF-8):	Tutorial az XCircuithoz
Group:		Applications/Engineering
Requires:	xcircuit = %{version}-%{release}

%description tutorial
Tutorial to XCircuit.

%description tutorial -l hu.UTF-8
Tutorial az XCircuithoz.

%prep
%setup -q
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure  \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} install-man \
	DESTDIR=$RPM_BUILD_ROOT

install lib/pixmaps/%{name}.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install -d $RPM_BUILD_ROOT%{_docdir}/xcircuit-tutorial
tar xf %{SOURCE2} -C $RPM_BUILD_ROOT%{_docdir}/xcircuit-tutorial

rm -rf $RPM_BUILD_ROOT%{_xcircuitdir}/man

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO examples
%attr(755,root,root) %{_bindir}/*
%dir %{_xcircuitdir}
%attr(755,root,root) %{_xcircuitdir}/*.so
%attr(755,root,root) %{_xcircuitdir}/*.tcl
%{_xcircuitdir}/*.cir
%{_xcircuitdir}/*.lps
#%{_xcircuitdir}/*.script
%{_xcircuitdir}/*.pro
%dir %{_xcircuitdir}/app-defaults
%{_xcircuitdir}/app-defaults/XCircuit
%dir %{_xcircuitdir}/fonts
%{_xcircuitdir}/fonts/*.lps
%{_xcircuitdir}/fonts/*.xfe
%dir %{_xcircuitdir}/pixmaps
%{_xcircuitdir}/pixmaps/*.gif
%{_xcircuitdir}/pixmaps/*.ico
%{_xcircuitdir}/pixmaps/*.xbm
%{_xcircuitdir}/xcircexec
%{_pixmapsdir}/*
%{_mandir}/man1/*.1*
%{_desktopdir}/%{name}.desktop

%files tutorial
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-tutorial
