# User Dashboard

A modern and responsive user dashboard built with React, Node.js, and PostgreSQL.

## Features

*   **User Authentication:** Secure login and registration using JWTs.
*   **Profile Management:** Users can update their profile information.
*   **Data Visualization:** Interactive charts and graphs to display key metrics.
*   **Responsive Design:** Adapts seamlessly to different screen sizes.
*   **Real-time Updates:** Uses WebSockets for real-time data updates.

## Technologies Used

*   **Frontend:**
    *   React
    *   Redux (for state management)
    *   React Router
    *   Material-UI (for UI components)
    *   Chart.js (for data visualization)
    *   Socket.IO Client (for real-time communication)
*   **Backend:**
    *   Node.js
    *   Express.js
    *   PostgreSQL
    *   Sequelize (ORM)
    *   JSON Web Tokens (JWT)
    *   Bcrypt (for password hashing)
    *   Socket.IO Server (for real-time communication)

## Getting Started

### Prerequisites

*   Node.js (v16 or higher)
*   npm or yarn
*   PostgreSQL

### Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/your-username/user-dashboard.git
    cd user-dashboard
    ```

2.  Install dependencies:

    ```bash
    npm install # or yarn install
    ```

3.  Set up the database:

    *   Create a PostgreSQL database named `user_dashboard`.
    *   Update the database configuration in `server/config/config.json` with your database credentials.

4.  Run database migrations:

    ```bash
    npx sequelize db:migrate
    ```

5.  Seed the database (optional):

    ```bash
    npx sequelize db:seed:all
    ```

6.  Start the development server:

    ```bash
    npm run dev # or yarn dev (if you have nodemon configured)
    ```

    This will start both the frontend and backend development servers.  The frontend will be accessible at `http://localhost:3000` and the backend API at `http://localhost:5000`.

### Environment Variables

The following environment variables are required:

*   `JWT_SECRET`:  A secret key used to sign JWTs.  Generate a strong, random string.
*   `DATABASE_URL`: The connection string to your PostgreSQL database (if not configured in `config.json`).
*   `NODE_ENV`: Set to `production` for production deployments.

## Deployment

A typical deployment would involve:

1.  Building the frontend: `npm run build` (or `yarn build`)
2.  Serving the static frontend files from the `build` directory using a web server like Nginx or Apache.
3.  Running the Node.js backend in a production environment (e.g., using PM2 or Docker).
4.  Configuring environment variables properly for the production environment.
5.  Setting up a reverse proxy to route requests to the frontend and backend.

## API Endpoints

The backend provides the following API endpoints:

*   `POST /api/auth/register`: Register a new user.
*   `POST /api/auth/login`: Log in an existing user.
*   `GET /api/users/me`: Get the current user's profile.
*   `PUT /api/users/me`: Update the current user's profile.
*   `GET /api/data/metrics`: Get sample data metrics.

## Contributing

We welcome contributions to the User Dashboard project! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise commit messages.
4.  Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.