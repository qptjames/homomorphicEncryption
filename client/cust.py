import phe as paillier
import json

def generate_and_store_keys():
    public_key, private_key = paillier.generate_paillier_keypair()
    keys = {}
    keys['public_key'] = {'n': public_key.n}
    keys['private_key'] = {'p': private_key.p, 'q': private_key.q}
    with open('client/keys.json', 'w') as file:
        json.dump(keys, file)

def load_keys():
    with open('client/keys.json', 'r') as file:
        keys = json.load(file)
        pub_key = paillier.PaillierPublicKey(n=int(keys['public_key']['n']))
        priv_key = paillier.PaillierPrivateKey(pub_key, keys['private_key']['p'], keys['private_key']['q'])
        return pub_key, priv_key

def serialize_data(public_key, data):
    encrypted_data_list = [public_key.encrypt(x) for x in data]
    encrypted_data = {}
    encrypted_data['public_key'] = {'n': public_key.n}
    encrypted_data['values'] = [(str(x.ciphertext()), x.exponent) for x in encrypted_data_list]
    serialized = json.dumps(encrypted_data)
    return serialized

def load_answer():
    with open('client/answer.json', 'r') as file:
        ans = json.load(file)
        answer = json.loads(ans)
        return answer

def create_data(data):
    pub_key, priv_key = load_keys()
    data_file = serialize_data(pub_key, data)
    with open('client/data.json', 'w') as file:
        json.dump(data_file, file)

def decrypt_data():
    pub_key, priv_key = load_keys()
    answer_file = load_answer()
    answer_key = paillier.PaillierPublicKey(n=int(answer_file['pubkey']['n']))
    answer = paillier.EncryptedNumber(answer_key, int(answer_file['values'][0]), int(answer_file['values'][1]))
    if answer_key == pub_key:
        decrypted_answer = priv_key.decrypt(answer)
        return decrypted_answer

def main():
    # generate_and_store_keys()
    # data = [24, 4, 6, 1]
    # create_data(data)

    print("Encrypted Answer: ", decrypt_data())

if __name__ == "__main__":
    main()
