from app import db

class Client(db.Model):
	__tablename__ = 'client'
	cid= db.Column('cid', db.Unicode, autoincrement=True, primary_key=True)
	cfname= db.Column('cfname', db.Unicode)
	clname= db.Column('clname', db.Unicode)
	ccontact= db.Column('ccontact', db.Integer)
	cemail= db.Column('cemail',db.Unicode)
	cpassword= db.Column('cpassword', db.Unicode)
	cadd1=db.column('cadd1', db.Unicode)
	cadd2=db.Column('cadd2',db.Unicode)						#Home location that the client can set
	cstreet= db.Column('street', db.Unicode)
	ccity= db.Column('city', db.Unicode)
	cparish= db.Column('parish', db.Unicode)

	def __init__(self,cfname,clname,ccontact,cemail,cpassword,cadd1,cadd2,cstreet,ccity,cparish):
		self.cfname= cfname
		self.clname= clname
		self.ccontact= ccontact
		self.cemail= cemail
		self.cpassword=cpassword
		self.cadd1=cadd1
		self.cadd2=cadd2
		self.cstreet= cstreet
		self.ccity= ccity
		self.cparish= cparish

        def __repr__(self):
			return '<Client %r>' % self.cid

class Driver(db.Model):
	__tablename__ = 'driver'
	trn= db.Column('trn', db.Integer, primary_key= True)
	dfname= db.Column('dfname', db.Unicode)
	dlname= db.Column('dlname', db.Unicode)
	dcontact= db.Column('dcontact',db.Integer)
	demail= db.Column('demail',db.Unicode)
	dpassword= db.Column('dpassword', db.Unicode)
	daddr1= db.Column('daddr1', db.Unicode)
	daddr2= db.Column('daddr2', db.Unicode)
	dstreet= db.Column('dstreet', db.Unicode)
	dcity= db.Column('dcity', db.Unicode)
	dparish= db.Column('dparish', db.Unicode)

	def __init__(self,trn,dfname,dlname,dstreet,dcity,dparish):
		self.trn= trn
		self.dfname= dfname
		self.dlname= dlname
		self.dstreet= dstreet
		self.dcity= dcity
		self.dparish= dparish


class Operator(db.Model):
	__tablename__ = 'operater'
	opID= db.Column('opID', db.Unicode, primary_key=True)
	ofname= db.Column('ofname', db.Unicode)
	olname= db.Column('olname', db.Unicode)
	otrn= db.Column('otrn', db.Integer)
	ostreet= db.Column('ostreet', db.Unicode)
	ocity= db.Column('ocity', db.Unicode)
	oparish= db.Column('oparish', db.Unicode)

	def __init__(self,opID,ofname,olname,otrn,ostreet,ocity,oparish):
		self.opID= opID
		self.ofname= ofname
		self.olname= olname
		self.otrn= otrn
		self.ostreet= ostreet
		self.ocity= ocity
		self.oparish= oparish


class Vehicle(db.Model):
	__tablename__ ='vehicle'
	platenum= db.Column('platenum', db.Unicode, primary_key=True)
	vmodel= db.Column('vmodel', db.Unicode)
	vmake= db.Column('vmake', db.Unicode)
	vcolour= db.Column('vcolour', db.Unicode)
	seat_cap= db.Column('seat_cap', db.Integer)

	def __init__(self,platenum,vmodel,vmake,vcolour,seat_cap):
		self.platenum= platenum
		self.vmodel= vmodel
		self.vmake= vmake
		self.vcolour= vcolour
		self.seat_cap= seat_cap

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
