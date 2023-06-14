""" debug error mensage sorter  """
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Defina o caminho completo do arquivo de entrada e saída
CAMINHO_ENTRADA = os.path.join(os.getcwd(), 'data', 'Erros.txt')
CAMINHO_SAIDA = os.path.join(os.getcwd(), 'data', 'output.txt')

# Ler as linhas do arquivo de entrada
with open(CAMINHO_ENTRADA, 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()

# Dicionário para armazenar os tipos de erros e os documentos correspondentes
tipos_erros = {}

# Expressão regular para identificar o tipo de erro em cada linha
PADRAO_ERRO = r'(\d+)\ -\ (.+)$'

# Iterar sobre as linhas e separar os documentos pelos tipos de erros
for i in range(0, len(linhas), 2):
    documento = linhas[i].strip()
    tipo_erro = linhas[i + 1].strip()
    if tipo_erro in tipos_erros:
        tipos_erros[tipo_erro].append(documento)
    else:
        tipos_erros[tipo_erro] = [documento]

# Escrever os documentos separados por tipo de erro no arquivo de saída
with open(CAMINHO_SAIDA, 'w', encoding='utf-8') as arquivo_saida:
    for tipo_erro, documentos in tipos_erros.items():
        arquivo_saida.write(f"Tipo de Erro {tipo_erro}:\n")
        arquivo_saida.write(f'"{tipo_erro}"\n')
        arquivo_saida.write("Arquivos:\n")
        if len(documentos) > 0:
            for i, documento in enumerate(documentos, start=1):
                arquivo_saida.write(f"- {i} - {documento}\n")
        else:
            arquivo_saida.write("Nenhum arquivo encontrado.\n")
        arquivo_saida.write("\n")
        arquivo_saida.write(
            "===================================================================================\n")
        arquivo_saida.write("\n")

    # Adicionar o total de arquivos com erro no final do arquivo de saída
    total_arquivos = sum(len(documentos)
                        for documentos in tipos_erros.values())
    arquivo_saida.write(f"Total de arquivos com erro: {total_arquivos}\n")
    arquivo_saida.write("\n")
    arquivo_saida.write(
        "===================================================================================\n")
    arquivo_saida.write("\n")
