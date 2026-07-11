%global tl_name context-letter
%global tl_revision 77841

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	ConTeXt package for writing letters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-letter
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A means of writing 'vanilla' letters and memos is provided, with support
covering ConTeXt Mkii and Mkiv. The design of letters may be amended by
a wide range of style specifications.

