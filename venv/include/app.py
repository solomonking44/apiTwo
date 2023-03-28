from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class Student(Resource):
    def get(self):
        return render_template('index.html')

    def post(self):
        return {"Content": "student"}


api.add_resource(Student, '/student')

if __name__ == '__main__':
    app.run(debug=True)

