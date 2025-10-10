import yaml
import os
import pandas as pd
import psycopg2
from psycopg2 import sql

# Configura la connessione al database PostgreSQL
DB_CONFIG = {
    "host": "137.204.72.88",  # Cambia con il tuo host
    "port": 5432,
    "database": "abds_irrigation",  # Cambia con il tuo database
    "user": "postgres",  # Cambia con il tuo user
    "password": "p0st615*",  # Cambia con la tua password
}

import os
import csv
import yaml
import psycopg2
import pandas as pd

# Carica il file YAML
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)


# Funzione per eseguire la query
def execute_query(query, start, end, field_name, plant_row):
    # Connessione al database (assicurati di sostituire i dettagli corretti)
    conn = psycopg2.connect(
        dbname=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        host=DB_CONFIG["host"],
        port=DB_CONFIG["port"],
    )
    # Prepara la query sostituendo i segnaposti con i valori specifici
    query = query.format(
        start=start,
        end=end,
        field_name=f"'{field_name}'",  # Aggiungi virgolette per il valore di field_name
        plant_row=f"'{plant_row}'",  # Aggiungi virgolette per il valore di plant_row
    )

    # Esegui la query e prendi il risultato
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# Cicla su ogni anno nel dizionario config
for year, data in config["years"].items():
    # Crea la cartella per l'anno se non esiste
    output_dir = f"{year}"
    os.makedirs(output_dir, exist_ok=True)

    # Cicla su ogni query definita
    for query_name, query_info in config["queries"].items():
        # Esegui la query
        df = execute_query(
            query_info["query"],
            data["start"],
            data["end"],
            data["field_name"],
            data["plant_row"],
        )

        # Salva il risultato in un file CSV
        output_file = os.path.join(output_dir, f"{query_name}.csv")
        df.to_csv(output_file, index=False)

        print(f"Query '{query_name}' per l'anno {year} salvata in {output_file}")
