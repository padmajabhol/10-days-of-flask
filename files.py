from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


# @app.route('/upload', methods=['PUT'])
# def upload():
#     with open('test.war', 'wb') as f:
#         print(dir(request))
#         f.write(request.data)
#     return 'OK'

@app.route("/")
def hello_world():
    return "Hello World"

# @app.route("/print_filename", methods=['POST','PUT'])
# def print_filename():
#     file = request.files['file']
#     filename=secure_filename(file.filename)   
#     return filename

@app.route("/gcbm/upload/disturbances", methods=['POST'])
def gcbm_upload():
  title = request.form.get("title") or "simulation"
    # Sanitize title
  title = "".join(c for c in title if c.isalnum())

  project_dir = f"{title}"
  if not os.path.exists(f"{os.getcwd()}/input/{project_dir}"):
      os.makedirs(f"{os.getcwd()}/input/{project_dir}")
#    logging.debug(os.getcwd())

# def print_filename_disturbances():
#     file = request.files['file']
#     filename=secure_filename(file.filename)   
#     return filename

# #  curl -F file='@disturbances_2011_moja.tiff' \
#    http://localhost:6969/print_filename_disturbances

# @app.route("/gcbm/upload/classifier", methods=['POST'])
# def print_filename_classifier():
#     file = request.files['file']
#     filename=secure_filename(file.filename)   
#     return filename

# @app.route("/gcbm/upload/database", methods=['POST'])
# def print_filename_database():
#     file = request.files['file']
#     filename=secure_filename(file.filename)   
#     return filename

# @app.route("/gcbm/upload/miscellaneous", methods=['POST'])
# def print_filename_misc():
#     file = request.files['file']
#     filename=secure_filename(file.filename)   
#     return filename

#  curl -X POST -F file=@test.txt http://localhost:6969/print_filename

if __name__ == '__main__':
    app.run(port=6969, debug=True)