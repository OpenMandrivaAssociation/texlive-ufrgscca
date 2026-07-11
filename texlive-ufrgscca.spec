%global tl_name ufrgscca
%global tl_revision 79593

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.13a
Release:	%{tl_revision}.1
Summary:	A bundle for undergraduate students final work/report (tcc) at UFRGS/EE
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ufrgscca
License:	lppl1.3c agpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ufrgscca.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ufrgscca.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle is aimed at producing undergraduate students' final
work/report at UFRGS/EE (Engineering School at the Federal University of
Rio Grande do Sul), closely following ABNT rules (Brazilian Association
for Technical Norms). It is composed of a main class, ufrgscca, and a
set of auxiliary packages, some of which can be used independently.

