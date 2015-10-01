from flask import Flask, render_template, request, json
from login import login
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash

__author__ = 'Lasse'

app = Flask(__name__)
# app.register_blueprint(login)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'nrg'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/showLogin")
def showLogin():
    return render_template('inloggen.html')


@app.route("/showSignUp")
def showSignUp():
    return render_template('aanmelden.html')


@app.route('/signUp', methods=['POST'])
def signUp():
    try:
        # read the posted values from the UI
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _phoneNumber = request.form['inputPhonenumber']

        # validate the received values
        if _name and _email and _password and _phoneNumber:
            conn = mysql.connect()
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',
                            (_name, _email, _hashed_password, _phoneNumber))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/validateLogin', methods=['POST'])
def validateLogin():
    try:
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        # connect to mysql

        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin', (_username,))
        data = cursor.fetchall()

        if len(data) > 0:
            if check_password_hash(str(data[0][3]), _password):
                session['user'] = data[0][0]
                return redirect('/homeUser')
            else:
                return render_template('error.html', error='Wrong Email address or Password.')
        else:
            return render_template('error.html', error='Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        con.close()


@app.route('/getHouseholdsdByUser', methods=['POST'])
def getHouseholdsdByUser():
    try:
        if session.get('user'):

            _id = request.form['userID']
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetHouseholdsByUser', (_id, _user))
            result = cursor.fetchone()
            households = []

            while result is not None:
                households.append(
                    {'Id': result[0][0], 'postcode': result[0][1], 'huisnummer': result[0][2], 'grootte': result[0][3]})
                result = cursor.fetchone()

            return json.dumps(households)
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/getDevicesByHouseHold', methods=['POST'])
def getDevicesByHouseHold():
    try:
        if session.get('user'):

            _household = session.get('householdID')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetDevicesByHousehold', (_household))
            result = cursor.fetchone()
            households = []

            while result is not None:
                households.append(
                    {'id': result[0][0], 'postcode': result[0][1], 'huisnummer': result[0][2], 'grootte': result[0][3]})
                result = cursor.fetchone()

            return json.dumps(households)
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/getDevices', methods=['GET'])
def getDevices():
    try:
        if session.get('user'):


            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_GetDevices')
            result = cursor.fetchone()
            devices = []

            while result is not None:
                devices.append(
                    {'id': result[0][0], 'naam': result[0][1], 'max': result[0][2]})
                result = cursor.fetchone()

            return json.dumps(devices)
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error=str(e))




if __name__ == "__main__":
    app.run()
