def read(file):
    fichier = open(file,"r")
    read_file = fichier.read()
    fichier.close()
    return read_file

def write(txt,output,mode):
    fichier = open(output,mode)
    fichier.write(txt)
    fichier.close()
