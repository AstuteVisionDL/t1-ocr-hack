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
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121
python app/main.py
```

P.S. be sure that your Cuda version is compatible wit

Фронтенд
```shell
cd frontend
npm install
npm run dev
```
