## Comando SQL Iniziale

```
CREATE DATABASE gestore_interrogazioni;

USE gestore_interrogazioni;

CREATE TABLE interrogazioni (
	id INT AUTO_INCREMENT PRIMARY KEY,
    materia VARCHAR(255) NOT NULL,
	giorno DATE	NOT NULL,
	ora TIME NOT NULL,
    stato VARCHAR(255) DEFAULT 'disponibile',
    studente VARCHAR(255) DEFAULT NULL
)

INSERT INTO interrogazioni (materia, giorno, ora) VALUES 
('Informatica', '2025-03-13', '10:00'), 
('Italiano', '2025-04-10', '11:00'), 
('Matematica','2025-03-20','10:30'),
('TPSIT','2025-03-15','12:10'),
('GPOI','2025-05-01','9:50');
```

## Comandi per installare le dipendenze

```
pip install jinja2
pip install fastapi
pip install uvicorn
pip install python-multipart
python.exe -m pip install --upgrade pip
```

