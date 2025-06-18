# 🔐 Vigenère Cipher GUI

A modern, user-friendly desktop application for encrypting and decrypting text using the classic Vigenère cipher algorithm. Built with Python and CustomTkinter for a sleek, contemporary interface.

## ✨ Features

- **🔒 Text Encryption & Decryption**: Secure your messages using the Vigenère cipher with custom keys
- **💾 Database Storage**: Automatically save encrypted messages to a local SQLite database
- **📋 Message Management**: View and decrypt all previously saved messages
- **🎨 Modern UI**: Beautiful, responsive interface built with CustomTkinter
- **🔑 Key Validation**: Ensures encryption keys contain only alphabetic characters
- **📝 Smart Text Handling**: Preserves numbers, punctuation, and spacing while encrypting only letters
- **ℹ️ Educational Info**: Built-in explanation of how the Vigenère cipher works

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/vigenere-cipher-gui.git
   cd vigenere-cipher-gui
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

## 📁 Project Structure

```
vigenere-cipher-app/
├── app.py              # Main GUI application
├── cipher.py           # Vigenère cipher encryption/decryption logic
├── db.py              # SQLite database operations
├── requirements.txt   # Python dependencies
├── messages.db        # SQLite database (created automatically)
└── README.md         # Project documentation
```

## 🔧 How It Works

### The Vigenère Cipher

The Vigenère cipher is a polyalphabetic substitution cipher that uses a keyword to encrypt text. Each letter in the plaintext is shifted by a different amount based on the corresponding letter in the key.

**Example:**
- **Key:** LEMON
- **Message:** ATTACK
- **Encrypted:** LXFOPV

### Application Workflow

1. **Enter your secret key** (letters only, A-Z)
2. **Input your message** in the text area
3. **Choose an action:**
   - **Encrypt & Save**: Encrypts your message and stores it in the database
   - **Decrypt Text**: Decrypts the text in the input area using the provided key
   - **Load Messages**: Displays all saved encrypted messages with their decrypted versions
   - **About Vigenère**: Shows information about how the cipher works

## 🎯 Usage Examples

### Encrypting a Message
1. Enter a key like "SECRET"
2. Type your message: "Hello World!"
3. Click "Encrypt & Save"
4. The encrypted result appears in the output area and is saved to the database

### Decrypting a Message
1. Enter the same key used for encryption
2. Paste the encrypted text in the message area
3. Click "Decrypt Text"
4. The original message appears in the output area

### Viewing Saved Messages
1. Click "Load Messages"
2. All previously encrypted messages will be displayed with:
   - Message ID
   - Encrypted text
   - Key used
   - Decrypted plaintext

## 🛠️ Technical Details

### Dependencies
- **customtkinter**: Modern UI framework for Python
- **sqlite3**: Built-in Python database library (no additional installation needed)

### Key Features of the Implementation

- **Input Validation**: Ensures keys contain only alphabetic characters
- **Case Preservation**: Maintains original capitalization in encrypted text
- **Non-alphabetic Character Handling**: Numbers, spaces, and punctuation pass through unchanged
- **Database Persistence**: All encrypted messages are stored locally for future reference
- **Error Handling**: User-friendly error messages for invalid inputs

### Security Notes

⚠️ **Important**: This is an educational implementation of the Vigenère cipher. While historically significant, the Vigenère cipher is not secure by modern cryptographic standards and should not be used for protecting sensitive information in real-world applications.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎓 Educational Purpose

This application was created as part of SWE4356 coursework to demonstrate:
- GUI development with Python
- Database integration
- Cryptographic algorithm implementation
- Software engineering best practices
- Code organization and modularity

## 📞 Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.

---

**Happy Encrypting!** 🔐✨
