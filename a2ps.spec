Summary:	Converts text and other types of files to PostScript(TM)
Name:		a2ps
Version:	4.14
Release:	28
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
%configure
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
%{_datadir}/emacs/site-lisp/*.elc

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%{_includedir}/*

%files static-devel
%defattr(644,root,root,755)
%{_libdir}/*.a
