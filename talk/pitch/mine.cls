\ProvidesClass{mine}

\RequirePackage{amssymb}
\RequirePackage{xcolor}
\RequirePackage{calc}
\RequirePackage{graphics}
\RequirePackage{newcent}
\RequirePackage{array}
\RequirePackage{ltxtable}
\RequirePackage{tabularx}

% font defaults
\def\rmdefault{cmss}
\def\sfdefault{cmss}
\def\ttdefault{cmtt}
\def\itdefault{sl}
\def\sldefault{sl}
\def\bfdefault{bx}

\DeclareMathSizes{20.74}{20.74}{17.28}{14.4}

\renewcommand\normalsize{
\fontsize{20.74}{23}\selectfont
\setlength\itemsep{10pt}
\setlength\topsep{10pt}
}
\normalsize
\ttfamily
\mdseries

\def\small{\fontsize{13.82}{16}\selectfont}
\def\large{\fontsize{28.66}{16}\selectfont}
\def\tiny{\fontsize{10.82}{16}\selectfont}
\def\huge{\fontsize{100}{23}\selectfont}

\setlength\paperwidth{11in}
\setlength\paperheight{8.5in}%
% no margins
\setlength\oddsidemargin{-0.5in}%
\setlength\evensidemargin{-0.5in}%

\setlength\textwidth{\paperwidth-1in}%
\setlength\textheight{\paperheight-0.6in}%
\setlength\hoffset{0in}
\setlength\voffset{0in}
% no header
\setlength\topmargin{-0.8in}%
\setlength\headheight{0in}%
\setlength\headsep{0.1in}%

% don't want any marginal notes
\setlength\marginparsep{0in}%
\setlength\marginparwidth{0in}%

% no footer
\setlength\footskip{0in}

% indentation for paragraph
\setlength\parindent{0in}
\setlength\parskip{0.5\baselineskip}


 %tabular

 \setlength\arraycolsep{5pt}
 \setlength\tabcolsep{6pt}
 \setlength\arrayrulewidth{0.4pt}
 \setlength\doublerulesep{2pt}
 \renewcommand\arraystretch{1.0}















% space after symbol in items and enums
\def\labelsep{0.5\baselineskip}
\setlength\tabbingsep{\labelsep}

% space before symbol
\setlength\leftmargini{1.3\baselineskip}

%
\newcommand\itemcolour{\color{red}}
\def\@listi{\leftmargin\leftmargini}
\newcommand\labelitemi{\itemcolour$\m@th\blacktriangleright$}
\newcommand\labelitemii{\itemcolour$\m@th\vartriangleright$}
\newcommand\labelitemiii{\itemcolour$\m@th\vartriangleright$}

% enums
\renewcommand\theenumi{\@arabic\c@enumi}
\renewcommand\theenumii{\@arabic\c@enumi}
\renewcommand\theenumiii{\@arabic\c@enumi}
\newcommand\labelenumi{\color{red}\theenumi.}
\newcommand\labelenumii{\color{red}\theenumii.}
\newcommand\labelenumiii{\color{red}\theenumiii.}


\renewcommand\baselinestretch{}


%

% headers

% old font commands
\DeclareOldFontCommand{\rm}{\normalfont\rmfamily}{\mathrm}
\DeclareOldFontCommand{\sf}{\normalfont\sffamily}{\mathsf}
\DeclareOldFontCommand{\tt}{\normalfont\ttfamily}{\mathtt}
\DeclareOldFontCommand{\bf}{\normalfont\bfseries}{\mathbf}
\DeclareOldFontCommand{\it}{\normalfont\itshape}{\mathit}
\DeclareOldFontCommand{\sl}{\normalfont\slshape}{\relax}
\DeclareOldFontCommand{\sc}{\normalfont\scshape}{\relax}
\DeclareRobustCommand*{\cal}{\@fontswitch{\relax}{\mathcal}}
\DeclareRobustCommand*{\mit}{\@fontswitch{\relax}{\mathnormal}}


