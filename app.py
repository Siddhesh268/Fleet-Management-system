import sys,pickle
from flask import Flask,flash, redirect, url_for, request, render_template, abort, jsonify,g
from socket import socket, AF_INET, SOCK_STREAM
from connection import setConnection
from Analysis import *


app = Flask(__name__)
app.secret_key = 'my unobvious secret key'
@app.route('/logout/')
def logout():
        flash(setConnection(["stop"]))
        return render_template('bye.html')
@app.route('/invoice/<trip_id>')
def invoice(trip_id):
        trip=setConnection(["read_tripByID",trip_id])
        return render_template('invoice.html',trip=trip)
@app.route('/expenseReport/')
def expenseReport():
        Expenditure()
        return redirect(url_for('index'))

@app.route('/ProfitLossReport/')
def ProfitLossReport():
        liabilityasset()
        return redirect(url_for('index'))
@app.route('/MaintenanceReport/')
def MaintenanceReport():
        Maintenance()
        return redirect(url_for('index'))
       
@app.route('/driver_on_vehicle/', methods=['POST'])
def driver_on_vehicle():
    if request.method == 'POST':
        lis = ["write_driverOnVehicle",request.form["veh_no"],request.form["driver_name"]]
        flash(setConnection(lis))
        return redirect(url_for('index'))
@app.route('/start_trip/<veh_no>', methods=['POST'])
def start_trip(veh_no):
    if request.method == 'POST':
        lis = ["write_trips",veh_no,request.form["customer_name"],request.form["source"],request.form["destination"],request.form["cost"],request.form["freight"]]
        flash(setConnection(lis))
        return redirect(url_for('vehicle',veh_no=veh_no))
@app.route('/stop_trip/<veh_no>/<trip_id>', methods=['POST'])
def stop_trip(veh_no,trip_id):
    if request.method == 'POST':
        lis = ["update_trip",trip_id]
        flash(setConnection(lis))
        return redirect(url_for('vehicle',veh_no=veh_no))

@app.route('/add_trip_details/<veh_no>/<trip_id>', methods=['POST'])
def add_trip_details(veh_no,trip_id):
    if request.method == 'POST':
        lis = ["write_trip_details",trip_id,request.form["amt"],request.form["date_of_tran"],request.form["place"],request.form["reason"]]
        flash(setConnection(lis))
        return redirect(url_for('vehicle',veh_no=veh_no))
@app.route('/deleteVehicle/<veh_no>', methods=['POST'])
def deleteVehicle(veh_no):
    if request.method == 'POST':
        flash(setConnection(["delete_vehicles",veh_no]))        
        return redirect(url_for('index'))
@app.route('/deleteDriver/<driver_id>', methods=['POST'])
def deleteDriver(driver_id):
    if request.method == 'POST':
        flash(setConnection(["delete_drivers",driver_id]))        
        return redirect(url_for('index'))

@app.route('/insurance/<veh_no>', methods=['POST'])
def insurance(veh_no):
    if request.method == 'POST':
        lis = ["write_insurances",veh_no,request.form["ins_no"],request.form["validf"],request.form["validu"],request.form["cost"],request.form["icomp"]]
        flash(setConnection(lis))        
        return redirect(url_for('vehicle',veh_no=veh_no))

@app.route('/permit/<veh_no>', methods=['POST'])
def permit(veh_no):
    if request.method == 'POST': 
        lis = ["write_permits",veh_no,request.form["pno"],request.form["validf"],request.form["validu"],request.form["cost"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle',veh_no=veh_no))


@app.route('/loan/<veh_no>', methods=['POST'])
def loan(veh_no):
    if request.method == 'POST':
        lis = ["write_loans",veh_no,request.form["lno"],request.form["costt"],request.form["lcomp"],request.form["dur"],request.form["intr"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle',veh_no=veh_no))

@app.route('/maintenance/<veh_no>', methods=['POST'])
def maintenance(veh_no):
    if request.method == 'POST':    
        lis = ["write_maintenance",veh_no,request.form["rmk"],request.form["plc"],request.form["cost"],request.form["vend"],request.form["dom"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle',veh_no=veh_no))

        
@app.route('/tax/<veh_no>', methods=['POST'])
def tax(veh_no):
    if request.method == 'POST':
        lis = ["write_taxes",veh_no,request.form["tno"],request.form["validf"],request.form["validu"],request.form["cost"]]
        flash(setConnection(lis))         
        return redirect(url_for('vehicle',veh_no=veh_no))


@app.route('/add_customer/', methods=['POST'])
def add_customer():
    if request.method == 'POST':
        lis = ["write_customers",request.form["Cus_name"],request.form["Comp_name"],request.form["Cus_contact"],request.form["Cus_address"]]
        flash(setConnection(lis))                 
        return redirect(url_for('index'))
@app.route('/add_driver/', methods=['POST'])
def add_driver():
    if request.method == 'POST':
        lis = ["write_drivers",request.form["driver_name"],request.form["License_no"],request.form["contact_no"]]
        flash(setConnection(lis))                 
        return redirect(url_for('index'))
@app.route('/add_vehicle/', methods=['POST'])
def add_vehicle():
    if request.method == 'POST':
        lis = ["write_vehicles",request.form["veh_no"],request.form["chassis_no"],request.form["vehicle_class"],request.form["vehicle_capacity"]]
        flash(setConnection(lis))
        return redirect(url_for('index'))
@app.route('/add_dependent/<driver_id>', methods=['POST'])
def add_dependent(driver_id):
    if request.method == 'POST':
        lis = ["write_dependents",driver_id,request.form["nm"],request.form["rel"],request.form["cnt"]]
        flash(setConnection(lis))                 
        return redirect(url_for('driver',driver_id=driver_id))
@app.route('/add_salary/<driver_id>', methods=['POST'])
def add_salary(driver_id):
    if request.method == 'POST':
        lis = ["write_salary",driver_id,request.form["salary"]]
        flash(setConnection(lis))                 
        return redirect(url_for('driver',driver_id=driver_id))
@app.route('/pay_loan/<veh_no>/<loan_no>', methods=['POST'])
def pay_loan(veh_no,loan_no):
    if request.method == 'POST':
        lis = ["write_loanPayRegister",loan_no,request.form["emi"]]
        flash(setConnection(lis))                 
        return redirect(url_for('vehicle',veh_no=veh_no))
@app.route('/')
def index():
        vehicles=setConnection(["read_vehicles"])
        drivers=setConnection(["read_drivers"])
        customers=setConnection(["read_customers"])
        return render_template('Mainboot.html',vehicles=vehicles,drivers=drivers,customers=customers)

@app.route('/driver/<driver_id>')
def driver(driver_id):
        driver=setConnection(["read_driver",driver_id])
        dependents=setConnection(["read_dependents",driver_id])
        return render_template('Driver.html',driver=driver,dependents=dependents)

@app.route('/vehicle/<veh_no>')
def vehicle(veh_no):
        vehicle=setConnection(["read_vehicle",veh_no])
        customers=setConnection(["read_customers"])
        tripDetail=setConnection(["read_tripDetails",veh_no])
        loanProgress=setConnection(["read_loans",veh_no])
        loanStatus=setConnection(["read_loanStatus",veh_no])
        status=setConnection(["read_trips",veh_no])
        status.append(0)
        loanProgress.append(0)
        return render_template('Vehicle.html',loanStatus=loanStatus,loanProgress=loanProgress,vehicle=vehicle,customers=customers,tripDetail=tripDetail,status=status)


if __name__ == '__main__':
   app.run(debug = True)
