This is the backend api for Bond, Legal Entity, and User resources

Applications are in 
**originmarkets/applications/**

### install packages
pip install -r requirements.txt (WAIT, are you in a virtual environment?)

### setup database
in **originmarkets/originmarkets/settings.py**
- Add the database, user credentials and host/port to point to a valid server
- This solution was tested with SQLite

### Run Migration
In the parent directory **originmarkets**
- python manage.py migrate

### Run App
In the parent directory **originmarkets**
- python manage.py runserver

### Try out api at
- {host}/api/
- bonds, legal_entities, and users are supported. 


### Remarks
- Testing is limited because of time but more cases need tests
- Legal Entity is created on first request and used for subsequent reqest (simple caching)
- Admin users can view all bonds, non-admin users view only their bonds
- filter bonds on fields 'isin', 'lei', 'legal_name'
- filter legal_entities on fields 'legal_name', 'legal_jurisdiction', 'status'

post example bond in the api Raw data section

```
{
    "isin": "FR0000131104",
    "size": 100000000,
    "currency": "EUR",
    "maturity": "2025-02-28",
    "lei": "R0MUWSFPU8MPRO8K5P83"
}

```

