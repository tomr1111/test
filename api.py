from flask import Flask, jsonify, request
from app.models import db, Volunteer, Role
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class VolunteerAPI(Resource):
    def get(self, volunteer_id=None):
        if volunteer_id:
            volunteer = Volunteer.query.get(volunteer_id)
            if not volunteer:
                return {'message': 'Volunteer not found'}, 404
            return jsonify(volunteer)
        volunteers = Volunteer.query.all()
        return jsonify([v.to_dict() for v in volunteers])

    def post(self):
        data = request.json
        new_volunteer = Volunteer(
            name=data['name'],
            contact_info=data['contact_info'],
            region=data['region']
        )
        db.session.add(new_volunteer)
        db.session.commit()
        return jsonify(new_volunteer.to_dict()), 201

api.add_resource(VolunteerAPI, '/volunteers', '/volunteers/<int:volunteer_id>')

if __name__ == '__main__':
    app.run(debug=True)
