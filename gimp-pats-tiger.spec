Summary:   The GNU Image Manipulation Program
Name:      gimp-pats-tiger
Version:   1.0
Release:   1
Copyright: GPL
Group:     X11/Applications/Graphics
Source0:   ftp://ftp.gimp.org/pub/gimp/0.99/contrib/pats-tigert-pov-granites.tar.gz
Source1:   ftp://ftp.gimp.org/pub/gimp/0.99/contrib/pats-tigert-pov-stones.tar.gz
Source2:   pats-tigert-pov.README
Requires:  gimp
Vendor:    Tuomas Kuosmanen <tigert@nettilinja.fi>
BuildRoot: /tmp/%{name}-%{version}-root
BuildArchitectures: noarch
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

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644, root, root)
%doc pats-tigert-pov.README
/usr/share/gimp/patterns/*

%changelog
* Fri May  1 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- first release in rpm package,
- spec contain %%{SOURCE2} and %defattr macros (this require using on
  rebuild rpm >= 2.4.99.