% pre-defined colours
\definecolor{Maroon}  {cmyk}{0,0.87,0.68,0.32}
\definecolor{Mulberry}{cmyk}{0.34,0.90,0,0.02}
\definecolor{DarkBlue}{rgb} {0.0,0.0,0.4}

\newcommand\headerbg{white}
\newcommand\headerfg{blue}


\newcommand\spanbox[2]
{
\colorbox{#1}{
\parbox[c][\baselineskip]{\textwidth-6\fboxsep}
{\makebox[\textwidth-8\fboxsep]{\color{\headerfg}\textbf{\sloppy#2}}}}
}


\newcommand{\slide}[1]
{\newpage
\spanbox{\headerbg}{\underline{#1}}
\\
}


\newenvironment{Slide}[1]{
\slide{#1}
\par
\hspace*{\stretch{1}}
\begin{minipage}[c]%
[\textheight-4\baselineskip+2\fboxsep][t]%
{\paperwidth-2\baselineskip-2\fboxsep}
}{
%footer
\end{minipage}\hspace*{\stretch{1}}
}


% sub-header
\newcommand\subheader[1]{\underline{\textbf{\color{blue}#1}}\vspace{10pt}}

% split page (50-50)
\newcommand\split[2]{
\begin{center}
\begin{minipage}{0.48\textwidth}
#1
\end{minipage}
\hspace*{0.02\textwidth}
\begin{minipage}{0.48\textwidth}
#2
\end{minipage}
\end{center}
}

\newcommand\Split[2]{
\begin{center}
\begin{minipage}{0.3\textwidth}
#1
\end{minipage}
\hspace*{0.024\textwidth}
\begin{minipage}{0.65\textwidth}
#2
\end{minipage}
\end{center}
}

\newcommand\Splitt[2]{
\begin{center}
\begin{minipage}{0.65\textwidth}
#1
\end{minipage}
\hspace*{0.01\textwidth}
\begin{minipage}{0.32\textwidth}
#2
\end{minipage}
\end{center}
}

% for including eps files
\newcommand{\inc}[1]{\resizebox{\textwidth}{!}{\rotatebox{0}{\includegraphics{#1}}}}
\newcommand{\incr}[1]{\resizebox{\textwidth}{!}{\rotatebox{-90}{\includegraphics{#1}}}}
\newcommand{\incs}[2]{\resizebox{#2}{!}{\rotatebox{0}{\includegraphics{#1}}}}

\definecolor{DarkGreen}{rgb}{0,0.7,0}
\definecolor{gray}{gray}{.8}
\newcommand{\textcol}  {\color{black}}
\newcommand{\eqncol}   {\color{Mulberry}}
\newcommand{\imp}[1]   {\textcolor{red}{#1}}
\newcommand{\name}[1]  {\textcolor{Maroon}{#1}}
\newcommand{\qt}[1]    {[\textcolor{red}{#1}]}
\newcommand{\bl}[1]    {{\textcolor{blue}{#1}}}
\newcommand\maths[1]{{\eqncol $#1$}}

% begin and end equations
\newcommand{\be}{
\eqncol
\begin{displaymath}
}

\newcommand{\ee}{
\end{displaymath}
\textcol
}

% begin and end equation arrays
\newcommand{\bea}{
\eqncol
\begin{eqnarray*}
}
\newcommand{\eea}{
\end{eqnarray*}
\textcol
}

%bch is good

\newcommand\titlepage[3]
{
\vspace*{\stretch{3}}
\begin{center}
\fontsize{15mm}{16mm}\usefont{T1}{ppl}{m}{n}
{\color{blue}#1}
\end{center}
\vspace*{\stretch{2}}
\begin{center}
\fontsize{10mm}{14mm}\usefont{T1}{ppl}{m}{n}
{\color{black}#2}
\end{center}
\vspace*{\stretch{1}}
\begin{center}
\fontsize{8mm}{8mm}\usefont{T1}{ppl}{m}{n}[{\color{red}#3}]
\end{center}
\vspace*{\stretch{7}}
}

% page numbering
\pagenumbering{arabic}
\onecolumn

