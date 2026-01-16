import json

def carregar(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar(arquivo, lista):
    try:
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        return True

    except FileNotFoundError:
        print('\033[31m [!] ARQUIVO NÃO ENCONTRADO!\033[0m')

    except Exception as e:
        print(f'\033[31m [!] ERRO CRITICO AO SALVAR! {e}\033[0m')

def cadastrar(arquivo, lista):
    print('\033[34m=-\033[0m'*10)
    print('\033[33m   NOVO ITEM')
    print('\033[34m=-\033[0m'*10)


    while True:

        nome = str(input('Digite o nome da despesa: '))

        if not nome:
            print(f'\033[31m [!] DIGITE UM NOME VÁLIDO!\033[0m')
            continue

        elif len(nome) < 2 or len(nome) > 20:
            print(f'\033[31m [!] NOME MUITO CURTO OU MUITO GRANDE\033[0m')
            continue

        else:
            break

    while True:
        try:
            valor = float(input('Digite o valor da despesa R$'))

            if not valor:
                print(f'\033[31m [!] DIGITE UM VALOR VÁLIDO!\033[0m')
                continue

            elif valor <= 0:
                print(f'\033[31m [!] O VALOIR NÃO PODE SER NEGATIVO!\033[0m')
                continue

            else:
                break

        except ValueError:
            print(f'\033[31m [!] DIGITE UM VALOR VÁLIDO!\033[0m')


    while True:

        categoria = str(input('Digite a categoria do despesa: ')).upper()

        if not categoria:
            print(f'\033[31m [!] DIGITE UM NOME VÁLIDO!\033[0m')
            continue

        elif len(categoria) < 2 or len(categoria) > 30:
            print(f'\033[31m [!] NOME MUITO CURTO OU MUITO GRANDE\033[0m')
            continue

        else:
            break

    nova_despesa = {
        'nome': nome,
        'valor': valor,
        'categoria': categoria,
    }

    lista.append(nova_despesa)
    salvar(arquivo, lista)

    print(f'\033[32m DESPESA - {nome} - ADICIONADA COM SUCESSO! \033[0m')

def mostrar(lista):

    if not lista:
        print(f"\n\033[31m[!] NENHUMA DESPESA CADASTRADA!.\033[0m")
        return

    print("\n" + "=-" * 20)
    print("\033[36m          LISTA DE DISPESAS\033[0m")
    print("=-" * 20)

    for d in lista:
        nome = d.get('nome', 'N/A')
        valor = d.get('valor', 'N/A')
        categoria = d.get('categoria', 'N/A')

        print(f"\033[37m• Nome: {nome} | Valor: {valor:.2f} | Categoria: {categoria}\033[0m")

def remover(arquivo, lista):
    nome_remover = input("Digite o nome do item que deseja remover: ").strip()
    encontrado = False

    for d in lista:
        if d.get('nome') == nome_remover:
            encontrado = True
            lista.remove(d)
            break

    if encontrado:
        print(f'\033[32m DESPESA - {nome_remover} - REMOVIDA COM SUCESSO! \033[0m')
    else:
        print(f'\n\033[31m [!] - {nome_remover} - NÃO EXISTE E NÃO PODE SER APAGADA!.\033[0m')

def filtrar(arquivo, lista):
    soma = 0
    qtd_itens = 0

    categoria_filtro = str(input('Digite a categoria que deseja filtrar: ')).strip().upper()

    if not categoria_filtro:
        print(f'\n\033[31m [!] DIGITE UMA CATEGORIA VÁLIDA!\033[0m')
        return

    categorias_existentes = [item.get('categoria', '').upper() for item in lista]

    if categoria_filtro not in categorias_existentes:
        print(f'\n\033[31m [!] - {categoria_filtro} - NÃO EXISTE NO SISTEMA!\033[0m')
        return

    for item in lista:
        if item.get('categoria', '').upper() == categoria_filtro:
            soma += float(item.get('valor', 0))
            qtd_itens += 1

    print("\n" + "=" * 25)
    print(f" RESUMO: {categoria_filtro}")
    print("=" * 25)
    print(f"• Itens encontrados: {qtd_itens}")
    print(f"• Valor Total: R$ {soma:.2f}")
    print("=" * 25 + "\n")












