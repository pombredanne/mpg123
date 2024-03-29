# This is a generic spec file that should "just work" with rpmbuild on any distro.
# Make sure you have appropriate -devel packes installed:
# - the package providing libltdl.so and .la (libtool or libtool-devel)
# - devel packages for alsa, sdl, etc... to build the respective output modules.
Summary:	The fast console mpeg audio decoder/player.
Name:		mpg123
Version:	1.15.4
Release:	1
URL:		http://www.mpg123.org/
License:	GPL
Group:		Applications/Multimedia
Source:		http://www.mpg123.org/download/mpg123-%{version}.tar.bz2
BuildRequires: autoconf
buildRequires: automake

%description
This is a console based decoder/player for mono/stereo mpeg audio files,
probably more familiar as MP3 or MP2 files. It's focus is speed.
It can play MPEG1.0/2.0/2.5 layer I, II, II (1, 2, 3;-) files
(VBR files are fine, too) and produce output on a number of different ways:
raw data to stdout and different sound systems depending on your platform.

%package devel
Summary:	Files needed for development with mpg123
Group:		Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Libraries and header files for development with mpg123.

%prep
%setup -q -n %name-%version

%build
%configure --with-cpu=generic_fpu --enable-shared --disable-static --disable-ltdl-install
make

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
ldconfig

%postun
ldconfig

%files
%defattr(755,root,root)
%{_bindir}/*
%defattr(644,root,root)
%doc %{_mandir}/*/mpg123.1.gz
%{_libdir}/libmpg123.so.*
#%{_libdir}/mpg123/output_*.la
#%{_libdir}/mpg123/output_*.so

%files devel
%defattr(644,root,root)
%{_libdir}/pkgconfig/libmpg123.pc
%{_includedir}/*.h
#%{_libdir}/libmpg123.a
%{_libdir}/libmpg123.la
%{_libdir}/libmpg123.so
#%exclude %{_libdir}/mpg123/output_*.a

%changelog
* Tue Jan  1 2008 Michael Ryzhykh <mclroy@gmail.com>
- Initial Version.

