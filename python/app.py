#importing
import json
from flask import Flask, request
import dbhelper

app = Flask(__name__)

#app based off the request type

#each api call has its own function

#every function the sends or receieves something back checks the type and returns, returns on error as well.  Delete calls have no type check.

#executes code on corresponding api request
@app.get('/api/return_all')
def select_all():
   try:   
      results = dbhelper.run_proceedure('CALL return_all', [])
      if(type(results)==list):
         results_json = json.dumps(results, default=str)
      else:
         print('error')
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')
#executes code on corresponding api request
@app.post('/api/insert_item')
def insert_item():
   try:   
      name = request.json.get('name')
      desc = request.json.get('description')
      price_var = request.json.get('price')
      results = dbhelper.run_proceedure('CALL make_collumn(?,?,?)', [name,desc,price_var])
      if(type(results)==list):
         results_json = json.dumps(results, default=str)
      else:
         print('error')
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')

#executes code on corresponding api request
@app.patch('/api/patch_item')
def patch_item():
   try:  
      id_var = request.json.get('id')
      price_var = request.json.get('price')
      results = dbhelper.run_proceedure('CALL patch_idprice(?,?)', [id_var,price_var])
      if(type(results)==list):
         results_json = json.dumps(results, default=str)
      else:
         print('error')
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')

#executes code on corresponding api request
@app.delete('/api/delete_item')
def delete_item():
   try:
      id_var = request.json.get('id')
      results = dbhelper.run_proceedure('CALL delete_item(?)', [id_var])
      results_json = json.dumps(results, default=str)
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')


#api -------------------------------------------------------functions for the employee table: ---------------------------------------------------

#executes code on corresponding api request
@app.post('/api/insert_employee')
def insert_employee():
   try:
      name = request.json.get('name')
      position_var = request.json.get('position')
      hourly_wage = request.json.get('hourly_wage')
      results = dbhelper.run_proceedure('CALL insert_employee(?,?,?)', [name, position_var, hourly_wage])
      if(type(results)==list):
         results_json = json.dumps(results, default=str)
      else:
         print('error')
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')

#executes code on corresponding api request
@app.get('/api/return_employee')
def select_spec_employee():
   try:
      id_var = request.json.get('id')
      results = dbhelper.run_proceedure('CALL return_spec_employee(?)', [id_var])
      if(type(results)==list):
         results_json = json.dumps(results, default=str)
      else:
         print('error')
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')

#executes code on corresponding api request
@app.patch('/api/update_employee_wage')
def update_employee_wage():
   try:
      id_var = request.json.get('id')
      new_wage = request.json.get('hourly_wage')
      results = dbhelper.run_proceedure('CALL update_employee_wage(?,?)', [id_var,new_wage])
      if(type(results)==list):
         results_json = json.dumps(results, default=str)
      else:
         print('error')
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')

#executes code on corresponding api request
@app.delete('/api/delete_employee')
def delete_employee():
   try:
      id_var = request.json.get('id')
      results = dbhelper.run_proceedure('CALL delete_employee(?)', [id_var])
      results_json = json.dumps(results, default=str)
      return results_json
   #catching errors
   except TypeError:
      print('invalid value type, try again.')
   except UnboundLocalError:
      print('python code is incorrectly indented')
   except ValueError:
      print('value outside range, try again')

#running @app
app.run(debug=True)
