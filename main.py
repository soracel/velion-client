from adapters.gps_adapter import GpsAdapter
from adapters.obd_adapter import ObdAdapter
from siot_client import SiotClient
from data_collector import DataCollector
import threading

# === Konfiguration SIOT
GPS_URL = "http://raspberrypi.local:8080/api/v1/data-elements/deine_gps_id/data/report?retain=true"
OBD_URL = "http://raspberrypi.local:8080/api/v1/data-elements/de_HxR98w4vafoCDXwSgCF5YT/data/report?retain=true"
API_KEY = "2v72ylqiPDx3y"

# === Komponenten initialisieren
gps = GpsAdapter()
obd = ObdAdapter()
gps_client = SiotClient(GPS_URL, API_KEY)
obd_client = SiotClient(OBD_URL, API_KEY)

# === Datensammler starten (parallel)
gps_collector = DataCollector(gps, gps_client, name="GPS")
obd_collector = DataCollector(obd, obd_client, name="OBD")

# === Threads starten
threading.Thread(target=gps_collector.run).start()
threading.Thread(target=obd_collector.run).start()