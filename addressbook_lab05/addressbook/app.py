from flask import Flask,render_template,jsonify,request,make_response,redirect,session
from controller import ContactController  
from contact import Contact

app = Flask(__name__,template_folder='./templates')
app.secret_key='HD9E8U234@#%#$%@q$%#$R2309'

ctrl = ContactController()

@app.route("/view_all_contacts")
@app.route("/")
def index(): 
    contacts = ctrl.getAllContacts() 
    name = request.args.get("name") 
    if name:
        contacts = [x for x in contacts if str(name).strip() in str(x['name']).strip() ]
        
    msg = session.get("msg")
    session['msg'] =  None
    
    return render_template("contacts.html",contacts=contacts,query=name,msg=msg)




@app.route("/create_contact",methods=["GET","POST"])
def create_contact():
    if request.method=="POST":
        name = request.form.get("name")
        city = request.form.get("city")
        profession = request.form.get("profession")
        mobile_no = request.form.get("mobile_no")
        
        
        temp_mobile_no = mobile_no
        allowed = True
        if "+" in temp_mobile_no and not temp_mobile_no.startswith("+"):
            allowed = False
        if not temp_mobile_no.replace("+","").strip().isnumeric():
            allowed = False
        if len(str(temp_mobile_no))>13 or len(str(temp_mobile_no))<9:
            allowed  = False

        if not allowed: 
            return render_template("create_contact.html",msg='Please enter a valid Mobile No.')
            
        
        data = {
            "name":name,
            "city":city,
            "profession":profession,
            "mobileno":mobile_no,
        }
        contact = Contact(data) 
        if not ctrl.insertConatct(contact):
            return render_template("create_contact.html",msg='Cannot insetr Record due to database problem.')
            
            
        
        session['msg'] = "Contact inserted successfully !"
        return  redirect('/')
    
    return render_template("create_contact.html")




if __name__=="__main__":
    app.run(debug=True,port=8000)