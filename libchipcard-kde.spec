Summary:	KDE tools for LibChipCard
Summary(pl):	Narzêdzia KDE dla LibChipCard
Name:		libchipcard-kde
Version:	0.9
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/libchipcard/%{name}-%{version}.tar.gz
# Source0-md5:	4c7fe55a9febb09ebb037430d55eebb0
URL:		http://www.libchipcard.de/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libchipcard-devel
BuildRequires:	pcsc-lite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the KDE tools for LibChipCard. The most
important tool is KCardSetup, the graphical setup tool for
LibChipCard.

%description -l pl
Ten pakiet zawiera narzêdzia KDE dla LibChipCard. Najwa¿niejsze to
KCardSetup, graficzny konfigurator do LibChipCard.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-applnk-dir=%{_applnkdir}/Utilities

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# kchipcardcontrol, kcardsetup, kmedicalcard, kpcscsetup
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/kchipcardcontrol
%attr(755,root,root) %{_bindir}/kcardsetup
%attr(755,root,root) %{_bindir}/kmedicalcard
%attr(755,root,root) %{_bindir}/kpcscsetup
%dir %{_applnkdir}/Utilities/Chipcard-Utilities
%{_applnkdir}/Utilities/Chipcard-Utilities/.directory
%{_applnkdir}/Utilities/Chipcard-Utilities/kchipcardcontrol.desktop
%{_applnkdir}/Utilities/Chipcard-Utilities/kcardsetup.desktop
%{_applnkdir}/Utilities/Chipcard-Utilities/kmedicalcard.desktop
%{_applnkdir}/Utilities/Chipcard-Utilities/kpcscsetup.desktop
