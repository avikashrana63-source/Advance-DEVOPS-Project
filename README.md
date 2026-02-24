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

Description what happen in Part-1
PART 1 PROJECT – Linux System Setup & Security
1. Creating a New System User (devopsuser)
Why: In Linux, it is a security best practice to avoid using the root account for daily operations.
Creating a separate user like 'devopsuser' ensures accountability, better security, and role-based
access control.
How: The command used:
sudo adduser devopsuser
This command:- Creates a home directory at /home/devopsuser- Assigns a unique UID (User ID)- Creates a private group for the user- Sets password and user details
What Happens Internally:
Linux updates system files:- /etc/passwd → Stores user account information- /etc/shadow → Stores encrypted password- /etc/group → Stores group membership details
2. Configuring Proper Permissions
Why: Linux is a multi-user operating system. Permissions control who can read, write, or execute
files.
Permission Types:
r (read), w (write), x (execute)
Example:
chmod 775 directory_name
Meaning:
Owner: read, write, execute
Group: read, write, execute
Others: read, execute
Ownership can be changed using:
chown devopsuser:devopsuser filename
Security Principle:
Least Privilege — Users should only have access necessary to perform their tasks.
3. Enabling and Configuring UFW Firewall
Why: Firewall protects the system by controlling incoming and outgoing network traffic.
We used UFW (Uncomplicated Firewall).
Commands:
sudo ufw allow 22
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
Explanation:
22 → SSH (remote login)
80 → HTTP (web traffic)
443 → HTTPS (secure web traffic)
By allowing only these ports, we reduce attack surface and block unnecessary services.
To delete a rule:
sudo ufw delete allow 80
Security Benefit:
Prevents unauthorized network access.
4. Installing Git, Docker, and Docker Compose
Git:
Why: Version control system to manage source code and collaboration.
Install:
sudo apt install git
Docker:
Why: Containerization platform that allows packaging applications with dependencies.
Install:
sudo apt install docker.io
Docker Compose:
Used to define and run multi-container applications.
Install:
sudo apt install docker-compose-plugin
What Happens:- Docker daemon runs in background- Containers share host kernel but run isolated
5. Adding User to Docker Group
Problem:
Docker socket (/var/run/docker.sock) is owned by root and docker group.
Without permission, user gets "permission denied" error.
Solution:
sudo usermod -aG docker devopsuser
Why:
This allows non-root execution of docker commands.
Security Note:
Users in docker group effectively have root-level privileges.
6. Enabling Docker Service at Boot
Command:
sudo systemctl enable docker
Why:
Ensures Docker starts automatically when system boots.
How:
Systemd creates symbolic link in:
/etc/systemd/system/multi-user.target.wants/
This tells system to start Docker during normal multi-user mode.
Verification:
systemctl is-enabled docker
systemctl status docker
7. Verification and Testing
Commands Used:
docker --version
docker ps
groups devopsuser
systemctl status docker
These confirm:- Docker installation- User permissions- Service running status
Final Outcome:
System is secured, firewall configured, Docker operational,
and user properly configured following DevOps best practices

Part-2 commands screenshots:
<img width="1727" height="576" alt="Screenshot 2026-02-19 124520" src="https://github.com/user-attachments/assets/d00a9188-56f9-4bc7-beb2-ba38844e5bb7" />

<img width="1006" height="160" alt="Screenshot 2026-02-19 124917" src="https://github.com/user-attachments/assets/7de21026-0235-4592-a5ed-1ce619a01520" />

<img width="1743" height="542" alt="Screenshot 2026-02-19 125142" src="https://github.com/user-attachments/assets/07298de7-76dc-492e-997e-e2463216b388" />

<img width="1228" height="952" alt="Screenshot 2026-02-19 130904" src="https://github.com/user-attachments/assets/c0fe233d-7c9a-425c-9a70-c35916f551fd" />

<img width="1090" height="788" alt="Screenshot 2026-02-19 130929" src="https://github.com/user-attachments/assets/0fec9007-5240-4f93-ba23-45a889aefe9c" />

<img width="1140" height="235" alt="Screenshot 2026-02-19 132220" src="https://github.com/user-attachments/assets/19203a87-064f-4e0d-8fdf-503ff0962a9c" />

<img width="1501" height="921" alt="Screenshot 2026-02-19 132639" src="https://github.com/user-attachments/assets/83690044-c114-45e0-b85f-fd079145aed6" />

