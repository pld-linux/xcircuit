# TODO:
# - pl-translation, icon and desktop
Summary:	Drawing electrical circuit schematic diagrams and related figure
Name:		xcircuit
Version:	3.1.38
Release:	0.1
License:	GPL
Group:		Applications/Engineering
Source0:	http://bach.ece.jhu.edu/~tim/programs/xcircuit/archive/%{name}-%{version}.tgz
# Source0-md5:	097a5001243c876a9bb0128d0b09d285
URL:		http://bach.ece.jhu.edu/~tim/programs/xcircuit/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xcircuitdir	%{_libdir}/%{name}-3.1

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README* TODO examples
%attr(755,root,root) %{_bindir}/*
%dir %{_xcircuitdir}
%{_xcircuitdir}/*.lps
%{_xcircuitdir}/*.script
%{_xcircuitdir}/*.pro
%dir %{_xcircuitdir}/app-defaults
%{_xcircuitdir}/app-defaults/XCircuit
%dir %{_xcircuitdir}/fonts
%{_xcircuitdir}/fonts/*.lps
%{_xcircuitdir}/fonts/*.xfe
#%{_desktopdir}/*.desktop
#%{_pixmapsdir}/*
%{_mandir}/man1/*.1*
