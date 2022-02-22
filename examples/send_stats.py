from zebra_statserve import StatServeClient

client = StatServeClient({
  'host': 'localhost',
  'port': 9001
})

response = client.update({
    'stream_name': 'test_stream',
    'metadata': {
        'event_tags': [
            {
                'name': 'test_tag',
                'value': 'hello!'
            }
        ]
    },
    'key': 'test_field',
    'value': 1
})

print(response)