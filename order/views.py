from django.shortcuts import render ,redirect , HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q 
from django.http import JsonResponse
from datetime import date

# Create your views here.
def index(request):
    #Cart.objects.all().delete()
    #NewCart.objects.all().delete()
    #OrderMaster.objects.all().delete()
    #OrderDetail.objects.all().delete()
    context={}
    orders=OrderDetail.objects.all().count()
    orders+=13000
    context={
        'orders':orders
    }
    print(orders)
    return render (request,'order/hotel/index.html',context)







# Sunil Code 


def sunil_login(request):
    if request.method == 'POST':
        a =int(request.POST["mb"])
        b =int(request.POST["pin"])
        s = a+b
        if s == 10000 :
            request.session['sunil_mobile'] = s
            return redirect('sunil_dashboard')
        else:
            return redirect('sunil_login')
    return render(request,'order/sunil/sunil_login.html')

def marketing_employee(request):
    if request.session.has_key('sunil_mobile'):
        e=Marketing_Employee.objects.all()
        context={
            'e':e
        }
        if request.method == "POST":
            if "Add" in request.POST:
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                #validatin
                if Marketing_Employee.objects.filter(employee_mobile=employee_mobile).exists():
                    messages.success(request,"Employee Allready Exits")
                else:
                    Marketing_Employee(
                        employee_name=employee_name,
                        employee_address=employee_address,
                        employee_mobile=employee_mobile,
                        pin=pin,
                    ).save()
                    messages.success(request,"Employee Edit Succesfully") 
            elif "Edit" in request.POST:
                id=request.POST.get('id')
                employee_name=request.POST.get('employee_name')
                employee_address=request.POST.get('employee_address')
                employee_mobile=request.POST.get('employee_mobile')
                pin=request.POST.get('pin')
                #print(id)
                Marketing_Employee(
                    id=id,
                    employee_name=employee_name,
                    employee_address=employee_address,
                    employee_mobile=employee_mobile,
                    pin=pin,
                ).save()
                messages.success(request,"Employee Edit Succesfully") 
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Marketing_Employee.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Marketing_Employee.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                #print(id)
                ac=Marketing_Employee.objects.get(id=id)
                ac.status='1'
                ac.save()                                                
        return render(request,'order/sunil/marketing_employee.html',context)
    else:   
        return redirect('sunil_login')

def sunil_dashboard(request):
    if request.session.has_key('sunil_mobile'):
        context={}
        o=Cart.objects.all().order_by('-added_date')
        context={
            'o':o
        }
        return render(request,'order/sunil/sunil_dashboard.html',context)
    else:   
        return redirect('sunil_login')

# marketing Employee Code

def marketing_employee_login(request):
    if request.method == "POST":
        mb=request.POST ['mb']
        pin=request.POST ['pin']
        s= Marketing_Employee.objects.filter(employee_mobile=mb,pin=pin,status=1)
        if s:
            request.session['marketing_employee_mobile'] = request.POST["mb"]
            return redirect('hotel')
        else:
            messages.success(request,"please insert correct information")            
            return redirect('marketing_employee_login')
    return render(request,'order/sunil/marketing_employee_login.html')




def hotel (request):
    if request.session.has_key('marketing_employee_mobile'):
        mk = request.session['marketing_employee_mobile']
        m=Marketing_Employee.objects.get(employee_mobile=mk) 
        marketing_employee_id=m.id
        h=Hotel.objects.filter(marketing_employee_id=marketing_employee_id)
        context={
            'm':m,    
            'marketing_employee_id':marketing_employee_id,
            'h':h
        }
        if request.method == "POST":
            if "Add" in request.POST:
                marketing_employee_id=request.POST.get('employee_id')
                hotel_name=request.POST.get('hotel_name')
                owner_name=request.POST.get('owner_name')
                hotel_address=request.POST.get('hotel_address')
                mobile=request.POST.get('mobile')
                pin=request.POST.get('pin')
                #validatin
                if Hotel.objects.filter(mobile=mobile).exists():
                    messages.success(request,"Hotel Allready Exits")
                else:
                    Hotel(
                        marketing_employee_id=marketing_employee_id,
                        hotel_name=hotel_name,
                        owner_name=owner_name,
                        hotel_address=hotel_address,
                        mobile=mobile,
                        pin=pin
                    ).save()
            elif "Edit" in request.POST:
                marketing_employee_id=request.POST.get('employee_id')
                hotel_name=request.POST.get('hotel_name')
                owner_name=request.POST.get('owner_name')
                hotel_address=request.POST.get('hotel_address')
                mobile=request.POST.get('mobile')
                pin=request.POST.get('pin')
                hotel_id=request.POST.get('hotel_id')
                Hotel(
                    marketing_employee_id=marketing_employee_id,
                    hotel_name=hotel_name,
                    owner_name=owner_name,
                    hotel_address=hotel_address,
                    mobile=mobile,
                    pin=pin,
                    id=hotel_id                
                    ).save()
                messages.success(request,"Hotel Edit Succesfully") 
        return render(request,'order/sunil/hotel.html',context=context)
    else:
        return redirect('marketing_employee_login')
    

