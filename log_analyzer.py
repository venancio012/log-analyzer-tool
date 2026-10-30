import os
from datetime import datetime

# Exemplo de log sintético simulando eventos de sistema
LOG_DATA = """2026-10-30 08:00:01 INFO User admin logged in successfully.
2026-10-30 08:02:15 ERROR Database connection failed on 192.168.1.50.
2026-10-30 08:05:22 WARNING Disk usage exceeded 85%.
2026-10-30 08:10:00 ERROR Failed password for invalid user root from 192.168.1.104 port 22.
2026-10-30 08:12:44 ERROR Database connection failed on 192.168.1.50.
2026-10-30 08:15:30 INFO Scheduled backup completed.
"""

def generate_sample_log(filename="app.log"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(LOG_DATA)

def analyze_logs(filename="app.log"):
    if not os.path.exists(filename):
        generate_sample_log(filename)

    errors = []
    warnings = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if "ERROR" in line:
                errors.append(line.strip())
            elif "WARNING" in line:
                warnings.append(line.strip())

    print("=" * 50)
    print(f" RELATÓRIO DE ANÁLISE DE LOGS - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    print(f"Total de Erros (ERROR):   {len(errors)}")
    print(f"Total de Avisos (WARNING): {len(warnings)}")
    print("-" * 50)
    print("Ocorrências Críticas Encontradas:")
    for err in errors:
        print(f" [!] {err}")
    print("=" * 50)

if __name__ == "__main__":
    analyze_logs()