import pandas
df = pandas.read_json("contacts.json")


class User:
    email = None
    id = None
    phone = None
    total_contacts = 0

    def __init__(self, email = None, id_num = None, phone = None):
        self.email = email
        self.id = id_num
        self.phone = phone

    def __repr__(self):
        return f"{self.email}, {self.id}, {self.phone}, {self.total_contacts}"
        
    def merge():
        pass


# email_dict = dict.fromkeys(df["Email"].tolist())
# order_dict = dict.fromkeys(df["Id"].tolist())
# phone_dict = dict.fromkeys(df["Phone"].tolist())