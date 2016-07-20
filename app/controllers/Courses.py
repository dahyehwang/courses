from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db

    def index(self):
        course = self.models['Course'].get_all_courses()
        return self.load_view('index.html', course=course)

    def add(self):
        if len(request.form['name']) == 0:
            flash("Please enter course name.")
            return redirect('/')

        elif len(request.form['name']) < 15:
            flash("Invalid Course Name!")
            return redirect('/')

        else:
            course_details = {
                'courses_name': request.form['name'],
                'description': request.form['description']
            }
            self.models['Course'].add_course(course_details)
            return redirect('/')

    def delete_submit(self, id):
        course = self.models['Course'].get_all_courses_by_id(id)
        return self.load_view('index2.html', course=course, id=id)

    def delete(self, id):
        course = self.models['Course'].delete_course(id)
        return redirect('/')
