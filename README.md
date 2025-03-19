# Инструкция по применению
## Установка
``` 
$ git clone https://github.com/Grokir/Student_Conference_2025.git
```

## Запуск
Для запуска уязвимого приложения нужно:
* В файле _Dockerfile_ раскомментировать строчку с ``` ADD vuln_app . ```
* В файле _Dockerfile_ закомментировать строчку с ``` ADD sec_app . ```
* Выполнить команду ```docker-compose up --build```


Для запуска защищённого приложения нужно:
* В файле _Dockerfile_ закомментировать строчку с ``` ADD vuln_app . ```
* В файле _Dockerfile_ раскомментировать строчку с ``` ADD sec_app . ```
* Выполнить команду ```docker-compose up --build```

## Удаление
Для удаления контейнера и образа выполните команду
```
docker-compose stop
```
