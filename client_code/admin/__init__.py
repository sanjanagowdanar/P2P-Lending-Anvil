import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
# from passlib.hash import pbkdf2_sha256

user = None

def admin_check(email):
  admin_user = app_tables.fin_admin_users.search(admin_email=email)
  if admin_user:
    role = admin_user[0]['admin_role']
    if (role == "super admin"):
      return True
    else:
      return False
  else:
    return False


def add_admin_details(email,name,mobile_no,dob,gender,role,password,created_date,status,ref_admin_name,ref_admin_email,customer_id):
  admin_users = app_tables.fin_admin_users.get(admin_email=email)
  if admin_users:
    return False
  else:
    app_tables.users.add_row(email=email,enabled=True,password_hash=password)
    app_tables.fin_admin_users.add_row(admin_email=email,admin_role=role,full_name=name, mobile_no=int(mobile_no), join_date = created_date, gender=gender, status=status, ref_admin_name=ref_admin_name, ref_admin_email=ref_admin_email )
    app_tables.fin_user_profile.add_row(full_name=name, email_user=email, last_confirm = True,usertype =role,gender=gender, mobile = str(mobile_no),registration_approve = True,customer_id=customer_id)
    return True   

