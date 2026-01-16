from funcoes import ler
from time import sleep

RESET = '\033[0m'
BLACK  = '\033[30m'
RED    = '\033[31m'
GREEN  = '\033[32m'
YELLOW = '\033[33m'
BLUE   = '\033[34m'
PURPLE = '\033[35m'
CYAN   = '\033[36m'
WHITE  = '\033[37m'

arquivo = "dados.json"
dispesas = ler.carregar(arquivo)

print(f'{BLUE}=-{RESET}'*20)
print(f'{YELLOW}         CONTROLE DE GASTOS')
print(f'{BLUE}=-'*20)

while True:
    print(f'{BLUE}-=-=-=-=-= {YELLOW}OPÇÕES{BLUE} =-=-=-=-=')
    print(f'{YELLOW}1 - {BLUE}CADASTRAR')
    print(f'{YELLOW}2 - {BLUE}REMOVER')
    print(f'{YELLOW}3 - {BLUE}VER')
    print(f'{YELLOW}4 - {BLUE}TOTAL POR CATEGORIA')
    print(f'{YELLOW}5 - {BLUE}SAIR {RESET}')

    try:
        escolha = int(input('Sua escolha: '))

        if escolha not in [1,2,3,4,5]:
            print(f'{RED}[!] DIGITE APENAS OS VALORES MENCIONADOS! {RESET}')

        elif escolha == 1:
            ler.cadastrar(arquivo, dispesas)

        elif escolha == 2:
            ler.remover(arquivo, dispesas)

        elif escolha == 3:
            ler.mostrar(dispesas)
            sleep(1.5)

        elif escolha == 4:
            ler.filtrar(arquivo, dispesas)
            sleep(1.5)

        elif escolha == 5:
            print(f'{CYAN}FECHANDO PROGRAMA...')
            sleep(2)
            print('ATÉ LOGO!')
            sleep(2)
            break


    except ValueError:
        print(f'{RED}[!] DIGITE UM VALOR VÁLIDO!{RESET}')




