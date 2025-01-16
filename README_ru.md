# Документация REST API для системы управления клиентами

## Обзор
Этот API позволяет управлять клиентами, включая добавление, удаление, обновление формул клиентов, расчёт платежей на основе клиентских формул и получение списка всех клиентов. API построен с использованием Flask и использует SQLite для хранения данных.

## Базовый URL
```
http://<ip-адрес-сервера>:5000/
```

## Эндпоинты

### 1. Добавить клиента
**POST** `/add_client`

Добавляет нового клиента с указанной формулой для расчёта платежей.

#### Тело запроса
- `name` (строка, обязательно): Имя клиента.
- `formula` (строка, обязательно): Формула для расчёта платежей для клиента.

#### Пример
```json
{
    "name": "client1",
    "formula": "payment * 0.1"
}
```

#### Ответы
- `201 Created`: Клиент успешно добавлен.
  ```json
  {
      "status": "success",
      "message": "Client 'client1' added."
  }
  ```
- `400 Bad Request`: Отсутствуют обязательные параметры.
  ```json
  {
      "status": "error",
      "message": "Name and formula are required."
  }
  ```
- `409 Conflict`: Клиент уже существует.
  ```json
  {
      "status": "error",
      "message": "Client 'client1' already exists."
  }
  ```
- `500 Internal Server Error`: Ошибка сервера.

### 2. Удалить клиента
**DELETE** `/delete_client/<name>`

Удаляет существующего клиента по имени.

#### Параметр URL
- `name` (строка, обязательно): Имя клиента для удаления.

#### Ответы
- `200 OK`: Клиент успешно удалён.
  ```json
  {
      "status": "success",
      "message": "Client 'client1' deleted."
  }
  ```
- `404 Not Found`: Клиент не найден.
  ```json
  {
      "status": "error",
      "message": "Client 'client1' not found."
  }
  ```
- `500 Internal Server Error`: Ошибка сервера.

### 3. Обновить формулу клиента
**PUT** `/update_client_formula`

Обновляет формулу для существующего клиента.

#### Тело запроса
- `name` (строка, обязательно): Имя клиента.
- `new_formula` (строка, обязательно): Новая формула для клиента.

#### Пример
```json
{
    "name": "client1",
    "new_formula": "payment * 0.2"
}
```

#### Ответы
- `200 OK`: Формула успешно обновлена.
  ```json
  {
      "status": "success",
      "message": "Client 'client1' formula updated."
  }
  ```
- `400 Bad Request`: Отсутствуют параметры или некорректная формула.
  ```json
  {
      "status": "error",
      "message": "Name and new formula are required."
  }
  ```
  ```json
  {
      "status": "error",
      "message": "Formula is not correct."
  }
  ```
- `404 Not Found`: Клиент не найден.
- `500 Internal Server Error`: Ошибка сервера.

### 4. Рассчитать платёж
**POST** `/calculate_payment`

Рассчитывает платёж для указанного клиента на основе его формулы.

#### Тело запроса
- `client_name` (строка, обязательно): Имя клиента.
- `payment` (число, обязательно): Сумма для расчёта.

#### Пример
```json
{
    "client_name": "client1",
    "payment": 1000
}
```

#### Ответы
- `200 OK`: Расчёт успешен.
  ```json
  {
      "status": "success",
      "payment": 100.0,
      "formula": "payment * 0.1"
  }
  ```
- `400 Bad Request`: Отсутствуют параметры.
  ```json
  {
      "status": "error",
      "message": "Client name and amount are required."
  }
  ```
- `404 Not Found`: Клиент не найден.
- `500 Internal Server Error`: Ошибка сервера.

### 5. Получить всех клиентов
**GET** `/get_all_clients`

Получает список всех клиентов.

#### Ответы
- `200 OK`: Список клиентов успешно получен.
  ```json
  {
      "status": "success",
      "clients": [
          [1, "client1", "payment * 0.1"],
          [2, "client2", "payment * 0.2"]
      ]
  }
  ```
- `500 Internal Server Error`: Ошибка сервера.

### 6. Добавить администратора
**POST** `/add_admin`

Добавляет нового администратора.

#### Тело запроса
- `id` (строка/целое число, обязательно): Telegram ID нового администратора.

#### Пример
```json
{
    "id": "123123123"
}
```

#### Ответы
- `201 Created`: Администратор успешно добавлен.
  ```json
  {
      "status": "success",
      "message": "Admin '123213213' added."
  }
  ```
- `400 Bad Request`: Отсутствуют обязательные параметры или id не является числом.
  ```json
  {
      "status": "error",
      "message": "Admin id is required as number."
  }
  ```
- `409 Conflict`: Администратор уже существует.
  ```json
  {
      "status": "error",
      "message": "Admin '123213213' already exists."
  }
  ```
- `500 Internal Server Error`: Ошибка на сервере.

### 7. Удалить администратора
**DELETE** `/remove_client/<id>`

Удаляет существующего администратора по id.

#### Параметры URL
- `id` (строка/целое число, обязательно): Telegram ID администратора, которого нужно удалить.

#### Ответы
- `200 OK`: Администратор успешно удален.
  ```json
  {
      "status": "success",
      "message": "Admin '123213123' deleted."
  }
  ```
- `400 Bad Request`: Отсутствуют обязательные параметры или id не является числом.
  ```json
  {
      "status": "error",
      "message": "Admin id is required as number."
  }
  ```
- `404 Not Found`: Администратор не найден.
  ```json
  {
      "status": "error",
      "message": "Admin '123213213' not found."
  }
  ```
- `500 Internal Server Error`: Ошибка на сервере.

## Обработка ошибок
Все ответы об ошибках включают поле `status`, указывающее "error", и поле `message`, предоставляющее дополнительные сведения об ошибке.

## Примечания
- Убедитесь, что сервер API запущен перед отправкой запросов.
- Используйте соответствующие заголовки (`Content-Type: application/json`) для запросов с телом.
- Обрабатывайте возможные ошибки сервера и некорректные входные данные в вашем клиентском приложении.

