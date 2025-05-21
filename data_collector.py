import time

class DataCollector:
    def __init__(self, adapter, siot_client, name="Sensor", interval=1):
        self.adapter = adapter
        self.client = siot_client
        self.interval = interval
        self.name = name

    def run(self):
        print(f"[{self.name}] Erfassung gestartet (Intervall: {self.interval}s)")
        while True:
            data = self.adapter.read()
            if data:
                payload = {"data": {k: v for k, v in data.items() if k != "time"}, "time": data["time"]}
                self.client.send(payload)
            time.sleep(self.interval)