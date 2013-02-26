%define		_class		HTML
%define		_subclass	Template
%define		upstream_name	%{_class}_%{_subclass}_Sigma

Name:		php-pear-%{upstream_name}
Version:	1.2.0
Release:	%mkrel 8
Summary:	Integrated Templates API implemetation with template 'compilation'
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Template_Sigma/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
HTML_Template_Sigma implements Integrated Templates API designed by
Ulf Wendel.

Features:
- Nested blocks. Nesting is controlled by the engine.
- Ability to include files from within template: <!-- INCLUDE -->
- Automatic removal of empty blocks and unknown variables (methods to
  manually tweak/override this are also available)
- Methods for runtime addition and replacement of blocks in templates
- Ability to insert simple function calls into templates:
  func_uppercase('Hello world!') and to define callback functions for
  these
- 'Compiled' templates: the engine has to parse a template file using
  regular expressions to find all the blocks and variable placeholders.
  This is a very "expensive" operation and is an overkill to do on every
  page request: templates seldom change on production websites. Thus
  this feature: an internal representation of the template structure is
  saved into a file and this file gets loaded instead of the source one
  on subsequent requests (unless the source changes)
- PHPUnit-based tests to define correct behaviour
- Usage examples for most of the features are available, look in the
  docs/ directory

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-6mdv2011.0
+ Revision: 667510
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-5mdv2011.0
+ Revision: 607108
- rebuild

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-4mdv2010.1
+ Revision: 477889
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.2.0-3mdv2010.0
+ Revision: 426644
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-2mdv2009.1
+ Revision: 321867
- rebuild

* Sat Aug 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdv2009.0
+ Revision: 272590
- 1.2.0

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1.6-3mdv2009.0
+ Revision: 224745
- rebuild

* Tue Feb 12 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1.6-2mdv2008.1
+ Revision: 166139
- rpmlint fixes

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.6-1mdv2008.0
+ Revision: 28897
- 1.1.6

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.5-1mdv2008.0
+ Revision: 15466
- 1.1.5


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2mdv2007.0
+ Revision: 81122
- Import php-pear-HTML_Template_Sigma

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.4-1mdk
- 1.1.4

* Thu Sep 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-1mdk
- 1.1.3

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-1mdk
- initial Mandriva package (PLD import)

