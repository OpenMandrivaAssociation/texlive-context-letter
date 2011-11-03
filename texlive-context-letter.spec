# revision 24045
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-letter
# catalog-date 2011-09-20 21:18:19 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-context-letter
Version:	20110920
Release:	1
Summary:	Context package for writing letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-letter
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-context
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3
Requires(post):	texlive-context.bin

%description
A means of writing 'vanilla' letters is provided; the design of
letters may be amended by a wide range of style specifications.

%pre
    %_texmf_mtxrun_pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mtxrun_post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_pre
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mtxrun_post
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/context/interface/third/t-letter.xml
%{_texmfdistdir}/tex/context/interface/third/t-resume.xml
%{_texmfdistdir}/tex/context/third/letter/base/t-correspondence.mkii
%{_texmfdistdir}/tex/context/third/letter/base/t-correspondence.mkiv
%{_texmfdistdir}/tex/context/third/letter/base/t-correspondence.tex
%{_texmfdistdir}/tex/context/third/letter/base/t-letter.tex
%{_texmfdistdir}/tex/context/third/letter/base/t-resume.tex
%{_texmfdistdir}/tex/context/third/letter/extension/addrentry.nle
%{_texmfdistdir}/tex/context/third/letter/extension/corres.nle
%{_texmfdistdir}/tex/context/third/letter/extension/label.nle
%{_texmfdistdir}/tex/context/third/letter/extension/optimize.nle
%{_texmfdistdir}/tex/context/third/letter/extension/pragma.nle
%{_texmfdistdir}/tex/context/third/letter/interface/default.nli
%{_texmfdistdir}/tex/context/third/letter/interface/default.nri
%{_texmfdistdir}/tex/context/third/letter/interface/knuth.nli
%{_texmfdistdir}/tex/context/third/letter/interface/moderncv.nri
%{_texmfdistdir}/tex/context/third/letter/interface/pragma.nli
%{_texmfdistdir}/tex/context/third/letter/style/blockstyle.nls
%{_texmfdistdir}/tex/context/third/letter/style/casual.nrs
%{_texmfdistdir}/tex/context/third/letter/style/classic.nrs
%{_texmfdistdir}/tex/context/third/letter/style/default.nls
%{_texmfdistdir}/tex/context/third/letter/style/default.nrs
%{_texmfdistdir}/tex/context/third/letter/style/dina.nls
%{_texmfdistdir}/tex/context/third/letter/style/dinb.nls
%{_texmfdistdir}/tex/context/third/letter/style/dutch.nls
%{_texmfdistdir}/tex/context/third/letter/style/english.nls
%{_texmfdistdir}/tex/context/third/letter/style/french.nls
%{_texmfdistdir}/tex/context/third/letter/style/fullblock.nls
%{_texmfdistdir}/tex/context/third/letter/style/gbrief.nls
%{_texmfdistdir}/tex/context/third/letter/style/hanging.nls
%{_texmfdistdir}/tex/context/third/letter/style/knuth.nls
%{_texmfdistdir}/tex/context/third/letter/style/memo.nls
%{_texmfdistdir}/tex/context/third/letter/style/modified.nls
%{_texmfdistdir}/tex/context/third/letter/style/pragma.nls
%{_texmfdistdir}/tex/context/third/letter/style/semiblock.nls
%{_texmfdistdir}/tex/context/third/letter/style/simplified.nls
%{_texmfdistdir}/tex/context/third/letter/style/swiss.nls
%{_texmfdistdir}/tex/context/third/letter/style/swissleft.nls
%{_texmfdistdir}/tex/context/third/letter/style/user.ori
%doc %{_texmfdistdir}/doc/context/third/letter/README
%doc %{_texmfdistdir}/doc/context/third/letter/correspondence.pdf
%doc %{_texmfdistdir}/doc/context/third/letter/todo.txt
#- source
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-environment.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-introduction.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-labeltext.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-background.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-beginner.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-examples.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-extension.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-header.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-interface.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-layout.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-pagenumber.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-reference.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-styles.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-letter-values.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-resume-examples.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-resume-interface.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence-revision.tex
%doc %{_texmfdistdir}/source/context/third/letter/doc/correspondence.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
