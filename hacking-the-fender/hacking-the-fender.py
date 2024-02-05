import csv
compromised_users = []
# creating a list (compromised_users) of users whose passwords have been compromised
with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    compromised_users.append(line['Username'])

print(compromised_users)

# writing to the file 'compromised_users.txt' each user's username that has been compromised
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(user)

import json
# notifying the boss that i was successful in retrieving that compromised data in json format.
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
  }
  json.dump(boss_message_dict, boss_message)

# creating a new with block and open "new_passwords.csv" in write-mode. Saving the file object to a variable called new_passwords_obj
# writing slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with
with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = "U GOT HACXED - SLASH NULL"
  new_passwords_obj.write(slash_null_sig)
