Name:		texlive-delimseasy
Version:	39589
Release:	1
Summary:	Delimiter commands that are easy to use and resize
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/delimseasy
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimseasy.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/delimseasy.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides commands to give a consistent,
easy-to-remember, easy to edit way to control the size and
blackness of delimiters: append 1-4 "b"s to command for larger
sizes; prepend "B" for for boldface. These commands reduce the
likelihood of incomplete delimeter pairs and typically use
fewer characters than the LaTeX default.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/delimseasy
%doc %{_texmfdistdir}/doc/latex/delimseasy

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
