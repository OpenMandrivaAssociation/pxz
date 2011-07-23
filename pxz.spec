%global git_date 20100608

Summary:	Parallel LZMA compressor using XZ
Name:		pxz
Version:	4.999.9
Release:	3.beta.%{git_date}git
License:	GPLv2+
Group:		Archiving/Compression
# source created as "make dist" in checked out GIT tree: git clone git://github.com/jnovy/pxz.git
Source0:	http://jnovy.fedorapeople.org/%{name}/%{name}-%{version}beta.%{git_date}git.tar.xz
URL:		http://jnovy.fedorapeople.org/pxz

%description
Parallel XZ is a compression utility that takes advantage of running
XZ compression simultaneously on different parts of an input file on
multiple cores and processors. This significantly speeds up compression time.

%prep
%setup -q -n %{name}-%{version}beta

%build
export CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE"
%make

%install
%makeinstall_std

%files
%{_mandir}/man1/pxz.1*
%{_bindir}/pxz
