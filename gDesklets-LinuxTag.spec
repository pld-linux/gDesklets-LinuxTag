%define		pname	LinuxTag
Summary:	This package contains some nice displays
Summary(pl.UTF-8):	Ten pakiet zawiera kilka ładnych wyświetlaczy
Name:		gDesklets-%{pname}
Version:	1
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://www.pycage.de/download/gdesklets/%{pname}.tar.bz2
# Source0-md5:	7954215d9fe249b679da49a50c572232
URL:		http://www.pycage.de/software_gdesklets.html
Requires:	gDesklets-StarterKit
Provides:	gDesklets-display
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains some nice displays.

%description -l pl.UTF-8
Ten pakiet zawiera kilka ładnych wyświetlaczy.

%prep
%setup -q -n %{pname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gdesklets/Displays/%{pname}

cp -R gfx *.display $RPM_BUILD_ROOT%{_datadir}/gdesklets/Displays/%{pname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_datadir}/gdesklets/Displays/*
