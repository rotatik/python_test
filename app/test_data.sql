-- Вставка тестовых данных в таблицу users
INSERT INTO users (title) VALUES ('Alice');
INSERT INTO users (title) VALUES ('Bob');
INSERT INTO users (title) VALUES ('Charlie');

-- Вставка тестовых данных в таблицу task
INSERT INTO task (user_id, description, completed, created_at) VALUES (1, 'Buy groceries', 0, '2023-10-01 10:00:00');
INSERT INTO task (user_id, description, completed, created_at) VALUES (1, 'Read a book', 1, '2023-10-02 12:00:00');
INSERT INTO task (user_id, description, completed, created_at) VALUES (2, 'Walk the dog', 0, '2023-10-03 08:30:00');
INSERT INTO task (user_id, description, completed, created_at) VALUES (3, 'Finish homework', 0, '2023-10-04 15:45:00');
INSERT INTO task (user_id, description, completed, created_at) VALUES (3, 'Go to the gym', 1, '2023-10-05 18:00:00');
