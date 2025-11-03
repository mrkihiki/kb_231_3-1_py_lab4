# Задания по программированию на PyQt

## Ссылки
- **Запуск приложения:** [start.py](start.py)
- **Исходные данные:**
  - [CSV-файл с результатами олимпиады](https://cloud.mail.ru/public/2Fjq/fd4yEdZuY)
  - [База данных фильмов](https://cloud.mail.ru/public/8rYA/5h2E3Novr)

## Содержание
1. [Задание №1 - Олимпиада](#task1) - [Form1.py](Form1.py)
2. [Задание №2 - Фильмы](#task2) - [Form2.py](Form2.py)
3. [Задание №3 - Рисование](#task3) - [Form3.py](Form3.py)
4. [Задание №4 - Убегающая кнопка](#task4) - [Form4.py](Form4.py)
5. [Задание №5 - Управление НЛО](#task5) - [Form5.py](Form5.py)
6. [Задание №6 - Каталог библиотеки](#task6) - [Form6.py](Form6.py)

---

<a id="task1"></a>
## Задание №1 - Олимпиада - [Form1.py](Form1.py)
**Баллы: 3**

### Описание
Программа для отображения и фильтрации результатов олимпиады из CSV-файла.

### Функциональность
- Загрузка данных из CSV-файла
- Отображение в виде таблицы с колонками: логин, ФИО, суммарный балл
- Фильтрация по номеру школы и классу
- Автоматическое определение списков школ и классов из данных
- Выделение цветом участников, занявших 1, 2 и 3 места
- Учет одинаковых баллов при определении мест

### Формат данных
Логин участника: `sh-kaluga16-**-##-@`
- `**` - номер школы
- `##` - номер класса  
- `@` - номер участника

---
<img width="787" height="594" alt="image" src="https://github.com/user-attachments/assets/98f80c25-716c-43cb-9aa6-18201de21113" />
<img width="801" height="547" alt="image" src="https://github.com/user-attachments/assets/0185e1f5-b8d5-4142-89d6-82e9d28c3863" />



<a id="task2"></a>
## Задание №2 - Фильмы - [Form2.py](Form2.py)
**Баллы: 3**

### Описание
Программа для работы с базой данных фильмов.

### Функциональность
- Просмотр данных из таблицы `Films` базы данных `films_db.sqlite`
- Добавление, изменение и удаление записей
- Отображение текстового названия жанра
- Динамическое получение названий полей из БД
- Отдельные окна для добавления и редактирования
- Валидация пользовательского ввода:
  - Проверка отрицательной длины
  - Проверка года в будущем
- Обработка ошибок пользователя

<img width="757" height="609" alt="image" src="https://github.com/user-attachments/assets/86756931-8c8f-467a-bf3e-7028e99897fc" />
<img width="183" height="115" alt="image" src="https://github.com/user-attachments/assets/66b653a2-293a-4a49-bb7a-1786fab77e1e" />
<img width="792" height="619" alt="image" src="https://github.com/user-attachments/assets/758ac395-1f63-4953-9828-6cfc95c403ea" />
<img width="276" height="111" alt="image" src="https://github.com/user-attachments/assets/9395eb66-3073-4399-a3fa-595a1d31f31e" />



---

<a id="task3"></a>
## Задание №3 - Рисование - [Form3.py](Form3.py)
**Баллы: 2**

### Описание
Программа для рисования фигур на форме.

### Управление
- **Левая кнопка мыши** - круг в месте курсора
- **Правая кнопка мыши** - квадрат в месте курсора  
- **Пробел** - треугольник в месте курсора

### Особенности
- Произвольные размеры и цвета фигур
- Сохранение рисунков не требуется

<img width="795" height="624" alt="image" src="https://github.com/user-attachments/assets/0ffdd380-9bfd-4bdc-94f8-81b43b161710" />


---

<a id="task4"></a>
## Задание №4 - Убегающая кнопка - [Form4.py](Form4.py)
**Баллы: 2**

### Описание
Программа "Убегающая кнопка".

### Механика
- Кнопка перемещается при приближении курсора мыши
- Кнопка не выходит за границы формы

<img width="785" height="618" alt="image" src="https://github.com/user-attachments/assets/89613b29-b410-4b83-9fa5-4cca3cd826f7" />
<img width="789" height="609" alt="image" src="https://github.com/user-attachments/assets/0307f04c-f289-4fa5-854b-27f8a7fb6bbd" />


---

<a id="task5"></a>
## Задание №5 - Управление НЛО - [Form5.py](Form5.py)  [Form5.exe](Form5.exe)
**Баллы: 3**

### Описание
Программа "Управление НЛО" с телепортацией.

### Управление
- **Стрелки на клавиатуре** - перемещение НЛО
- Фиксированное расстояние перемещения
- Телепортация при выходе за границы формы

### Требования к сдаче
- Standalone приложение
- Исходный код
- Файл `requirements.txt`

<img width="796" height="622" alt="image" src="https://github.com/user-attachments/assets/b4f80d05-750b-4c37-97e1-56f4856b0c75" />
<img width="790" height="616" alt="image" src="https://github.com/user-attachments/assets/6e27ff1f-cecb-4edc-ac36-339b9885b82c" />


---

<a id="task6"></a>
## Задание №6 - Каталог библиотеки - [Form6.py](Form6.py)
**Баллы: 7**

### Описание
Приложение "Каталог библиотеки" с системой авторизации.

### Функциональность

#### Авторизация
- Форма входа и регистрации
- Уникальные логины
- Хеширование паролей
- Хранение учетных данных в БД

#### Основные функции
- Отображение книг в табличном виде с изображениями
- Поиск по автору и названию
- Полное отображение информации о книге (включая картинку)
- Добавление, изменение и удаление книг
- Стандартное изображение при отсутствии картинки

#### Хранение данных
- Название, автор, год издания, жанр, изображение
- Возможность хранения относительного пути к изображению

<img width="234" height="343" alt="image" src="https://github.com/user-attachments/assets/d1a42340-03ac-4d99-8883-3e5c208be672" />
<img width="932" height="249" alt="image" src="https://github.com/user-attachments/assets/041e2d10-3faf-49fa-aea8-cfc81d803307" />
<img width="565" height="415" alt="image" src="https://github.com/user-attachments/assets/1650dc1a-1139-4668-83e9-4055290e0f58" />
<img width="942" height="358" alt="image" src="https://github.com/user-attachments/assets/fb347ba9-bdd4-4603-b497-bb3ec12a63c9" />
<img width="940" height="256" alt="image" src="https://github.com/user-attachments/assets/6cdb0b1d-6ac7-48c9-88cd-69002b639fa9" />
<img width="941" height="202" alt="image" src="https://github.com/user-attachments/assets/5f93a8f4-93ca-4fa7-864f-879373f60e98" />




