Name:		texlive-ufrgscca
Version:	70161
Release:	1
Summary:	A bundle for undergraduate students final work/report (tcc) at UFRGS/EE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ufrgscca
License:	lppl1.3c gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ufrgscca.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ufrgscca.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundled is aimed at producing undergraduate students'
final work/report at UFRGS/EE (Engineering School at the
Federal University of Rio Grande do Sul), closely following
ABNT rules (Brazilian Association for Technical Norms). It is
composed of a main class, ufrgscca, and a set of auxiliary
packages, some of which can be used independently.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/ufrgscca
%doc %{_texmfdistdir}/doc/latex/ufrgscca

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
