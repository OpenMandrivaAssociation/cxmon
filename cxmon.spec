%define name	cxmon
%define version	3.2
%define release	%mkrel 4

Summary:	Command-line file manipulation tool and disassembler
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
URL:		http://cxmon.cebix.net/
Source0:	http://cxmon.cebix.net/downloads/%name-%version.tar.gz
Patch0:		cxmon-3.2-includes.patch
Patch1:		cxmon-3.1-pef-decoder.patch
Patch2:		cxmon-3.2-fix-str-fmt.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	readline-devel, ncurses-devel

%description
cxmon is an interactive command-driven file manipulation tool that is
inspired by the "Amiga Monitor" by Timo Rossi. It has commands and
features similar to a machine code monitor/debugger, but it lacks any
functions for running/tracing code. There are, however, built-in
PowerPC, 680x0, 80x86, AMD64, 6502 and Z80 disassemblers and special
support for disassembling MacOS code (LowMem globals, named A-Traps).

%prep
%setup -q
%patch0 -p1 -b .includes
%patch1 -p1 -b .pef-decoder
%patch2 -p0 -b .str

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README ChangeLog
%_bindir/cxmon
%_mandir/man1/cxmon.1*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2-4mdv2011.0
+ Revision: 617489
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 3.2-3mdv2010.0
+ Revision: 437212
- rebuild

* Fri Apr 03 2009 Funda Wang <fwang@mandriva.org> 3.2-2mdv2009.1
+ Revision: 363654
- fix str fmt
- rediff includes patch

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3.2-2mdv2009.0
+ Revision: 266548
- rebuild early 2009.0 package (before pixel changes)

* Fri May 02 2008 Funda Wang <fwang@mandriva.org> 3.2-1mdv2009.0
+ Revision: 200033
- New version 3.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.1-3mdv2008.1
+ Revision: 123629
- kill re-definition of %%buildroot on Pixel's request


* Mon Mar 13 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 3.1-3mdk
- Add PEF object decoder
- Update to CVS snapshot 2006/03/13:
  * 64-bit fixes to m68k disassembler
  * Add AltiVec support to ppc disassembler

* Mon Apr 04 2005 Nicolas Lécureuil <neoclust@mandrake.org> 3.1-2mdk
- %%mkrel
- Rebuild for readline

* Mon Jun 07 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.1-1mdk
- 3.1

* Mon Apr 28 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-10mdk
- Fix printing of m68k addresses though we assume they are always
  32-bit values even in real addressing mode.

* Thu Feb 06 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-9mdk
- Update to CVS snapshot 2003/02/06:
  - Force use of AT&T syntax for x86[-64] disassembly
  - Fix x86-64 disassembly for movd with REX prefixes

* Wed Jan 29 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-8mdk
- Fix x86-64 disassembler usage

* Fri Jan 17 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-7mdk
- Rebuild

* Sat Sep 07 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-6mdk
- BuildRequires: readline-devel, ncurses-devel
- Update to CVS snapshot 2002/09/07:
  - Merge and update 64-bit fixes
  - Make LowMem globals as predefined variables
  - Add x86-64 disassembler from binutils 2.12.90.0.15

* Fri Sep 06 2002 Lenny Cartier <lenny@mandrakesoft.com> 3.0-5mdk
- rebuild

* Wed Jul 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 3.0-4mdk
- rebuild for new readline

* Tue May 28 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-3mdk
- Rebuild with gcc3.1

* Thu Dec 06 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-2mdk
- Rpmlint odyssey
- Patch0: Add missing includes
- Patch1: Tentative patch for 64-bit architecture support

* Tue Apr 10 2001 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 3.0-1mdk
- First Mandrake package

