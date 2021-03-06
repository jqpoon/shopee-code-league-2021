import pandas as pd
import time
df = pd.read_json("contacts.json")

class User:

    def __init__(self, idx, email, phone, order_id, contacts):
        self.all_idx = {idx}
        self.email = email
        self.phone = phone
        self.total_contacts = contacts
        self.order_id = order_id

    def __repr__(self):
        return f"{self.all_idx}, {self.email}, {self.phone}, {self.order_id}, {self.total_contacts}"


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
    
    elif order_id != "" and order_id in id_dict:
        merge(id_dict[order_id], index, email, phone, order_id, contacts)
        user_exists = True

    elif phone != "" and phone in phone_dict:
        merge(phone_dict[phone], index, email, phone, order_id, contacts)
        user_exists = True

    if not user_exists:
        create_new_user(index, email, phone, order_id, contacts)


print(time.time() - s)

# Combine all 3 dictionaries into one set
user_set = set()

for key, value in email_dict.items():
    user_set.add(value)

for key, value in id_dict.items():
    user_set.add(value)

for key, value in phone_dict.items():
    user_set.add(value)

# Parse set into final output
output = []
for value in user_set:
    sorted_tickets = list(value.all_idx)
    sorted_tickets.sort()
    tickets_as_strings = [str(i) for i in sorted_tickets]

    ticket_trace = "-".join(tickets_as_strings)
    contact = value.total_contacts
    right_column = ticket_trace + ", " + str(contact)

    for item in tickets_as_strings:
        output.append([item, right_column])

df = pd.DataFrame(output, columns=["ticket_id", "ticket_trace/contact"])
df[["ticket_id"]] = df[["ticket_id"]].apply(pd.to_numeric)
df = df.sort_values(by="ticket_id")

print(df.info())
print(df.head(20))

df.to_csv("test.csv", index=None)