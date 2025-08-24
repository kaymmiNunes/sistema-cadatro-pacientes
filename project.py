# ===============================
# Sistema de Gestão - Clínica Vida+
# ===============================

pacientes = []

def cadastrar_paciente():
    nome = input("\nNome do paciente: ")
    try:
        idade = int(input("\nIdade: "))
    except ValueError:
        print("\n⚠ Idade inválida! Tente novamente.")
        return
    telefone = input("\nTelefone: ")

    pacientes.append({
        "nome": nome,
        "idade": idade,
        "telefone": telefone
    })

    print("\n✅ Paciente cadastrado com sucesso!")

def ver_estatisticas():
    if not pacientes:
        print("\n⚠ Nenhum paciente cadastrado.")
        return

    total = len(pacientes)
    media_idade = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print("\n", ("-" * 20))
    print(f"📊 Total de pacientes: {total}")
    print(f"📊 Idade média: {media_idade:.1f}")
    print(f"🧒 Mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"👴 Mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)")
    print("-" * 20)


def buscar_paciente():
    nome_busca = input("\nDigite o nome: ").lower()
    encontrados = [p for p in pacientes if nome_busca in p["nome"].lower()]

    if encontrados:
        for p in encontrados:

            print(("\n"),"-" * 20)
            print(f"Nome: {p['nome']}")
            print(f"Idade: {p['idade']} anos")
            print(f"Telefone: {p['telefone']}")
            print("-" * 20)
    else:
        print("\n⚠ Paciente não encontrado.")

def listar_pacientes():
    if not pacientes:
        print("\n⚠ Nenhum paciente cadastrado.")
        return

    for p in pacientes:
        print("\n")
        print("-" * 20)
        print(f"Nome: {p['nome']}")
        print(f"Idade: {p['idade']} anos")
        print(f"Telefone: {p['telefone']}")
        print("-" * 20)

def menu():
    while True:
        print("\n=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("\nEncerrando...")
            break
        else:
            print("\n⚠ Opção inválida!")


if __name__ == "__main__":
    menu()
