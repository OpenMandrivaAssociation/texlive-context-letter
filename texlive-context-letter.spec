Name:		texlive-context-letter
Version:	20171114
Release:	2
Summary:	Context package for writing letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-letter
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
A means of writing 'vanilla' letters and memos is provided,
with support covering Context Mkii and Mkiv. The design of
letters may be amended by a wide range of style specifications.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-letter.xml
%{_texmfdistdir}/tex/context/interface/third/t-memo.xml
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-00.lua
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-00.mkii
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-00.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-01.mkii
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-01.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-02.mkii
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-02.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-03.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/s-cor-06.mkvi
%{_texmfdistdir}/tex/context/third/letter/base/t-letter.mkii
%{_texmfdistdir}/tex/context/third/letter/base/t-letter.mkiv
%{_texmfdistdir}/tex/context/third/letter/base/t-memo.mkii
%{_texmfdistdir}/tex/context/third/letter/base/t-memo.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-blockstyle.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-blockstyle.mkiv
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
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-fullblock.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-fullblock.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-gbrief.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-gbrief.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-hanging.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-hanging.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-knuth.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-knuth.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-modified.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-modified.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-semiblock.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-semiblock.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-setups.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-setups.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-simplified.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-simplified.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swiss.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swiss.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swissleft.mkii
%{_texmfdistdir}/tex/context/third/letter/style/letter-imp-swissleft.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-default.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-default.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-margin.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-margin.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-memo.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-memo.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-table.mkii
%{_texmfdistdir}/tex/context/third/letter/style/memo-imp-table.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-casual-blue.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-casual-green.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-casual-grey.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-casual-orange.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-casual-red.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-casual.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-classic-blue.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-classic-green.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-classic-grey.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-classic-orange.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-classic-red.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-classic.mkiv
%{_texmfdistdir}/tex/context/third/letter/style/resume-imp-default.mkiv
%doc %{_texmfdistdir}/doc/context/third/letter/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
