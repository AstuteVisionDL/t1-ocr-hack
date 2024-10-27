# T1 OCR 

## Как запустить сервис

Clone repository (with git lfs)
```
git clone 
```

```shell
docker-compose up
```
Фронтенд откроётся по ссылке http://localhost:5173/
Бэкенд доступен по ссылке http://localhost/
Документация доступна по ссылке http://localhost/docs


## Альтернатива запуска для дебага (если не работает docker compose up)

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
