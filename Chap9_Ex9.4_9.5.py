
# coding: utf-8

# In[4]:


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.res_name = restaurant_name
        self.cus_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        a = self.res_name.title() + " serves " + self.cus_type + "."
        print("\n" + a)

    def open_restaurant(self):
        a = self.res_name.title() + " is open. Welcome!"
        print("\n" + a)

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('Bar B Tonight', 'BBQ')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 205
print("Number served: " + str(restaurant.number_served))

restaurant.set_number_served(800)
print("Number served: " + str(restaurant.number_served))

restaurant.increment_number_served(250)
print("Number served: " + str(restaurant.number_served))


# In[10]:


class User():

    def __init__(self, first_name, last_name, username, email, location):
        self.f_name = first_name.title()
        self.l_name = last_name.title()
        self.u_name = username
        self.e_mail = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print("\n" + self.f_name + " " + self.l_name)
        print("  Username: " + self.u_name)
        print("  Email: " + self.e_mail)
        print("  Location: " + self.location)

    def greet_user(self):
        print("\nWelcome back, " + self.u_name + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

msgs = User('imran', 'sheikh', 'im_sheikh', 'imran.sh.iobm@gmail.com', 'karachi')
msgs.describe_user()
msgs.greet_user()

print("\nMaking 3 login attempts...")
msgs.increment_login_attempts()
msgs.increment_login_attempts()
msgs.increment_login_attempts()
print("  Login attempts: " + str(msgs.login_attempts))

print("Resetting login attempts...")
msgs.reset_login_attempts()
print("  Login attempts: " + str(msgs.login_attempts))

