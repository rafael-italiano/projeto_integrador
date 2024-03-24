# Projeto integrador

## Configurando o ambiente

Para configurar o ambiente de desenvolvimento rode os seguintes comandos:

```bash
poetry shell
poetry install
``` 

## Comandos úteis
Todos os comandos aqui seguem o padrão task [comando]
```bash
task lint
task format
task run
task pre_test
task test
task post_test
```
Os comandos definidos fazem o seguinte:
- lint: executa o ruff para ver se não temos nenhum problema com o código, após isso faz a checagem da formatação com o blue em relação a PEP-8. Caso nenhum dos dois apontem problemas, será feita uma checagem na ordenação dos imports com isort
- format: formata o código usando blue e isort
- run: executa o servidor de desenvolvimento do FastAPI
- pre_test: executa a camada de lint antes de executar os testes
- test: executa os testes com pytest de forma verbosa (-vv) e adiciona nosso código como base de cobertura
- post_test: gera um report de cobertura após os testes

#continua...