
pacientes = []

def cadastrar_paciente():
    nome = input("Nome do paciente: ")
    try:
        idade = int(input("Idade: "))
    except ValueError:
        print("Idade inválida! Tente novamente.")
        return
    telefone = input("Telefone: ")
    pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
    print("Paciente cadastrado com sucesso!")

def ver_estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    total = len(pacientes)
    media_idade = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p["nome"])
    mais_velho = max(pacientes, key=lambda p: p["nome"])
    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media_idade:.1f}")
    print(f"Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")

def buscar_paciente():
    nome_busca = input("Digite o nome: ").lower()
    encontrados = [p for p in pacientes if nome_busca in p["nome"].lower()]
    if encontrados:
        for p in encontrados:
            print(f"- - - - - - - - -")
            print(f"Nome do paciente: {p['nome']}")
            print(f"Idade: {p['idade']} anos")
            print(f"Telefone: {p['telefone']}")
    else:
        print("Paciente não encontrado.")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return
    for p in pacientes:
            print(f"- - - - - - - - -")
            print(f"Nome do paciente: {p['nome']}")
            print(f"Idade: {p['idade']} anos")
            print(f"Telefone: {p['telefone']}")

while True:
    print("\n=== SISTEMA CLÍNICA VIDA+ ===")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_paciente()
    elif opcao == "2":
        ver_estatisticas()
    elif opcao == "3":
        buscar_paciente()
    elif opcao == "4":
        listar_pacientes()
    elif opcao == "5":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
