from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo

class LoginForm(Form):
	user_name = TextField('user_name', validators=[Required(), Email(message=u'Invalid email address')])
	#Not an encrypted PasswordField
	password = PasswordField('password', validators=[Required()])

class SignupForm(Form):
	user_name = TextField('user_name', validators = [Required(), Email(message=u'Invalid email address')])
	password = PasswordField('password', validators = [Required(), EqualTo('confirm_password', message='Passwords must match')])
	confirm_password = PasswordField('confirm_password', validators = [Required()])