# BNK Web Application for political candidate

This is a web application built using Django for creating and managing blog posts.

## Prerequisites

- Python 3.x
- Docker

## Getting Started

Follow these steps to set up and run the blog web application on your local machine.

### Local Development (venv)

1. Clone the repository:
   git clone https://github.com/bnk-01/l3t10-capstone1
   cd l3t10-capstone1

2. Create and activate a virtual environment:
   python3 -m venv venv
   source venv/bin/activate

3. Install the dependencies:
   pip install -r requirements.txt

4. Apply the database migrations:
   python manage.py migrate

5. Start the development server:
   python manage.py runserver

6. Open your web browser and visit http://localhost:8000 to access the blog application.

### Docker

1. Clone the repository:
   git clone https://github.com/bnk-01/l3t10-capstone1
   cd l3t10-capstone1

2. Build the Docker image:
   docker build -t l3t10-capstone1 .

3. Run the Docker container:
   docker run -p 8000:8000 l3t10-capstone1

4. Open your web browser and visit http://localhost:8000 to access the blog application.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to submit a pull request.

## License

This project was created by BNK.
