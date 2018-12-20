from hcloud import HcloudClient
from hcloud.images.domain import Image

client = HcloudClient(token="{YOUR_API_TOKEN}")  # Please paste your API token here between the quotes
response = client.servers.create(name="my-server", server_type="cx11", image=Image(name="ubuntu-18.04"))
server = response.server
print("Server was created!\n")
print('\tServer ID: {server_id}\n'.format(server_id=server.id))
print('\tServer Name: ' + server.name + '\n')
print('\tServer IPv4: ' + server.public_net["ipv4"]["ip"] + '\n')
print('\tRoot password: ' + response.root_password + '\n')

print("Now we delete the server\n")
server.delete()
