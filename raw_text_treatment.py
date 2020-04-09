###############################################################################
# Date ! 07/04/2020
# Auteur : SYC
# Comment : Tratier text avec brut
###############################################################################

import os
import sys
sys.path.insert(1, 'C:\\Users\\sclerc\\github\\PYTHON_SMALL_PROJECT\\MODULES_SYC\\') #add specific root to current path
from syc_modules import read, write

INPUT_ROOT = "C:\\Users\\sclerc\\github\\INPUT_FILES\\"
OUTPUT_ROOT = "C:\\Users\\sclerc\\github\\OUTPUT_FILES\\"
FILE = "mails.txt"

#list_file_in_dir = os.listdir(ROOT))

texte=read(INPUT_ROOT+FILE)
tmp = texte.split(";")
tmp = [i.replace(">","") for i in tmp]
tmp_2 = [i.split("<") for i in tmp]

for i in tmp_2:
    txt = i[0] + ";" + i[1] + "\n"
    write(txt,OUTPUT_ROOT+'output.txt','a')
