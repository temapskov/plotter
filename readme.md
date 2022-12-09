# Plotter

Скрипт на Python, который отрисовывает графики на данных из CSV файла.
Получает на вход CSV файл, если в нем больше 3 колонок - считается что график будет 3D, если 3 то обычный график.

**Пример данных:**

- **x;y;group_id** (scatter plot)
- **x;y;z;group_id** (scatter 3D plot )

___

### Системные требования:

- Python 3.10 
- Git (потребуется для клонирования репозитория)

### Установка и запуск

1. Склонировать репозиторий и перейти в директорию.

```
git clone git@github.com:temapskov/plotter.git ; cd plotter
```

2. Создать виртуальное окружение и активировать его

```
python3.10 -m venv .venv
```
Активация:
```
. .venv/bin/activate
```

3. Установить зависимости

```
pip install -r requirements.txt
```

4. Запустить файл main.py, в качестве параметра передать имя файла.
```
python main.py input.csv
```

### Использование
Plotter будет доступен по локальному http адресу, указанному в консоли, вероятнее всего - это будет http://127.0.0.1:8050/

Кнопки Next и Prev для навигации между группами.

### Скриншоты

![Снимок экрана 2022-12-09 в 22.48.30](https://downloader.disk.yandex.ru/preview/228fd9296904ecb7afcff2fc50e984c52f6c29c60c6bf27e4d78bf9e9758bd64/6393cbcf/Jde04pTzavkgJ1XLLYpcuv4CzPJasEsmHjiD3cuMl45c9RI4XurXbWGGqm2qe-cNvcHWaScSgTi8uXMtC9tyzQ%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-12-09%20%D0%B2%2022.48.30.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2880x1414)

![](https://4.downloader.disk.yandex.ru/preview/497140d98bc2c7cd9696758bf32468f92c60b3486111934fdf983735529ad6f6/inf/Nie0Ed24Ddye7St5USv5BP4CzPJasEsmHjiD3cuMl45yEB4STOIqYFbWx5zakYF-gU4ewY0xfW3sGOfZzjgc1A%3D%3D?uid=116051647&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-12-09%20%D0%B2%2022.47.57.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=116051647&tknv=v2&size=2880x1414)

![Снимок экрана 2022-12-09 в 22.47.57](https://downloader.disk.yandex.ru/preview/4037104867c23c1a60bf0bbb237c985abc49c32c5f4b8560502adb7a944b9451/6393cc53/Nie0Ed24Ddye7St5USv5BP4CzPJasEsmHjiD3cuMl45yEB4STOIqYFbWx5zakYF-gU4ewY0xfW3sGOfZzjgc1A%3D%3D?uid=0&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202022-12-09%20%D0%B2%2022.47.57.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2880x1414)

