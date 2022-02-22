from statserve import StatServeClient

client = StatServeClient({
  'host': 'localhost',
  'port': 9001
})

response = client.register({
  'stream_name': 'test_stream'
})

print(response)