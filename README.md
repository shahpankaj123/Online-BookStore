# Bookstore Project

## Overview

Welcome to the Bookstore Project, a web application built using Django! This project aims to create an online bookstore where users can browse, search, and purchase books. It includes features such as user authentication, a shopping cart, and order processing.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication:** Users can create accounts, log in, and log out. Authenticated users have access to additional features such as the ability to view order history.

- **Book Catalog:** The application provides a catalog of books with details such as title, author, and price. Users can browse the catalog, search for specific books, and view detailed information about each book.

- **Shopping Cart:** Authenticated users can add books to their shopping cart. The shopping cart allows users to review their selected items, update quantities, and proceed to checkout.

- **Order Processing:** The application supports the processing of orders. Users can place orders, view their order history, and receive confirmation emails.

## Installation

To run the Bookstore Project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/bookstore-project.git
    ```

2. Change to the project directory:

    ```bash
    cd bookstore-project
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:

    ```bash
    python manage.py runserver
    ```

Visit `http://127.0.0.1:8000` in your web browser to access the application.

## Usage

- Access the admin interface by visiting `http://127.0.0.1:8000/admin` and log in with the superuser account.
- Use the catalog to browse and search for books.
- Add books to the shopping cart and proceed to checkout.
- View order history in the user account section.

## Contributing

Contributions are welcome! If you would like to contribute to the project, please follow the [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.
