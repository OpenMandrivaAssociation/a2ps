%define version 4.14

Summary:	Converts text and other types of files to PostScript(TM)
Name:		a2ps
Version:	%{version}
Release:	%mkrel 1
License:	GPLv3+
Group:		Publishing
Url:		http://www.gnu.org/software/a2ps/
Source:		http://ftp.gnu.org/gnu/a2ps/%{name}-%{version}.tar.gz
Requires(post):	info-install
Requires(preun):info-install
BuildRequires:	X11-devel
BuildRequires:	bison
BuildRequires:	emacs-bin
#BuildRequires:	fetchmail
BuildRequires:	flex
BuildRequires:	gettext
BuildRequires:	mawk
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	texinfo
#BuildRequires:	xemacs
BuildRequires:  psutils
#Buildrequires:  gv
BuildRequires:  ImageMagick
Buildrequires:  groff
#Requires: ImageMagick groff gv psutils tetex-dvips tetex-latex texinfo
Requires:	ImageMagick groff psutils
Requires:	file binutils
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
Group:          Development/Other
Requires(pre):  %{name}-devel = %{version}-%{release}

%description static-devel
The a2ps filter converts text and other types of files to PostScript(TM).
A2ps has pretty-printing capabilities and includes support for a wide
number of programming languages, encodings (ISO Latins, Cyrillic, etc.),
and medias.

This package holds static libraries.

%prep
%setup -q -n %{name}-%{version}

%build

%configure
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
%_install_info a2ps.info
%_install_info ogonkify.info
%_install_info regex.info
# Adapt /usr/share/a2ps/afm/fonts.map to the current system environment
( cd %{_datadir}/%{name}/afm/
  ./make_fonts_map.sh > /dev/null 2>&1
  mv -f fonts.map.new fonts.map
)

%preun
%_remove_install_info a2ps.info
%_remove_install_info ogonkify.info
%_remove_install_info regex.info

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
%attr(755,root,root) %{_libdir}/*.la

%files static-devel
%defattr(644,root,root,755)
%{_libdir}/*.a


