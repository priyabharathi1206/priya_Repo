from flask import Flask,render_template,request,url_for,redirect
from flask_mysqldb import MySQL

app=Flask(__name__)
#app.secret_key ='pri'

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="kGISL"
app.config["MYSQL_DB"]="fkiteissue"
app.config["MYSQL_CURSORCLASS"]="DictCursor"
conn=MySQL(app)


@app.route('/',methods = ['GET','POST'])
def index():
   return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
   if (request.method =='POST'):
      rollno=request.form['rollno']
      password=request.form['password']
      con=conn.connection.cursor()
      # query = "Select * from register "
      # con.execute(query)
      # id_column = con.fetchall()
      # print(id_column)
      # pass_column = con.fetchall()
      # if(rollno in id_column and password in pass_column):
      sql="insert into login(rollno,password) values(%s,%s)"
      
      con.execute(sql,(rollno,password))
      con.connection.commit()
      con.close()
      return render_template('complaint.html')
   return render_template('login.html')

@app.route('/about',methods = ['GET','POST'])
def about():
   return render_template('about.html')

@app.route('/contact',methods = ['GET','POST'])
def contact():
   return render_template('contact.html')

@app.route('/complaint',methods = ['GET','POST'])
def complaint():

   return render_template('complaint.html')

@app.route('/admin',methods = ['GET','POST'])
def admin():
   return render_template('admin.html')

@app.route('/cleanliness',methods=['GET','POST'])
def cleanliness():
   if request.method =='POST':
      issue=request.form['issue']
      date=request.form['date']
      description=request.form['description']
      image=request.files['image']
      image.save(r'C:\Users\ADMIN\Desktop\kite_issue_track\final\NAAC\ok'+image.filename)
      with open(r'C:\Users\ADMIN\Desktop\kite_issue_track\final\NAAC\ok'+image.filename,'rb')as file:
         binaryimage=file.read()

      con=conn.connection.cursor()

      # sql="INSERT INTO  clean (issue,date,description) VALUES(%s,%s,%s)"
      con.execute("INSERT INTO  clean (issue,date,description,image,binaryimage) VALUES(%s, %s, %s,%s,%s)",(issue, date, description,image,binaryimage))
      con.connection.commit()
      con.close()
      return render_template('success.html')
   return render_template('cleanliness.html')

# @app.route('/cleanliness',methods=['GET','POST'])
# def cleanliness():
#    if (request.method =='POST'):
#       issuename=request.form['issuename']
#       date=request.form['date']
#       description=request.form['description']
      
#       con=conn.connection.cursor()

#       sql="insert into login(rollno,password) values(%s,%s)"
#       con.execute(sql,(rollno,password))
#       con.connection.commit()
#       con.close()
#       return render_template('complaint.html')
#    return render_template('login.html')

# @app.route('/cleanliness',methods = ['GET','POST'])
# def cleanliness():
#     if(request.method == 'POST'):
#         issuename = request.form['issuename']
#         date = request.form['date']
#         proof = request.files['image']
#         proof.save('uploads/'+ proof.filename)
#         description = request.form['description']
#         cur = conn.connection.cursor()
#         with open('uploads/' + proof.filename,'rb') as file:
#             binaryimage= file.read()
#         cur.execute("insert into Cleanliness(issuename,date,image,description,binaryimage) values(%s,%s,%s,%s,%s)" ,(issuename,date,proof.filename,description,binaryimage) )
#         conn.connection.commit()
#         cur.close()
#         return redirect(url_for('success.html'))
#     return render_template('cleanliness.html')
    
# @app.route('/login',methods = ['GET','POST'])
# def login():
#    if request.method =='POST':
#       rollno=request.form['rollno']
#       password=request.form['password']
#       name=request.form['rolno']
#       email=request.form['email']
#       pas=request.form['pass']
#       confirmpassword=request.form['confirmpassword']

#       if (rollno !=None and password !=None):
         
#          con=conn.connection.cursor()

#          sql="insert into login(rollno,password) values(%s,%s)"
#          con.execute(sql,(rollno,password))
#          con.connection.commit()
#          con.close()
#          return render_template('complaint.html')
#       # return render_template('login.html')
   
#       elif (rolno !=None and email != None and pas != None and confirmpassword !=None):
#          con=conn.connection.cursor()
      
#          sql="insert into (name,email,pas,confirmpassword) values(%s,%s,%s,%s)"
#          con.execute(sql,(name,email,pas,confirmpassword))
#          con.connection.commit()
#          con.close()
#          return render_template('login.html')
#       return render_template('complaint.html')
#    return render_template('login.html')
   

