Summary:	The GNU Image Manipulation Program
Summary(pl):	GNU Gimp program do tworzenia i obróki grafiki
Name:		gimp-pats-tiger
Version:	1.0
Release:	5
License:	GPL
Group:		X11/Applications/Graphics
Vendor:		Tuomas Kuosmanen <tigert@nettilinja.fi>
Source0:	ftp://ftp.gimp.org/pub/gimp/contrib/pats-tigert-pov-granites.tar.gz
# Source0-md5:	5da8dfad505f3087f8de6521d76ee257
Source1:	ftp://ftp.gimp.org/pub/gimp/contrib/pats-tigert-pov-stones.tar.gz
# Source1-md5:	52fa33b8c881ff61f1f4e8fe640e8ca1
Source2:	ftp://ftp.gimp.org/pub/gimp/contrib/pats-tigert-pov.README
# Source2-md5:	f7fb7d743a8ba221412feede8c50b5f1
BuildRequires:	gimp-devel >= 1.2
Requires:	gimp >= 1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Buildarch:	noarch

%define		_gimpdatadir	%(gimp-config --gimpdatadir)

%description
Gimp patterns converted from the raytracing program Persistence of
Vision (PoVRay, see http://www.povray.org)

The packages contain gimp patterns from PoVRay's standard textures
T_Stone1-24 and T_Grnt1-29.

The patterns are meant to be used with GIMP, and are therefore
released under GPL - see www.gnu.org for more details.

%description -l pl
Wzorce Gimpa przekonwertowne z programu ¶ledz±cego promienie
Persistence of Vision (PoVRay, zob. http://www.povray.org). Pakiet
zawiera wzorce Gimpa ze standardowych tekstur PoVRay'a: T_Stone1-24
oraz T_Grnt1-29. Wzorce s± przeznaczone dla Gimpa i dlatego s±
udostêpnione na licencji GPL; Wiêcej szczegó³ów na temat GPL mo¿na
znale¼æ na stronach www.gnu.org.

%prep
%setup -q -c 0 -a 1
install %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_gimpdatadir}/patterns

install *pat $RPM_BUILD_ROOT%{_gimpdatadir}/patterns

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc pats-tigert-pov.README
%{_gimpdatadir}/patterns/*
