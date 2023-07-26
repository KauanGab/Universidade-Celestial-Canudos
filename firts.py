import math
import pandas as pd
import numpy as np
import time
from abc import ABC, abstractmethod
import random

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
        self.listalun = None

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

class Funcionario(Pessoa):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
            nivel: str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo)        
        self.nivel = nivel

class Professor(Funcionario):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
             nivel: str, disciplina:str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, nivel)
        self.disciplina = disciplina
        self.salarioProfessor = 0
        self.nivel = nivel
        self.matricula = 0

    def CadastrarProfessor(self):
        if self.nivel == "I":
            self.salarioProfessor = 6500
        elif self.nivel == "II":
            self.salarioProfessor = 8325.5
        elif self.nivel == "III":
            self.salarioProfessor = 12568.43

        creatmat = [random.randint(1, 9) for _ in range(5)]
        self.matricula=''.join(map(str,creatmat))

        arquivo_csv = "lista_professores.csv"
        try:
            df = pd.read_csv(arquivo_csv)
        except FileNotFoundError:
            df = pd.DataFrame()
        prox_id = df["ID"].max() + 1 if "ID" in df.columns else 1
        data_nascimento = f"{self.diaNasc}/{self.mesNasc}/{self.anoNasc}"

        novo_professor = pd.DataFrame({
            "ID": [prox_id],
            "Nome": [self.nome],
            "RG": [str(self.rg)],
            "CPF": [str(self.cpf)],
            "Data de nascimento": [data_nascimento],
            "Sexo": [self.sexo],
            "Matricula": [str(self.matricula)],
            "Nivel":[self.nivel],
            "disciplina": [self.disciplina],
            "salario":[str(self.salarioProfessor)]
        })
        df = pd.concat([df, novo_professor], ignore_index=True)
        df.to_csv(arquivo_csv, index=False)

class Coordenador(Professor):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
             nivel: str, disciplina:str, area:str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, nivel,
                         disciplina)
        self.area = area
        self.salarioCordenador = 0

    def CadastrarCoordenador(self):
        if self.nivel == "I":
            salarioProfessor = 6500
            self.salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor
        elif self.nivel == "II":
            salarioProfessor = 8325.5
            self.salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor
        elif self.nivel == "III":
            salarioProfessor = 12568.43
            self.salarioCordenador = (0.15 * salarioProfessor) + salarioProfessor

        creatmat = [random.randint(1, 9) for _ in range(5)]

        self.matricula=''.join(map(str,creatmat))

        arquivo_csv = "lista_coordnadores_professores.csv"
        try:
            df = pd.read_csv(arquivo_csv)
        except FileNotFoundError:
            df = pd.DataFrame()
        prox_id = df["ID"].max() + 1 if "ID" in df.columns else 1
        data_nascimento = f"{self.diaNasc}/{self.mesNasc}/{self.anoNasc}"

        novo_coordena = pd.DataFrame({
            "ID": [prox_id],
            "Nome": [self.nome],
            "RG": [str(self.rg)],
            "CPF": [str(self.cpf)],
            "Data de nascimento": [data_nascimento],
            "Sexo": [self.sexo],
            "Matricula": [str(self.matricula)],
            "Nivel":[self.nivel],
            "disciplina": [self.disciplina],
            "salario":[str(self.salarioCordenador)],
            "Area":[self.area]
        })
        df = pd.concat([df, novo_coordena], ignore_index=True)
        df.to_csv(arquivo_csv, index=False)

class CoordenadorAdm(Funcionario):
    def __init__(self, nome: str, rg: str, cpf: str, anoNasc: int, mesNasc: int, diaNasc: int, sexo: str,
            nivel: str, area:str):
        super().__init__(nome, rg, cpf, anoNasc, mesNasc, diaNasc, sexo, nivel)
        self.area = area

    def cadastrarCoordenadorAdm(self):
        if self.nivel == "A":
            salarioTecnico = 1520.25
        elif self.nivel == "B":
            salarioTecnico = 2362.67
        elif self.nivel == "C":
            salarioTecnico = 2988.92
        elif self.nivel == "D":
            salarioTecnico = 3572.77
        elif self.nivel == "E":
            salarioTecnico = 4878.67
        creatmat = [random.randint(1, 9) for _ in range(5)]

        self.matricula=''.join(map(str,creatmat))

        arquivo_csv = "lista_coordenadores_administrativo.csv"
        try:
            df = pd.read_csv(arquivo_csv)
        except FileNotFoundError:
            df = pd.DataFrame()
        prox_id = df["ID"].max() + 1 if "ID" in df.columns else 1
        data_nascimento = f"{self.diaNasc}/{self.mesNasc}/{self.anoNasc}"

        novo_adm = pd.DataFrame({
            "ID": [prox_id],
            "Nome": [self.nome],
            "RG": [str(self.rg)],
            "CPF": [str(self.cpf)],
            "Data de nascimento": [data_nascimento],
            "Sexo": [self.sexo],
            "Matricula": [str(self.matricula)],
            "Nivel":[self.nivel],
            "salario":[str(salarioTecnico)],
            "Area":[self.area]
        })
        df = pd.concat([df, novo_adm], ignore_index=True)
        df.to_csv(arquivo_csv, index=False)
       
