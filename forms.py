from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField


class AddForm(FlaskForm):
    name = StringField('Name of Puppy:')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):
    id = IntegerField("Id Number of Puppy to Remove:")
    submit = SubmitField("Remove Puppy")


class AddOwnerForm(FlaskForm):
    name = StringField('Name of Owner')
    puppy_id = IntegerField('Id of the puppy you wish to adopt')
    submit = SubmitField('Add Owner')


class DeleteOwnerForm(FlaskForm):
    id = IntegerField('Id of the Owner you wish to Remove:')
    submit = SubmitField('Remove Owner')
