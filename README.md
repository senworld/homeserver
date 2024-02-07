## homeserver

Transform your old laptop into a powerful home server!

## Overview

This project aims to repurpose an older laptop running Linux into a versatile and secure home server, capable of hosting various self-hosted applications for media management, file sharing, and more. By leveraging containerization, automation, and enhanced security measures, this setup ensures seamless operation and data protection for personal use.

## Features

- **Containerization**: Utilize Docker Compose to encapsulate services, ensuring efficient resource utilization and easy management.
- **Automated Management**: Employ Python scripts for automated management tasks, ensuring smooth operation without constant monitoring.
- **Enhanced Security**: Implement Pihole and Unbound for filtered DNS resolution, Wireguard for VPN server setup, and Syncthing for configuration backup, ensuring data privacy and protection against online threats.
- **Versatile Applications**: Host a variety of open-source applications for media management, file sharing, and more, tailored to personal needs.

## Getting Started

To set up your own home infrastructure using this project:

1. **Requirements**: All you need is a device running linux.
2. **Installation**: Clone this repository and follow the setup instructions provided in the documentation.
3. **Configuration**: Customize the Docker Compose file and Python scripts to fit your specific requirements.
4. **Deployment**: Deploy the services using Docker Compose and start enjoying your self-hosted applications!

## Documentation

Welcome to the documentation for the Home Infrastructure Self-Hosting project! This guide will walk you through setting up and configuring your own home server using an older laptop running Linux.
Table of Contents

1. Introduction
2. Requirements
3. Installation
4. Configuration
5. Deployment

#Introduction

The Home Infrastructure Self-Hosting project aims to repurpose an older laptop into a powerful home server capable of hosting various self-hosted applications. By utilizing containerization, automation, and enhanced security measures, this setup ensures seamless operation and data protection for personal use.
Requirements

Before getting started, ensure you have the following prerequisites:

- Any device running Linux
- Internet connection
- Docker & Python Installed
- Basic understanding of Linux and command-line interface

#Installation

To install the Home Infrastructure Self-Hosting project:

Clone this repository to your Linux laptop:
    
    git clone https://github.com/kurosensama/homeserver.git

#Extract

Navigate to the project directory:

    cd homeserver

Go into the folder that you want to deploy.

#Configuration

Customize the configuration files according to your specific requirements. Modify the Docker Compose file and Python scripts to add or remove services, adjust settings, and configure networking options as needed.
Deployment

To deploy the services on your home server:

Run the Docker Compose command to start the containers:

    docker compose up -d

Access the self-hosted applications using your web browser and the appropriate URLs specified in the compose file.