def print_com_atraso(atraso_segundos):
    time.sleep(atraso_segundos)

def viewDados(categoria: str, diretorio: str):
    print(f"Aqui está a lista com todos os {categoria}: ")
    df = pd.read_csv(diretorio)
    if df.empty:
        print("A lista está vazia.")
    else:
        print(df[['ID', 'Nome']].to_string(index=False))

        disjuntor = False

        while not disjuntor:
            try:
                test = int(input(f"Informe o número do ID do {categoria} que deseja visualizar: "))

                if test < 1 or test > len(df):
                    print("ID inválido. Por favor, informe um número de ID válido.\n")
                else:
                    print(f"\n\n  Dados do {categoria}")
                    test = test - 1
                    print(df.iloc[test])
                    disjuntor = True
            except ValueError:
                print("Entrada inválida. Por favor, informe um número inteiro válido.\n")

def remDados(categoria: str, diretorio: str):
            print(f"Aqui está a lista com todos os {categoria}: ")
            df = pd.read_csv(diretorio)
            print(df[['ID', 'Nome']].to_string(index=False))

            disjuntor = False

            while not disjuntor:
                test = int(input(f"Informe o número do ID do {categoria} que deseja remover do sistema: "))

                for i in df['ID']:
                    if i == test:
                        confirma = input(f"\n \nTem certeza que deseja apagar os dados de {df.loc[df['ID'] == test, 'Nome'].values[0]}\nSe quiser apagar use S, se nao use N: ").upper()
                        if confirma == "S":
                            df = df[df['ID'] != test]
                            df['ID'] = range(1, len(df) + 1)
                            print(f"\n{categoria} removido com sucesso.\n")
                            print(df[['ID', 'Nome']].to_string(index=False))
                            df.to_csv(diretorio, index=False)
                        elif confirma == "N":
                            print("Operação cancelada.")
                        disjuntor = True

                if not disjuntor:
                    print("ID não encontrado. Por favor, informe um número de ID válido.\n")

