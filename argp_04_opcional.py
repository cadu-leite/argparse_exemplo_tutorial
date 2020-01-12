import argparse
parser = argparse.ArgumentParser()

# isso é um parâmetro opcional. porque adicionamos '--' ao nome do parâmetro.
parser.add_argument(
    '-p', '--param_01_opt', help='este param é opcional',
)

args = parser.parse_args()

print(f'==> O arg posicinal `param_01_opt` recebeu o valor = {args.param_01_opt} \n')