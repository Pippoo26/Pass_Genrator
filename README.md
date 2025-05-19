
# 🔐 Pass_Genrator

A simple yet powerful Python-based password generator application with a user-friendly GUI built using `tkinter`. Easily generate strong, secure passwords, store them with associated website and username/email information, and manage your credentials in one place.

## 🚀 Features

- ✅ Generate strong, random passwords
- ✅ Copy passwords to clipboard with one click
- ✅ Save login credentials (website, username/email, password)
- ✅ Retrieve saved credentials using search
- ✅ Simple and intuitive GUI using `tkinter`
- ✅ Data stored securely in a local JSON file

## 📁 Project Structure

```
Pass_Genrator/
├── main.py             # Main application file
├── data.json           # Stores saved credentials (auto-created)
└── README.md           # Project documentation
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Pippoo26/Pass_Genrator.git
   cd Pass_Genrator
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

> ✅ No external dependencies required – built using standard Python libraries.

## 💾 How Data is Stored

- All credentials are saved in `data.json` using a dictionary structure:
```json
{
  "example.com": {
    "email": "user@example.com",
    "password": "GeneratedPassword123!"
  }
}
```

## 🔐 Security Note

- This tool is for personal use. Credentials are stored in plaintext in a local `.json` file.
- If you plan to use it for sensitive data, consider adding encryption or secure storage.

## 📌 Future Improvements

- Add password strength indicator
- Encrypt stored passwords
- Add master password for access
- Export/Import credentials

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo, submit pull requests, or report issues.

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
