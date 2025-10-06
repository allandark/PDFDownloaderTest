## Logger alle de nødvendige indikatorer for succesfulde og fejlede downloads
# Import tidsstempler til log beskeder
from datetime import datetime

class LoggerService:
    # Definerer beskeder der informerer brugeren
    def log_info(self, message: str) -> None:
        print(f"[{datetime.now():%H:%M:%S}] INFO: {message}")

    # Definerer beskeder der viser fejl til brugeren
    def log_error(self, message: str) -> None:
        print(f"[{datetime.now():%H:%M:%S}] ERROR: {message}")