Name:		texlive-context-letter
Version:	60787
Release:	1
Summary:	Context package for writing letters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-letter
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-letter.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/context/third/letter
%doc %{_texmfdistdir}/doc/context/third/letter

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
