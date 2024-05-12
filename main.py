from flask import  Flask,render_template,request,redirect, url_for,flash
from flask_mysqldb import MySQL
from datetime import datetime

app=Flask(__name__,template_folder='templates')
app.secret_key = 'HHHHHHHH'


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='0000'
app.config['MYSQL_DB']='surgery'

mysql=MySQL(app)


@app.route('/')

def login():

    return render_template('log_in.html')



@app.route('/home',methods=['POST','GET'])

def home():

       return render_template('start,welcome.html')





@app.route('/patient')

def patient():
    cur=mysql.connection.cursor()
    cur.execute("SELECT*FROM patients")
    data=cur.fetchall()
    cur.close()
    return render_template('all_patients.html',patients=data)

@app.route('/add_patient', methods=['POST','GET'])
def add_patient():
    # extract data from form
    if request.method=='POST':
            patient_id = request.form['patient_id']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            birth_date = request.form['birth_date']
            gender = request.form['gender']
            address = request.form['address']
            phone = request.form['phone']
                        
            
            # insert new patient into database
            cursor = mysql.connection.cursor()
            query = "SELECT * FROM patients WHERE patient_id = %s"
            cursor.execute(query, (patient_id,))
            result = cursor.fetchone()
            
            if result:
                flash("Patient ID already exists")
            else:
                # insert new patient into database
                birth_dateobj=datetime.strptime(birth_date, '%Y-%m-%d').date()
                query = "INSERT INTO patients (patient_id,first_name, last_name, birth_date, gender, address, phone) VALUES (%s,%s, %s, %s, %s, %s, %s)"
                values = (patient_id,first_name, last_name, birth_dateobj, gender, address, phone)
                cursor.execute(query, values)
                mysql.connection.commit()

            
    # redirect back to index page
    return render_template('add_patient.html')




@app.route('/delete_patient/<string:patient_id>',methods=['POST','GET'])
def delete_patient(patient_id):
        
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM appointments WHERE patient_id=%s",(patient_id,)) 
        cursor.execute("DELETE FROM patients WHERE patient_id=%s",(patient_id,)) 
        mysql.connection.commit()

        return redirect(url_for('patient'))



#patient_appintment

@app.route('/patient_appointment/<string:patient_id>')
def patient_appointment(patient_id):
    # Query the database to get the appointments for the selected patient
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM appointments WHERE patient_id=%s",(patient_id)) 
    appointments = cursor.fetchall()
    if appointments:
        return render_template('all_appointments.html', patient_id=patient_id, appointments=appointments)
    else:
        flash("patient doesn't have appointment")
        return render_template('all_patients.html')


#-------------------------------------------------------------------------


@app.route('/surgeon')

def surgeon():
    cur=mysql.connection.cursor()
    cur.execute("SELECT*FROM surgeons")
    data=cur.fetchall()
    cur.close()
    return render_template('all_surgeons.html',surgeons=data)



