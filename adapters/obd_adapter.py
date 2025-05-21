import obd
from datetime import datetime, timezone

class ObdAdapter:
    def __init__(self, port="/dev/ttyUSB0"):
        self.connection = obd.OBD(portstr=port, fast=False)
        if not self.connection.is_connected():
            raise RuntimeError("OBD-II Verbindung fehlgeschlagen")

        self.commands = {
            "speed": obd.commands.SPEED,
            "rpm": obd.commands.RPM,
            "throttle": obd.commands.THROTTLE_POS,
            "consumption": obd.commands.FUEL_RATE,
        }

    def read(self):
        result = {}
        for name, cmd in self.commands.items():
            response = self.connection.query(cmd)
            if not response.is_null() and response.value:
                result[name] = round(response.value.magnitude, 2)

        result["time"] = datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
        return result