#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <sstream>

using namespace std;

class Book {
public:
    int id;
    string title;
    string author;
    bool taken;
    string customerName;

    Book(int id, string title, string author, bool taken = false, string customerName = "") {
        this->id = id;
        this->title = title;
        this->author = author;
        this->taken = taken;
        this->customerName = customerName;
    }
};

class Library {
private:
    vector<Book> books;
    int nextBookId;

public:
    Library() {
        nextBookId = 21;
    }

    void addBook(string title, string author) {
        Book book(nextBookId, title, author);
        books.push_back(book);
        cout << "Book added: ID " << nextBookId << ", " << title << " by " << author << endl;
        nextBookId++;
    }

    void removeBook(int id) {
        for (auto it = books.begin(); it != books.end(); ++it) {
            if ((*it).id == id) {
                if ((*it).taken) {
                    cout << "Cannot remove book with ID " << id << ". Book is currently taken." << endl;
                    return;
                }
                books.erase(it);
                cout << "Book removed: ID " << id << endl;
                return;
            }
        }
        cout << "Book not found: ID " << id << endl;
    }

    void searchBook(int id) {
        for (const auto& book : books) {
            if (book.id == id) {
                cout << "Book found: ID " << book.id << ", " << book.title << " by " << book.author << endl;
                if (book.taken) {
                    cout << "This book is currently taken by " << book.customerName << endl;
                } else {
                    cout << "This book is available" << endl;
                }
                return;
            }
        }
        cout << "Book not found: ID " << id << endl;
    }

    void markBookTaken(int id, string customerName) {
        for (auto& book : books) {
            if (book.id == id) {
                if (book.taken) {
                    cout << "Book with ID " << id << " is already taken." << endl;
                } else {
                    book.taken = true;
                    book.customerName = customerName;
                    cout << "Book with ID " << id << " is marked as taken by " << customerName << endl;
                }
                return;
            }
        }
        cout << "Book not found: ID " << id << endl;
    }

    void markBookReturned(int id) {
        for (auto& book : books) {
            if (book.id == id) {
                if (book.taken) {
                    book.taken = false;
                    book.customerName = "";
                    cout << "Book with ID " << id << " is marked as returned" << endl;
                } else {
                    cout << "Book with ID " << id << " is already available" << endl;
                }
                return;
            }
        }
        cout << "Book not found: ID " << id << endl;
    }

    void saveBooksToFile(string filename) {
        ofstream file(filename);
        if (file.is_open()) {
            for (const auto& book : books) {
                file << book.id << "," << book.title << "," << book.author << "," << book.taken << "," << book.customerName << endl;
            }
            cout << "Books saved to file: " << filename << endl;
            file.close();
        } else {
            cout << "Error opening file: " << filename << endl;
        }
    }

    void loadBooksFromFile(string filename) {
        ifstream file(filename);
        if (file.is_open()) {
            books.clear();
            string line;
            while (getline(file, line)) {
                stringstream ss(line);
                string item;
                vector<string> tokens;
                while (getline(ss, item, ',')) {
                    tokens.push_back(item);
                }
                if (tokens.size() >= 5) {
                    int id = stoi(tokens[0]);
                    string title = tokens[1];
                    string author = tokens[2];
                    bool taken = stoi(tokens[3]);
                    string customerName = tokens[4];
                    Book book(id, title, author, taken, customerName);
                    books.push_back(book);
                }
            }
            cout << "Books loaded from file: " << filename << endl;
            file.close();
        } else {
            cout << "Error opening file: " << filename << endl;
        }
    }

    void showBooks() {
        cout << "List of Books:" << endl;
        for (const auto& book : books) {
            cout << "ID: " << book.id << ", Title: " << book.title << ", Author: " << book.author;
            if (book.taken) {
                cout << ", Taken by: " << book.customerName;
            } else {
                cout << ", Available";
            }
            cout << endl;
        }
    }
};

class User {
public:
    string username;
    string password;

    User(string username, string password) {
        this->username = username;
        this->password = password;
    }
};

class LoginSystem {
private:
    map<string, string> users;

public:
    LoginSystem() {
        users["admin"] = " "; //ADD your own password
    }

    bool login(string username, string password) {
        if (users.find(username) != users.end() && users[username] == password) {
            cout << "Login successful!" << endl;
            return true;
        }

        cout << "Invalid username or password. Login failed." << endl;
        return false;
    }
};

int main() {
    Library library;
    LoginSystem loginSystem;

    cout << "Welcome to the Library Management System!" << endl;

    string username, password;
    while (true) {
        cout << "---------------------" << endl;
        cout << "Login required" << endl;
        cout << "Username: ";
        cin >> username;
        cout << "Password: ";
        cin >> password;

        if (loginSystem.login(username, password)) {
            break;
        }
    }

    // Load books from file
    library.loadBooksFromFile("books.txt");

    while (true) {
        cout << "---------------------" << endl;
        cout << "Options:" << endl;
        cout << "1. Add a book" << endl;
        cout << "2. Remove a book" << endl;
        cout << "3. Search for a book" << endl;
        cout << "4. Mark a book as taken" << endl;
        cout << "5. Mark a book as returned" << endl;
        cout << "6. Save books to file" << endl;
        cout << "7. Show books" << endl;
        cout << "8. Exit" << endl;
        cout << "---------------------" << endl;
        cout << "Enter your choice: ";

        int choice;
        cin >> choice;

        if (choice == 1) {
            cout << "Enter the title of the book: ";
            string title;
            cin.ignore();
            getline(cin, title);

            cout << "Enter the author of the book: ";
            string author;
            getline(cin, author);

            library.addBook(title, author);
        } else if (choice == 2) {
            cout << "Enter the ID of the book to remove: ";
            int id;
            cin >> id;

            library.removeBook(id);
        } else if (choice == 3) {
            cout << "Enter the ID of the book to search: ";
            int id;
            cin >> id;

            library.searchBook(id);
        } else if (choice == 4) {
            cout << "Enter the ID of the book to mark as taken: ";
            int id;
            cin >> id;

            cout << "Enter the customer name: ";
            string customerName;
            cin.ignore();
            getline(cin, customerName);

            library.markBookTaken(id, customerName);
        } else if (choice == 5) {
            cout << "Enter the ID of the book to mark as returned: ";
            int id;
            cin >> id;

            library.markBookReturned(id);
        } else if (choice == 6) {
            library.saveBooksToFile("books.txt");
        } else if (choice == 7) {
            library.showBooks();
        } else if (choice == 8) {
            cout << "Exiting the program..." << endl;
            break;
        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    return 0;
}
