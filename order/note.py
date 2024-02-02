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







def hotel_dashboard(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h = Hotel.objects.get(mobile=hotel_mobile)
        hotel_id = h.id
        cart = Cart.objects.filter(hotel_id=hotel_id)

        send_table = []
        processed_combinations = set()

        for c in cart:
            tbn = c.table_number
            th_id = c.hotel_id
            combination = (th_id, tbn)

            if combination not in processed_combinations:
                one_table = Table.objects.filter(hotel_id=th_id, table_number=tbn).first()
                if one_table:
                    send_table.append(one_table)
                    processed_combinations.add(combination)
                    print(one_table)

        data = {
            'all_table': send_table,
        }
        return render(request, 'order/hotel_dashboard.html', data)
    
    else:
        return redirect('hotel_login')
    









def hotel_dashboard (request):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hm)
        t=Cart.objects.filter(hotel_id=h.id)
        for cart_item in t:
                    total += (cart_item.price*cart_item.qty)
        context={
            'h':h,
            't':t,
            'total':total,
        }
        return render(request,'order/hotel_dashboard.html',context=context)
    else:
        return redirect('hotel_login')






def hotel_dashboard(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h = Hotel.objects.get(mobile=hotel_mobile)
        hotel_id = h.id
        cart = Cart.objects.filter(hotel_id=hotel_id)

        send_table = []
        for c in cart:
            tbn = c.table_number
            th_id = c.hotel_id
            send_table.extend(Table.objects.filter(hotel_id=th_id, table_number=tbn))
            print(send_table)

        data = {
            'all_table': send_table,
        }
        return render(request, 'order/hotel_dashboard.html', data)
    
    else:
        return redirect('hotel_login')
    























    




<div  class="container border">
   <h1 class="text-center bg"> Running Table </h1>
 </div>
   <div class="container border">
     
     <table class="table">
       <thead>
         <tr>
           <th scope="col">Table Number</th>
           <th scope="col">Waiter Name</th>
           <th scope="col">Total Amount</th>
           <th scope="col">Action</th>
         </tr>
       </thead>
       <tbody>
         {% for t in t %}
         <tr>
           <td>{{t.table.table_number}}</td>
           <td>{{t.employee.employee_name}}</td>
           <td>{{total}}</td>
           <td><button type="button" class="btn btn-primary">View</button></td>
         </tr>
         {% endfor %}
       </tbody>
     </table>
   </div>