@app.route('/add_surgeon', methods=['POST','GET'])
def add_surgeon():

    if request.method=='POST':

        # extract data from form
        surgeon_id = request.form['surgeon_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        specialty = request.form['specialty']
        phone = request.form['phone_number']
        e_mail = request.form['e_mail']
        
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM surgeons WHERE surgeon_id = %s"
        value = (surgeon_id,)
        cursor.execute(query, value)
        result = cursor.fetchone()

        if result:
            # surgeon_id already exists, display error message
            flash("Surgeon ID already exists.")
            return render_template('add_surgeon.html')

        else:
            # insert new surgeon into database
            query = "INSERT INTO surgeons (surgeon_id, first_name, last_name, specialty, phone_number, e_mail) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (surgeon_id, first_name, last_name, specialty, phone, e_mail )
            cursor.execute(query, values)
            mysql.connection.commit()

    # redirect back to index page
    return render_template('add_surgeon.html')



@app.route('/delete_surgeon/<string:surgeon_id>',methods=['POST','GET'])
def delete_surgeon(surgeon_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM appointments WHERE surgeon_id=%s",(surgeon_id,)) 
    cursor.execute("DELETE FROM surgeons WHERE surgeon_id=%s",(surgeon_id,)) 
    mysql.connection.commit()

    return redirect(url_for('surgeon'))





#surgeon_appointment

@app.route('/surgeon_appointment/<string:surgeon_id>')
def surgeon_appointment(surgeon_id):
    # Query the database to get the appointments for the selected surgeon
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM appointments WHERE surgeon_id=%s",(surgeon_id,)) 
    appointments = cursor.fetchall()

    if appointments:
        return render_template('all_appointments.html', surgeon_id=surgeon_id, appointments=appointments)
    else:
        flash("Surgeon doesn't have appointment")
        return render_template('all_surgeons.html')





#-------------------------------------------------------------------------


@app.route('/operation')

def operation():
    cur=mysql.connection.cursor()
    cur.execute("SELECT*FROM operations")
    data=cur.fetchall()
    cur.close()
    return render_template('all_procedure.html',operations=data)


@app.route('/add_operation', methods=['POST','GET'])
def add_operation():

    if request.method=='POST':
        # extract data from form
        operation_id = request.form['operation_id']
        operation = request.form['operation']
        describtion = request.form['describtion']
        cost = request.form['cost']
        
        
        # check if operation_id already exists in database
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM operations WHERE operation_id = %s"
        cursor.execute(query, (operation_id,))
        result = cursor.fetchone()
        
        if result:
            flash('Operation ID already exists!')
            return render_template('add_procedure.html')
            
        # insert new operation into database
        query = "INSERT INTO operations (operation_id,operation, describtion, cost) VALUES (%s,%s, %s, %s)"
        values = (operation_id,operation, describtion, cost )
        cursor.execute(query, values)
        mysql.connection.commit()
    # redirect back to index page
    return render_template('add_procedure.html')



@app.route('/delete_operation/<string:operation_id>',methods=['POST','GET'])
def delete_operation(operation_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM appointments WHERE operation_id=%s",(operation_id,))
    cursor.execute("DELETE FROM operations WHERE operation_id=%s",(operation_id,)) 
    mysql.connection.commit()

    return redirect(url_for('operation'))



#------------------------------------------------------------


@app.route('/appointment')

def appointment():
    cur=mysql.connection.cursor()
    cur.execute("SELECT*FROM appointments")
    data=cur.fetchall()
    cur.close()
    return render_template('all_appointments.html',appointments=data)





@app.route('/add_appointment', methods=['POST','GET'])
def add_appointment():

    if request.method=='POST':
        # extract data from form
        appointment_id = request.form['appointment_id']
        patient_id = request.form['patient_id']
        surgeon_id = request.form['surgeon_id']
        operation_id = request.form['operation_id']
        appointments_date_str = request.form['appointments_date']
        appointments_date = datetime.strptime(appointments_date_str, '%Y-%m-%dT%H:%M')
        operationroom_id=request.form['operationroom_id']

        
        # check if surgeon_id has an appointment at the same entered date
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM appointments WHERE surgeon_id = %s AND appointments_date = %s"
        cursor.execute(query, (surgeon_id, appointments_date))
        result = cursor.fetchone()

        #check if appointment id existed
        query = "SELECT * FROM appointments WHERE appointment_id = %s"
        cursor.execute(query, (appointment_id,))
        result2 = cursor.fetchone()
        
        #check if the operation room is reserved at the same date
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM appointments WHERE operationroom_id = %s AND appointments_date = %s"
        cursor.execute(query, (operationroom_id, appointments_date))
        result3 = cursor.fetchone()


        # check if patient_id has an appointment at the same entered date
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM appointments WHERE patient_id = %s AND appointments_date = %s"
        cursor.execute(query, (patient_id, appointments_date))
        result4 = cursor.fetchone()


        # check if patient_id exist
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM patients WHERE patient_id = %s"
        cursor.execute(query, (patient_id,))
        result5 = cursor.fetchone()

        # check if surgeon_id exist
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM surgeons WHERE surgeon_id = %s"
        cursor.execute(query, (surgeon_id,))
        result6 = cursor.fetchone()

        # check if operation_id exist
        cursor = mysql.connection.cursor()
        query = "SELECT * FROM operations WHERE operation_id = %s"
        cursor.execute(query, (operation_id,))
        result7 = cursor.fetchone()



        # display flash message
        if result:
            flash('Surgeon ID already has an appointment on the entered date!')
            return render_template('add_appointment.html')
        elif result2:
            flash('Appointment ID already exists!')
            return render_template('add_appointment.html')
        elif result3:
            flash('operation Room already reserved')
            return render_template('add_appointment.html')
        elif result4:
            flash('patient ID already has an appointment on the entered date!')
            return render_template('add_appointment.html')
        elif not result5:
            flash('patient ID doesnt exist!')
            return render_template('add_appointment.html')
        elif not result6:
            flash('surgeon ID doesnt exist!')
            return render_template('add_appointment.html')
        elif not result7:
            flash('operation ID doesnt exist!')
            return render_template('add_appointment.html')



        # insert new appointment into database
    
        query = "INSERT INTO appointments (appointment_id,patient_id, surgeon_id, operation_id ,appointments_date,operationroom_id) VALUES (%s,%s, %s, %s,%s,%s)"
        values = (appointment_id,patient_id, surgeon_id, operation_id , appointments_date_str ,operationroom_id)
        cursor.execute(query, values)
        mysql.connection.commit()
        
        # redirect back to index page
    return render_template('add_appointment.html')



@app.route('/delete_appointment/<string:appointment_id>',methods=['POST','GET'])
def delete_appointment(appointment_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM appointments WHERE appointment_id=%s",(appointment_id,)) 
    mysql.connection.commit()

    return redirect(url_for('appointment'))


app.run(debug=True)