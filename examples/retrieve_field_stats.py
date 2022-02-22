from zebra_statserve import StatServeClient

client = StatServeClient({
  'host': 'localhost',
  'port': 9001
})

response = client.register({
  'stream_name': 'test_stream'
})

response = client.get_field_stats({
    'stream_name': 'test_stream',
    'key': 'test_field'
})

print(response)