travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country (country_name, times_visit, city_list):
   travel_log.append(
        {
            "country": country_name,
            "visits": times_visit,
            "cities": city_list,
        }
   )

# def add_new_country (country_name, times_visit, city_list):
#     new_country={}
#     new_country["country"]=country_name
#     new_country["visits"]=times_visit
#     new_country["cities"]=city_list
    
#     travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)