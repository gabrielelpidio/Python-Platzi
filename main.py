import sys
import csv
import os


CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
	with open(CLIENT_TABLE, mode='r') as f:
		reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

		for row in reader:
			clients.append(row)

def _save_clients_to_storage():
	tmp_table_name = f'{CLIENT_TABLE}.tmp.'
	with open(tmp_table_name, mode='w') as f:
		writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
		writer.writerows(clients)

		os.remove(CLIENT_TABLE)
	os.rename(tmp_table_name, CLIENT_TABLE)

def create_client(client):
	global clients

	if client not in clients:
		clients.append(client)
	else:
		print('Client already is in the client\'s list')


def list_clients(): 
	for idx, client in enumerate(clients):
		print ('{uid} | {name} | {company} | {email} | {position}'.format(
			uid=idx,
			name=client['name'],
			company=client['company'],
			email=client['email'],
			position=client['position']))

def _get_client_for_edit(action):
	print('What is the number of the client you want to {action}?')
	return int(input()) #ADD ERROR HANDLER

def update_client(): 
	global clients 

	list_clients()
	client_number = _get_client_for_edit('update')
	if clients[client_number]:
		print('What do you want to edit?')
		print('[A]ll')
		print('[N]ame')
		print('[C]ompany')
		print('[E]mail')
		print('[P]osition')

		command = _get_command()

		def _updated_input(key): 
			return input(f'What is the new {key} of the client?')

		if command == 'A':
			clients[client_number] = _get_client_from_input()
		elif command == 'N':
			clients[client_number]['name'] = _updated_input('name')
		elif command == 'C': 
			clients[client_number]['company'] = _updated_input('company')
		elif command == 'E': 
			clients[client_number]['email'] = _updated_input('email')
		elif command == 'P': 
			clients[client_number]['position'] = _updated_input('position')
	else: 
		_client_not_found()


def delete_client(): 
	global clients
	client_number = _get_client_for_edit('remove')

	if clients[client_number]:
		del clients[client_number]
	else:
		_client_not_found()



def search_client(client_name): 
	for client in clients:
		if client['name'] != client_name:
			print(client['name'])
			continue
		else:
			return client

def _client_not_found(): 
	print ('Client is not in clients list')


def _print_welcome(): 
	print ('WELCOME TO PLATZI VENTAS')
	print ('*' * 50)
	print ('What would you like to do today')
	print ('[C]reate client')
	print ('[D]elete client')
	print ('[L]ist client')
	print ('[U]pdate client')
	print ('[S]earch client')



def _get_client_field(field_name): 
	return _input_field(f'What is the client {field_name}?')


def _input_field(message):
	field = None

	while not field:
		field = input(message)

		if field == 'exit()':
			sys.exit()

	return field

def _get_client_from_input(): 
	client = {
			'name': _get_client_field('name'),
			'company':  _get_client_field('company'),
			'email': _get_client_field('email'),
			'position': _get_client_field('position'),
			}
	return client


def _get_command(): 
	command = input()
	command = command.upper()
	return command

if __name__ == '__main__': 
	_initialize_clients_from_storage()

	_print_welcome()
	
	command = _get_command()	

	if command == 'C':
		client = _get_client_from_input()
		create_client(client)
	elif command == 'D':
		delete_client()
	elif command == 'U':
		update_client()
	elif command == 'S':
		client_name = _input_field('Wich is the client name?')
		found = search_client(client_name)
		if found:
			print(f'{client_name} is in the client\'s list')
		else:
			print(f'The client: {client_name} is not in our client\'s list')
	elif command == 'L':
		list_clients()
	else:
		print ('Invalid command')

	_save_clients_to_storage()