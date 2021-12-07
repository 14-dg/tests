#https://stackoverflow.com/questions/7014953/i-need-to-securely-store-a-username-and-password-in-python-what-are-my-options

import keyring

MAGIC_USERNAME_KEY = 'im_the_magic_username_key'

# the service is just a namespace for your app
service_id = 'IM_YOUR_APP!'  

username = 'dustin'

# save password
keyring.set_password(service_id, username, "password")

# optionally, abuse `set_password` to save username onto keyring
# we're just using some known magic string in the username field
keyring.set_password(service_id, MAGIC_USERNAME_KEY, username)

# again, abusing `get_password` to get the username.
# after all, the keyring is just a key-value store
username = keyring.get_password(service_id, MAGIC_USERNAME_KEY)
password = keyring.get_password(service_id, username)  

print(username, password)