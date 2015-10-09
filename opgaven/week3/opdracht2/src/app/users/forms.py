from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import Required, EqualTo, Email

class LoginForm(Form):
    email = TextField('Emailadres', [Required(), Email()])
    password = PasswordField('Wachtwoord', [Required()])

class RegisterForm(Form):
    name = TextField('Naam', [Required()])
    email = TextField('Emailadres', [Required(), Email()])
    password = PasswordField('Wachtwoord', [Required()])
    confirm = PasswordField('Wachtwoord verificatie', [
        Required(),
        EqualTo('password', message='Wachtwoord moet gelijk zijn')
    ])
    phonenumber = TextField('Telefoonnummer')