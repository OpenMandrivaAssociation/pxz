%global git_date 20100608

Summary:	Parallel LZMA compressor using XZ
Name:		pxz
Version:	4.999.9
Release:	3.beta.%{git_date}git
License:	GPLv2+
Group:		Archiving/Compression
# source created as "make dist" in checked out GIT tree: git clone git://github.com/jnovy/pxz.git
Source0:	http://jnovy.fedorapeople.org/%{name}/%{name}-%{version}beta.%{git_date}git.tar.xz
URL:		https://jnovy.fedorapeople.org/pxz
BuildRequires:	liblzma-devel libgomp-devel

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


%changelog
* Sat Jul 23 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 4.999.9-3.beta.20100608git
+ Revision: 691259
- add buildrequires
- adapt to mandriva packaging
- imported package pxz


* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.999.9-2.beta.20100608git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun  8 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-1.beta.20100608git
- initial import release

* Thu Jun  3 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20100603git
- review fixes (#598902)

* Wed May 26 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20100526git
- add -D option to specify context size per thread

* Fri Feb 19 2010 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20100217git
- better error handling and stability fixes

* Wed Dec  9 2009 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20091209git
- use fixed size context per thread (3x dict size by default)
- reduce memory requirements for compression

* Wed Nov 18 2009 Jindrich Novy <jnovy@redhat.com> 4.999.9-0.1.beta.20091118git
- initial packaging
