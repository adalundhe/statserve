from zebra_statserve import StatServeClient

client = StatServeClient({
  'host': 'localhost',
  'port': 9001
})

response = client.get_field_stat({
    'stream_name': 'test_stream',
    'key': 'test_field',
    'type': 'stat',
    'stat': 'med'
})

print(response)