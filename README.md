## Overview

This project is a containerized web application built using Flask, Nginx, and MongoDB. The architecture consists of multiple Flask application containers behind an Nginx load balancer, 
a MongoDB container for data storage, and a data collector container that retrieves data from MongoDB and stores it on an NFS server.

## Project Structure
```sh
.
├── compose.yml                    # Docker Compose configuration
├── data_collector/                 # Data collector service
│   ├── collector.py                # Collects data from MongoDB
│   └── Dockerfile                   # Dockerfile for the collector
├── flask-mongoDB-App/               # Flask application
│   ├── app.py                       # Main Flask app
│   ├── Dockerfile                   # Dockerfile for Flask app
│   ├── req.txt                      # Python dependencies
│   ├── static/                      # Static assets (CSS, JS, images)
│   │   └── css/
│   │       └── styles.css
│   └── templates/                   # HTML templates
│       └── index.html
└── /etc/nginx/conf.d/loadbalancer.conf  # Nginx Load Balancer Configuration
```
