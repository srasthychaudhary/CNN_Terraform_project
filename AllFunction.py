import os

#Defining function to send an E-mail
def email_sent():
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    fromaddr = "chaudharysrasthy1528@gmail.com"
    toaddr = "srishtichaudhary1415@gmail.com"
   
    #Instance of MIMEMultipart
    msg = MIMEMultipart()
  
    #Store the sender E-mail address  
    msg['From'] = fromaddr
  
    #Store the receiver E-mail address 
    msg['To'] = toaddr
  
    #Store the subject 
    msg['Subject'] = "Srasthy Chaudhary Pic"
  
    #Store the body of an E-mail
    body = "Hey, This is the face of Srasthy Chaudhary"
  
    #Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
  
    #Open the file to be sent 
    filename = "pic.jpg"
    attachment = open("./pic.jpg", "pic")
  
    #Instance of MIMEBase(named as p)
    p = MIMEBase('application', 'octet-stream')
  
    #To change the payload into encoded form
    p.set_payload((attachment).read())
  
    #Encode into base64
    encoders.encode_base64(p)
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
  
    #Attach the instance 'p' to instance 'msg'
    msg.attach(p)
  
    #Creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
  
    #Start TLS for security
    s.starttls()
  
    #Authentication
    s.login(fromaddr, "password-of-sender-id")
  
    #Converts the Multipart msg into a string
    text = msg.as_string()
  
    #Send an E-mail
    s.sendmail(fromaddr, toaddr, text)
  
    #Terminate the session
    s.quit()

    
#Function to send whatsapp message
def whatsapp_msg_sent():
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly(
        phone_no="+918923093647", 
        message="Hey Mumma, my app is working fine"
)
    
#Function to launch EC2 Instance
def ec2_launch():
    #Create an EC2 instance on AWS cloud
    os.system("aws ec2 run-instances  --image-id ami-011c99152163a87ae --instance-type t2.micro  --subnet-id subnet-baddc8d2  --count 1 --security-group-ids  sg-6b84ab0c  --key-name RHkey > ec2_out.txt")
    print("EC2 Instance Launched")
  
#Function for launching ebs volume
def ebs_launch():
    os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 5 --volume-type gp2 --tag-specification  ResourceType=volume,Tags=[{Key=aws,Value=key}]")    
    print("EBS volume Launched")