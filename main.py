from flask import Flask, request, jsonify, session
from flask_cors import CORS
# from flask_session import Session


app = Flask(__name__, static_folder='static')
app.secret_key = 'elias'
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200/*"}}, supports_credentials=True)
# # Configure session
# app.config['SESSION_TYPE'] = 'filesystem'
# app.config['PERMANENT_SESSION_LIFETIME'] = 1200
# app.config['SESSION_USE_SIGNER'] = True
# app.config['SESSION_COOKIE_SECURE'] = True
# app.config['SESSION_COOKIE_HTTPONLY'] = True
# app.config['SESSION_COOKIE_PATH'] = '/'
# app.config['SESSION_COOKIE_SAMESITE'] = 'None'

@app.route('/api/return-hello', methods=['POST'])
def sendmsg():
    return resp('Hello', 200)



def resp(message, status):
  response = jsonify({'message': message})
  response.status_code = status
  response.headers.add('Access-Control-Allow-Headers',
                       "Origin, X-Requested-With, Content-Type, Accept, x-auth")
  response.headers['Content-Type'] = 'application/json'
  response.headers['charset'] = 'UTF-8'
  response.headers['x-content-type-options'] = 'nosniff'  # Add 'x-content-type-options' header

  return response

if __name__ == "__main__":
  app.run()



