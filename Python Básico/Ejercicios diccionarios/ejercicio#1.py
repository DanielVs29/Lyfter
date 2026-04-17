
roms = []

hotel_information = { 
    'name': 'Hotel Costa Rica',
    'stars': '4 stars',
    'rooms': [
        { 'number': 101,
          'floor': 1, 
          'price': 100 },
          
          { 'number': 102,
          'floor': 2, 
          'price': 150 },

          { 'number': 103,
          'floor': 3, 
          'price': 300 },
    ]
}

print(hotel_information['name'])
print(hotel_information['stars'])
for room in hotel_information['rooms']:
    print(f"Room number: {room['number']}, Floor: {room['floor']}, Price: {room['price']}")