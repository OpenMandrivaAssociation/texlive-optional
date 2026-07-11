%global tl_name optional
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.2b
Release:	%{tl_revision}.1
Summary:	Facilitate optional printing of parts of a document
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/optional
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/optional.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/optional.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Optional provides simple, flexible, optional compilation of LaTeX
documents. Option switches may be given via package options, by the
\UseOption command, or interactively via the \AskOption command (help
text may be provided, by defining the \ExplainOptions command). The
package is not robust, in the way that comment package is, against ill-
behaved text. In particular, verbatim text may not be directly included
in optional sections (whether they're included or not).

