# Nome do Projeto:
Simulador de Implantação de Aplicação

# Descrição:
É um sistema de software projetado para observar, medir e registrar continuamente o estado e o desempenho de uma infraestrutura de TI, aplicações, redes ou qualquer outro sistema tecnológico.
Seu objetivo principal é transformar dados brutos de operação em informações úteis que permitam identificar problemas, prever falhas e garantir que tudo funcione como esperado.
De uma forma mais simples pense nela como o "sistema nervoso" de uma operação de tecnologia. Ela sente o que está acontecendo em todas as partes do corpo (servidores, bancos de dados, aplicações) e envia sinais (alertas) quando algo está errado ou fora do padrão, permitindo uma reação rápida antes que um problema pequeno se torne uma falha crítica.

# Como Instalar: 
Este script não precisa de uma "instalação" complexa, pois ele usa apenas bibliotecas que já vêm com o Python. Você só precisa ter o Python instalado no seu computador.
Guia de instalação
Pré-requisito: Certifique-se de que você tem o Python instalado. Se não tiver, baixe-o do site oficial python.org.
Salve o Código: Copie todo o código que você enviou e salve-o em um arquivo no seu computador. Dê um nome a ele, por exemplo, simulador_deploy.py.
Crie a Pasta de Logs: O script tentará salvar os logs na pasta criada no seu Disco Local(C:), exemplo: C:\Logs\monitoramento_alertas. Para evitar qualquer erro de permissão, você pode criar essa estrutura de pastas manualmente no seu Disco Local (C:).

Execute o Script via Terminal:
Abra o terminal do seu sistema (Prompt de Comando ou PowerShell no Windows).
Use o comando cd para navegar até a pasta onde você salvou o arquivo. Por exemplo, se você salvou na sua Área de Trabalho, o comando seria:
Bash
cd C:\Users\SeuUsuario\Desktop
Agora, execute o script com o seguinte comando:
Bash
python simulador_deploy.py
Após executar o comando, a janela do "Simulador de Implantação de Aplicação" estará pronto para ser usado.


# Funcionalidades:
A funcionalidade principal é visualizar e registrar um processo de implantação simulado.
Interface Gráfica: Fornece uma janela com campos para inserir informações sobre a aplicação a ser "implantada", como: Nome da Aplicação, URL do Repositório (de onde o código viria, como o GitHub), nome do Serviço (o processo que roda a aplicação no servidor).
simulação do Processo: Ao clicar em "Iniciar Implantação", o programa não congela. Ele inicia uma tarefa em segundo plano (threading) que exibe, passo a passo, uma sequência de implantação comum. Parando o serviço atual, puxando a nova versão do código, instalando dependências, rodando migrações de banco de dados e reiniciando o serviço com a nova versão.
Geração de Logs: Esta é uma das partes mais importantes. A ferramenta faz duas coisas com os logs.
Exibe na Tela: Mostra cada passo em tempo real na área de "Logs da Implantação" dentro da própria janela.
Salva em Arquivo: Cria um arquivo de log (.log) com data e hora no nome, e o salva na pasta C:\Logs\monitoramento_alertas. Isso é excelente para auditoria e para entender o que aconteceu em cada implantação simulada.

# Tecnologias Usadas:
Linguagem Python
