from statserve import StatServeClient

client = StatServeClient({
  'host': 'localhost',
  'port': 9001
})

response = client.get_stream_stats({
    'stream_name': 'test_stream'
})

print(response)