clients = []

clients.append("Joseph")
clients.append("Samuel")
clients.append("Jones")
clients.append("Daniel")

new_client = input("New clients name: ")
clients.append(new_client)

for client in clients:
    print(client)
