def gas_stations(distance, tank_size, stations):
	stations_to_visit = []

	stations.append(distance)

	i = tank_size
	while i < distance:
		for j in range(len(stations)):
			if stations[j] > i:
				break
		stations_to_visit.append(stations[j-1])

		i = stations[j-1] + tank_size

	return stations_to_visit

print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
