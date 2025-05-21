from gps3 import gps3
from datetime import datetime, timezone

class GpsAdapter:
    def __init__(self):
        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

    def read(self):
        for new_data in self.gps_socket:
            if new_data:
                self.data_stream.unpack(new_data)
                if self.data_stream.lat != 'n/a' and self.data_stream.lon != 'n/a':
                    return {
                        "lat": float(self.data_stream.lat),
                        "lon": float(self.data_stream.lon),
                        "alt": float(self.data_stream.alt) if self.data_stream.alt != 'n/a' else None,
                        "time": datetime.utcnow().replace(tzinfo=timezone.utc).isoformat()
                    }
        return None