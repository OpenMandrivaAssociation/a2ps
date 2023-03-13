%global _disable_rebuild_configure 1

Summary:	Converts text and other types of files to PostScript(TM)
Name:		a2ps
Version:	4.15.1
Release:	1
License:	GPLv3+
Group:		Publishing
Url:		http://www.gnu.org/software/a2ps/
Source:		http://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
Patch1:		a2ps-4.14-enable-display.patch
#Patch2:		a2ps-4.14-fix-str-fmt.patch
#Patch3:		a2ps-4.14-glibcpaper.patch
#Patch4:		a2ps-4.14-texinfo-5.x.patch
#Patch5:		a2ps-4.14-security.patch
Patch2:		a2ps-gnulib-attribute-malloc.patch

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
BuildRequires:	pkgconfig(bdw-gc)

Requires:	binutils
Requires:	file
Requires:	groff-perl
Requires:	imagemagick
Requires:	psutils

# The library was never used by anything and is not built anymore either
Obsoletes:	%{name}-devel < %{EVRD}
Obsoletes:	%{name}-static-devel < %{EVRD}

%description
The a2ps filter converts text and other types of files to PostScript(TM).
a2ps has pretty-printing capabilities and includes support for a wide
number of programming languages, encodings (ISO Latins, Cyrillic, etc.),
and medias.

%prep
%autosetup -p1
%configure --with-encoding=utf-8

%build
%make_build

%install
%make_install

%find_lang %{name} --all-name

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
%dir %{_datadir}/%{name}/afm
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
