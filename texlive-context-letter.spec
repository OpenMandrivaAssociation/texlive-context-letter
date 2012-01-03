# revision 24882
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-letter
# catalog-date 2011-12-14 08:38:50 +0100
# catalog-license pd
# catalog-version undef
Name:		texlive-context-letter
Version:	20111214
Release:	2
Summary:	Context package for writing letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-letter
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
A means of writing 'vanilla' letters is provided; the design of
letters may be amended by a wide range of style specifications.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-correspondence.xml
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-00.lua
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-00.mkii
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-00.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-01.mkii
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-01.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-02.mkii
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-02.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/t-letter.mkii
%{_texmfdistdir}/tex/context/third/letter/base/t-letter.mkiv
%{_texmfdistdir}/tex/context/third/letter/base/t-memo.mkii
%{_texmfdistdir}/tex/context/third/letter/base/t-memo.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-default.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-default.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-dina.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-dina.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-dinb.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-dinb.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-dutch.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-dutch.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-french.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-french.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-gbrief.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-gbrief.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swiss.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swiss.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swissleft.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swissleft.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-test.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-default.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-default.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-margin.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-margin.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-memo.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-memo.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-table.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-table.mkiv
%doc %{_texmfdistdir}/doc/context/third/letter/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
