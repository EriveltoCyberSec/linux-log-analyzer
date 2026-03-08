# Analisador de Logs do Linux (Python)

Este projeto é uma ferramenta simples baseada em Python, desenvolvida para analisar logs de autenticação do Linux e identificar tentativas de login falhas que podem indicar ataques de força bruta ou atividades suspeitas.

## O que este projeto faz
- Analisa entradas de logs de autenticação do Linux (ex.: logins SSH com falha)
- Extrai endereços IP de origem das tentativas de login falhadas
- Conta falhas repetidas por endereço IP
- Gera um relatório simples de segurança

## Por que isso é importante para cibersegurança
Analisar logs de autenticação é uma tarefa comum em ambientes de SOC e equipes Blue Team. Múltiplas tentativas de login falhadas vindas do mesmo endereço IP podem indicar ataques de força bruta ou tentativas de acesso não autorizado.

## Como executar
Certifique-se de que o Python 3 está instalado e execute:

```bash
python log_analyzer.py
