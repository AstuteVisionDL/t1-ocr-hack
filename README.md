# T1 OCR 

## Как запустить сервис

```shell
docker-compose up
```
Фронтенд откроётся по ссылке http://localhost:5173/
Бэкенд доступен по ссылке http://localhost/
Документация доступна по ссылке http://localhost/docs


## Альтернатива запуска для дебага

Бэк
```shell
cd ocr 
poetry install
python app/main.py
```

Фронтенд
```shell
cd frontend
npm install
npm run dev
```
