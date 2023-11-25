# Step 1
Delete all .json files in both the client and server folders if any Exist

# Step 2
Run client/cust.py with this main function:
def main():
    generate_and_store_keys()
    data = [24, 4, 6, 1]
    create_data(data)

This should generate two files:
    data.json
    keys.json

# Step 3
Move data.json to the server file. This simulates a user sending their encypted data to the company.

# Step 4
Run server/servercalc.py with this main function:
def main():
	datafile=serializeData()
	with open('server/answer.json', 'w') as file:
		json.dump(datafile, file)

This should generate one file:
    answer.json

# Step 5
Move answer.json to the client folder. This simulated the company sending a user an answer based on their trained model.

# Step 6
Run client/cust.py with this main function:
def main():
    print("Encrypted Answer: ", decrypt_data())
This should print a number.

# Step 7
Run server/servercalc.py with this main function:
def main():
	print("Non Encrypted Answer: ", testNonEncryptedData([24, 4, 6, 1]))
This should print a number.

# Step 8
Verify that the numbers printed in Steps 6 & 7 are equivalent. If so, the model accurately did ML with the encrypted data.