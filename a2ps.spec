Summary:	Converts text and other types of files to PostScript(TM)
Name:		a2ps
Version:	4.14
Release:	17
License:	GPLv3+
Group:		Publishing
Url:		http://www.gnu.org/software/a2ps/
Source:		http://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
Patch1:		a2ps-4.14-enable-display.patch
Patch2:		a2ps-4.14-fix-str-fmt.patch
Patch3:		a2ps-4.14-glibcpaper.patch
Patch4:		a2ps-4.14-texinfo-5.x.patch
Patch5:		a2ps-4.14-security.patch

BuildRequires:	bison
BuildRequires:	emacs-bin
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	gperf
BuildRequires:	groff-perl
BuildRequires:	html2ps
BuildRequires:	imagemagick
BuildRequires:	mawk
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	texinfo
BuildRequires:	psutils

Requires:	binutils
Requires:	file
Requires:	groff-perl
Requires:	imagemagick
Requires:	psutils

%description
The a2ps filter converts text and other types of files to PostScript(TM).
a2ps has pretty-printing capabilities and includes support for a wide
number of programming languages, encodings (ISO Latins, Cyrillic, etc.),
and medias.

%package devel
Summary:	Include files for %{name}
Group:		Development/Other
Requires(pre):	%{name} = %{version}-%{release}

%description devel
The a2ps filter converts text and other types of files to PostScript(TM).
A2ps has pretty-printing capabilities and includes support for a wide
number of programming languages, encodings (ISO Latins, Cyrillic, etc.),
and medias.

This package holds include files.

%package static-devel
Summary:	Static libraries for %{name}
Group:		Development/Other
Requires(pre):	%{name}-devel = %{version}-%{release}

%description static-devel
The a2ps filter converts text and other types of files to PostScript(TM).
A2ps has pretty-printing capabilities and includes support for a wide
number of programming languages, encodings (ISO Latins, Cyrillic, etc.),
and medias.

This package holds static libraries.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1 -b .enable-display
%patch2 -p0 -b .str

# Ensure the paper size is properly modified upon locale (from fedora)
%patch3 -p1

%patch4 -p1 -b .texi~

# Security enhancement (from fedora)
%patch5 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%post
# Adapt /usr/share/a2ps/afm/fonts.map to the current system environment
( cd %{_datadir}/%{name}/afm/
  ./make_fonts_map.sh > /dev/null 2>&1
  mv -f fonts.map.new fonts.map
)

%files -f %{name}.lang
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/a2ps.cfg
%config(noreplace) %{_sysconfdir}/a2ps-site.cfg
%doc AUTHORS NEWS README TODO THANKS
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_datadir}/%{name}/afm/make_fonts_map.sh
%{_infodir}/a2ps.info*
%{_infodir}/ogonkify.info*
%{_infodir}/regex.info*
%{_mandir}/man1/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/README
%{_datadir}/%{name}/afm/*.afm
%{_datadir}/%{name}/afm/*.map
%{_datadir}/%{name}/encoding/
%{_datadir}/%{name}/fonts/
%{_datadir}/%{name}/ppd/
%{_datadir}/%{name}/ps/
%{_datadir}/%{name}/sheets/
%{_datadir}/ogonkify/
%{_datadir}/emacs/site-lisp/a2ps-print.el
%{_datadir}/emacs/site-lisp/a2ps.el
%{_datadir}/emacs/site-lisp/*.elc

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%{_includedir}/*

%files static-devel
%defattr(644,root,root,755)
%{_libdir}/*.a


%changelog
* Sat Jun 02 2012 Andrey Bondrov <abondrov@mandriva.org> 4.14-12mdv2012.0
+ Revision: 801901
- Don't use info-install for mdver >= 201200, minor cleanups

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 4.14-11
+ Revision: 662746
- mass rebuild

* Wed Feb 02 2011 Funda Wang <fwang@mandriva.org> 4.14-10
+ Revision: 634991
- rebuild
- tighten BR

* Mon Nov 29 2010 Oden Eriksson <oeriksson@mandriva.com> 4.14-9mdv2011.0
+ Revision: 603164
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - rebuild

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 4.14-7mdv2010.1
+ Revision: 506942
- rebuild for missing SRPM

* Sun Jan 03 2010 Stéphane Téletchéa <steletch@mandriva.org> 4.14-6mdv2010.1
+ Revision: 486078
- Remove encoding patch for now since it breaks badly the program

* Fri Oct 09 2009 Stéphane Téletchéa <steletch@mandriva.org> 4.14-5mdv2010.0
+ Revision: 456289
- Add paper size autorecognition (fixes #36107)
- Add locale autodectection
- Security enhancement
- Inline dependencies so they are better visible, add html2ps
- Add groff-perl instead of groff as indicated during the build

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 4.14-4mdv2010.0
+ Revision: 413016
- rebuild

* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 4.14-3mdv2009.1
+ Revision: 364705
- fix str fmt

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 4.14-3mdv2009.0
+ Revision: 264317
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 22 2008 Tiago Salem <salem@mandriva.com.br> 4.14-2mdv2009.0
+ Revision: 196581
- add a 'display' printer by default (#20416)

* Wed Jan 30 2008 Marcelo Ricardo Leitner <mrl@mandriva.com> 4.14-1mdv2008.1
+ Revision: 160231
- added buildrequires to gperf.
- New upstream: 4.14 from Frederik Himpe.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Feb 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.13b-12mdv2007.0
+ Revision: 120245
- set correct bits on make_fonts_map.sh

* Mon Feb 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 4.13b-11mdv2007.1
+ Revision: 119945
- Import a2ps

* Fri Feb 24 2006 Till Kamppeter <till@mandrakesoft.com> 4.13b-10mdk
- Fixed BuildRequires for X11 ("X11-devel").

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 4.13b-9mdk
- Rebuild

* Fri Aug 12 2005 Nicolas L�cureuil <neoclust@mandriva.org> 4.13b-8mdk
- Fix PreReq

* Thu Aug 11 2005 Nicolas L�cureuil <neoclust@mandriva.org> 4.13b-7mdk
- Fix PreReq

* Wed Nov 24 2004 Till Kamppeter <till@mandrakesoft.com> 4.13b-6mdk
- SECURITY FIX: File name command execution vulnerability (bug 11895) fixed
  by Patch 3.

* Sat Oct 02 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 4.13b-5mdk
- includes, 64-bit & varargs & 64-bit fixes

* Sun Mar 14 2004 Till Kamppeter <till@mandrakesoft.com> 4.13b-4mdk
- Removed "gv" from "Requires:".

