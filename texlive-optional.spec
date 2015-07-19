# revision 18131
# category Package
# catalog-ctan /macros/latex/contrib/optional
# catalog-date 2010-05-11 12:50:01 +0200
# catalog-license lppl
# catalog-version 2.2b
Name:		texlive-optional
Version:	2.2b
Release:	10
Summary:	Facilitate optional printing of parts of a document
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/optional
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optional.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/optional.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2b-2
+ Revision: 754553
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2b-1
+ Revision: 719166
- texlive-optional
- texlive-optional
- texlive-optional
- texlive-optional

