import os
from dotenv import load_dotenv
load_dotenv()

ADMIN_ID = int(os.getenv("ADMIN_ID"))
BOT_TOKEN = os.getenv("BOT_TOKEN")
UPI_ID = os.getenv("UPI_ID")
QR_CODE_LINK = os.getenv("QR_CODE_LINK")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
MERCHANT_ID = os.getenv("MERCHANT_ID")
API_KEY = os.getenv("API_KEY")
SUPPORT_URL = os.getenv("SUPPORT_URL")

HEADERS_5SIM = {
    "Authorization": f"Bearer {API_KEY}"
}