while True:
    print("Iniciando sistema da Universidade Celestial de Canudos")
    print_com_atraso(2)

    resposta = input("A) Matricular nova pessoa:\nB) Ver dados de funcionario ou aluno:\nC) Apagar dados:\nResposta: ").upper()

    while resposta not in ["A", "B", "C"]:
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
            nome = input("Qual o nome do aluno: ")
            rg = int(input("Qual o RG do aluno: "))
            cpf = int(input("Qual o CPF do aluno: "))
            ano = int(input("Qual ano aluno nasceu: "))
            mes = int(input("Qual mes aluno nasceu: "))
            dia = int(input("Qual dia aluno nasceu: "))
            sexo = input("Qual o sexo do Aluno: ").upper()
            curso = input("Qual o curso do Aluno: ")

            aluno_obj = Aluno(nome, rg, cpf, ano, mes, dia, sexo, curso)
            aluno_obj.CadastrarAluno()

        elif matricular == "B":
            print("Aqui esta a lista com todos os Cargos:")
            print("1)Professor \n2)Coordenador Professor\n3)Coordenador Administrador")
            cargo = input("Enumere o cargo que deseja cadastrar:")
            while cargo not in ["1", "2","3"]:
                print("Opção inválida. Digite '1' para Matricular um novo professor, '2' para Matricular um novo Coordenador Professor ou '3' para Matricular um novo Coordenador Administrador.")
                cargo = input("Resposta: ").upper()
            if cargo == "1":
                print("Iniciando Cadastro do professor")
                print_com_atraso(0.5)
                nome = input("Qual o nome do professor: ")
                rg = int(input("Qual o RG do professor: "))
                cpf = int(input("Qual o CPF do professor: "))
                ano = int(input("Qual ano professor nasceu: "))
                mes = int(input("Qual mes professor nasceu: "))
                dia = int(input("Qual dia professor nasceu: "))
                sexo = input("Qual o sexo do professor: ").upper()
                nivel = input("Qual o nivel do professor(Use I, II ou III): ").upper()
                while nivel not in ["I", "II","III"]:
                    print("Opção inválida. Use I, II ou III para classificar o nivel do professor.")
                    nivel = input("Resposta: ").upper()
                disciplina = input("Qual disciplina o professor vai ensinar: ")

                professor_obj = Professor(nome, rg, cpf, ano, mes, dia, sexo, nivel, disciplina)
                professor_obj.CadastrarProfessor()

            elif cargo == "2":
                print("Iniciando Cadastro do Coordenador Professor")
                print_com_atraso(0.5)
                nome = input("Qual o nome do Coordenador Professor: ")
                rg = int(input("Qual o RG do Coordenador Professor: "))
                cpf = int(input("Qual o CPF do Coordenador Professor: "))
                ano = int(input("Qual ano Coordenador Professor nasceu: "))
                mes = int(input("Qual mes Coordenador Professor nasceu: "))
                dia = int(input("Qual dia Coordenador Professor nasceu: "))
                sexo = input("Qual o sexo do Coordenador Professor: ").upper()
                nivel = input("Qual o nivel do Coordenador Professor(Use I,II,III): ").upper()
                while nivel not in ["I", "II","III"]:
                    print("Opção inválida. Use I, II ou III para classificar o nivel do Coordenador Professor.")
                    nivel = input("Resposta: ").upper()
                disciplina = input("Qual disciplina o Coordenador Professor vai ensinar: ")
                area = input("Qual area o Coordenador Professor atuar: ")
                

                coorf_prof_obj = Coordenador(nome, rg, cpf, ano, mes, dia, sexo, nivel, disciplina, area)
                coorf_prof_obj.CadastrarCoordenador()

            elif cargo == "3":
                print("Iniciando Cadastro do Coordenador Administrativo")
                print_com_atraso(0.5)
                nome = input("Qual o nome do Coordenador Administrativo: ")
                rg = int(input("Qual o RG do Coordenador Administrativo: "))
                cpf = int(input("Qual o CPF do Coordenador Administrativo: "))
                ano = int(input("Qual ano Coordenador Administrativo nasceu: "))
                mes = int(input("Qual mes Coordenador Administrativo nasceu: "))
                dia = int(input("Qual dia Coordenador Administrativo nasceu: "))
                sexo = input("Qual o sexo do Coordenador Administrativo: ").upper()
                nivel = input("Qual o nivel do Coordenador Administrativo(Use A,B,C,D,E): ").upper()
                while nivel not in ["A", "B","C","D","E"]:
                    print("Opção inválida. Use A, B, C, D ou E para classificar o nivel do Coordenador Administrativo.")
                    nivel = input("Resposta: ").upper()
                area = input("Qual area o Coordenador Administrativo atuar: ")
                

                coor_adm_obj = CoordenadorAdm(nome, rg, cpf, ano, mes, dia, sexo, nivel, area)
                coor_adm_obj.cadastrarCoordenadorAdm()
            

    elif resposta == "B":
        visuDados = input("Voce deseja ver dados dos:\nA) Alunos\nB) Funcionarios\nResposta: ").upper()

        while visuDados not in ["A", "B"]:
            print("Opção inválida. Digite 'A' para ver dados dos Alunos ou 'B' para ver dados dos Funcionários.")
            visuDados = input("Resposta: ").upper()

        if visuDados == "A":
            viewDados("Alunos", "lista_alunos.csv")                   
                    
        elif visuDados == "B":
            print("Aqui esta a lista com todos os Cargos:")
            print("1)Professor \n2)Coordenador Professor\n3)Coordenador Administrador")
            cargo = input("Enumere o cargo do funcionario que deseja inspecionar:")
            while cargo not in ["1", "2","3"]:
                print("Opção inválida. Digite '1' para Professor, '2' para Coordenador Professor ou '3' para Coordenador Administrador.")
                cargo = input("Resposta: ").upper()

            if cargo == "1":
                viewDados("Professores", "lista_professores.csv") 

            elif cargo == "2":
                viewDados("Coordenador Professor", "lista_coordnadores_professores.csv")     

            elif cargo == "3":
                viewDados("Coordenador Administrativo", "lista_coordenadores_administrativo.csv")                   

    elif resposta == "C":
        delDados = input("Voce deseja apagar os dados de:\nA) Aluno\nB) Funcionario\nResposta: ").upper()

        while delDados not in ["A", "B"]:
            print("Opção inválida. Digite 'A' para apagar dados dos Alunos ou 'B' para apagar dados dos Funcionários.")
            delDados = input("Resposta: ").upper()

        if delDados == "A":
            remDados("Alunos", "lista_alunos.csv")

        elif delDados == "B":
                print("Aqui está a lista com todos os Funcionários: ")
                print("1) Professor \n2) Coordenador Professor \n3) Coordenador Administrativo")
                cargo = input("Enumere o cargo do funcionário que deseja remover: ")

                while cargo not in ["1", "2", "3"]:
                    print("Opção inválida. Digite '1' para remover um Professor, '2' para remover um Coordenador Professor ou '3' para remover um Coordenador Administrativo.")
                    cargo = input("Resposta: ").upper()

                if cargo == "1":
                    remDados("Professores", "lista_professores.csv")

                elif cargo == "2":
                    remDados("Coordenadores Professor", "lista_coordnadores_professores.csv")


                elif cargo == "3":
                    print("Aqui está a lista com todos os Coordenadores Administrativos: ")
                    df = pd.read_csv('lista_coordenadores_administrativo.csv')
                    remDados("Coordenadores Administrativos", "lista_coordenadores_administrativo.csv")



    finalizar = input("Digite 'C' para fechar o programa ou 'D' para recomeçar: ").upper()
    while finalizar not in ["C", "D"]:
        print("Opção inválida. Digite 'C' para fechar o programa ou 'D' para recomeçar.")
        finalizar = input("Resposta: ").upper()

    if finalizar == "C":
        print("Programa fechando em")
        print("3")
        print_com_atraso(0.5)
        print("2")
        print_com_atraso(0.5)
        print("1")
        print_com_atraso(0.5)
        break