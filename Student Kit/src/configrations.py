import main
from main import *

toaster = ToastNotifier()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['UPLOADED_FILES_DEST'] = 'uploads'
db = SQLAlchemy(app)
ui = FlaskUI(app)
all_events = []
all_todos = []

all = UploadSet(name='files', extensions=('c', 'cpp', 'rb', 'go', 'js', 'html', 'java', 'css', 'scss', 'txt', 'py', 'rtf', 'odf', 'ods', 'gnumeric', 'abw', 'doc', 'docx', 'xls', 'xlsx', 'jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'csv', 'ini', 'json', 'plist', 'xml', 'yaml', 'yml', 'pdf', 'pptx'))
configure_uploads(app, all)


#database classes
class Theme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    theme = db.Column(db.String(20))


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000))
    date = db.Column(db.String(20))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    content = db.Column(db.String(1000))
    date_created = db.Column(db.DateTime)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return 'Todo ' + str(self.id)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(50))
    path = db.Column(db.String(20))