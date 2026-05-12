def order_songs_by_name(file_path, new_file):

    with open(file_path, "r", encoding="utf-8") as file:
        songs = file.readlines()

    songs.sort(key=str.lower)
    

    with open(new_file, "w", encoding="utf-8") as file:
        file.writelines(songs)

order_songs_by_name(
    "C:/Users/Danie/Documents/Lyfter/Python/Ejercicios de Manejo de Archivos/songs.txt",
    "C:/Users/Danie/Documents/Lyfter/Python/Ejercicios de Manejo de Archivos/sorted_songs.txt"
)

