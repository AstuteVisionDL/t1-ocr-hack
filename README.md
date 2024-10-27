# T1 OCR 

## Как запустить сервис

Clone repository (with git lfs)
```
git clone 
```

```shell
MAX_WORKERS=1 docker compose up
```
Фронтенд откроётся по ссылке http://localhost:5173/
Бэкенд доступен по ссылке http://localhost/
Документация доступна по ссылке http://localhost/docs

## Как обращаться к бэкенду
Чтобы сделать запрос к бэкенду (в случае если не получается воспользоваться фронтендом), можно обратиться к нему напрямую через такую команду:

```shell
curl -X POST "http://localhost/upload-document/"      -H "accept: application/json"      -H "Content-Type: multipart/form-data"      -F "file=@/home/user/0_kop_0.png"
```
Где /home/user/0_kop_0.png можно заменить на путь до вашего файла 
http://localhost - адрес бэкенда

## Альтернатива запуска для дебага (если не работает docker compose up)

Бэк
```shell
cd ocr 
poetry install
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121
python app/main.py
```

P.S. Index url должен соответствовать версии CUDA на устройстве

Фронтенд
```shell
cd frontend
npm install
npm run dev
```
