import time
import cianparser
import datetime

def run(city_name, proxy_list, deal_type_list, room_list, page_start, page_end):
	parser = cianparser.CianParser(location=city_name)
	
	for deal_type in deal_type_list:
		for room in room_list:
			data = parser.get_flats(deal_type=deal_type, rooms=room, with_saving_csv=True, additional_settings={"start_page":page_start, "end_page": page_end})
			
			now = time.localtime()
			print(f'{time.strftime("%H:%M:%S", now)}: city: {city_name}, deal type: {deal_type}, room: {room}: data len: {len(data)}\n\n')


proxies = []
deal_types = ["sale", "rent_long"]
# deal_types = ["rent_long"]
rooms = [1, 2, 3, 4, 5, 'studio']
# run('Ханты-Мансийск', proxies, deal_types, rooms)
# run('Нижневартовск', proxies, deal_types, rooms)

page_limit = 50
cities = ['Нягань', 'Когалым', 'Мегион', 'Радужный', 'Лангепас', 'Урай', 'Лянтор', 'Пыть-Ях', 'Югорск', 'Советский', 'Белоярский', 'Покачи']

run('Нефтеюганск', proxies, deal_types, rooms, 22, page_limit)

for city in cities:
	run(city, proxies, deal_types, rooms, 1, page_limit)