import mysql.connector
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import uvicorn

app = FastAPI()

# configurazione database
db_config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "",
    "database" : "gestore_interrogazioni"
}
templates = Jinja2Templates(directory="templates")

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM interrogazioni")
    
    interrogazioni = cursor.fetchall()
    cursor.close()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "interrogazioni": interrogazioni})

@app.post("/prenota", response_class=HTMLResponse)
def prenota_interrogazione(request: Request, id: int = Form(...), studente : str = Form(...)):
    conn = get_db_connection()
    cursor = conn.cursor()

    #controllo se l'interogazione è disponibile
    cursor.execute("SELECT stato FROM interrogazioni WHERE id = %s",(id,))
    result = cursor.fetchone()
    if result [0] == "disponibile":
        cursor.execute("UPDATE interrogazioni SET studente = %s, stato = 'prenotato' WHERE id = %s",(studente, id))
    conn.commit()
    cursor.close()
    conn.close()

@app.post("/cancella", response_class=HTMLResponse)
def cancella_prenotazione(request: Request, id: int = Form(...), studente : str = Form(...)):
    conn = get_db_connection()
    cursor = conn.cursor()
    #Cancello la prenotazione
    cursor.execute("SELECT stato FROM interrogazioni WHERE id = %s",(id,))
    result = cursor.fetchone()
    if result [0] != "disponibile":
        cursor.execute("DELETE FROM interrogazioni WHERE id = %s",(id))



    conn.commit()
    conn.close()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)