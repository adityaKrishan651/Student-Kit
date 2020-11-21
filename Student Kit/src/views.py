import configrations
from configrations import *

def main():
    @app.route('/')
    def home():
        theme = Theme.query.all()[0].theme
        return render_template('home.html', theme=theme)


    @app.route('/note/<int:id>')
    def note(id):
        theme = Theme.query.all()[0].theme
        note = Note.query.filter_by(id=id).one()
        return render_template("note.html", note=note, theme=theme)


    @app.route('/notes/edit/<int:id>', methods=['POST'])
    def editNote(id):
        note = Note.query.get_or_404(id)
        if request.method == 'POST':
            note.content = request.form['content']
            db.session.commit()

            return redirect('/notes')


    @app.route('/notes/delete/<int:id>')
    def delete_note(id):
        note = Note.query.get_or_404(id)
        db.session.delete(note)
        db.session.commit()
        return redirect('/notes')


    @app.route('/add_note', methods=["GET", "POST"])
    def add_note():
        theme = Theme.query.all()[0].theme
        if request.method == "POST":
            title = request.form['title']
            content = request.form['content']
            note = Note(title=title, content=content, date_created=datetime.now())
            db.session.add(note)
            db.session.commit()

            return redirect(url_for("notes"))
        return render_template("add_note.html", theme=theme)


    @app.route('/notes')
    def notes():
        notes = Note.query.order_by(Note.date_created.desc()).all()
        theme = Theme.query.all()[0].theme

        return render_template("notes.html", notes=notes, theme=theme)


    @app.route('/todos', methods=['GET', 'POST'])
    def todo():
        theme = Theme.query.all()[0].theme
        if request.method == 'POST':
            todo_new = request.form['todo']
            new_todo = Todo(todo=todo_new)
            db.session.add(new_todo)
            db.session.commit()

            return redirect('/todos')

        elif request.method == 'GET':
            all_todos = Todo.query.order_by(Todo.date_posted).all()
            return render_template('todo.html', todos=all_todos, db=Todo, theme=theme)


    @app.route('/todos/new', methods=['POST'])
    def new_todo():
        theme = Theme.query.all()[0].theme
        if request.method == 'POST':
            todo_new = request.form['todo']
            new_todo = Todo(todo=todo_new)
            db.session.add(new_todo)
            db.session.commit()

            return redirect('/todos')


    @app.route('/todos/delete/<int:id>', methods=['POST', 'GET'])
    def delete(id):
        todo = Todo.query.get_or_404(id)
        db.session.delete(todo)
        db.session.commit()

        return redirect('/todos')


    @app.route('/upload', methods=["POST", "GET"])
    def upload():
        files = File.query.all()
        theme = Theme.query.all()[0].theme
        if request.method == "POST":
            filename = all.save(request.files['file'])
            path = "uploads/" + filename
            files = File(file_name=filename, path=path)
            db.session.add(files)
            db.session.commit()
            files = File.query.all()
            return render_template("upload.html", files=files, theme=theme)
        return render_template("upload.html", files=files, theme=theme)


    @app.route('/upload/download/<int:id>', methods=['GET', 'POST'])
    def download(id):
        file_ = File.query.get_or_404(id)

        return send_file(file_.path, as_attachment=True, attachment_filename=file_.file_name)

    @app.route('/upload/delete/<int:id>', methods=['GET', 'POST'])
    def delete_file(id):
        if request.method == 'GET':
            file = File.query.get_or_404(id)
            db.session.delete(file)
            db.session.commit()

            if os.path.exists(file.path):
                os.remove(file.path)
            else:
                pass
        return redirect('/upload')


    @app.route('/events', methods=['GET', 'POST'])
    def allEvents():
        theme = Theme.query.all()[0].theme
        if request.method == 'POST':
            title = request.form['title']
            date = request.form['date']
            new_event = Event(title=title, date=date)
            db.session.add(new_event)
            db.session.commit()

            return redirect('/events')
        else:
            all_events = Event.query.all()
            return render_template('calendar.html', events=all_events, theme=theme)


    @app.route('/calculator')
    def cal():
        theme = Theme.query.all()[0].theme
        return render_template('calculator.html', theme=theme)


    @app.route('/clock', methods=['GET'])
    def clock():
        theme = Theme.query.all()[0].theme
        if request.method == 'GET':
            res = requests.get(secrets.URL)
            data = res.json()

            temp = data['main']['temp']
            wind_speed = data['wind']['speed']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
            city = data['name']

            return render_template("clock.html", theme=theme, city=city, icon=icon, temperature=temp, wind_speed=wind_speed, humidity=humidity, description=description)

    @app.route('/change_theme', methods=['POST'])
    def change_theme():
        theme = Theme.query.get_or_404(1)
        if request.method == 'POST':
            if theme.theme == 'dark':
                theme.theme = 'light'
                db.session.commit()
            elif theme.theme == 'light':
                theme.theme = 'dark'
                db.session.commit()
        return redirect('/')