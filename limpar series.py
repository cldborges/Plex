#!/usr/bin/env python
# coding: utf-8

import os
import re

pastas_base = []
pastas_a_corrigir = []
#i = 1
#drives = [r'C:\Users\z0026jjc\OneDrive - abc\Séries'] #Siemens
#drives = [r'C:\Users\Claudio\OneDrive - abc\Séries', r'C:\Users\Claudio\OneDrive - abc (1)\Filmes\Series'] #Notebook pessoal
drives = [r'C:\Onedrives\OneDrive - abc\Séries', r'D:\OneDrives\OneDrive - abc\Séries'] #PC Casa
for drive in drives:
    pastas = os.listdir(drive)
    for pasta in pastas:
    # pesquisa no nome da pasta se tem ponto ou a palavra depois do |
        x = re.search('^.*((\.)|(Temporada)).*$', pasta)
        excessoes = re.search('sync.ffs_db', pasta)
        if x == None:
            pastas_base.append(pasta)
        elif excessoes != None:
            pass
        else:
            pastas_a_corrigir.append(pasta)
    for pasta_a_corrigir in pastas_a_corrigir:
        for pasta_base in pastas_base:
            if pasta_base in pasta_a_corrigir or pasta_base in pasta_a_corrigir.replace('.', ' '):
                caminho_completo = os.path.join(drive, pasta_a_corrigir)
                caminho_completo_novo = os.path.join(drive, pasta_base)
                for arquivo in os.listdir(caminho_completo):
                    if os.path.getsize(os.path.join(caminho_completo, arquivo)) > 200000 * 1024 or 'srt' in (arquivo):
                        print(os.path.join(caminho_completo, arquivo), ' para ', os.path.join(caminho_completo_novo, arquivo))
                        os.replace(os.path.join(caminho_completo, arquivo), os.path.join(caminho_completo_novo, arquivo))
                    else:
                        os.chmod(os.path.join(caminho_completo, arquivo), 0o777)
                        os.remove(os.path.join(caminho_completo, arquivo))
                os.rmdir(caminho_completo)
                #os.chmod(caminho_completo, 0o777)
                #os.remove(caminho_completo)
    pastas_a_corrigir.clear()
