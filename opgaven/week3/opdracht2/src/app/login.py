from django.core.serializers import json
from flask import render_template, session, request
from werkzeug.utils import redirect
from app import app
from app.main import mysql


@app.route("/test")
def test():
    return render_template('index.html')

@app.route("/showLogin")
def showLogin():
    return render_template('inloggen.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

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
            # _hashed_password = generate_password_hash(_password)
            cursor.callproc('sp_createUser',
                            (_name, _email, _password, _phoneNumber))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                cursor.callproc('sp_validateLogin', (_email,))
                data = cursor.fetchall()
                if _password == str(data[0][3]):
                    session['user'] = data[0][0]

                return redirect('/userHome')
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
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        # connect to mysql

        con = mysql.connect()
        cursor = con.cursor()
        cursor.callproc('sp_validateLogin', (_email,))
        data = cursor.fetchall()

        if len(data) > 0:
            if _password == str(data[0][3]):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html', error='Wrong Email address or Password.')
        else:
            return render_template('error.html', error='Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html', error=str(e))
    finally:
        cursor.close()
        con.close()
