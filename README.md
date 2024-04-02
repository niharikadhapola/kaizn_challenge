# kaizn_challenge

## Set Up
```
pip install -r requirements.txt
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
## API
```
deployed on Render [https://web-nzcq.onrender.com] -> sometimes it takes seconds to a minute to get the response due to inactivity. 

API's
https://web-nzcq.onrender.com/admin/
admin panel credential
username:ndhapola
password: 1234


api/ register/ [name='register']
    POST
    https://web-nzcq.onrender.com/api/register/
    Body : {"username": "testuser1", "password": "1234", "email": "test12@example.com"}

api/ login/ [name='login']
    POST
    https://web-nzcq.onrender.com/api/login/
    Body : {"username":"testuser","password":"1234"}

api/ logout/ [name='logout']
    POST
    https://web-nzcq.onrender.com/api/logout/
    token:984fa52fa98626687c50c5227cd4e8036b0166ab

api/ items/ [name='item-list']
    GET
    https://web-nzcq.onrender.com/api/items/?in_stock=100&page=1&page_size=10 
    token:984fa52fa98626687c50c5227cd4e8036b0166ab

api/ items_create/ [name='item-create']
    POST
    https://web-nzcq.onrender.com/api/items_create/
    Body: {
            "sku": "BWax",
            "name": "Beeswax",
            "category": "raw Materials",
            "tags": "cart, dollar",
            "stock_status": "0",
            "in_stock": 8875,
            "available_stock": 0
        }
    token:984fa52fa98626687c50c5227cd4e8036b0166ab   
```



