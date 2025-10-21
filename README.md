# Factcheck App

A Flask-based fact-checking application that uses OpenAI's GPT-4 to verify claims and statements.

## Features

- 🔍 AI-powered fact-checking using GPT-4
- 🐳 Fully Dockerized for easy deployment
- 🚀 CI/CD with GitHub Actions
- 📱 Simple and intuitive web interface

## Tech Stack

- **Backend**: Flask (Python 3.11)
- **Frontend**: HTML, CSS, JavaScript
- **AI**: OpenAI GPT-4 Mini
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions

## Project Structure

```
factcheck-app/
├── .github/
│   └── workflows/
│       └── docker-publish.yml    # GitHub Actions workflow
├── backend/
│   ├── app.py                    # Flask application
│   ├── requirements.txt          # Python dependencies
│   └── .env                      # Environment variables (not in git)
├── frontend/
│   ├── index.html               # Web interface
│   └── script.js                # Frontend logic
├── Dockerfile                   # Docker build instructions
├── docker-compose.yml           # Docker Compose configuration
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## Prerequisites

- Docker and Docker Compose installed
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- (Optional) GitHub account for CI/CD
- (Optional) Docker Hub account for image registry

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/cloudcaptain9/factcheck-github-action.git
cd factcheck-app
```

### 2. Configure Environment Variables

Create a `.env` file in the `backend/` directory:

```bash
cat > backend/.env << 'EOF'
OPENAI_API_KEY=your-openai-api-key-here
TEST_MODE=false
EOF
```

Replace `your-openai-api-key-here` with your actual OpenAI API key.

### 3. Run with Docker Compose

```bash
# Build and start the application
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop the application
docker-compose down
```

### 4. Access the Application

Open your browser and navigate to:
```
http://localhost:5000
```

## Manual Docker Commands

If you prefer to use Docker directly without Compose:

```bash
# Build the image
docker build -t factcheck-app .

# Run the container
docker run -d \
  -p 5000:5000 \
  --env-file backend/.env \
  --name factcheck-app \
  factcheck-app

# View logs
docker logs -f factcheck-app

# Stop and remove
docker stop factcheck-app
docker rm factcheck-app
```

## Deployment

### Deploy from Docker Hub

After setting up GitHub Actions (see below), you can deploy from Docker Hub:

```bash
# Pull the latest image
docker pull cloudcaptain9/factcheck-github-action.git

# Run the container
docker run -d \
  -p 5000:5000 \
  -e OPENAI_API_KEY=your-key-here \
  --name factcheck-app \
  yourusername/factcheck-app:latest
```

### GitHub Actions CI/CD

The project includes automated Docker Hub deployment via GitHub Actions.

**Setup:**

1. Create a Docker Hub access token at https://hub.docker.com/settings/security

2. Add secrets to your GitHub repository:
   - Go to Settings → Secrets and variables → Actions
   - Add `DOCKERHUB_USERNAME` (your Docker Hub username)
   - Add `DOCKERHUB_TOKEN` (your access token)

3. Push to main/master branch:
   ```bash
   git push origin main
   ```

The workflow automatically builds and pushes the image to Docker Hub.

## API Endpoints

### POST `/factcheck`

Verify a claim using AI.

**Request:**
```json
{
  "claim": "The Earth is flat"
}
```

**Response:**
```json
{
  "result": "{\"verdict\": \"False\", \"reason\": \"Scientific evidence shows Earth is an oblate spheroid...\"}"
}
```

### GET `/`

Serves the web interface.

## Development

### Local Development without Docker

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd backend
pip install -r requirements.txt

# Run the application
python app.py
```

The app will be available at `http://localhost:5000`

### Project Configuration

- **Port**: The application runs on port 5000 by default
- **Debug Mode**: Enabled in development (see `app.py`)
- **Model**: Uses `gpt-4o-mini` for cost-effective fact-checking

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `TEST_MODE` | Enable test mode (true/false) | No |

## Troubleshooting

### Container won't start

```bash
# Check logs
docker logs factcheck-app

# Verify environment variables
docker exec factcheck-app env | grep OPENAI
```

### Port 5000 already in use

Change the port in `docker-compose.yml`:
```yaml
ports:
  - "8080:5000"  # Access via port 8080
```

### OpenAI API errors

- Verify your API key is correct
- Check your OpenAI account has credits
- Ensure the `.env` file is in the `backend/` directory

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Security Notes

- **Never commit `.env` files** - they contain sensitive API keys
- The `.gitignore` file prevents accidental commits of secrets
- Use environment variables for all sensitive data
- Rotate your API keys regularly

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for the GPT-4 API
- Flask framework
- Docker for containerization

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Made with ❤️ using Flask and OpenAI**
