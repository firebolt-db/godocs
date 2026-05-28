SELECT TO_JSON_STRING({
  'id': 1,
  'name': { 'first': 'John', 'last': 'Doe' },
  'addresses': [
    {
      'street_name': 'Jane St.',
      'street_no': 42,
      'city': 'New York'
    },
    {
      'street_name': 'King St.',
      'street_no': 17,
      'city': 'Los Angeles'
    }
  ]
}) AS js;