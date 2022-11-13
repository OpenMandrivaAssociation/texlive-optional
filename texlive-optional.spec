Name:		texlive-optional
Version:	18131
Release:	1
Summary:	Facilitate optional printing of parts of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/optional
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optional.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optional.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Optional provides simple, flexible, optional compilation of
LaTeX documents. Option switches may be given via package
options, by the \UseOption command, or interactively via the
\AskOption command (help text may be provided, by defining the
\ExplainOptions command). The package is not robust, in the way
that comment package is, against ill-behaved text. In
particular, verbatim text may not be directly included in
optional sections (whether they're included or not).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/optional/optional.sty
%doc %{_texmfdistdir}/doc/latex/optional/optional.pdf
%doc %{_texmfdistdir}/doc/latex/optional/optional.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
