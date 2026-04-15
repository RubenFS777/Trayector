# Trayector
Programa para visualizar trayectorias de sondas y misiones espaciales con datos tomados del SBDB del JPL

Pasos necesarios para obtener el CSV adecuado para la misión Artemis II

Ir a la paǵina web https://ssd.jpl.nasa.gov/horizons/app.html#/

En las configuraciones (Settings) dar los siguientes valores

* 1 Ephemeris Type: Vector Table
* 2 Target Body: -1024
* 3 Coordintate Center: 500
* 4 Time Specification: Start=2026-04-02 01:58:33 TDB, Stop=2026-04-10 23:54:22, Step=15 (minutes)
* 5 Tablet Settings:
  * Select Output Quantities (menú desplegable): 2. State vector {x,y,x,Vx,Vy,Vz}
  * Statistical Uncertainties: No seleccionar ninguna.
  * Additional Table Settings:
    * Reference frame: ICRF
    * Reference plane: ecliptic x-y plane
    * Vector correction: geometric states
    * Calendar type: Mixed
    * Output units: km and seconds
    * Vector lables: seleccionado
    * Output TDB-UT: no seleccionar
    * CSV format: seleccionado
    * Object summary: seleccionado
  
Pulsar el botón "Generate Ephemeris"

Pulsar el botón "Download Results"

Cambiar el nombre del archivo descargado a artemis_vectors.csv

# Requisitos
* Instalar python https://www.python.org/downloads/
* Instalar biblioteca numpy https://numpy.org/install/
* Instalar biblioteca matplotlib https://matplotlib.org/stable/install/index.html
* Descargar archivo de posición en el tiempo como se indica más arriba.

