import math
import pandas as pd
import numpy as np
import time
from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.anoNasc = anoNasc
        self.mesNasc = mesNasc
        self.diaNasc = diaNasc
        self.sexo = sexo


class Aluno(Pessoa):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str, curso: str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)
        self.curso= curso

    
    def CadastrarAluno(self):
        arquivo_csv = "lista_alunos.csv"
        try:
            df = pd.read_csv(arquivo_csv)
        except FileNotFoundError:
            df = pd.DataFrame()
        prox_id = df["ID"].max() + 1 if "ID" in df.columns else 1
        data_nascimento = f"{self.diaNasc}/{self.mesNasc}/{self.anoNasc}"
        novo_aluno = pd.DataFrame({
            "ID": [prox_id],
            "Nome": [self.nome],
            "RG": [str(self.rg)],
            "CPF": [str(self.cpf)],
            "Data de nascimento": [data_nascimento],
            "Sexo": [self.sexo],
            "Curso": [self.curso]
        })
        df = pd.concat([df, novo_aluno], ignore_index=True)
        df.to_csv(arquivo_csv, index=False)

        

    def ExibirAluno(self):
        a = 0


def print_com_atraso(atraso_segundos):
    time.sleep(atraso_segundos)

while True:
    print("Iniciando sistema da Universidade Celestial de Canudos")
    print_com_atraso(2)

    resposta = input("A) Matricular nova pessoa:\nB) Ver dados de funcionario ou aluno:\nResposta: ").upper()

    while resposta not in ["A", "B"]:
        print("Opção inválida. Digite 'A' para Matricular nova pessoa ou 'B' para Ver dados de funcionario ou aluno.")
        resposta = input("Resposta: ").upper()

    if resposta == "A":
        print("Universidade Celestial de Canudos\n      MATRICULA")
        print_com_atraso(1)
        matricular = input("O que deseja matricular:\nA) Matricular Aluno\nB) Matricular Funcionario\nResposta: ").upper()

        while matricular not in ["A", "B"]:
            print("Opção inválida. Digite 'A' para Matricular Aluno ou 'B' para Matricular Funcionário.")
            matricular = input("Resposta: ").upper()

        if matricular == "A":
            print("Iniciando matricula do aluno")
            print_com_atraso(0.5)
            nome = input("qual o nome do aluno: ")
            rg = int(input("qual o RG do aluno: "))
            cpf = int(input("qual o CPF do aluno: "))
            ano = int(input("qual ano aluno nasceu: "))
            mes = int(input("qual mes aluno nasceu: "))
            dia = int(input("qual dia aluno nasceu: "))
            sexo = input("qual o sexo do Aluno: ")
            curso = input("qual o curso do Aluno: ")

            aluno_obj = Aluno(nome, rg, cpf, ano, mes, dia, sexo, curso)
            aluno_obj.CadastrarAluno()

        elif matricular == "B":
            print("Aqui esta a lista com todos os Cargos:")
            # lista com Cargos dos funcionarios
            print("Enumere o cargo que deseja cadastrar:")

    elif resposta == "B":
        visuDados = input("Voce deseja ver dados dos:\nA) Alunos\nB) Funcionarios\nResposta: ").upper()

        while visuDados not in ["A", "B"]:
            print("Opção inválida. Digite 'A' para ver dados dos Alunos ou 'B' para ver dados dos Funcionários.")
            visuDados = input("Resposta: ").upper()

        if visuDados == "A":
            print("Aqui esta a lista com todos os Alunos:")
            # lista com nomes de todos alunos
            print("Enumere o aluno que deseja ver:")
        elif visuDados == "B":
            print("Aqui esta a lista com todos os Cargos:")
            # lista com Cargos dos funcionarios
            print("Enumere o cargo que deseja ver:")
            # lista com nomes de todos funcionarios do cargo escolhido

    finalizar = input("Digite 'C' para fechar o programa ou 'D' para recomeçar: ").upper()
    while finalizar not in ["C", "D"]:
        print("Opção inválida. Digite 'C' para fechar o programa ou 'D' para recomeçar.")
        finalizar = input("Resposta: ").upper()

    if finalizar == "C":
        break  