# end Sunil Code
    


# Login Code 
    
def login (request):
    if request.session.has_key('hotel_mobile'):
        return redirect('hotel_dashboard')
    if request.session.has_key('waiter_mobile'):
        return redirect('waiter_dashboard')
    if request.session.has_key('chef_mobile'):
        return redirect('chef_dashboard')
    else:
        if request.method == "POST":
            mb=request.POST ['mb']
            pin=request.POST ['pin']
            s= Hotel.objects.filter(mobile=mb,pin=pin,status=1)
            if s:
                request.session['hotel_mobile'] = request.POST["mb"]
                return redirect('hotel_dashboard')
            e= Employee.objects.filter(employee_mobile=mb,pin=pin,status=1,department='waiter')
            if e:
                request.session['waiter_mobile'] = request.POST["mb"]
                return redirect('waiter_dashboard')
            e= Employee.objects.filter(employee_mobile=mb,pin=pin,status=1,department='chef')
            if e:
                request.session['chef_mobile'] = request.POST["mb"]
                return redirect('chef_dashboard')
            else:
                messages.success(request,"please insert correct information or call more suport 9730991252")            
                return redirect('login')
    return render(request,'order/login.html')



def logout (request):
    del request.session['hotel_mobile']
    return redirect('/')


def waiter_logout(request):
    del request.session['waiter_mobile']
    return redirect('/')

def chef_logout(request):
    del request.session['chef_mobile']
    return redirect('/')






# Hotel Code Start


