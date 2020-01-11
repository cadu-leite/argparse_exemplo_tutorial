***************************
ArgParse tutorial  exemplos
***************************

A interface mais simples que você pode ter com o usuário e um script Python - a linha de comando.

O `$ ` indica que o que vem a seguir foi digitado na linha de comando do shell.

.. code-block:: bash

    $ <comando>


Argparse - Help Grátis
======================

Com o `argparse` você ganha uma mensagem de "help" sem praticamente configurar nada.

Somente criado o parser  é possível usar o parâmetro `--help` ou na forma abreviada `-h`.

.. code-block:: python

    # exemplo
    # file: argp_01.py
    import argparse
    parser = argparse.ArgumentParser()
    parser.parse_args()

chamada do script no shell

.. code-block:: bash

    $ python argp_01.py --help

saída ...

::

    usage: argp_01.py [-h]

    optional arguments:
        -h, --help  show this help message and exit


Desligar o help padrão
----------------------

para desligar o help padrão use o parâmetro `add_help=False`.

.. code-block:: python

    # exemplo
    # arquivo: argp_02_nohelp.py
    import argparse
    parser = argparse.ArgumentParser(add_help=False)
    parser.parse_args()

chamada do script no shell

.. code-block:: bash

    $ python argp_02_nohelp.py -h

saída

::

    usage: argp_02_nohelp.py

    argp_02_nohelp.py: error: unrecognized arguments: -h


Parâmetros posicionais
======================


Código com parâmetro posicional (obrigatório)
---------------------------------------------

.. code-block:: python

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


.. note::
    Para o `print` ficar mais legível concatenei um sinal "==> mensagem" e
    utilizei  `F strings` do Python 3.
    saiba mais em  https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals

Voltando ao nosso exemplo de ArgParse...

ao adicionarmos um argumento posicional, o `argparse` adiciona este ao help, e faz as validações indicando se o parâmetro obrigatório foi ou não passado.


Chamada com `-h` após parâmetro posicional
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ python argp_03_posicional.py -h

**saída**

::

    usage: argp_03_posicional.py [-h] param_01_pos

    positional arguments:
      param_01_pos  msg de help do parametro "param_01_pos"

    optional arguments:
      -h, --help    show this help message and exit


Adicionando o parâmetro posicional no script passa a ser obrigatório informar o tal parâmetro.

O ArgParse trata a entrada e se não informada, ele mostra uma mensagem de erro informando o usuário que um parâmetro é requerido.


Chamada do script sem o parâmetro obrigatório
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ python argp_03_posicional.py

e quando o script é chamado sem parâmetro nenhum, nem mesmo o `--help`, ai sim, temos uma indicação de erro.

**saída** com **erro** por falta do parâmetro obrigatório

::

    usage: argp_03_posicional.py [-h] param_01_pos
    argp_03_posicional.py: error: the following arguments are required: param_01_pos

... e claro, se passarmos o argumento corretamente ao executar o script, o `argparse` coloca o valor recebido "dentro" do atributo `param_01_pos` para que o script possa utilizá-lo.


chamada passando o parâmetro obrigatório
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ python argp_03_posicional.py ArgumentoPosicional

**saída** da chamada com parâmetro ...

::

    ==> O arg posicinal `param_01_pos` recebeu o valor = ArgumentoPosicional


Parâmetros Opcionais
====================


Parâmetros opcionais são adicionados da mesma maneira que parâmetro posicionais, ou seja, utilizando o `add_argument` do `parser`.

**Uma** das várias maneiras, a mais simples, é adicionar dois traços "--" como prefixo do nome.

.. code-block:: python

    # isso é um parâmetro posicional (obrigatório)
    parser.add_argument(
        "param_01_pos", help='este param é obrigatório'
    )

    # isso é um parâmetro opcional. QUASE a mesma coisa só que com `action
    parser.add_argument(
        "--param_01_opt", help='este param é opcional', action="store_true"
    )



Código com parâmetro opcional (não obrigatório e não posicional)
----------------------------------------------------------------


.. code-block:: python

    import argparse
    parser = argparse.ArgumentParser()

    # isso é um parâmetro opcional. porque adicionamos '--' ao nome do parâmetro.
    parser.add_argument(
        "--param_01_opt", help='este param é opcional',
    )

    args = parser.parse_args()

    print(f'==> O arg posicinal `param_01_opt` recebeu o valor = {args.param_01_opt} \n')








