#!/usr/bin/env python
# coding: utf-8

# In[137]:


import os
import re

tipos = ['Filmes', 'Infantis']
for tipo in tipos:
    raiz = 'D:\\OneDrives\\OneDrive - xKx - Onedrive SharePoint have been block\\Filmes\\' + tipo
    pastas = os.listdir(raiz)
    #pastas_corrigir = []
    for pasta in pastas:
        #print (pasta)
        x = re.search('\s\(\d{4}\)$|sync.ffs_db', pasta)
        if not x:
            #pastas_corrigir.append(pasta)
            caminho_completo = os.path.join(raiz, pasta)
            #print(caminho_completo)
            for arquivo in os.listdir(caminho_completo):
                caminho_arquivo = os.path.join(caminho_completo, arquivo)
                if os.path.getsize(caminho_arquivo) < 200000 * 1024 and 'srt' not in (arquivo):
                    print(arquivo)
                    os.chmod(caminho_arquivo, 0o777)
                    #print(caminho_arquivo, os.path.getsize(caminho_arquivo))
                    try:
                        os.remove(caminho_arquivo)
                    except:
                        pass
            nome_pasta = pasta
            palavras_retirar = ['[]', 'WWW.BLUDV.COM', 'LAPUMiA.Org', 'WEB-DL', '720p', 'BluRay', '1080p', 'DUAL', '5.1', 'www.ThePirateFilmes.com', 'x264', 'VERSÃO ESTENDIDA', '[ACESSE COMANDOTORRENTS.COM]', 'WWW.LAPUMiAFiLMES.COM', 'WWW.WOLVERDONFILMES.COM', 'WEBRip', 'Dual Audio', 'BDRip', '()']
            for palavra in palavras_retirar:
                nome_pasta = nome_pasta.replace(palavra, '')
                nome_pasta = nome_pasta.replace('  ', ' ')
                nome_pasta = nome_pasta.strip()
            os.rename(caminho_completo, os.path.join(raiz,nome_pasta))

