import sqlite3

class ClimaDatos:
  def __init__(self):
    self.conn = sqlite3.connect("weather.db")
    cursor = self.conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS clima(
      codigo INTEGER PRIMARY KEY AUTOINCREMET,
      ciudad TEXT NOT NULL,
      pais TEXT NOT NULL,
      idciudad TEXT NOT NUll,
      temperatura REAL NOT NULL,
      humedad REAL NOT NULL,
      presion REAL NOT NULL,
      tempmax REAL NOT NULL,
      tempmin REAL NOT NULL,
      temppercibida REAL NOT NULL
    );''')
    self.con.commit()
  def agregarClima(self, ciudad, pais, idciudad, temperatura, humedad, presion, tempmax, tempmin, temppercibida):
    cursor = self.conn.cursor()
    cursor.execute(
        '''INSERT INTO clima (ciudad, pais, idciudad, temperatura, humedad,
        presion, tempmax, tempmin, temppercibida) VALUES (
        ?, ?, ?, ?, ?, ?, ?, ?, ?
        ); ''', ciudad, pais, idciudad, temperatura, humedad, presion, tempmax, tempmin, temppercibida)
    self.conn.commit()
