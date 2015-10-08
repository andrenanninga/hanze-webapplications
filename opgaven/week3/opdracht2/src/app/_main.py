from app import app
import os
from flask import Flask, render_template, request, json, redirect, session

from flask.ext.mysql import MySQL

__author__ = 'Lasse'

app.secret_key = os.urandom(24)
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


@app.route("/showSignUp")
def showSignUp():
    return render_template('aanmelden.html')


@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error='Unauthorized Access')






@app.route('/showHouseholds')
def showHouseHolds():
    try:
        if session.get('user'):
            _user = session.get('user')

            conn = mysql.connect()
            cursor = conn.cursor()

            # Get household with userID
            cursor.execute('select * from huishouden where gebruiker_fk =%s' % (_user))
            result = cursor.fetchone()

            if result is None:
                return render_template('households.html')

            # Set householdID for session
            session['householdID'] = result[0]
            household = {
                'postcode': result[3],
                'huisnummer': result[2],
                'grootte': result[1],
            }

            cursor.callproc('sp_getDevicesByUser', [_user])
            result = cursor.fetchall()

            devices = []
            for idx, item in enumerate(result):
                devices.append({'id': result[idx][0], 'naam': result[idx][1],
                                'max': result[idx][2], 'merk': result[idx][3], 'type': result[idx][4]})

            return render_template('households.html', household=household, devices=devices)
        else:
            return render_template('error.html', error='Unauthorized Access')

    except Exception as e:
        return json.dumps({'error': str(e)})
    finally:
        cursor.close()
        conn.close()


@app.route('/getDevicesByHouseHold', methods=['POST'])
def getDevicesByHouseHold():
    try:
        if session.get('user'):

            _household = session.get('householdID')

            conn = mysql.connect()
            cursor = conn.cursor()

            getDevicesQuery = 'SELECT * FROM huishouden WHERE gebruiker_fk =%s'
            cursor.execute(getDevicesQuery, _household)
            result = cursor.fetchone()
            households = []

            while result is not None:
                households.append(
                    {'id': result[0][0], 'postcode': result[0][1],
                     'huisnummer': result[0][2], 'grootte': result[0][3]})
                result = cursor.fetchone()

            return json.dumps(households)
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/showAddDevice')
def showAddDevice():
    return render_template('addDevice.html')


@app.route('/getDevices', methods=['POST'])
def getDevices():
    try:
        if session.get('user'):

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_getDeviceById')
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



#
# Add Devices to the household
#

@app.route('/addDevice', methods=['POST'])
def addDevice():
    try:
        # if session.get('user'):
        _name = request.form['inputName']
        _brand = request.form['inputBrand']
        _type = request.form['inputType']
        _huishouden = '64'

        if _name and _brand and _type:

            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.callproc('sp_addDevice', (_name, _brand, _type, _huishouden))
            result = cursor.fetchall()
            if len(result) is 0:
                conn.commit()
                return redirect('/showAddDevice')
            else:
                return render_template('error.html',error = 'An error occurred!')
        # else:
        #     return render_template('error.html', error='Unauthorized Access')

        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

    except Exception as e:
        return render_template({'': str(e)})



#
# Add Devices to the household
#
@app.route('/addDeviceToHousehold', methods=['POST'])
def addDeviceToHousehold():
    try:
        if session.get('user'):
            return redirect('/showHouseHolds')
        else:
            return json.dumps({'status': 'An Error occured'})
    except Exception as e:
        return json.dumps({'error': str(e)})

@app.route('/removeDeviceById', methods=['POST'])
def removeDeviceById():
    try:
        if session.get('user'):
            _input = request.form['inputDelete']
            _household = session.get('householdID')

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                'delete from apparaat_huishouden where apparaat_fk = %s '
                'and huishouden_fk = %s' % (_input, _household))
            result = cursor.fetchall()

            if len(result) is 0:
                conn.commit()
                return redirect('/showHouseholds')
            else:
                return json.dumps({'status': 'An Error occured'})
        else:
            return render_template('error.html', error='Unauthorized Access')
    except Exception as e:
        return json.dumps({'error': str(e)})
