from faker import Faker
fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, first_name, last_name, tel_priv, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.tel_priv = tel_priv
        self.email_address = email_address
    def contact(self):
        return f"Wybieram numer domowy: {self.tel_priv} i dzwonię do {self.first_name} {self.last_name} "
    
    @property
    def label_lenght(self):
        return sum([len(self.first_name), len(self.last_name)])


class BusinessContact(BaseContact):
    def __init__(self, tel_work, company, occupation, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tel_work = tel_work
        self.company = company
        self.occupation = occupation
    def contact_work(self):
        return f"Wybieram numer służbowy: {self.tel_work} i dzownię do {self.first_name} {self.last_name}"


human_1 = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), occupation=fake.job(),
              email_address=fake.email(), tel_priv=fake.phone_number(), tel_work=fake.phone_number())

print(human_1)
print(human_1.contact())
print(human_1.contact_work())
print(human_1.label_lenght)


kind = int(input("Jaki rodzaj wizytówki utworzyć? 1 - domowa, 2 - biznesowa: "))
how_many = int(input("Podaj ilość wizytówek"))

#def create_contacts (kind, how_many):

for i in range(how_many):
  if kind == 1:
    contact = f"{fake.first_name()}, {fake.last_name()}, {fake.phone_number()}, {fake.email()}"
    print(contact)
  elif kind == 2:
    contact = f"{fake.first_name()}, {fake.last_name()}, {fake.phone_number()}, {fake.email()}, {fake.phone_number()}, {fake.job()}"
    print(contact)