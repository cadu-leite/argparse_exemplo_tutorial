
.. meta::
    :title: ARGPARSE Tutorial
    :author: Carlos Leite /
    :description: exemplos sobre o módulo python argparse
    :description lang=en: samples about python argparse module
    :keywords: python, argparse, sample, tutorial

.. sectnum::
    :depth: 3


***************************
ArgParse tutorial  exemplos
***************************

A interface mais simples que você pode ter com o usuário e um script Python - a linha de comando.

Sobre este doc, há várias chamadas do script pelo shell do OS representadas como abaixo.

    O `$ ` indica que o que vem a seguir foi digitado na linha de comando do shell.

    .. code-block:: bash

        $> <comando>


Argparse - Help Grátis
======================

Com o `argparse` você ganha uma mensagem de "help" sem praticamente configurar nada.

Somente criado o parser  é possível usar o parâmetro `--help` ou na forma abreviada `-h`.

.. code-block:: python

    # exemplo file: argp_01.py
    import argparse
    parser = argparse.ArgumentParser()
    parser.parse_args()
|

    execução do script no shell

    .. code-block:: bash

        $> python argp_01.py --help

    saída ...

    ::

        usage: argp_01.py [-h]

        optional arguments:
            -h, --help  show this help message and exit


Para desligar o help padrão use o parâmetro `add_help=False`.

.. code-block:: python

    # exemplo
    # arquivo: argp_02_nohelp.py
    import argparse
    parser = argparse.ArgumentParser(add_help=False)
    parser.parse_args()
|

    execução do script no shell

    .. code-block:: bash

        $> python argp_02_nohelp.py -h

    **saída**

    ::

        usage: argp_02_nohelp.py

        argp_02_nohelp.py: erro: unrecognized arguments: -h


Parâmetros Posicionais
======================

Parâmetros posicionais são obrigatórios por padrão.

Para definirmos uma parâmetro, usamos o método `add_argument`_


.. code-block:: python

    # exemplo
    # arquivo: argp_03_posicional.py
    import argparse
    parser = argparse.ArgumentParser()

    # adiciona um parâmetro chamado `param_01_pos` com msg de help
    # o parâmetro help é opcional !
    parser.add_argument("param_01_pos", help='msg de help do parametro "param_01_pos"')
    args = parser.parse_args()

    # print para vermos a saida  "==> O arg ... <valor>"
    print(f'==> O arg posicinal `param_01_pos` recebeu o valor = {args.param_01_pos} \n')


.. note::
    Para o `print` ficar mais legível concatenei um sinal "==> mensagem" e
    utilizei  `F strings` do Python 3.
    saiba mais em  https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals


Novo parâmetro, nova msg de ajuda (help)
----------------------------------------

O help gerado pelo argparse, automaticamente reconhece o novo parâmetro.

Podemos ver o help, incluindo a ajuda citando o parâmetro obrigatório que está definido no script acima.

    Mensagem de ajuda, incluindo o parâmetro obrigatório.
    Chamada do script com parâmetro ``-h``

    .. code-block:: bash

        $> python argp_03_posicional.py -h

    resultado no shell

    ::

        usage: argp_03_posicional.py [-h] param_01_pos

        positional arguments:
          param_01_pos  msg de help do parametro "param_01_pos"

        optional arguments:
          -h, --help    show this help message and exit


Passando o parâmetro pelo "*shell*"
-----------------------------------

    execução do script com o parâmetro posicional (obrigatório).

    .. code-block:: bash

        $> python argp_03_posicional.py ArgumentoPosicional

    saída do script executado com parâmetro ...

    ::

        ==> O arg posicinal `param_01_pos` recebeu o valor = ArgumentoPosicional


Erro - se não for passado o parâmetro posicional
------------------------------------------------

