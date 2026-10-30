# Log Analyzer Tool

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

## 📝 Descrição
Script em Python para triagem rápida de ficheiros de log do sistema. Faz o parsing das linhas, contabiliza falhas/avisos e destaca os erros que exigem intervenção imediata da equipa de suporte N2.

## 🚀 Como Executar

```bash
python log_analyzer.py

📸 Exemplo de Execução Real
Plaintext
==================================================
 RELATÓRIO DE ANÁLISE DE LOGS - 2026-10-30 08:00:00
==================================================
Total de Erros (ERROR):   3
Total de Avisos (WARNING): 1
--------------------------------------------------
Ocorrências Críticas Encontradas:
 [!] 2026-10-30 08:02:15 ERROR Database connection failed on 192.168.1.50.
 [!] 2026-10-30 08:10:00 ERROR Failed password for invalid user root from 192.168.1.104 port 22.
 [!] 2026-10-30 08:12:44 ERROR Database connection failed on 192.168.1.50.
==================================================