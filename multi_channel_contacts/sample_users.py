import pandas as pd

df = pd.read_json("contacts.json")
df.info()

print(df.loc[[1, 2458, 98519, 115061, 476346]])

class User:

    def __init__(self, idx, email, phone, order_id, contacts):
        self.all_idx = {idx}
        self.email = email
        self.phone = phone
        self.order_id = order_id
        self.total_contacts = contacts

    def __repr__(self):
        return f"{self.all_idx}, {self.email}, {self.phone}, {self.order_id}, {self.total_contacts}"


user1 = User("1", "bla@gmail.com", "abcde", "98990000", 5)
user1.all_idx.add("3")
user1.all_idx.add("5")

user2 = User("10", "bottle@gmail.com", "", "", 10)
user2.all_idx.add("14")

user3 = User("20", "hehe@gmail.com", "", '', 15)
user3.all_idx.add("24")

user4 = User("30", "try@yahoo.com", "testst", "12345678", 30)
user4.all_idx.add("34")
user4.all_idx.add("35")
user4.all_idx.add("36")

email_dict = {"bla@gmail.com": user1, "hehe@gmail.com": user3, "bottle@gmail.com": user2, "try@yahoo.com": user4}
id_dict = {"abcde": user1, "testst": user4}
phone_dict = {"98990000": user1, "12345678": user4}
