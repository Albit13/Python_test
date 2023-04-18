import json

def parse_users_file(input_file, output_json_file, output_txt_file):
    users = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(';')
            name = parts[0].strip()
            age = parts[1].strip() or None
            try:
                age = int(age)
            except ValueError:
                age = None
            phones = [phone.strip() for phone in parts[2].split(',')] if len(parts) > 2 else []
            users.append({'name': name, 'age': age, 'phones': phones})

    with open(output_json_file, 'w') as f:
        json.dump(users, f)

    with open(output_txt_file, 'w') as f:
        for user in users:
            age = str(user['age']) if user['age'] is not None else ''
            phones = ','.join(user['phones']) if user['phones'] else ''
            f.write(f"{user['name']};{age};{phones}\n")
