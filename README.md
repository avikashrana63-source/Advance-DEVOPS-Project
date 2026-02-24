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

Part-1 commands scrrenshots:
<img width="948" height="498" alt="Screenshot 2026-02-18 124648" src="https://github.com/user-attachments/assets/bf1c4f73-f837-4561-a831-bec5737aa2f1" />

<img width="722" height="47" alt="Screenshot 2026-02-18 131014" src="https://github.com/user-attachments/assets/5bd7054f-8566-4aa5-9f50-23351d4ebeee" />

<img width="927" height="705" alt="Screenshot 2026-02-18 131528" src="https://github.com/user-attachments/assets/fd912065-9449-4cb9-a1de-f24a00b1d9b0" />

<img width="1052" height="308" alt="Screenshot 2026-02-18 132301" src="https://github.com/user-attachments/assets/08db10ea-9ed2-460f-8b9e-c1f7bf056fbd" />

<img width="848" height="82" alt="Screenshot 2026-02-18 132854" src="https://github.com/user-attachments/assets/bbf2ad5e-54c1-471a-8b00-2859518deb35" />

<img width="1347" height="290" alt="Screenshot 2026-02-18 134311" src="https://github.com/user-attachments/assets/d433d0a7-0eff-4f3b-822a-ff3f8c5be22e" />


