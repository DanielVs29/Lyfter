import csv

games_list = []

game_headers = (
	'name',
	'genre',
	'developer',
	'esrb_rating',
)

def add_new_game():

    while True:
        game = {
            "name": input("Ingrese el nombre del juego: "),
            "genre": input("Ingrese el genero del juego: "),
            "developer": input("Ingrese el desarrollador: "),
            "esrb_rating": input("Ingrese la calificacion ESRB: ")
        }
        
        games_list.append(game)
        
        again = input("Desea agregar otro juego? (si/no): ").lower()
        if again != "si":
            break


def write_csv_file(file_path, data, headers):
  with open(file_path, 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, headers, delimiter='\t')
    writer.writeheader()
    writer.writerows(data)


add_new_game()
write_csv_file('gamesTab.csv', games_list, game_headers)