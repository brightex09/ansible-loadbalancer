# 🌀 Ansible-Driven NGINX Load Balancer with Flask Upstream Servers

This project demonstrates how to use **Ansible** to configure a **NGINX-based Load Balancer** that distributes traffic to multiple **Flask-based upstream application servers** using the **round-robin** algorithm.

---

## 📌 Project Objectives

✅ Provision a Load Balancer on a dedicated VM instance  
✅ Configure NGINX using **Ansible** only, not the manual setup
✅ Implement a **round-robin algorithm** for traffic distribution  
✅ Setup **5 Flask application servers** as upstreams  
✅ Deploy a tiny Flask app on each upstream server  
✅ Flask app must:
- Display **which server** received the request
- Show a list of **all currently online upstream servers**

---

## 🗂️ Project Structure

- Created 6 EC2 instance on AWS, used one as loadbalancer VM and the other 5 as the flask-based upstream servers
- Obtained the ips of EC2 instances which was used in creating the inventory file
- Create other file; ansible config file, app-deploy.yaml (playbook to deploy and run flask app on upstreams), loadbalancer-setup.yaml (to configure Nginx load balancer on localhost)
- flask-app; contains the neccessary files and codes for app development
- nginx.conf.j2; jinja template for Nginx configuration
