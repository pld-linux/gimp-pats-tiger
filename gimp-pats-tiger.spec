Summary:	The GNU Image Manipulation Program
Summary(pl):	GNU Gimp program do tworzenia i obr�ki grafiki 
Name:		gimp-pats-tiger
Version:	1.0
Release:	3
Copyright:	GPL
Group:		X11/Applications/Graphics
Group:		X11/Aplikacje/Grafika
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

%prep
%setup -q -c 0 -a 1
install %{SOURCE2} .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/share/gimp/patterns
install *pat $RPM_BUILD_ROOT/usr/share/gimp/patterns

gzip -9nf pats-tigert-pov.README
%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root)
%doc *gz
/usr/share/gimp/patterns/*

%changelog
* Thu Mar 25 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.0-2]
- added Group(pl),
- added gzipping %doc.

* Fri May  1 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
- first release in rpm package,
- spec contain %%{SOURCE2} and %defattr macros (this require using on
  rebuild rpm >= 2.4.99.
