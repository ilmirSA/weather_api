# weather-api
Получает погоду по указанному городу и прибовляет его к балансу либо уменьаешт его взависимости от выбранного метода api


# Как запустить
Перейдите в папку с кодом.
* Создайте виртуальное окружение


```python
python3 -m venv venv
```
или
```python
python -m venv venv
```

* Активируйте виртуальное окружение следующей командой

```python
source venv/bin/activate - для Linux 
```

* Установите зависимости следующей командой

  

```python
pip install -r requirements.txt
```

  
 

# Запуск скрипта

  Запустите скрипт следующей командой.
```python
 gunicorn -w 4 -b 0.0.0.0:5000 app:app
```
Примеры запросов в [Postman](https://www.postman.com/altimetry-astronaut-55219238/workspace/weather-api/request/28935355-6ad1c2e7-43d2-4e6c-94c2-b1303fea85de)

  

