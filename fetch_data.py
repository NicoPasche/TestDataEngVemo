import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Country

def fetch_data():
    # Crea la base de datos
    engine = create_engine('sqlite:///countries.db')
    Base.metadata.create_all(engine)

    # Inicia la sesión de la base de datos
    Session = sessionmaker(bind=engine)
    session = Session()

    # Obtiene los datos de la API
    response = requests.get('https://restcountries.com/v3.1/all')
    data = response.json()

    # Procesa los datos y los almacena en la base de datos
    countries = []
    for country_data in data:
        country = Country(
            name=country_data['name']['common'],
            capital=','.join(country_data['capital']) if 'capital' in country_data else None,
            currency=list(country_data['currencies'].keys())[0] if 'currencies' in country_data else None,
            continent=country_data['region'],
            language=','.join(country_data['languages'].keys()) if 'languages' in country_data else None,
            population=int(country_data['population']) if 'population' in country_data and country_data['population'] is not None else 0,
            flag=country_data['flags']['png']
        )
        session.add(country)
        countries.append({
            'name': country.name,
            'capital': country.capital,
            'currency': country.currency,
            'continent': country.continent,
            'language': country.language,
            'population': country.population,
            'flag': country.flag
        })

    session.commit()

    # Devuelve los datos procesados
    return countries
