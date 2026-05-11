# 🚀 Деплой Tennis Predictor

## Пошаговая инструкция

### 1. Supabase (База данных)

1. Зарегистрируйтесь на [supabase.com](https://supabase.com)
2. Создайте новый проект
3. Перейдите в SQL Editor
4. Скопируйте содержимое `supabase/init.sql` и выполните
5. Скопируйте `Project URL` и `anon public key` из Settings → API

### 2. Render (Backend) — Подробная инструкция

#### Шаг 1: Регистрация на Render

1. Откройте [render.com](https://render.com)
2. Нажмите **"Get Started for Free"** или **"Sign Up"**
3. Выберите **"Sign up with GitHub"** (рекомендуется) или создайте аккаунт по email
4. Авторизуйтесь через GitHub, если выбрали этот вариант

#### Шаг 2: Создание нового Web Service

1. После входа в Dashboard нажмите кнопку **"New +"** в верхнем правом углу
2. В выпадающем меню выберите **"Web Service"**
3. Вам предложат подключить репозиторий:
   - Если вы уже подключили GitHub аккаунт, вы увидите список ваших репозиториев
   - Найдите ваш репозиторий с проектом (например, `tennis-predictor`)
   - Нажмите **"Connect"** рядом с ним
   - Если репозитория нет в списке, нажмите **"Configure account"** и выберите репозиторий для доступа

#### Шаг 3: Настройка Web Service

Заполните форму создания сервиса:

| Поле | Значение |
|------|----------|
| **Name** | `tennis-predictor-api` (или любое другое уникальное имя) |
| **Region** | Выберите ближайший к вам (например, `Frankfurt` для Европы) |
| **Branch** | `main` (или `master`) |
| **Root Directory** | `tennis_predictor` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r backend/requirements.txt` |
| **Start Command** | `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT` |
| **Instance Type** | `Free` (бесплатный тариф) |

**Важно:**
- **Root Directory** — это папка внутри репозитория, где находится ваш backend код
- **$PORT** — переменная Render, не меняйте её
- На бесплатном тарифе сервис "засыпает" после 15 минут бездействия (первый запрос будет медленным)

#### Шаг 4: Добавление переменных окружения

1. На странице создания сервиса прокрутите вниз до секции **"Environment Variables"**
2. Нажмите **"Add Environment Variable"**
3. Добавьте следующие переменные (каждую отдельно):

| Ключ | Значение | Описание |
|------|----------|----------|
| `DATABASE_URL` | `postgresql://postgres.aaairrmmjggxijnjgccl:Qlsjfapg25!@aws-0-eu-north-1.pooler.supabase.com:6543/postgres` | URL вашей базы данных Supabase |
| `SECRET_KEY` | Сгенерируйте случайную строку (например, `my-super-secret-key-12345`) | Ключ для шифрования JWT токенов |
| `TELEGRAM_BOT_TOKEN` | Токен от @BotFather (получите на шаге 4) | Токен Telegram бота |
| `MINI_APP_URL` | `https://your-username.github.io/tennis-predictor/frontend/` | URL фронтенда (после шага 3) |
| `DEBUG` | `false` | Отключает режим отладки |
| `SUPABASE_URL` | `https://aaairrmmjggxijnjgccl.supabase.co` | Project URL от Supabase |
| `SUPABASE_ANON_KEY` | Ваш anon public key (JWT токен) | Ключ для доступа к Supabase API |

**Как добавить переменную:**
1. Нажмите **"Add Environment Variable"**
2. В поле **Key** введите имя (например, `DATABASE_URL`)
3. В поле **Value** вставьте значение
4. Нажмите **"Add"**
5. Повторите для каждой переменной

#### Шаг 5: Создание сервиса

1. Проверьте все настройки ещё раз
2. Нажмите кнопку **"Create Web Service"** внизу страницы
3. Render начнёт сборку (Build) — это займёт 2-5 минут
4. Вы увидите логи сборки в реальном времени
5. После успешной сборки сервис будет доступен по URL: `https://tennis-predictor-api.onrender.com`

#### Шаг 6: Проверка

1. Перейдите по URL вашего сервиса: `https://<your-app-name>.onrender.com`
2. Проверьте health endpoint: `https://<your-app-name>.onrender.com/health`
3. Проверьте API документацию: `https://<your-app-name>.onrender.com/docs`

#### Возможные ошибки и решения

| Ошибка | Решение |
|--------|---------|
| `ModuleNotFoundError` | Проверьте, что все зависимости в `requirements.txt` |
| `Connection refused` | Проверьте `DATABASE_URL` и доступность Supabase |
| `Port not found` | Убедитесь, что в Start Command используется `$PORT` |
| Build failed | Проверьте логи сборки, возможно проблема в `requirements.txt` |

### 3. GitHub Pages (Frontend) — Подробная инструкция

#### Шаг 1: Установка Git (если ещё не установлен)

**Проверка:** Откройте терминал (Command Prompt) и введите:
```bash
git --version
```
Если видите версию — Git установлен. Если нет — скачайте с [git-scm.com](https://git-scm.com/download/win)

#### Шаг 2: Создание репозитория на GitHub

1. Откройте [github.com](https://github.com) и войдите в аккаунт
2. Нажмите **"+"** в верхнем правом углу → **"New repository"**
3. Заполните форму:
   - **Repository name:** `tennis_predictor`
   - **Public** (бесплатно)
   - **НЕ ставьте галочку** "Add a README file"
4. Нажмите **"Create repository"**
5. Скопируйте URL: `https://github.com/diman2384/tennis_predictor.git`

#### Шаг 3: Настройка Git на компьютере

Откройте терминал и выполните (один раз):
```bash
git config --global user.name "diman2384"
git config --global user.email "ваш@email.com"
```

#### Шаг 4: Загрузка кода на GitHub

Откройте терминал в папке `c:\WORK\CRM` и выполните по очереди:

```bash
# Инициализация Git
git init

# Добавить все файлы
git add .

# Создать коммит
git commit -m "Initial commit: Tennis Predictor"

# Связать с GitHub
git remote add origin https://github.com/diman2384/tennis_predictor.git

# Переименовать ветку
git branch -M main

# Загрузить на GitHub
git push -u origin main
```

**Если запросит пароль при push:**
Нужен **Personal Access Token** вместо пароля:
1. Откройте [github.com/settings/tokens](https://github.com/settings/tokens)
2. **"Generate new token"** → **"Generate new token (classic)"**
3. Название: "Git Push", галочка: **"repo"**
4. Нажмите **"Generate token"**, **скопируйте токен**
5. Используйте токен вместо пароля

#### Шаг 5: Включение GitHub Pages

1. Откройте репозиторий: `https://github.com/diman2384/tennis_predictor`
2. Нажмите **"Settings"** (вкладка вверху)
3. В левом меню: **"Pages"**
4. В разделе **"Build and deployment"**:
   - **Source:** `Deploy from a branch`
   - **Branch:** `main`
   - **Folder:** `/ (root)`
   - Нажмите **"Save"**
5. Подождите 1-2 минуты
6. Ваш сайт: `https://diman2384.github.io/tennis_predictor/`

#### Шаг 6: Проверка

Откройте: `https://diman2384.github.io/tennis_predictor/frontend/demo.html`

#### Шаг 7: Обновление MINI_APP_URL на Render

1. Откройте [dashboard.render.com](https://dashboard.render.com)
2. Выберите ваш Web Service → **"Environment"**
3. Измените `MINI_APP_URL` на:
   ```
   https://diman2384.github.io/tennis_predictor/frontend/
   ```
4. Нажмите **"Save Changes"**

### 4. Telegram Bot

1. Откройте @BotFather в Telegram
2. Отправьте `/newbot`
3. Следуйте инструкциям
4. Скопируйте токен
5. В @BotFather отправьте `/setmenubutton` и укажите URL вашего Mini App

### 5. Переменные окружения

Создайте `.env` файл на Render:
```
DATABASE_URL=postgresql://... (из Supabase)
SECRET_KEY=your-secret-key
TELEGRAM_BOT_TOKEN=your-bot-token
MINI_APP_URL=https://your-username.github.io/tennis-predictor/frontend/
DEBUG=false
```

## Проверка

- Backend: `https://your-app.onrender.com/health`
- Frontend: `https://your-username.github.io/tennis-predictor/frontend/demo.html`
- API Docs: `https://your-app.onrender.com/docs`