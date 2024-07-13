# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

#venv
    #bin
    #lib
    #include


#Instalando
# pip install virtualenv

#Criando
# python3 -m venv <nome_projeto>

#Ativando e desativando
# . venv/bin/activate
# source venv/bin/activate

#REQUIREMENTS
# pip freeze - verificar as libs instalados no ambiente
# pip freeze >> requirements.txt
# pip install -r <requirements-file.txt>