<img width="1558" height="430" alt="Screenshot 2026-02-19 132821" src="https://github.com/user-attachments/assets/3dc7ee3d-68ce-4d93-9d1b-dfa34f3d2eea" />

Description What happen in Part-2
Part-2 Project – Git & GitHub Workflow
This document explains the complete Git and GitHub workflow implemented for the
Production-Ready Multi-Container Application Deployment project. It covers what was done, how it
was done, and why each step is important in real DevOps environments.
Step 1: Repository Creation (What)
Created a remote repository named advanced-devops-project to store and manage project code
centrally.
Step 1: How
Used GitHub web interface to create a public repository without initializing README to allow local
control.
Step 1: Why
A remote repository enables collaboration, version tracking, and CI/CD integration.
Step 2: Local Repository Initialization
Initialized Git locally using git init and renamed default branch to main to follow industry standards.
Step 3: Branching Strategy
Implemented GitFlow-style branches: main, develop, feature/frontend, feature/backend to maintain
clean workflow.
Step 4: Frontend Implementation
Added interactive poem in frontend/index.html where each word plays sound on click.
Step 5: Pull Requests
Created pull requests from feature branches into develop to simulate team review workflow.
Step 6: Release Flow
Merged develop into main to represent production release process.
Step 7: Version Tagging
Created annotated tag v1.0 to mark stable release version.
Step 8: Branch Protection
Enabled protection rules on main branch to prevent direct pushes and enforce PR-based workflow.
Challenges Faced
1 Git branch not visible before first commit – understood that branches appear only after initial
commit.
2 Authentication asked for password – resolved by switching from HTTPS to SSH remote.
3 Merge conflicts understanding during PR creation.
4 Ensuring meaningful commit messages following conventional commit format.
Conclusion: The Part-2 workflow successfully demonstrates professional Git practices including
branching strategy, pull requests, tagging, and repository protection suitable for production DevOps
environments

Part-3 screenshots:

<img width="937" height="386" alt="Screenshot 2026-02-19 151655" src="https://github.com/user-attachments/assets/28f18799-c8af-4a11-9924-7ea9db708fd7" />

<img width="1022" height="337" alt="Screenshot 2026-02-19 151809" src="https://github.com/user-attachments/assets/3ff41f80-8bee-4594-b732-c7112da4c5df" />

<img width="1197" height="372" alt="Screenshot 2026-02-19 153032" src="https://github.com/user-attachments/assets/154e8bca-09ee-424a-8eb7-a1de0242289b" />

<img width="1596" height="518" alt="Screenshot 2026-02-20 122437" src="https://github.com/user-attachments/assets/2c354cd5-9e39-4cfb-bba7-1692e2388ffd" />

<img width="1141" height="781" alt="Screenshot 2026-02-20 122734" src="https://github.com/user-attachments/assets/0551003f-f91d-467d-ad72-1bd2759e805d" />

<img width="1698" height="582" alt="Screenshot 2026-02-20 124101" src="https://github.com/user-attachments/assets/982dde6f-6023-4b5f-8e8e-1ab9470bac86" />

Description what happen in Part-3
Part-3 Project: Production-Ready Multi-Container
Deployment Guide
Overview
This document explains the complete implementation of Part-3 of the Advanced DevOps Project. It
describes what was built, why each component was required, and how the system works
end-to-end.
Architecture
The system uses a multi-container Docker setup including:
• Frontend container (serves index.html)
• Backend API (Flask + Gunicorn)
• PostgreSQL database with named volume
• Nginx reverse proxy
• Custom Docker bridge network
Flow (How it works)
User → Nginx → Frontend → Backend API → Database
Why each component
• Docker Compose: orchestration of services
• Nginx: reverse proxy and single entry point
• Gunicorn: production WSGI server for Flask
• PostgreSQL: persistent structured storage
• Named Volume: keeps DB data after restart
• Healthchecks: ensure container reliability
Key Verifications Done
• Application accessible via browser
• Containers communicate over network
• Database data persists after restart
• Backend health endpoint configured
• Restart policies applied
Production Best Practices Applied
• No use of latest image tags
• Environment variables used for secrets
• Custom network isolation
• Reverse proxy implemented
• Container health monitoring enabled
Common Issues Faced
• Port 80 conflict with Apache
• Missing .env file
• Nginx config mount error
• Backend marked unhealthy before health route added
Conclusion
Part-3 successfully demonstrates a production-style multi-container deployment using Docker
Compose. The setup is scalable, maintainable, and follows DevOps best practices












