import pandas
import time
df = pandas.read_json("contacts.json")


class User:

    def __init__(self, idx, email, phone, order_id, contacts):
        self.all_idx = {idx}
        self.email = email
        self.phone = phone
        self.order_id = order_id
        self.total_contacts = contacts

    def __repr__(self):
        return f"{self.email}, {self.id}, {self.phone}, {self.total_contacts}"


email_dict = {}
id_dict = {}
phone_dict = {}


def merge(user, index, email, phone, order_id, contacts):
    user.all_idx.add(index)

    user.total_contacts += contacts

    if email != "":
        user.email = email
        email_dict[email] = user
    
    if phone != "":
        user.phone = phone
        phone_dict[phone] = user

    if order_id != "":
        user.order_id = order_id
        id_dict[order_id] = user

def create_new_user(index, email, phone, order_id, contacts):
    new_user = User(index, email, phone, order_id, contacts)

    if new_user.email != "":
        email_dict[new_user.email] = new_user

    if new_user.order_id != "":
        id_dict[new_user.order_id] = new_user
    
    if new_user.phone != "":
        phone_dict[new_user.phone] = new_user


s = time.time()

for index,row in df.iterrows():

    email = row["Email"]
    phone = row["Phone"]
    order_id = row["OrderId"]
    contacts = row["Contacts"]
    user_exists = False

    if email != "" and email in email_dict:
        merge(email_dict[email], index, email, phone, order_id, contacts)
        user_exists = True
    
    if order_id != "" and order_id in id_dict:
        merge(id_dict[order_id], index, email, phone, order_id, contacts)
        user_exists = True

    if phone != "" and phone in phone_dict:
        merge(phone_dict[phone], index, email, phone, order_id, contacts)
        user_exists = True

    if not user_exists:
        create_new_user(index, email, phone, order_id, contacts)


print(len(email_dict), len(id_dict), len(phone_dict))
print(time.time() - s)