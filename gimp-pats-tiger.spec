Summary:	The GNU Image Manipulation Program
Summary(pl):	GNU Gimp program do tworzenia i obróki grafiki 
Name:		gimp-pats-tiger
Version:	1.0
Release:	3
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Vendor:		Tuomas Kuosmanen <tigert@nettilinja.fi>
Source:		ftp://ftp.gimp.org/pub/gimp/contrib/pats-tigert-pov-granites.tar.gz
Source1:	ftp://ftp.gimp.org/pub/gimp/contrib/pats-tigert-pov-stones.tar.gz
Source2:	ftp://ftp.gimp.org/pub/gimp/contrib/pats-tigert-pov.README
Requires:	gimp
BuildRoot:	/tmp/%{name}-%{version}-root
Buildarch:	noarch

%description
Gimp patterns converted from the raytracing             
program Persistence of Vision (PoVRay, see http://www.povray.org)       
                                                                                
The packages contain gimp patterns from PoVRay's standard               
textures T_Stone1-24 and T_Grnt1-29.                                    
                                                                                
The patterns are meant to be used with GIMP, and are therefore          
released under GPL - see www.gnu.org for more details.                  

%description -l pl
Wzorce Gimpa przekonwertowne z programu ¶ledz±cego promienie Persistence of 
Vision (PoVRay, zob. http://www.povray.org).
Pakiet zawiera wzorce Gimpa ze standardowych tekstur PoVRay'a:
T_Stone1-24 oraz T_Grnt1-29.                                    
Wzorce s± przeznaczone dla Gimpa i dlatego s± udostêpnione na licencji GPL;
Wiêcej szczegó³ów na temat GPL mo¿na znale¼æ na stronach www.gnu.org.

%prep
%setup -q -c 0 -a 1
install %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gimp/patterns
install *pat $RPM_BUILD_ROOT%{_datadir}/gimp/patterns

gzip -9nf pats-tigert-pov.README

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root)
%doc *gz
%{_datadir}/gimp/patterns/*
