%define name	cxmon
%define version	3.2
%define release	%mkrel 2

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

