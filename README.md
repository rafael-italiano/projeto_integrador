# projeto_integrador
DRP03-PJI110-SALA-003GRUPO-013

# Configuração do ambiente de desenvolvimento
## WSL
Para os usuários de Windows, recomendo trabalhar dentro do WSL.

Instalem o VS Code, instalem a extensão do WSL, abram o terminal e, com o PowerShell, usem o seguinte comando:

wsl --install

Isso vai habilitar uma (mais ou menos) máquina virtual do Ubuntu (por padrão, mas podem instalar outras distros se quiserem) no seu Windows.

Depois, usem:

wsl

Isso os vai colocar dentro do WSL2

Abram um terminal Bash e usem o seguinte comando:

cd ~

## Docker

Instalem Docker a partir dessas instruções. Se você estiver usando Windows, usem WSL:
https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/engine/install/linux-postinstall/

O primeiro tutorial é obrigatório, o segundo é muito conveniente e eu recomendo.

Se vocês fizerem isso, rodem o seguinte comando para a aplicação subir:

## Rodando a aplicação

No repositório do projeto, renomeiem o arquivo .env.template para .env

Depois, executem o seguinte comando:

docker compose up -d

Depois de um tempo, a aplicação vai buildar (é só uma vez) e estará rodando!

Abram seu browser e entrem na seguinte url

localhost:8081

Para verem a magia de inserção de eventos, usem o seguinte comando:

curl -X POST http://localhost:8000/events \
-H "Content-Type: application/json" \
-d '{
    "title": "sample",
    "start_timestamp": 500,
    "end_timestamp": 800,
    "all_day": false,
    "url": "https://www.google.com",
    "description": "Event 1 Description",
   "address": "sei la"
}'

Atualizem o browser e voilà.

Para acessar outras possibilidades da api, acessem:
localhost:8000/docs