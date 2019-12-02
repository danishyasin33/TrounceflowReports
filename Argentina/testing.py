import numpy as np
import pandas
from pylatex import Document, PageStyle, Section, MultiColumn, MultiRow, Subsection, Center, Subsubsection, Tabularx, Tabular, Math, TikZ, Axis, Plot, Figure, Matrix, Alignat, Command, NewPage, NewLine, section,HugeText, LargeText, SmallText, PageStyle
from pylatex.utils import italic, NoEscape, bold
import os
import csv 

import requests 
import json
import impFunc

number = 1000000

doc = Document(documentclass='report', document_options=['11pt'])



doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))
doc.preamble.append(NoEscape(r'\usepackage{pdflscape}'))
doc.preamble.append(NoEscape(r'\usepackage[margin=1in]{geometry}'))
doc.preamble.append(NoEscape(r'\usepackage{hyperref}'))
doc.preamble.append(NoEscape(r'\hypersetup{colorlinks=true, linkcolor=blue, filecolor=magenta, urlcolor=cyan}'))
doc.preamble.append(NoEscape(r'\urlstyle{same}'))

#doc.preamble.append(NoEscape(r'\setlength{\parindent}{4em}'))
#doc.preamble.append(NoEscape(r'\setlength{\parskip}{1em}'))
doc.preamble.append(NoEscape(r'\linespread{1.6}'))

with doc.create(Center()) as centered: 

    doc.append(NoEscape(r'\scalebox{0.8}{'))
    with centered.create(Tabular('c|c|c|c|c|c',row_height=1.5)) as table:
        #first row
        table.add_row((LargeText(bold('Issuer Entity')), LargeText(bold('Name')), LargeText(bold('Currency')),LargeText(bold('Coupon')),LargeText(bold('Maturity')),LargeText(bold('Adjustment'))))
        table.add_hline()
        table.add_row((MultiRow(2,data='BCRA'),MultiRow(2,data='Nobacs'),MultiRow(2,data='ARS'),'Fixed','2 to 4 years','CER'))
        table.add_hline(4,6)
        table.add_row(('','','','Variable','2 to 4 years','-'))
        table.add_hline()
        #second row (13 rows)
        table.add_row((MultiRow(13,data='National Government'),'LECAPS','ARS','Fixed','1 to 12 years',number))
        table.add_hline(2,6)
        table.add_row(('','BONCER','ARS','Fixed','4 to 5 years','10000000'))
        table.add_hline(2,6)
        table.add_row(('','BOGAR','ARS','Fixed','10 to 16 years','CER'))
        table.add_hline(2,6)
        table.add_row(('','BOTAPO','ARS','Variable','2 to 4 years','Monetary Policy Rate'))
        table.add_hline(2,6)
        table.add_row(('',MultiRow(2,data='BODEN'),'ARS','Fixed','5 to 10 years','CER*'))
        table.add_hline(3,6)
        table.add_row(('','','USD','Variable','5 to 10 years','-'))
        table.add_hline(2,6)
        table.add_row(('',MultiRow(2,data='BOCON'),'ARS','Fixed','5 to 20 years','CER*'))
        table.add_hline(3,6)
        table.add_row(('','','ARS','Variable','10 to 16 years','-'))
        table.add_hline(2,6)
        table.add_row(('',MultiRow(2,data='BONAR'),'USD','Fixed','2 to 4 years','-'))
        table.add_hline(3,6)
        table.add_row(('','','ARS','Variable','1 to 12 months','BADLAR**'))
        table.add_hline(2,6)
        table.add_row(('','LETES','ARS','At Discount','2 to 12 months','-'))
        table.add_hline(2,6)
        table.add_row(('','LECER','ARS','-','-','-'))
        table.add_hline(2,6)
        table.add_row(('','LELINKS','USD','-','-','-'))
        table.add_hline()
        table.add_row((MultiRow(2,data='Provinces'),'-','ARS','Fixed','16 years','CER*'))
        table.add_hline(2,6)
        table.add_row(('','-','ARS','Variable','16 years','-'))
        table.add_hline()
    doc.append(NoEscape(r'}'))
doc.append('Overview of Debt Securities in Argentina Market\n')
doc.append('*CER: refers to benchmark inﬂation stabilization coeﬃcient\n**BADLAR: is an average rate regarding the nominal annual interest rate in peso-denominated time deposits of more than 1.0 million ARS from 30 to 35 days\n')

doc.generate_pdf('TestingMultirow', clean=True)