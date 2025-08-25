countries = ('USA', 'ARG', 'BRB', 'BLZ', 'BOL', 'BRA', 'CAN', 'CHL', 'COL', 'CRI', 'CUB', 'DOM', 'ECU', 'SLV', 'GRD', 'GTM', 'GUY', 'HTI', 'HND', 'MEX', 'NIC', 'PRY', 'KNA', 'LCA', 'VCT', 'SUR', 'BHS', 'TTO', 'URY', 'KOR', 'CHN', 'MYS', 'PHL', 'SGP', 'TWN', 'THA', 'IDN', 'JAM')

# 각 값의 빈도를 세기 위해 Counter 클래스를 사용합니다.
from collections import Counter

# Counter 객체를 사용하여 각 국가 코드의 빈도를 계산합니다.
country_counts = Counter(countries)

# 빈도가 1보다 큰 값(즉, 중복된 값)을 출력합니다.
duplicates = [country for country, count in country_counts.items() if count > 1]

print("중복된 값:", duplicates)