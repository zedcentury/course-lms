import xmlrpc.client

url = "https://edu-asliddin.odoo.com"
db = "edu-asliddin"
username = "admin@gmail.com"
password = "29f8d8f581d21a42946cd589d381fc7f1e9181c7"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# MODEL = 'res.partner'
# METHOD = 'search_read'
# domain = ['|', ['is_company', '=', True], ['name', 'like', 'A']]
# partners = models.execute_kw(db, uid, password, MODEL, METHOD, [domain], {
#     'fields': ['name', 'email', 'country_id'],
#     'limit': 4,
#     'offset': 10,
# })
# print(partners)

MODEL = 'res.partner'
METHOD = 'create'
BODY = [{'name': 'New Partner'}]
partner_id = models.execute_kw(db, uid, password, MODEL, METHOD, BODY)
print(partner_id)
