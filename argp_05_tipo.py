import argparse


def par(n):
    '''verifica se numero par
    [en] check number is ODD
    '''
    n = int(n)
    return not(bool(n % 2))


parser = argparse.ArgumentParser()

# isso é um parâmetro opcional. porque adicionamos '--' ao nome do parâmetro.
parser.add_argument(
    "param01", type=int, help='para para verificar o tipo',
)

args = parser.parse_args()

print(f'==> O arg posicinal `param01` é do tipo = {type(args.param01)} \n')