"""
class LoggerService
En service der deler informationer i konsollen

Args:
    message (str): Beskeden der skal deles

Functions:
    log_info(message):  Funktion der skriver en information i konsollen
    log_error(message): Funktion der skriver en fejlbesked i konsollen

Returns:
    Printer beskeder i konsollen ved kald
"""

# Import tidsstempler til log beskeder
from datetime import datetime

class LoggerService:
    # Definerer beskeder der informerer brugeren
    def log_info(self, message: str) -> None:
        print(f"[{datetime.now():%H:%M:%S}] INFO: {message}")

    # Definerer beskeder der viser fejl til brugeren
    def log_error(self, message: str) -> None:
        print(f"[{datetime.now():%H:%M:%S}] ERROR: {message}")