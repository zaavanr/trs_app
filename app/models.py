from app import db

class Client(db.Model):
	__tablename__ = 'client'
	cid= db.Column('cid', db.Integer, autoincrement=True, primary_key=True)
	cfname= db.Column('cfname', db.Unicode)
	clname= db.Column('clname', db.Unicode)
	ccontact= db.Column('ccontact', db.Integer)
	cemail= db.Column('cemail',db.Unicode)
	cpassword= db.Column('cpassword', db.Unicode)
	cadd1=db.column('cadd1', db.Unicode)
	cadd2=db.Column('cadd2',db.Unicode)
	ccity= db.Column('city', db.Unicode)
	cparish= db.Column('parish', db.Unicode)

	def __init__(self,cfname,clname,ccontact,cemail,cpassword,cadd1,cadd2,ccity,cparish):
		self.cfname= cfname
		self.clname= clname
		self.ccontact= ccontact
		self.cemail= cemail
		self.cpassword=cpassword
		self.cadd1=cadd1
		self.cadd2=cadd2
		self.ccity= ccity
		self.cparish= cparish

        def __repr__(self):
			return '<Client %r>' % self.cid

class Driver(db.Model):
	__tablename__ = 'driver'
	dtrn= db.Column('dtrn', db.Integer, primary_key= True)
	dfname= db.Column('dfname', db.Unicode)
	dlname= db.Column('dlname', db.Unicode)
	dcontact= db.Column('dcontact',db.Integer)
	demail= db.Column('demail',db.Unicode)
	dpassword= db.Column('dpassword', db.Unicode)
	daddr1= db.Column('daddr1', db.Unicode)
	daddr2= db.Column('daddr2', db.Unicode)
	dcity= db.Column('dcity', db.Unicode)
	dparish= db.Column('dparish', db.Unicode)

	def __init__(self,dtrn,dfname,dlname,dcontact,demail,dpassword,daddr1,daddr2,dcity,dparish):
		self.dtrn= dtrn
		self.dfname= dfname
		self.dlname= dlname
		self.dcontact=dcontact
		self.demail=demail
		self.dpassword=dpassword
		self.daddr1 =daddr1
		self.daddr2=daddr2
		self.dcity= dcity
		self.dparish= dparish


class Operator(db.Model):
	__tablename__ = 'operator'
	opID= db.Column('opID', db.Integer, primary_key=True)
	ofname= db.Column('ofname', db.Unicode)
	olname= db.Column('olname', db.Unicode)
	oadd1=db.Column('oadd1',db.Unicode)
	oadd2=db.Column('oadd2',db.Unicode)
	ocity= db.Column('ocity', db.Unicode)
	oparish= db.Column('oparish', db.Unicode)
	otrn= db.Column('otrn', db.Integer)

	def __init__(self,ofname,olname,oadd1,oadd2,otrn,ocity,oparish):
		self.ofname= ofname
		self.olname= olname
		self.otrn= otrn
		self.oadd1=oadd1
		self.oadd2=oadd2
		self.ocity= ocity
		self.oparish= oparish


class Vehicle(db.Model):
	__tablename__ ='vehicle'
	platenum= db.Column('platenum', db.Unicode, primary_key=True)
	vmodel= db.Column('vmodel', db.Unicode)
	vmake= db.Column('vmake', db.Unicode)
	vcolour= db.Column('vcolour', db.Unicode)
	seat_cap= db.Column('seat_cap', db.Integer)
	vclass= db.Column('class', db.Integer)

	def __init__(self,platenum,vmodel,vmake,vcolour,seat_cap,vclass):
		self.platenum= platenum
		self.vmodel= vmodel
		self.vmake= vmake
		self.vcolour= vcolour
		self.seat_cap= seat_cap
		self.vclass=vclass

# class Report(db.Model):		#Report that the operator would see from viewing the driver
# 	__tablename__= 'report'
# 	dtrn= db.Column('dtrn',db.Integer, primary_key=True)
# 	date= db.Column('date',db.Date)
# 	time= db.Column('time',)
# 	job_status= db.Column('job_status',db.Unicode)
#
#
# class Job_History(db.Model):
# 	__tablename__= 'job_history'
# 	dtrn= db.Column('dtrn',db.Integer)
# 	time= db.Column('time',)
# 	p_loc= db.Column('p_loc',) #Pick up location
# 	d_loc= db.Column('d_loc',)	#drop off location