O argParse automaticamente gerencia os parâmetros gerando uma mensagem de erro caso algum parâmetronao esteja correto, ou neste caso, como um parâmetro obrigatório não foi informado o argparse já retorna uma msg de erro formatada para o usuário.

    Execução do script sem o parâmetro obrigatório

    .. code-block:: bash

        $> python argp_03_posicional.py


    **saída** com **erro** por falta do parâmetro obrigatório

    ::

        usage: argp_03_posicional.py [-h] param_01_pos
        argp_03_posicional.py: error: the following arguments are required: param_01_pos


Parâmetros Opcionais
====================


Parâmetros opcionais são adicionados da mesma maneira que parâmetro posicionais, ou seja, utilizando o `add_argument` do `parser`.

O que torna um argumento opcional é adicionar ``--`` a frente do nome do argumento - ex.: ``--param01`` 



.. code-block:: python

    # adicionar é um parâmetro POSICIONAL (obrigatório)
    parser.add_argument("param_01_pos", help='este param é obrigatório')

    # adiciona parâmetro OPCIONAL.
    parser.add_argument("--param_01_opt", help='este param é opcional', action="store_true")


Script com parâmetro OPCIONAL (não obrigatório e não posicional)
----------------------------------------------------------------


.. code-block:: python

    import argparse
    parser = argparse.ArgumentParser()
    # isso é um parâmetro opcional. porque adicionamos '--' ao nome do parâmetro.
    parser.add_argument("--param_01_opt", help='este param é opcional')
    args = parser.parse_args()

    print(f'==> O arg posicinal `param_01_opt` recebeu o valor = {args.param_01_opt} \n')


Chamada do script com parâmetro opcional
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Quando o parâmetro é opcional, temos que passar o nome do parâmetro e o valor (não eomente o valor) para que o argparse possa fazer o recorte ("parser") dos valores.

    Chamada no shell

    .. code-block:: bash

        $python argp_04_opcional.py --param_01_opt EuSouOpcional

    saida

    ::

        ==> O arg posicinal `param_01_opt` recebeu o valor = EuSouOpcional
|

    **Execução** chamada do script que espera SOMENTE um parâmetro opcional,
    mas o parâmetro é passado sem um nome.

    .. code-block:: bash

        $> python argp_04_opcional.py EuSouOParametro

    **saída** com erro, indicando que o argparse não reconheceu o parâmetro informado, porque não há um nome para o parâmetro e também não há um parâmetro posicional.

    ::

        usage: argp_04_opcional.py [-h] [--param_01_opt PARAM_01_OPT]
        argp_04_opcional.py: error: unrecognized arguments: EuSouOParametro
|

    **Execução:** O "help" do comando também é atualizado sobre o parâmetro opcional.

    chamada no shell

    .. code-block:: bash

        $> python argp_04_opcional.py -h

    **saída**

    Ao pedir o "help" do script, repare que argparse mostra  o argumento abaixo dos parâmetros opcionais ("optional arguments:")

    ::

        usage: argp_04_opcional.py [-h] [--param_01_opt PARAM_01_OPT]

        optional arguments:
          -h, --help            show this help message and exit
          --param_01_opt PARAM_01_OPT

podemos executar o script sem nenhum parâmetro ...


Chamada sem o parâmetro opcional
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    **Execução**: nada é passado ao parâmetro posicional.

    .. code-block:: bash

        $> python argp_04_opcional.py

    **saída**

    ::

        ==> O arg posicinal `param_01_opt` recebeu o valor = None

como não passamos nenhum parâmetro, o valor atribuído ao parâmetro dentro do script é `none`.

Mas não houve erro, como acontece em `Chamada do script sem o parâmetro obrigatório`_


Forma "curta"
^^^^^^^^^^^^^

como vários comandos no `bash` ou outros shell do linux,
podemos implementar para o nosso script a forma curta do comando,
usando mais um parâmetro no `add_argument`.

ao invés de chamarmos o script passando o nome completo da variável como abaixo.

.. code-block:: bash

    # forma longa
    $> python argp_04_opcional.py --param_01_opt EuSouOpcional


Se adicionarmos mais um parâmetro ao comando, neste caso o `-p`.

