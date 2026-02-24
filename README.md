# Advance-Devops-Project
PART 1 – Linux System Setup & Security
• Create a new system user: devopsuser
• Configure proper permissions
• Enable and configure UFW firewall (allow only 22, 80, 443)
• Install Git, Docker, and Docker Compose
• Add your user to the docker group
• Enable Docker service at boot
• Provide screenshots and short explanations of system configuration

PART 2 – Git & GitHub Workflow
• Create repository: advanced-devops-project
• Implement branching strategy:

main
develop
feature/frontend
feature/backend
• Minimum 10 meaningful commits
• Create at least 2 pull requests
• Add README.md and .gitignore
• Create version tag v1.0
• Protect main branch (no direct push)
PART 3 – Multi-Container Docker Setup
Create a docker-compose setup including:
• Frontend service
• Backend API service
• Database (MySQL or PostgreSQL)
• Nginx reverse proxy
• Custom Docker network
• Named volumes for database persistence
• Environment variables using .env file
• Restart policies
• Healthchecks

Verify:
• Application accessible via browser
• Database data persists after container restart

PART 4 – Networking & Debugging
Demonstrate:
• Checking open ports
• Inspecting Docker networks
• Viewing container logs
• Understanding bridge networking and port mapping
• Explain difference between localhost and 0.0.0.0
