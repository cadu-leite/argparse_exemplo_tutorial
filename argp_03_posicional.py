# exemplo
# arquivo: argp_03_posicional.py
import argparse
parser = argparse.ArgumentParser()

# adiciona um parâmetro chamado `param_01_pos` com msg de help
# o parâmetro help é opcional !
parser.add_argument("param_01_pos", help='msg de help do parametro "param_01_pos"')
args = parser.parse_args()

# print para vermos a saida  ...  ==> mensagem <valor>
# estou usando `f string` saiba mais aqui https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals
print(f'==> O arg posicinal `param_01_pos` recebeu o valor = {args.param_01_pos} \n')