def hotel_dashboard(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        context={}
        hl = Hotel.objects.filter(mobile=hotel_mobile).first()
        
        if hl:
            h = Hotel.objects.get(mobile=hotel_mobile)
            e=Employee.objects.filter(hotel_id=h.id).count()
            d=Dish.objects.filter(hotel_id=h.id).count()
            t=Table.objects.filter(hotel_id=h.id).count()
            o=OrderMaster.objects.filter(hotel_id=h.id).count()
            total=0

            total_amount=OrderDetail.objects.filter(hotel_id=h.id,date__gte=date.today(),date__lte=date.today())
            for total_amount in total_amount:
                temp=(total_amount.qty*total_amount.price)
                total+=temp
            context={
                'h':h,
                'e':e,
                'd':d,
                't':t,
                'o':o,
                'total':total
            }
        return render(request, 'order/hotel/hotel_dashboard.html',context)
    
    else:
        return redirect('login')
    


def employee(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        context={}
        hl=Hotel.objects.filter(mobile=hotel_mobile).first()
        if hl:
            h=Hotel.objects.get(mobile=hotel_mobile)
            e=Employee.objects.filter(hotel_id=h.id)
            context={
                'h':h,
                'e':e
            }
            if request.method == "POST":
                if "Add" in request.POST:
                    hotel_id=request.POST.get('hotel_id')
                    employee_name=request.POST.get('employee_name')
                    employee_address=request.POST.get('employee_address')
                    employee_mobile=request.POST.get('employee_mobile')
                    pin=request.POST.get('pin')
                    department=request.POST.get('department')
                    #validatin
                    if Employee.objects.filter(employee_mobile=employee_mobile).exists():
                        messages.success(request,"Employee Allready Exits")
                    else:
                        Employee(
                            hotel_id=hotel_id,
                            employee_name=employee_name,
                            employee_address=employee_address,
                            employee_mobile=employee_mobile,
                            pin=pin,
                            department=department,
                            added_by=h.hotel_name,
                        ).save()
                        messages.success(request,"Employee Edit Succesfully") 
                elif "Edit" in request.POST:
                    hotel_id=request.POST.get('hotel_id')
                    id=request.POST.get('id')
                    employee_name=request.POST.get('employee_name')
                    employee_address=request.POST.get('employee_address')
                    employee_mobile=request.POST.get('employee_mobile')
                    pin=request.POST.get('pin')
                    department=request.POST.get('department')
                    #print(id)
                    Employee(
                        hotel_id=hotel_id,
                        id=id,
                        employee_name=employee_name,
                        employee_address=employee_address,
                        employee_mobile=employee_mobile,
                        pin=pin,
                        department=department,
                        added_by=h.hotel_name,
                    ).save()
                    messages.success(request,"Employee Edit Succesfully") 
                elif "Delete" in request.POST:
                    id=request.POST.get('id')
                    Employee.objects.get(id=id).delete()
                    messages.success(request,"Category Delete Successfully")
                elif "Active" in request.POST:
                    id=request.POST.get('id')
                    #print(id)
                    ac=Employee.objects.get(id=id)
                    ac.status='0'
                    ac.save()
                elif "Deactive" in request.POST:
                    id=request.POST.get('id')
                    #print(id)
                    ac=Employee.objects.get(id=id)
                    ac.status='1'
                    ac.save()                                                
        return render(request,'order/hotel/employee.html',context=context)
    else:   
        return redirect('login')



def table(request):
    if request.session.has_key('hotel_mobile'):
        request.session.has_key('hotel_mobile')
        hotel_mobile = request.session['hotel_mobile']
        context={}
        hl=Hotel.objects.filter(mobile=hotel_mobile).first()
        if hl:
            h=Hotel.objects.get(mobile=hotel_mobile)
            t=Table.objects.filter(hotel_id=h.id)
            context={
                't':t,
                'h':h,       
            }
            if request.method == "POST":
                if "Add" in request.POST:
                    
                    t=Table.objects.filter(hotel_id=h.id).count()
                    t+=1
                    hotel_id = request.POST.get('hotel_id')
                    Table(
                        table_number=t,
                        hotel_id=hotel_id
                    ).save()
                    messages.success(request,"Table Added Succesfully")
                elif "Delete" in request.POST:
                    id=request.POST.get('id')
                    Table.objects.get(id=id).delete()
                    messages.success(request,"Table Delete Successfully")
                elif "Active" in request.POST:
                    id=request.POST.get('id')
                    ac=Table.objects.get(id=id)
                    ac.status='0'
                    ac.save()
                elif "Deactive" in request.POST:
                    id=request.POST.get('id')
                    ac=Table.objects.get(id=id)
                    ac.status='1'
                    ac.save()            
        return render(request,'order/hotel/table.html',context=context)
    else:
        return redirect('login')

    
def dish_category(request):
    if request.session.has_key('hotel_mobile'):
        request.session.has_key('hotel_mobile')
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        dc=Dish_category.objects.filter(hotel_id=h.id)
        context={
            'dc':dc,
            'h':h,       
        }
        if request.method == "POST":
            if "Add" in request.POST:
                name=request.POST.get('name')
                hotel_id = request.POST.get('hotel_id')
                Dish_category.objects.create(
                    category_name=name,
                    hotel_id=hotel_id
                )
                messages.success(request,"Category Added Succesfully")
            elif "Edit" in request.POST:
                name=request.POST.get('name')
                id=request.POST.get('id')
                edit_category=Dish_category.objects.get(id=id)
                edit_category.category_name=name
                edit_category.save()
                messages.success(request,"Category Edit Successfully")
            elif "Delete" in request.POST:
                id=request.POST.get('id')
                Dish_category.objects.get(id=id).delete()
                messages.success(request,"Category Delete Successfully")
            elif "Active" in request.POST:
                id=request.POST.get('id')
                ac=Dish_category.objects.get(id=id)
                ac.status='0'
                ac.save()
            elif "Deactive" in request.POST:
                id=request.POST.get('id')
                ac=Dish_category.objects.get(id=id)
                ac.status='1'
                ac.save()            
        return render(request,'order/hotel/dish_category.html',context=context)
    else:
        return redirect('login')




def dish(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        dc=Dish_category.objects.filter(hotel_id=h.id,status=1)
        d=Dish.objects.filter(hotel_id=h.id).order_by('-dish_category_id')
        context={
            'c':dc,
            'h':h,
            'd':d       
        }
        if "Add" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_marathi_name=request.POST.get('dish_marathi_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            hotel_id=request.POST.get('hotel_id')
            Dish(
                dish_name=dish_name,
                dish_marathi_name=dish_marathi_name,
                dish_category_id=dish_category_id,
                price=price,
                hotel_id=hotel_id,

            ).save()
            messages.success(request,"Dish Added Succesfully")
        elif "Edit" in request.POST:
            dish_name=request.POST.get('dish_name')
            dish_marathi_name=request.POST.get('dish_marathi_name')
            dish_category_id=request.POST.get('dish_category_id')
            price=request.POST.get('price')
            hotel_id=request.POST.get('hotel_id')
            dish_id=request.POST.get('dish_id')
            Dish(
                dish_name=dish_name,
                dish_marathi_name=dish_marathi_name,
                dish_category_id=dish_category_id,
                price=price,
                hotel_id=hotel_id,
                id=dish_id
            ).save()
            messages.success(request,"Dish Edit Succesfully")            
        elif "Delete" in request.POST:
            dish_id=request.POST.get('dish_id')
            Dish.objects.get(id=dish_id).delete()
            messages.success(request,"Dish Delete Successfully")
        elif "Active" in request.POST:
            id=request.POST.get('id')
            ac=Dish.objects.get(id=id)
            ac.status='0'
            ac.save()
        elif "Deactive" in request.POST:
            id=request.POST.get('id')
            ac=Dish.objects.get(id=id)
            ac.status='1'
            ac.save()            
        return render(request,'order/hotel/dish.html',context=context)
    else:
        return redirect('login')
    




def running_table(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        data={}
        hl = Hotel.objects.filter(mobile=hotel_mobile).first()
        if hl:
            h = Hotel.objects.get(mobile=hotel_mobile)
            hotel_id = h.id
            table=Table.objects.filter(hotel_id=hotel_id,status=1)
            cart = Cart.objects.filter(hotel_id=hotel_id).order_by('table_id')

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
                        #print(one_table)

            data = {
                'all_table': send_table,
                'table':table,
                'h':h
            }
        return render(request, 'order/hotel/running_table.html', data)
    
    else:
        return redirect('login')
    



def change_color(request):
    if request.method == 'GET':
        hotel_id = request.GET['hotel_id']
        c=Cart.objects.values().filter(hotel_id=hotel_id)
        cart=[]
        if c:
            cart=list(c)
                
        return JsonResponse({'status': 1,'cart':cart})
    else:
        return JsonResponse({'status': 0})



def view_order(request,id):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        hotel=Hotel.objects.get(mobile=hm)
        ng=len(Cart.objects.filter(hotel_id=hotel.id,table_id=id))
        dish_category=Dish_category.objects.filter(hotel_id=hotel.id,status=1).order_by('category_name')
        cart=Cart.objects.filter(hotel_id=hotel.id,table_id=id).order_by('dish_id')
        table=Table.objects.get(id=id)
        amount=0
        if "Delete" in request.POST:
            cart_id=request.POST.get('cart_id')
            if Cart.objects.filter(id=cart_id).exists():
                Cart.objects.get(id=cart_id).delete()
        ct=Cart.objects.filter(hotel_id=hotel.id,table_id=id)
        if ct:
            for tb in ct:
                tempamount=(tb.qty*tb.price)
                amount+=tempamount
                #print(amount)

        return render(request,'order/hotel/view_order.html',{'cart':cart,'table':table,'hotel':hotel,'dish_category':dish_category,'amount':amount,'ng':ng})
    else:
        return redirect('login')
    




def filter_by_category(request):
    if request.method == 'GET':
        dish_category_id = request.GET['dish_category_id']
        hotel_id = request.GET['hotel_id']
        filter_result = Dish.objects.values().filter(dish_category_id=dish_category_id,hotel_id=hotel_id,status=1).order_by('dish_marathi_name')
        dish = list(filter_result)
        #print(dish)
        return JsonResponse({'status': 1, 'dish': dish})
    else:
        return JsonResponse({'status': 0})
    

def dish_filter(request):
    if request.method == 'GET':
        filter_data = request.GET['filter']
        hotel_id = request.GET['hotel_id']
        filter_result = Dish.objects.values().filter(dish_name__icontains=filter_data,hotel_id__icontains=hotel_id,status=1)
        dish = list(filter_result)
        #print(dish)
        return JsonResponse({'status': 1, 'dish': dish})
    else:
        return JsonResponse({'status': 0})



def add_to_cart(request):
    if request.method == 'GET':
        hotel_id = request.GET['hotel_id']
        table_id = request.GET['table_id']               
        dish_id = request.GET['dish_id']
        qty = request.GET['qty']
        price = request.GET['price']
        note = request.GET['note']
        table_number = request.GET['table_number']
        total_price = request.GET['total_price']
        d=Dish.objects.get(id=dish_id)
        Cart(
            dish_id=dish_id,
            dish_marathi_name=d.dish_marathi_name,
            hotel_id=hotel_id,
            table_id=table_id,            
            qty=qty,
            price=price,
            note=note,
            total_price=total_price,
            table_number=table_number
            ).save()
        cart=Cart.objects.values().filter(hotel_id=hotel_id,table_id=table_id).order_by('dish_id')
        cart=list(cart)
        ng=len(cart)
        print(ng)
        c=Cart.objects.filter(hotel_id=hotel_id,table_id=table_id)
        total_amount=0
        if c:
            for c in c:
                tempamount=(c.qty*c.price)
                total_amount+=tempamount
                #print(total_amount)
        return JsonResponse({'status': 1,'cart':cart,'total_amount':total_amount,'ng':ng})
    else:
        return JsonResponse({'status': 0})


def remove_cart(request):
    if request.method == 'GET':
        id = request.GET['id']
        if Cart.objects.filter(id=id).exists():
                Cart.objects.get(id=id).delete()
        return JsonResponse({'status': 1,})
    else:
        return JsonResponse({'status': 0})


def merge_card(request,table_id,hotel_id):
    cart_item=Cart.objects.filter(hotel_id=hotel_id,table_id=table_id)
    if cart_item :
        for c in cart_item:
            dish_id=c.dish_id
            d=Cart.objects.filter(hotel_id=hotel_id,table_id=table_id,dish_id=dish_id)
            new_qty=0
            new_dish_id=0
            new_total_price=0
            if d:
                for d in d:
                    new_dish_id=d.dish_id
                    qty=d.qty
                    total_price=d.total_price
                    new_total_price+=total_price
                    new_qty+=qty
                NewCart(
                    dish_id=new_dish_id,
                    dish_marathi_name=d.dish_marathi_name,
                    hotel_id=d.hotel_id,
                    table_id=d.table_id,            
                    qty=new_qty,
                    price=d.price,
                    note=d.note,
                    total_price=new_total_price,
                    table_number=d.table_number
                    ).save()
                Cart.objects.filter(hotel_id=hotel_id,table_id=table_id,dish_id=d.dish_id).delete()
    return redirect(f'/place_order/{table_id}')      





def place_order(request,id):
    hotel_mobile = request.session['hotel_mobile']
    h=Hotel.objects.get(mobile=hotel_mobile)
    hotel_id=h.id
    f=OrderMaster.objects.filter(hotel_id=hotel_id).count()
    #print(f)
    f+=1
    amount=0
    c=NewCart.objects.filter(hotel_id=hotel_id,table_id=id)
    if c:
        for c in c:
            
            qty=c.qty
            price=c.price
            t=(qty*price)
            amount+=t
            table_number=c.table_number
            dish_name=c.dish.dish_name
            total_price=c.total_price
        OrderMaster(
            hotel_id=hotel_id,
            table_id=id,
            order_filter=f,
            total_price=amount
            ).save()
        cart=NewCart.objects.filter(hotel_id=hotel_id,table_id=id)
        for cart in cart:
            qty=cart.qty
            price=cart.price
            table_number=cart.table_number
            dish_marathi_name=cart.dish.dish_marathi_name
            total_price=cart.total_price
            OrderDetail(
                hotel_id=hotel_id,
                dish_id=cart.dish_id,
                table_number=table_number,
                dish_marathi_name=dish_marathi_name,
                qty=qty,price=price,
                total_price=total_price,
                order_filter=f
                ).save()
            NewCart.objects.filter(hotel_id=hotel_id,table_id=id).delete()
    return redirect(f'/complate_view_order/{f}')



def complate_view_order(request,id):
    if request.session.has_key('hotel_mobile'):
        hm = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hm)
        hotel_id=h.id
        od=OrderDetail.objects.filter(hotel_id=hotel_id,order_filter=id)
        total=0
        context={}
        if od :
            for t in od:
                total += (t.price*t.qty)
                table_number=t.table_number
                date=t.ordered_date
                bill_number=t.order_filter
            context={
                'h':h,
                'od':od,
                'total':total,
                'table_number':table_number,
                'date':date,
                'bill_number':bill_number
            }
        return render(request,'order/hotel/complate_view_order.html',context)
    else:
        return redirect('login')
    



def complate_order(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        hotel_id=h.id
        m=OrderMaster.objects.filter(hotel_id=hotel_id).order_by('-order_filter')
        context={
            'm':m
        }
        return render(request, 'order/hotel/complate_order.html',context)
    else:
        return redirect('login')
    




def daily_report(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        hotel_id=h.id
        dc=Dish.objects.filter(hotel_id=hotel_id).order_by('dish_category')        
        result={}
        total=0
        qty=0
      
        if "Search" in request.POST:
            fromdate=request.POST.get('fromdate')
            todate=request.POST.get('todate')
            dish_id=request.POST.get('dish_id')
            #print(dish_id)
            result=OrderDetail.objects.filter(hotel_id=hotel_id,date__gte=fromdate,date__lte=todate,dish_id=dish_id)
            if result:
                for r in result:
                    total +=r.total_price
                    qty +=r.qty            
            if dish_id == '0':
                result=OrderDetail.objects.filter(hotel_id=hotel_id,date__gte=fromdate,date__lte=todate)
                if result:
                    for r in result:
                        total +=r.total_price
                        qty +=r.qty
            

        return render(request, 'order/hotel/daily_report.html',{'result':result,'dc':dc,'total':total,'qty':qty,'h':h})
    
    else:
        return redirect('login')
    

def profile(request):
    if request.session.has_key('hotel_mobile'):
        hotel_mobile = request.session['hotel_mobile']
        h=Hotel.objects.get(mobile=hotel_mobile)
        context={}
        if "Edit" in request.POST:
            hotel_name=request.POST.get('hotel_name')
            owner_name=request.POST.get('owner_name')
            hotel_address=request.POST.get('hotel_address')
            pin=request.POST.get('pin')
            hotel_id=request.POST.get('hotel_id')
            e=Hotel.objects.get(id=hotel_id)
            e.hotel_name=hotel_name
            e.owner_name=owner_name
            e.hotel_address=hotel_address
            e.pin=pin
            e.save()
            messages.success(request,"Hotel Edit Succesfully") 
            h=Hotel.objects.get(mobile=hotel_mobile)
        context={
            'h':h
        }
        return render(request, 'order/hotel/profile.html',context)
    else:
        return redirect('login')

# Waiter Code Start 




def waiter_dashboard (request):
    if request.session.has_key('waiter_mobile'):
        wm = request.session['waiter_mobile']
        context={}
        wh=Employee.objects.filter(employee_mobile=wm).first()
        if wh:
            w=Employee.objects.get(employee_mobile=wm) 
            h=Hotel.objects.get(id=w.hotel_id)
            t=Table.objects.filter(hotel_id=w.hotel_id,status=1) 
            #pravin Code


            table=Table.objects.filter(hotel_id=h.id,status=1)        
            cart = Cart.objects.filter(hotel_id=h.id).order_by('table_id')
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
                        #print(one_table)







            context={
                'w':w,    
                't':t,
                'h':h,
                'running_table':send_table
            }
        return render(request,'order/waiter/waiter_dashboard.html',context=context)
    else:
        return redirect('login')
    

def waiter_add_order(request,id):
    if request.session.has_key('waiter_mobile'):
        wm = request.session['waiter_mobile']
        w=Employee.objects.get(employee_mobile=wm)
        h=Hotel.objects.get(id=w.hotel_id)  
        dish_category=Dish_category.objects.filter(hotel_id=w.hotel_id,status=1).order_by('category_name')
        t=Table.objects.get(id=id)        
        cart=Cart.objects.filter(hotel_id=w.hotel_id,table_id=id).order_by('dish_id')
        ng=len(Cart.objects.filter(hotel_id=w.hotel_id,table_id=id))
        context={
            'w':w,    
            't':t,
            'dc':dish_category,
            'h':h,
            'cart':cart,
            'ng':ng
        }
        if "Delete" in request.POST:
            cart_id=request.POST.get('cart_id')
            if Cart.objects.filter(id=cart_id).exists():
                Cart.objects.get(id=cart_id).delete()
        return render(request,'order/waiter/waiter_add_order.html',context=context)
    else:
        return redirect('login')
    
def remove_cart_waiter(request):
    if request.method == 'GET':
        id = request.GET['id']
        if Cart.objects.filter(id=id,status='Pending').exists():
                Cart.objects.get(id=id,status='Pending').delete()
        return JsonResponse({'status': 1,})
    else:
        return JsonResponse({'status': 0})

# Chef Code Start
    


def chef_dashboard(request):
    if request.session.has_key('chef_mobile'):
        cf = request.session['chef_mobile']
        context={}
        e=Employee.objects.filter(employee_mobile=cf).first()
        if e:
            d=Cart.objects.filter(hotel_id=e.hotel_id,cook_status=0).order_by('dish_id')
            tcount=Cart.objects.filter(hotel_id=e.hotel_id,cook_status=0).count()
            Accepted_dish=Cart.objects.filter(hotel_id=e.hotel_id,cook_status=1,chef_id=e.id,status='Accepted').order_by('dish_id')
            Delivered_dish=Cart.objects.filter(hotel_id=e.hotel_id,chef_id=e.id,status='Delivered')
            #print(e.id)
            context={
                'e':e,
                'd':d,
                'p':Accepted_dish,
                'Delivered_dish':Delivered_dish,
                'tcount':tcount
            }   
            if "Accepted" in request.POST:
                id=request.POST.get('id')
                chef_id=request.POST.get('chef_id')
                if Cart.objects.filter(id=id).exists():           
                    c=Cart.objects.get(id=id)
                    c.chef_id=chef_id
                    c.cook_status='1'
                    c.status='Accepted'
                    c.save()
                messages.success(request,"You Accepted this Dish for Processing")            
            elif "Delivered" in request.POST:
                id=request.POST.get('id')
                chef_id=request.POST.get('chef_id')
                if Cart.objects.filter(id=id).exists():  
                    c=Cart.objects.get(id=id)
                    c.chef_id=chef_id
                    c.cook_status='1'
                    c.status='Delivered'
                    c.save()
                messages.success(request,"You Accepted this Dish for Processing") 
                d=Cart.objects.filter(hotel_id=e.hotel_id,cook_status=0)

        return render(request,'order/chef/chef_dashboard.html',context=context)
    else:
        return redirect('login')


def multiple_select(request):
    if request.method == 'GET':
        hotel_id = request.GET['hotel_id']
        dish_id = request.GET['dish_id']
        chef_id = request.GET['chef_id']        
        cart=Cart.objects.filter(hotel_id=hotel_id,dish_id=dish_id,status='Pending',cook_status=0)
        cook_status='1'
        status='Accepted'
        if cart:
            for c in cart:
                id=c.id
                Cart(
                        id=id,
                        qty=c.qty,
                        status=status,
                        dish_id=c.dish_id,
                        hotel_id=c.hotel_id,
                        table_id=c.table_id,
                        cook_status=cook_status,
                        chef_id=chef_id,
                        note=c.note,
                        price=c.price,
                        total_price=c.total_price,
                        table_number=c.table_number,
                        dish_marathi_name=c.dish_marathi_name,

                        ).save()
    return JsonResponse({'status': 1,})                    



def multiple_order(request):
    if request.method == 'GET':
        hotel_id = request.GET['hotel_id']
        c=Cart.objects.filter(hotel_id=hotel_id,cook_status=0)
        for c in c:
            i=c.dish_id
            #print(i)
            cart=Cart.objects.values().filter(hotel_id=hotel_id,cook_status=0)
            cart=list(cart)    

        return JsonResponse({'status': 1,'cart':cart})                    



def test(request):
    total_amount=OrderDetail.objects.filter(hotel_id=1,date__gte=date.today(),date__lte=date.today())
    total=0
    for total_amount in total_amount:
        temp=(total_amount.qty*total_amount.price)
        total+=temp
    test=date.today()
    return render(request,'order/test.html',{'test':total})