%global tl_name delimseasy
%global tl_revision 77161

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Delimiter commands that are easy to use and resize
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/delimseasy
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delimseasy.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/delimseasy.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides commands to give a consistent, easy-to-remember,
easy to edit way to control the size and blackness of delimiters: append
1-4 "b"s to command for larger sizes; prepend "B" for boldface. These
commands reduce the likelihood of incomplete delimiter pairs and
typically use fewer characters than the LaTeX default.

