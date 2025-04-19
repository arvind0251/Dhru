import requests
from constants import ACCESS_TOKEN, MERCHANT_ID

def verify_utr_with_bharatpay(utr):
    try:
        r = requests.post("https://api.bharatpe.in/v1/payment/verify", headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json"
        }, json={"utr": utr, "merchant_id": MERCHANT_ID})
        return r.json().get("status") == "PAID"
    except:
        return False
