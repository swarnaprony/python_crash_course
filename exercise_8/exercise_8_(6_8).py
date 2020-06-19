#exercise_8_(6_8)
#date: 26/03/2020

#exercise_8_6
#city_names

def city_country(city, country):
    """name of city and country"""
    city_country_name = f'"{city}, {country}"'
    return city_country_name
name = city_country('hamburg', 'germany').title()
print(f"{name}")
name_1 = city_country('dhaka', 'bangladesh').title()
print(f"{name_1}")
name_2 = city_country('upsala', 'sweden').title()
print(f"{name_2}")

#exercise_8_7
#album

def make_album(artist_name, album_title, total_song = None):
    if total_song:
        album = {'artist_name': f"{artist_name}", 'album_title': f"{album_title}", 'total_song': f"{total_song}"}
    else:
        album = {'artist_name': f"{artist_name}", 'album_title': f"{album_title}"}
    return album
new_album = make_album('selena','rare')
print(new_album)
new_album_1 = make_album('anjan_datta','valobasi tomay')
print(new_album_1)
new_album_2 = make_album('pinl_floyd','wish you were here')
print(new_album_2)
new_album_3 = make_album('pinl_floyd','wish you were here', '10')
print(new_album_3)


#exercise_8_8
#user_albums

def album_list():
    artist_name = input('write name of the artist: ')
    album_title = input('title of album: ')
    album = f"{artist_name}, {album_title}"
    return album
while True:
    list_of_albums = album_list()
    print(list_of_albums)
    terminaion = input('if you want to quit write "quit" otherwise "no": ')
    if terminaion == 'quit':
        break