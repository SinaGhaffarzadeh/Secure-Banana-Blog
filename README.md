# 🍍 FastAPI RESTful Blog API (Router-Based Architecture)

This is a modular and scalable RESTful API built using **FastAPI** with a focus on clean project structure using **routers**. It includes full CRUD functionality for blogs and users, plus secure **JWT authentication** using OAuth2.

---

## 🚀 Features

- ⚙️ **Modular router-based structure**
- 📚 CRUD operations for Blogs and Users
- 🔐 JWT authentication using OAuth2PasswordBearer
- 💾 SQLite database using SQLAlchemy ORM
- 🔒 Secure password hashing with Passlib
- 🧪 Swagger UI documentation (at `/docs`)
- 🧑‍💻 Tested with Postman

---

## 📁 Project Structure

```
app/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── hashing.py
├── oauth2.py
├── token.py
├── repository/
│   ├── blog.py
│   └── user.py
└── routers/
    ├── blog.py
    ├── user.py
    └── authentication.py
```

---

## 🔧 How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. **Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Start the server:**

```bash
uvicorn app.main:app --reload
```

---

## 🔑 JWT Authentication (Step-by-Step)

1. **Register a User:**
   - `POST /user`
   - Provide `email` and `password`

2. **Login to get Token:**
   - `POST /login`
   - Use form data: `username`, `password`
   - On success, you’ll receive a **JWT access token**

3. **Authorize in Swagger UI:**
   - Click "Authorize"
   - Paste: `Bearer <your_token>`

4. **Access Protected Routes:**
   - Example: `GET /blog` now requires authorization
   - Or use Postman:
     - Add `Authorization: Bearer <your_token>` in Headers

---

## 💡 Notes

- The API uses `APIRouter` to organize endpoints.
- Business logic is offloaded to `repository` modules.
- The `oauth2.py` file handles token validation and access control.
- `token.py` handles JWT creation and decoding with `python-jose`.

---


