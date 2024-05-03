### School Backend API

This application is a Python backend API for managing school data. It provides endpoints for creating, updating, deleting, and fetching school information.

#### Swagger Documentation

To explore the API documentation, navigate to [/api/docs/](#).

#### Endpoints

- **Import excel file,all data will automatically inserted to database:** `POST /import/upload-file`
- **Create School:** `POST /school`
- **Update School:** `PUT /school`
- **Delete School:** `DELETE /school`
- **Fetch All Schools:** `GET /school`
- **Fetch School by ID:** `GET /school/{id}`

#### How to Run

You have three options for running this application:

1. **Running Locally:**
   - First, ensure that PostgreSQL is running. This application expects PostgreSQL to be running on port `5433`. If your PostgreSQL instance uses a different port, you can configure it in the config file located in the `config` folder, or set the environment variable `DB_PORT` accordingly.
   - install dependencies to run application locally:
     ```
     pip install -r requirements.txt
     ```
   - Example command to start the application locally:
     ```
     python app.py
     ```

2. **Using Docker:**
   - Use Docker Compose to run the application:
     ```
     docker-compose up --build
     ```
   This command will build the image and create containers to run the application. You can then access the application externally.

   **Environment Variables:**
   - For the web application:
     ```
     DB_HOST: 0.0.0.0
     DB_PORT: 5433
     DB_USER: postgres
     DB_PASSWORD: 1234
     DB_NAME: postgres
     DB_PROTOCOL: postgresql://
     ```
   - For PostgreSQL:
     ```
     POSTGRES_PASSWORD: '1234'
     ```

3. **Pulling from Docker Hub:**
   - You can also pull the image from Docker Hub directly:
     ```
     docker pull santosfefe4/eto-moy-api-school
     ```

#### Authority

- **Name:** Santos Campos
- **GitHub:** [HipsterSantos](https://github.com/HipsterSantos)
- **Email:** santoscampos269@gmail.com
- **DockerHub:** https://hub.docker.com/r/santosfefe4/eto-moy-api-school

Feel free to adjust the configuration based on your environment requirements.