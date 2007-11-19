Summary:	Additional themes for splashy
Name:		splashy-themes
Version:	0.3.5
Release:	0.1
License:	GPL v2+
Group:		Themes
Source0:	themes.tar.bz2
# Source0-md5:	369e08eecb85f9b06bd6910c5165914a
Provides:	splashy-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_themedir	/etc/splashy/themes

%description
Available themes:
- fingerprint
- aqua
- mepis baghira

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_themedir}
cp -a themes/* $RPM_BUILD_ROOT%{_themedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_themedir}/*
