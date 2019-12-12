import numpy as np
import pandas
from pylatex import Document, Foot, PageStyle, Section, MultiColumn, MultiRow, Subsection, Center, Subsubsection, Tabularx, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Command, NewPage, NewLine, section,HugeText, LargeText, SmallText, PageStyle
from pylatex.utils import italic, NoEscape, bold
import os
import csv 

import datetime
import requests 
import json
import impFunc

#getting authentication code
authCode = impFunc.getAuthCode('DanishYasin','Alpha103')



#_______________________________________________
mar18Date = '12/03/2018'
sep18Date = '30/09/2018'
janDate = '31/01/2019'
marDate = '31/03/2019'
mayDate = '31/05/2019'
junDate = '30/06/2019'
julDate = '31/07/2019'
augDate = '31/08/2019'
augDate2 = '30/08/2019'
sepDate = '30/09/2019'
sepDate2 = '01/09/2019'
octDate = '01/10/2019'
octDate2 = '31/10/2019'
novDate = '30/11/2019'

#___________________SUMMARY_____________________
#central government




#_______________________________________________
doc = Document(documentclass='report', document_options=['11pt, notitlepage'])

#doc.preamble.append(NoEscape(r'\usepackage{appendix}'))
doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{pdflscape}'))
doc.preamble.append(NoEscape(r'\usepackage[margin=1in]{geometry}'))
doc.preamble.append(NoEscape(r'\usepackage{hyperref}'))
doc.preamble.append(NoEscape(r'\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan}'))
doc.preamble.append(NoEscape(r'\urlstyle{same}'))

doc.preamble.append(NoEscape(r'\linespread{1.6}'))

#Generating Title
doc.preamble.append(Command('title','Trounceflow Countries: Dominican Republic'))
doc.preamble.append(Command('author', 'Michael Trounce'))
doc.preamble.append(Command('date', NoEscape(r'\today')))
doc.append(NoEscape(r'\maketitle'))

doc.append(NoEscape(r'\begin{abstract}'))
doc.append("The `Trounceflow Countries' series of `living' documents provide real-time dynamic summaries of macroeconomic data relevant to the flows-and-positions analysis of emerging market debt. These macroeconomic data concentrate on the structure of the government bond market but also include other useful but hard-to-wrangle data such as the structure of the local institutional investor base. The data is obtained from the Trounceflow App (trounceflow.com) and the document data is automatically updated in line with the automatic updates on the App; links to the underlying national sources are also given in the `living' documents.")
doc.append(LargeText("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThe values presented in this report are the face values of the bonds"))
doc.append(NoEscape(r'\end{abstract}'))
doc.append(NewPage())

#Table of Contents
doc.append(NoEscape(r'\tableofcontents'))
doc.append(NewPage())

#Summary Chapter 1
doc.append(NoEscape(r'\chapter{Executive Summary}'))
doc.append(NewPage())







doc.generate_pdf('Dominican Republic', clean=True)
