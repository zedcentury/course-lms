import json

import requests

URL = "https://edu-asliddin.odoo.com"
DB = "edu-asliddin"
USERNAME = "admin@gmail.com"
PASSWORD = "12345678"


def authenticate(url, db, login, password):
    auth_url = f'{url}/jsonrpc'
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "common",
            "method": "login",
            "args": [db, login, password]
        }
    }

    # So'rovni yuborish
    headers = {"Content-Type": "application/json"}
    response = requests.post(auth_url, data=json.dumps(payload), headers=headers)

    print(response.status_code)

    # Javobni tekshirish
    if response.status_code == 200:
        result = response.json().get('result')
        if result:
            # Tizimga kirgan foydalanuvchining ID-si
            uid = result
            print(f"✅ Autentifikatsiya muvaffaqiyatli. User ID (UID): {uid}")
            return uid

    print("❌ Autentifikatsiya muvaffaqiyatsiz.")
    return None


uid = authenticate(URL, DB, USERNAME, PASSWORD)
print(uid)


# --- 3. Ma'lumotlarni o'qish (Product Template) ---
# JSON-RPC "object" endpointidan foydalanib ma'lumotlar bazasi bilan ishlanadi

def read_data(url, db, uid, password, model, search_domain, fields_to_read):
    read_url = f'{url}/jsonrpc'

    # 'execute_kw' metodi Odoo model funksiyalarini chaqirish uchun asosiy metoddur.
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [
                db,
                uid,
                password,
                model,  # Ishlayotgan model: 'product.template'
                "search_read",  # Chaqlirayotgan model metodi
                [search_domain],  # Qidiruv filtri (domain)
                {'fields': fields_to_read, 'limit': 2}  # Parametrlar: o'qiladigan maydonlar
            ]
        }
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(read_url, data=json.dumps(payload), headers=headers)

    print(response.status_code)
    return response.json()


data = read_data(URL, DB, uid, PASSWORD, 'res.users', [], ['name'])

print(data)
