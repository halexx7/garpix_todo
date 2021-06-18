from flask import Flask, request
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app = app, 
		  version = "1.0", 
		  title = "Name Recorder", 
		  description = "Manage names of various users of the application")

ns = api.namespace('names', description='Manage names')

model = api.model('Name Model', 
				  {'name': fields.String(required = True, 
    					  				 description="Name of the person", 
    					  				 help="Name cannot be blank.")})

list_of_names = {}

@ns.route("/<int:id>")
class MainClass(Resource):

	@ns.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	def get(self, id):
		try:
			name = list_of_names[id]
			return {
				"status": "Person retrieved",
				"name" : list_of_names[id]
			}
		except KeyError as e:
			ns.abort(500, e.__doc__, status = "Could not retrieve information", statusCode = "500")
		except Exception as e:
			ns.abort(400, e.__doc__, status = "Could not retrieve information", statusCode = "400")


	@ns.doc(responses={ 200: 'OK', 400: 'Invalid Argument', 500: 'Mapping Key Error' }, 
			 params={ 'id': 'Specify the Id associated with the person' })
	@ns.expect(model)		
	def post(self, id):
		try:
			list_of_names[id] = request.json['name']
			return {
				"status": "New person added",
				"name": list_of_names[id]
			}
		except KeyError as e:
			ns.abort(500, e.__doc__, status = "Could not save information", statusCode = "500")
		except Exception as e:
			ns.abort(400, e.__doc__, status = "Could not save information", statusCode = "400")

if __name__ == '__main__':
    app.run(debug=True)