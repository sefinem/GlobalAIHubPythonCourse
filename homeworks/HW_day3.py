# Day - 3
# print('='*5, 'login page', '='*5)
# username = input('Enter your username: ')
# password = input('Enter your password: ')

# user_list = ['user1','user4','user3']
# pass_list = ['pass1','pass4','pass3']

# if username in user_list:
#   index = user_list.index(username)
#   if password in pass_list and pass_list.index(password) == index:
#     print(f'Welcome {username}')
#   else:
#     print('Invalid credentials, rerun the login program!')  
# else:
#   print('Invalid credentials, rerun the login program!')


# EXTRA
print('='*5, 'login page', '='*5)
username = input('Enter your username: ')
password = input('Enter your password: ')

credentials_dict = {
  'user1': 'pass1',
  'user2': 'pass2',
  'user3': 'pass3'
} 

if username in credentials_dict and credentials_dict[username] == password:
  print(f'Welcome {username}')
else:
  print('Invalid credentials, rerun the login program!')
