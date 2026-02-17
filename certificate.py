#!/usr/bin/env python
# coding: utf-8

import numpy as np

from pylatex import Document, Command, MiniPage
from pylatex.utils import NoEscape
from pylatex import Document, Section, Command, Package, HFill, LargeText, Center

import os

import pandas as pd
from multiprocessing import Pool
from pathlib import Path
import shutil
import zipfile


def certificate_no_exam_mlv(name, surname):

    """
    Input(str): name and surname
    Output(pdf): certificato della scuola con nome e cognome [certificato_nome_cognome_no_exam.pdf]
    """

    # Use Beamer as document class
    doc = Document(documentclass="article", inputenc='utf8', geometry_options={'a4paper', 'landscape'})
    # doc = Document(geometry_options={'a4paper', 'landscape'})
    # doc.packages.append(Command('usepackage', 'geometry'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('xcolor'))
    doc.packages.append(Package('fontspec'))
    doc.packages.append(Package('fontsetup'))

    doc.preamble.append(NoEscape(r"\graphicspath{{" + 'Figures' + r"/}}"))
    doc.preamble.append(NoEscape(r"\pagestyle{empty}"))

    doc.preamble.append(NoEscape(r"\setmainfont{Fira Sans}"))

    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='MaLGa_orizzontale_esteso.pdf'))
    doc.append(HFill())
    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='QR_Code'))
    # doc.append(NoEscape(r'\vspace{0.5cm}'))
    doc.append(Command('\\'))

    with doc.create(Center()):
        doc.append(NoEscape(r'\textcolor{red}{\fontsize{22pt}{24pt}\selectfont \textbf{A Journey through Deep Learning 2025}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont \textbf{A PhD school organised within the Ph.D. Program in Computer Science and Systems Engineering Università degli Studi di Genova.}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{18pt}{18pt}\selectfont This is to certify that'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(rf'\fontsize{{20pt}}{{20pt}}\selectfont\textbf{{{name} {surname}}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont has participated in the PhD school \textbf{A Journey through Deep Learning}, held at MaLGa Center, Genoa from the 16th to the 20th of June 2025, for a total of \textbf{40 hours}.'))
        doc.append(Command('\\'))

    doc.append(NoEscape(r'\vspace{1cm}'))
    doc.append(NoEscape(r'\textcolor{red}{\fontsize{14pt}{15pt}\selectfont\textbf{Prof.ssa Francesca Odone}}'))
    doc.append(HFill())
    doc.append(NoEscape(r'\textcolor{red}{\fontsize{14pt}{15pt}\selectfont\textbf{Prof.ssa Nicoletta Noceti}}'))
    doc.append(Command('\\'))

    doc.append(Command('includegraphics', options = 'scale=0.25', arguments='Odone.png'))
    doc.append(HFill())
    doc.append(Command('includegraphics', options = 'scale=0.15', arguments='Noceti.png'))


    # Generate the PDF
    doc.generate_pdf(f"certificate_{name}_{surname}_no_exam", clean_tex = True, compiler='xelatex')

def certificate_yes_exam_mlv(name, surname):

    """
    Input(str): name and surname
    Output(pdf): certificato della scuola con nome e cognome [certificato_nome_cognome_no_exam.pdf]
    """

    # Use Beamer as document class
    doc = Document(documentclass="article", inputenc='utf8', geometry_options={'a4paper', 'landscape'})
    # doc = Document(geometry_options={'a4paper', 'landscape'})
    # doc.packages.append(Command('usepackage', 'geometry'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('xcolor'))
    doc.packages.append(Package('fontspec'))
    doc.packages.append(Package('fontsetup'))

    doc.preamble.append(NoEscape(r"\graphicspath{{" + 'Figures' + r"/}}"))
    doc.preamble.append(NoEscape(r"\pagestyle{empty}"))

    doc.preamble.append(NoEscape(r"\setmainfont{Fira Sans}"))

    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='MaLGa_orizzontale_esteso.pdf'))
    doc.append(HFill())
    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='QR_Code'))
    # doc.append(NoEscape(r'\vspace{0.5cm}'))
    doc.append(Command('\\'))

    with doc.create(Center()):
        doc.append(NoEscape(r'\textcolor{red}{\fontsize{22pt}{24pt}\selectfont \textbf{A Journey through Deep Learning 2025}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont \textbf{A PhD school organised within the Ph.D. Program in Computer Science and Systems Engineering Università degli Studi di Genova.}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{18pt}{18pt}\selectfont This is to certify that'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(rf'\fontsize{{20pt}}{{20pt}}\selectfont\textbf{{{name} {surname}}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont has participated in the PhD school \textbf{A Journey through Deep Learning}, held at MaLGa Center, Genoa from the 16th to the 20th of June 2025, for a total of \textbf{40 hours}, and passed the final examination.'))
        doc.append(Command('\\'))

    doc.append(NoEscape(r'\vspace{1cm}'))
    doc.append(NoEscape(r'\textcolor{red}{\fontsize{14pt}{15pt}\selectfont\textbf{Prof.ssa Francesca Odone}}'))
    doc.append(HFill())
    doc.append(NoEscape(r'\textcolor{red}{\fontsize{14pt}{15pt}\selectfont\textbf{Prof.ssa Nicoletta Noceti}}'))
    doc.append(Command('\\'))

    doc.append(Command('includegraphics', options = 'scale=0.25', arguments='Odone.png'))
    doc.append(HFill())
    doc.append(Command('includegraphics', options = 'scale=0.15', arguments='Noceti.png'))


    # Generate the PDF
    doc.generate_pdf(f"certificate_{name}_{surname}_yes_exam", clean_tex = True, compiler='xelatex')

def call_certificate_yes_exam_mlv(args):
    name, surname = args
    certificate_yes_exam_mlv(name, surname)

def call_certificate_no_exam_mlv(args):
    name, surname = args
    certificate_no_exam_mlv(name, surname)

def certificate_no_exam_loz(name, surname):

    """
    Input(str): name and surname
    Output(pdf): certificato della scuola con nome e cognome [certificato_nome_cognome_no_exam.pdf]
    """

    # Use Beamer as document class
    doc = Document(documentclass="article", inputenc='utf8', geometry_options={'a4paper', 'landscape'})
    # doc = Document(geometry_options={'a4paper', 'landscape'})
    # doc.packages.append(Command('usepackage', 'geometry'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('xcolor'))
    doc.packages.append(Package('fontspec'))
    doc.packages.append(Package('fontsetup'))

    doc.preamble.append(NoEscape(r"\graphicspath{{" + 'Figures' + r"/}}"))
    doc.preamble.append(NoEscape(r"\pagestyle{empty}"))

    doc.preamble.append(NoEscape(r"\setmainfont{Fira Sans}"))

    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='MaLGa_orizzontale_esteso.pdf'))
    doc.append(HFill())
    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='QR_Code'))
    # doc.append(NoEscape(r'\vspace{0.5cm}'))
    doc.append(Command('\\'))

    with doc.create(Center()):
        doc.append(NoEscape(r'\textcolor{red}{\fontsize{22pt}{24pt}\selectfont \textbf{Theoretical Foundations of Machine Learning (TFML) 2025}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont \textbf{A PhD school organised within the Ph.D. Program in Computer Science and Systems Engineering Università degli Studi di Genova.}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{18pt}{18pt}\selectfont This is to certify that'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(rf'\fontsize{{20pt}}{{20pt}}\selectfont\textbf{{{name} {surname}}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont has attended and actively took part in \textbf{TFML 2025}, held at MaLGa Center, University of Genoa from the 23rd to the 27rd of June 2025, for a total of \textbf{20 hours}.'))
        doc.append(Command('\\'))

    doc.append(NoEscape(r'\vspace{1cm}'))
    doc.append(NoEscape(r'\textcolor{red}{\fontsize{14pt}{15pt}\selectfont\textbf{Prof. Lorenzo Rosasco}}'))
    doc.append(Command('\\'))

    doc.append(Command('includegraphics', options = 'scale=0.8', arguments='rosasco.png'))


    # Generate the PDF
    doc.generate_pdf(f"certificate_{name}_{surname}_no_exam", clean_tex = True, compiler='xelatex')

def certificate_yes_exam_loz(name, surname):

    """
    Input(str): name and surname
    Output(pdf): certificato della scuola con nome e cognome [certificato_nome_cognome_no_exam.pdf]
    """

    # Use Beamer as document class
    doc = Document(documentclass="article", inputenc='utf8', geometry_options={'a4paper', 'landscape'})
    # doc = Document(geometry_options={'a4paper', 'landscape'})
    # doc.packages.append(Command('usepackage', 'geometry'))
    doc.packages.append(Package('graphicx'))
    doc.packages.append(Package('xcolor'))
    doc.packages.append(Package('fontspec'))
    doc.packages.append(Package('fontsetup'))

    doc.preamble.append(NoEscape(r"\graphicspath{{" + 'Figures' + r"/}}"))
    doc.preamble.append(NoEscape(r"\pagestyle{empty}"))

    doc.preamble.append(NoEscape(r"\setmainfont{Fira Sans}"))

    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='MaLGa_orizzontale_esteso.pdf'))
    doc.append(HFill())
    doc.append(Command('includegraphics', options = 'scale=0.7', arguments='QR_Code'))
    # doc.append(NoEscape(r'\vspace{0.5cm}'))
    doc.append(Command('\\'))

    with doc.create(Center()):
        doc.append(NoEscape(r'\textcolor{red}{\fontsize{22pt}{24pt}\selectfont \textbf{Theoretical Foundations of Machine Learning (TFML) 2025}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont \textbf{A PhD school organised within the Ph.D. Program in Computer Science and Systems Engineering Università degli Studi di Genova.}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{0.5cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{18pt}{18pt}\selectfont This is to certify that'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(rf'\fontsize{{20pt}}{{20pt}}\selectfont\textbf{{{name} {surname}}}'))
        doc.append(Command('\\'))

        doc.append(NoEscape(r'\vspace{1cm}'))
        # doc.append(Command('centering'))
        doc.append(NoEscape(r'\fontsize{12pt}{15pt}\selectfont  has attended and actively took part in \textbf{TFML 2025}, held at MaLGa Center, Genoa from the 23rd to the 27th of June 2025, for a total of \textbf{20 hours}, and passed the final examination.'))
        doc.append(Command('\\'))

    doc.append(NoEscape(r'\vspace{1cm}'))
    doc.append(NoEscape(r'\vspace{1cm}'))
    doc.append(NoEscape(r'\textcolor{red}{\fontsize{14pt}{15pt}\selectfont\textbf{Prof. Lorenzo Rosasco}}'))
    doc.append(Command('\\'))

    doc.append(Command('includegraphics', options = 'scale=0.8', arguments='rosasco.png'))


    # Generate the PDF
    doc.generate_pdf(f"certificate_{name}_{surname}_yes_exam", clean_tex = True, compiler='xelatex')

def call_certificate_yes_exam_loz(args):
    name, surname = args
    certificate_yes_exam_loz(name, surname)

def call_certificate_no_exam_loz(args):
    name, surname = args
    certificate_no_exam_loz(name, surname)


def call_file_mover(args):
    filename, source_folder, destination_folder = args
    src_path = source_folder / filename
    dst_path = destination_folder / filename
    shutil.move(src_path, dst_path)

def zip_folder(folder_path, zip_path):
    folder_path = Path(folder_path)
    zip_path = Path(zip_path)
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in folder_path.rglob('*'):  # Recursively go through all files
            if file.is_file():
                # Write file to zip, keeping relative path inside the archive
                zipf.write(file, arcname=file.relative_to(folder_path))

def dir_remover(dir_path):
    # Remove the directory and all its contents
    if dir_path.exists() and dir_path.is_dir():
        shutil.rmtree(dir_path)



file = pd.read_excel(next(filter(lambda x: x.endswith(".xlsx"), os.listdir("./"))))

destination_folder_yes = Path("./Certificates_yes_exam")
destination_folder_no = Path("./Certificates_no_exam")

destination_folder_no.mkdir(parents = True, exist_ok = True)
destination_folder_yes.mkdir(parents = True, exist_ok = True)

source_folder = Path("./")

name_surname_list = file[['First name', 'Last name']].values.tolist()

schools = ["mlv", "loz"]
school = int(input("scegliere la scuola 0 - MLV, 1 - Rosasco "))

if schools[school] == "mlv":

    with Pool() as pool:
        pool.map(call_certificate_no_exam_mlv, name_surname_list)
        pool.map(call_certificate_yes_exam_mlv, name_surname_list)

elif schools[school] == "loz":

    with Pool() as pool:
        pool.map(call_certificate_no_exam_loz, name_surname_list)
        pool.map(call_certificate_yes_exam_loz, name_surname_list)

filename_no = list(filter(lambda x: x.endswith("no_exam.pdf"), os.listdir(source_folder)))
filename_yes = list(filter(lambda x: x.endswith("yes_exam.pdf"), os.listdir(source_folder)))

move_args_no = [(f, source_folder, destination_folder_no) for f in filename_no]
move_args_yes = [(f, source_folder, destination_folder_yes) for f in filename_yes]

with Pool() as pool:
    pool.map(call_file_mover, move_args_no)
    pool.map(call_file_mover, move_args_yes)


zip_folder('Certificates_yes_exam', 'Certificates_yes_exam.zip')
zip_folder('Certificates_no_exam', 'Certificates_no_exam.zip')

dir_remover(destination_folder_yes)
dir_remover(destination_folder_no)

