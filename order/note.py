[Unit]
Description=tejorder.com.gunicorn socket

[Socket]
ListenStream=/run/tejorder.com.gunicorn.sock

[Install]
WantedBy=sockets.target











[Unit]
Description=tejorder.com.gunicorn daemon
Requires=tejorder.com.gunicorn.socket
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/Hotel4
ExecStart=/home/ubuntu/Hotel4/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/tejorder.com.gunicorn.sock \
          hotel.wsgi:application

[Install]
WantedBy=multi-user.target



server{
    listen 80;
    listen [::]:80;

    server_name tejorder.com www.tejorder.com;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/run/tejorder.com.gunicorn.sock;
    }

    

    
}





