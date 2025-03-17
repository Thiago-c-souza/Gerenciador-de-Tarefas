import json

def menu():
    print("\n📌 Gerenciador de Tarefas")
    print("1 - Adicionar Tarefa")
    print("2 - Listar Tarefas")
    print("3 - Marcar Tarefa como Concluída")
    print("4 - Editar Tarefas")
    print("5 - Excluir Tarefa")
    print("6 - Sair")

def salvar_tarefas(tarefas, arquivo="tarefas.json"):
    with open(arquivo, "w") as f:
        json.dump(tarefas, f, indent=4)

def carregar_tarefas(arquivo="tarefas.json"):
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def adicionar_tarefa(tarefas):
    descricao = input("✏ Digite a descrição da tarefa: ")
    nova_tarefa = {"id": len(tarefas) + 1, "descricao": descricao, "concluido": False}
    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)
    print("✅ Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("📭 Nenhuma tarefa encontrada!")
        return
    for tarefa in tarefas:
        status = "✔ Concluída" if tarefa["concluido"] else "❌ Pendente"
        print(f'{tarefa["id"]} - {tarefa["descricao"]} [{status}]')

def marcar_como_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("✅ Digite o ID da tarefa concluída: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluido"] = True
                salvar_tarefas(tarefas)
                print("✔ Tarefa marcada como concluída!")
                return
        print("⚠ Tarefa não encontrada.")
    except ValueError:
        print("⚠ Digite um número válido.")

def editar_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("✅ Digite o ID da tarefa: "))
        for tarefa in tarefas:
            if tarefa["id"] == id_tarefa:
                nova_desc = input("✏ Digite a descrição da tarefa: ").strip()
                if not nova_desc:
                    print("⚠ A descrição não pode estar vazia.")
                    return
                tarefa["descricao"] = nova_desc
                salvar_tarefas(tarefas)
                print("✔ Tarefa atualizada!")
                return
        print('⚠ Tarefa não encontrada.')
    except ValueError:
        print("⚠ Digite um número válido.")

def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        id_tarefa = int(input("🗑️ Digite o ID da tarefa para excluir: "))
        nova_lista = [tarefa for tarefa in tarefas if tarefa["id"] != id_tarefa]
        if len(nova_lista) == len(tarefas):
            print("⚠ Tarefa não encontrada.")
        else:
            tarefas.clear()
            tarefas.extend(nova_lista)
            salvar_tarefas(tarefas)
            print("🗑️ Tarefa excluída com sucesso!")
    except ValueError:
        print("⚠ Digite um número válido.")



tarefas_lista = carregar_tarefas()

while True:
    menu()
    opcao = input("💡 Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa(tarefas_lista)
    elif opcao == "2":
        listar_tarefas(tarefas_lista)
    elif opcao == "3":
        marcar_como_concluida(tarefas_lista)
    elif opcao == "4":
        editar_tarefa(tarefas_lista)
    elif opcao == "5":
        excluir_tarefa(tarefas_lista)
    elif opcao == "6":
        salvar_tarefas(tarefas_lista)
        print("👋 Saindo... Suas tarefas foram salvas!")
        break
    else:
        print("⚠ Opção inválida, tente novamente.")
