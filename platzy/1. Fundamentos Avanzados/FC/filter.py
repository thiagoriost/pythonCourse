numbers = list(range(1,6))
new_numbers = list(filter(lambda x : x % 2 == 0, numbers))
print("new_numbers => ", new_numbers)

print("-"*40)

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print("matches => ", matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))

print("new_list => ", new_list, len(new_list))

print("matches => ", matches)
print(len(matches))

print("Playgrounds: Retorna solo palabras de 4 letras y más ")
def filter_by_length(words):
   # Escribe tu solución 👇
   return list(filter(lambda e : len(e) >= 4, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)

