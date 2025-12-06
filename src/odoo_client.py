import json

import requests

URL = "https://edu-asliddin.odoo.com"
DB = "edu-asliddin"
USERNAME = "admin@gmail.com"
PASSWORD = "12345678"


class OdooClient:
    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password

    def authenticate(self):
        auth_url = f"{self.url}/jsonrpc"
        payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "service": "common",
                "method": "login",
                "args": [self.db, self.username, self.password]
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

    def search_read(self, model, domain, fields, limit):
        uid = self.authenticate()

        read_url = f'{self.url}/jsonrpc'

        # 'execute_kw' metodi Odoo model funksiyalarini chaqirish uchun asosiy metoddur.
        payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "service": "object",
                "method": "execute_kw",
                "args": [
                    self.db,
                    uid,
                    self.password,
                    model,  # Ishlayotgan model: 'product.template'
                    "search_read",  # Chaqlirayotgan model metodi
                    [domain],  # Qidiruv filtri (domain)
                    {'fields': fields, 'limit': limit}  # Parametrlar: o'qiladigan maydonlar
                ]
            }
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(read_url, data=json.dumps(payload), headers=headers)

        return response.json()

    def create(self, model, body):
        uid = self.authenticate()

        read_url = f'{self.url}/jsonrpc'

        # 'execute_kw' metodi Odoo model funksiyalarini chaqirish uchun asosiy metoddur.
        payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": {
                "service": "object",
                "method": "execute_kw",
                "args": [
                    self.db,
                    uid,
                    self.password,
                    model,  # Ishlayotgan model: 'product.template'
                    "create",  # Chaqlirayotgan model metodi
                    body
                ]
            }
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(read_url, data=json.dumps(payload), headers=headers)

        return response.json()


odoo_client = OdooClient(URL, DB, USERNAME, PASSWORD)

uid = odoo_client.authenticate()

partners = odoo_client.search_read('res.partner', [['is_company', '=', False]], ['name'], 5)
print(partners)

partner_id = odoo_client.create('res.partner', [{'name': 'Odoo Client Partner'}])
print(partner_id)
