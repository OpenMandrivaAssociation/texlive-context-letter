# revision 27229
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-letter
# catalog-date 2012-02-13 08:46:03 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-letter
Version:	20120213
Release:	3
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
%doc %{_texmfdistdir}/doc/context/third/letter/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120213-2
+ Revision: 812175
- Update to latest release.
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120213-1
+ Revision: 779425
- Update to latest release.

* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120122-1
+ Revision: 770137
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111214-3
+ Revision: 758838
- Update to latest upstream release

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111214-2
+ Revision: 750500
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111214-1
+ Revision: 745170
- texlive-context-letter

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110920-1
+ Revision: 718135
- texlive-context-letter
- texlive-context-letter
- texlive-context-letter
- texlive-context-letter