.. code-block:: python

    parser.add_argument(
        '-p', '--param_01_opt', help='este param é opcional',
    )

podemos executar o comando

.. code-block:: bash

    # podemos utilizar a forma curta do comando.
    $> python argp_04_opcional.py -p EuSouOpcionalCURTO

o help do ArgParse também mostra a forma curta

    **execução**

    .. code-block:: bash

        $> python argp_04_opcional.py -h

    **saída**

    ::

        usage: argp_04_opcional.py [-h] [-p PARAM_01_OPT]

        optional arguments:
          -h, --help            show this help message and exit
          -p PARAM_01_OPT, --param_01_opt PARAM_01_OPT
                                este param é opcional


Existem várias outras maneiras de implementar comandos opcionais com o argparse... veja mais em

- https://docs.python.org/3/library/argparse.html#action
- https://docs.python.org/3/library/argparse.html#nargs


Argumento com tipo definido - além do tipo `string`
===================================================

Por padrão, tudo que vc passar em um parâmetro para o argparse será lido dentro do seu script como um tipo `string`.

.. warning:: se o *arg* for opcional e nada for passado este assumirá `none`  !

.. _check arg sem tipo:

Checando argumento sem tipo
---------------------------

.. code-block:: python

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("param01", help='para para verificar o tipo')
    args = parser.parse_args()
    # a saída do script é o tipo do argumento de entrada.
    print(f'==> O arg posicinal `param_01_opt` é do tipo = {type(args.param01)} \n')

|
    execução do script sem o *type* - com tipo indefinido

    .. code-block:: bash

        $python argp_05_tipo.py 3
|
    saída: o tipo de saída é string, mesmo passando um número (supostamente um inteiro)

    ::

        ==> O arg posicinal `param_01_opt` é do tipo = <class 'str'>

Para definir o tipo esperado na entrada usamos o argumento `type`, no método `add_argument`.


Script com Tipo do argumento definido
-------------------------------------

Vamos definir um tipo de entrada como inteiro (`<class int>`)

.. code-block:: python

    import argparse
    parser = argparse.ArgumentParser()
    # repare no argumento `type=int`
    parser.add_argument("param01", type=int, help='para para verificar o tipo')
    args = parser.parse_args()
    print(f'==> O arg posicinal `param_01_opt` é do tipo = {type(args.param01)} \n')
|

Executamos o script passando um argumento capaz de ser transformado em um inteiro

    Chamada do ecript com um argumento capaz de ser entendido como um tipo `int`

    .. code-block:: bash

        $> python argp_05_tipo.py 3


    saida: ao definir o tipo (`type=int`), temos um objeto `int`

    ::

        ==> O arg posicinal `param01` é do tipo = <class 'int'>

Ao verificarmos a saída acima, o tipo recebido pelo script é tratado como  um inteiro, e não uma *string* como nos exemplos anteriores.

E se, passarmos um valor, o qual não pode ser "transformado" em um inteiro ?

    execução: Passando um *string* quando esperado um tipo *int*

    .. code-block:: bash

        $> python argp_05_tipo.py EuNãoSouUmNúmero

    saída: com erro de *parâmetro inválido*

    ::

        usage: argp_05_tipo.py [-h] param01
        argp_05_tipo.py: error: argument param01: invalid int value: 'EuNãoSouUmNúmero'


mais info em `type argument`_


- `type argument doc <https://docs.python.org/3/library/argparse.html#type>`_


.. type_add : https://docs.python.org/3/library/argparse.html#type

--------------------------------------------------


.. _`add_argument`: https://docs.python.org/3/library/argparse.html#the-add-argument-method

--------------------------------


application's ``models.py`` or ``models/__init__.py``.

Returns a date object containing the first day of the week after the date provided.

This function can also return ``None`` or raise an

:class:`~django.http.Http404` exception, depending on the values of

:attr:`~BaseDateListView.allow_empty` and

:attr:`~DateMixin.allow_future`.