# correct
# @app.route('/cleanliness',methods = ['GET','POST'])
# def cleanliness():
#     if(request.method == 'POST'):
#         issuename = request.form['issuename']
#         date = request.form['date']
#         proof = request.files['image']
#         proof.save('uploads/'+ proof.filename)
#         description = request.form['description']
#         cur = conn.connection.cursor()
#         with open('uploads/' + proof.filename,'rb') as file:
#             binaryimage= file.read()
#         cur.execute("insert into Cleanliness(issuename,date,image,description,binaryimage) values(%s,%s,%s,%s,%s)" ,(issuename,date,proof.filename,description,binaryimage) )
#         conn.connection.commit()
#         cur.close()
#         return redirect(url_for('success.html'))
#     return render_template('cleanliness.html')

@app.route('/canteen',methods = ['GET','POST'])
def canteen():
   if(request.method == 'POST'):
      complaint = request.form['complaint']
      date = request.form['date']
      description = request.form['description']
      cur = conn.connection.cursor()
      cur.execute("insert into Canteen(complaint,date,description) values(%s,%s,%s)" ,(complaint,date,description))
      cur.connection.commit()
      cur.close()
      return redirect(url_for('success'))
   return render_template('canteen.html')
   

@app.route('/Hostelissues',methods = ['GET','POST'])
def Hostelissues():
   if(request.method == 'POST'):
      firstname = request.form['firstname']
      email = request.form['email']
      phone = request.form['phone']
      room = request.form['room']
      cot = request.form['cot']
      description = request.form['description']
      qualityoffood = request.form['qualityoffood']
      details = request.form['details']
      
      cur = conn.connection.cursor()
      
      cur.execute("insert into hostel(firstname,email,phone,room,cot,description,qualityoffood,details) values(%s,%s,%s,%s,%s,%s,%s,%s)",(firstname,email,phone,room,cot,description,qualityoffood,details))
      cur.connection.commit()
      cur.close()
      return redirect(url_for('success'))
   return render_template('Hostelissues.html')

@app.route('/restroom',methods = ['GET','POST'])
def restroom():
   if(request.method == 'POST'):
      complaint = request.form['complaint']
      date = request.form['date']
      description = request.form['description']
      cur = conn.connection.cursor()
      
      cur.execute("insert into restroom(complaint,date,description) values(%s,%s,%s)" ,(complaint,date,description))
      cur.connection.commit()
      cur.close()
      return redirect(url_for('success'))
   return render_template('restroom.html')

@app.route('/Transportissues',methods = ['GET','POST'])
def Transportissues():
   if(request.method == 'POST'):
      issuename = request.form['issuename']
      date = request.form['date']
        
      description = request.form['description']
      cur = conn.connection.cursor()
        
      cur.execute("insert into Transport(issuename,date,description) values(%s,%s,%s)" , (issuename,date,description))
      cur.connection.commit()
      cur.close()
      return redirect(url_for('success'))
   return render_template('Transportissues.html')

@app.route('/wifiissues',methods = ['GET','POST'])
def wifiissues():
   if(request.method == 'POST'):
      name = request.form['name']
      email = request.form['email']
      macaddress = request.form['macaddress']
      otherissue = request.form['otherissue']
      con=conn.connection.cursor()
      sql="insert into wifi(name,email,macaddress,otherissue) values(%s,%s,%s,%s)"
      con.execute(sql,(name,email,macaddress,otherissue))
      con.connection.commit()
      con.close()
      # cur = conn.connection.cursor()
      # cur.execute("insert into wifiissue(name,email,macaddress,otherissue) values(%s,%s,%s,%s)" , (name,email,macaddress,otherissue))
      # cur.commit()
      # cur.close()
      return redirect(url_for('success'))
   return render_template('wifiissues.html')

@app.route('/infra',methods = ['GET','POST'])
def infra():
   if(request.method=='POST'):
      complaint = request.form['complaint']
      date = request.form['date']
      description = request.form['description']
      cur = conn.connection.cursor()
      cur.execute("insert into infra(complaint,date,description) values(%s,%s,%s)" , (complaint,date,description))
      cur.connection.commit()
      cur.close()
      return redirect(url_for('success'))
    
   return render_template('infra.html')

# @app.route('/others',methods = ['GET','POST'])
# def wifiissues():
#    if(request.method == 'POST'):
#       name = request.form['name']
#       email = request.form['email']
#       macaddress = request.form['macaddress']
#       otherissue = request.form['otherissue']
#       con=conn.connection.cursor()
#       sql="insert into wifi(name,email,macaddress,otherissue) values(%s,%s,%s,%s)"
#       con.execute(sql,(name,email,macaddress,otherissue))
#       con.connection.commit()
#       con.close()
#       # cur = conn.connection.cursor()
#       # cur.execute("insert into wifiissue(name,email,macaddress,otherissue) values(%s,%s,%s,%s)" , (name,email,macaddress,otherissue))
#       # cur.commit()
#       # cur.close()
#       return redirect(url_for('success'))
#    return render_template('wifiissues.html')


@app.route('/success',methods = ['GET','POST'])
def success():
    return render_template('success.html')
   










if __name__=='__main__':
    app.run(debug=True)