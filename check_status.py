import json
import random
from datetime import datetime

# Dados de exemplo para simular a leitura de um log/configuração
status_data = {
    "timestamp": datetime.now().isoformat(),
    "system_name": "Antenna_Subsystem_Status",
    "nominal_temp_c": 25,
    "current_temp_c": random.randint(22, 28)
}

# Verifica se a temperatura está fora da faixa (simula uma falha)
if status_data["current_temp_c"] > 27:
    status_data["alert"] = "WARNING: High Temperature Detected!"
    status_data["status_code"] = 500
else:
    status_data["status_code"] = 200
    status_data["alert"] = "Status OK"

# Imprime o resultado formatado em JSON (padrão de comunicação moderno)
print(json.dumps(status_data, indent=4))