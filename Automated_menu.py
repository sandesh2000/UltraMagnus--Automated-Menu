
import os
import pyfiglet
import xml.etree.ElementTree as obj
def updateXML(filename):
        tree=obj.ElementTree(file=filename)
        root=tree.getroot()

        for value in root.iter("value"):
            port=input("Enter port : ")
            ip=input("Enter ip : ")
            value.text="hdfs://{}:{}".format(ip,port)

        tree=obj.ElementTree(root)
        with open(filename,"wb")as fileupdate:
            tree.write(fileupdate)
#m=l=pyfiglet.figlet_format("------------WELCOME-----------",font="big")
os.system("tput setaf 2")
l=pyfiglet.figlet_format("ARTH DIVERGENTS",font="big")
r=pyfiglet.figlet_format("THANK YOU...See You Next Time----!!",font="slant")
while True:

		os.system("clear")
		os.system("tput setaf 6")
		print("""
							------------------------------------------------------------------

									WELCOME TO THE AUTOMATION MENU **


					Press 1:  FOR HADOOP MENU!!					Press 2:  FOR LVM_PARTITION MENU !!
						
					Press 3:  FOR DOCKER MENU !!					Press 4:  FOR AWS MENU !!
						
										Press 5: To Exit


							------------------------------------------------------------------		
		""")
		os.system("tput setaf 2")
		print(l)
		os.system("tput setaf 7")
		choice=input("ENTER YOUR CHOICE : ")
		if int (choice) == 1:
			os.system("tput setaf 9")
			a=input("Are you sure that you have rpm file of hadoop and java [yes/no] :  " )
			b='yes'		
			if a != b:
				os.system("tput setaf 9")
				print("First get that file : ")
				exit()
			
			while True:
				os.system("clear")
				os.system("tput setaf 6")
				print("""
			    ------------------------------------------------------------------
			        "WELCOME TO THE HADOOP SETUP MENU...."
			        Press 1:  Install java and hadoop ..
			        Press 2:  Configure data node
			        Press 3:  Configure master node
			        Press 4:  Configure client
			        Press 5:  To Start/Stop name node
			        Press 6:  To Start/Stop data node
			        Press 7:  To get Hadoop Admin report
			        Press 8:  To get Hadoop Admin report using WebUI
			        Press 9:  To make a file for upload
			        Press 10: To upload the file on cluster
			        Press 11: To delete the file from cluster
			        Press 12: To read the uploaded file
				Press 13: Back To MAin Menu
			        Press 14: To Exit
			    ------------------------------------------------------------------
        """)			
				os.system("tput setaf 2")				
				print(l)
				ch = int(input("Enter your option : "))
				if ch == 1:
					while True:
						
						print("""
                				Press 1 : to check java is installed or not
						Press 2 : to installed java
						Press 3 : to check hadoop is installed or not
                				Press 4 : to install hadoop
                				Press 5 : to exit
                				""")
						nch = int(input("Enter your option : "))
						if nch == 1:
							os.system("java -version")
						elif nch == 2:
							os.system("rpm -ivh jdk-8u171-linux-x64.rpm")
						elif nch == 3:
							os.system("hadoop version")
            	
						elif nch == 4:
							os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")
						elif nch == 5:
							break
						else:
							print("INVALID INPUT")
						os.system("tput setaf 9")
						input("Enter to continue...")
						os.system("tput setaf 7")
						os.system("clear")
	
				elif ch == 2:
					print("CONFIGURING DATANODE")
					os.system("rm -rf /dn")
					os.system("mkdir /dn")
					os.system("cd /etc/hadoop")
					os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/dn</value>\n</property>\n</configuration> ' > /etc/hadoop/hdfs-site.xml")
					os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://IP:Port</value>\n</property>\n</configuration> ' > /etc/hadoop/core-site.xml")
					updateXML("/etc/hadoop/core-site.xml")
				
				elif ch == 3:
					print("CONFIGURING NAMENODE")
					os.system("mkdir /nn")
					os.system("cd /etc/hadoop")
					os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/nn</value>\n</property>\n</configuration> ' > /etc/hadoop/hdfs-site.xml")
					os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://IP:Port</value>\n</property>\n</configuration> ' > /etc/hadoop/core-site.xml")
					updateXML("/etc/hadoop/core-site.xml")

				elif ch== 4:
					print("CONFIGURING CLIENT")
					os.system("echo \'<?xml version=\"1.0\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n<!-- Put site-specific property overrides in this file. -->\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://IP:Port</value>\n</property>\n</configuration> ' > /etc/hadoop/core-site.xml")
					updateXML("/etc/hadoop/core-site.xml")

				elif ch == 5:
					print("""
                Press 1 : Start Name Node
                Press 2 : Stop Name Node
            """)
					x = int(input ("Enter choice : "))
					if x == 1 :
						os.system("hadoop namenode -format")
						os.system("hadoop-daemon.sh start namenode")
						os.system("jps")
					elif x ==2  : 
						os.system("hadoop-daemon.sh stop namenode")
						os.system("jps")
                	
					else :
						print("INVALID INPUT")
	
				elif ch ==6:
					print("""
                Press 1 : Start Data Node
                Press 2 : Stop Data Node
            """)
					x = int(input ("Enter choice : "))
					if x == 1 :
						os.system("hadoop-daemon.sh start datanode ")
						os.system("jps")
                	
					elif x ==2  : 
						os.system("hadoop-daemon.sh stop datanode ")
						os.system("jps")
                	
					else :
						print("INVALID INPUT")
	
				elif ch == 7 :
				
					os.system("hadoop dfsadmin -report")
	
				elif ch ==8 : 
					ip=input("Enter Master node IP : ")
					os.system("firefox {}:50070 &  ".format(ip))
	
				elif ch ==9 :
					x=input("What name u want to give your file : ")
					os.system("vi {}".format(x))
	
				elif ch == 10:
					file_name=input("Enter the file name which you want to upload : ")
					os.system("hadoop fs -put {} /".format(file_name))
					os.system("hadoop fs -ls /")
	
				elif ch == 11:
					r_name=input("Enter the file name which you want to remove : ")	
					os.system("hadoop fs -rm /{}".format(r_name))
				elif ch == 12 :
					read_file=input("Enter the file name which you want to read : ")	
					os.system("hadoop fs -cat /{}".format(read_file))
				elif ch == 13:
					break
				elif ch ==14 :
					os.system("tput setaf 1")
					print(r)
					exit()
					
				else:
					print("INVALID INPUT !!")
        	   
				os.system("tput setaf 9")
				input("Enter to continue...")
				os.system("tput setaf 7")
				os.system("clear")
        	
	



		elif int (choice) == 2:
			
			os.system("tput setaf 9")
			a=input("Are u sure that your system have attached new Hard disk [yes/no] " )

			os.system("tput setaf 7")
			b='yes'		
			if a != b:
				os.system("tput setaf 9")
				print("First attach your hard disk..")
				exit()
	
			while True: 
				os.system("clear")
				os.system("tput setaf 6")
				print("""
							------------------------------------------------------------------

									"WELCOME TO THE PARTITION MENU...."

						Press 1:  Hard disk Description..
						Press 2:  To see the device name ..
						Press 3:  Create physical volume..
						Press 4:  Detail of physical volume..
						Press 5:  Create volume group..
						Press 6:  Detail of Volume group..
						Press 7:  Create Logical Volume..
						Press 8:  Detail of Logical Volume...
						Press 9:  Format the partition...
						Press 10: Mount that partition with folder..
						Press 11: Check that partition is linked with folder or not..
						Press 12: Back to Main Menu ..
						Press 13: To exit 

							------------------------------------------------------------------		
		""")		
				os.system("tput setaf 2")
				print(l)

				ch = input("Enter your option : ")
			
				os.system("tput setaf 7")
				if int(ch)==1:
					os.system("fdisk -l")
				elif int (ch)==2:
					os.system("lsblk")
				elif int (ch)==3 :
					device_name=input("Enter your device name: ")
					os.system("pvcreate {}".format(device_name))
				elif int (ch)==4:
					os.system("pvdisplay")
				elif int (ch)==5:
					V_G=input("What name you want to give to volume group : ")
					D_N=input("Enter your device name : ")
					os.system("vgcreate {} {}".format(V_G , D_N))
				elif int (ch)==6:
					os.system("vgdisplay")
				elif int (ch)==7:
					size=input("How much size of logical volume you want to create : ")
					lv_name=input("What name you want to give to your logical volume : ")
					vg_name=input("Enter your volume group name : ")
					os.system("lvcreate --size {} --name {} {}".format(size,lv_name,vg_name))
				elif int (ch)==8:
					os.system("lvdisplay")
				elif int (ch)==9:
					os.system("udevadm settle")
					f_n=input("Enter the logical volume path which you want to format : ")
					os.system("mkfs.ext4 {}".format (f_n))
				elif int (ch)==10:
					c=input("Want to make new folder to mount [yes/no] : ")
					if c == 'yes':
						make_folder=input("What name you want to give to your folder : ")
						os.system("mkdir {}".format(make_folder))
						print("Folder is created  successfully")
						partition_name=input("Enter the path of the logical volume  : ")
						os.system("mount {0} {1}".format(partition_name , make_folder))	
					else:	
						folder_name=input("Enter the folder name : ")
						device=input("Enter the path of logical volume : ")
						os.system("mount {0} {1}". format(device,folder_name))
				elif int (ch) ==11:
					os.system("df -h")
				elif int (ch)==12:
					break	
				elif int (ch)==13:
					os.system("tput setaf 1")
					print(r)
					exit()	
				else:
					print("Enter a valid number")
				os.system("tput setaf 9")
				input("Enter to continue...")
				os.system("tput setaf 7")
				os.system("clear")
		

		elif int(choice) == 3:
			os.system("clear")
			os.system("tput setaf 9")
			a=input("Please make sure that your yum has configured [yes/no] :  " )
			os.system("tput setaf 7")
			b='yes'
			if a != b:
				os.system("tput setaf 9")
				print("First configure your yum..")
				exit()
	
			while True: 
				os.system("tput setaf 6")
				print("""
					------------------------------------------------------------------
								"WELCOME TO THE DOCKER MENU...."

	
						Press 1:  Install docker & Start it's Service !!
						Press 2:  Pull image!!
						Press 3:  Detail of images!!
						Press 4:  Install OS!!
						Press 5:  Detail of OS!!
						Press 6:  Configure Web Server!!
						Press 7:  Back To Main Menu !!
						Press 8:  To exit 
	
					-------------------------------------------------------------------------		
		""")		
				os.system("tput setaf 2")
				print(l)


				ch = input("Enter your option : ")
			
				os.system("tput setaf 7")
				if int(ch)==1:
					os.system("yum install docker-ce --nobest")
					os.system("systemctl start docker")
					print("SUCCESSFULLY DONE")
				elif int (ch)==2:
					image=input("Enter the image name : ")
					os.system("docker pull {}:latest".format(image))
				elif int (ch)==3:
					os.system("docker images")

				elif int (ch)==4 :
					os.system("systemctl start docker")
					os_name=input("What name you want to give your os : ")
					image=input("Enter the image name : ")
					os.system("docker run -it --name {} {}:latest".format(os_name,image))
				elif int (ch)==5:
					os.system("docker ps -a")
				elif int (ch)==6:
					os.system("tput setaf 9")
					ip=input("Enter the IP Address of your host: ")					
					os.system("mkdir /workspace")
					os.system("echo '<style>' > /workspace/survey.html")
					os.system("echo 'body{' >>/workspace/survey.html")
					os.system("echo 'background-image: url('https://bit.ly/3n2w98W');' >> /workspace/survey.html")
					os.system("echo '}' >>/workspace/survey.html")
					os.system("echo '</style>' >>/workspace/survey.html")
					os.system("echo '<marquee>' >>/workspace/survey.html")
					os.system("echo '<p style='font-size:40px'>Hey buddy!! Docker server is Up:)</p>' >> /workspace/survey.html")
					os.system("echo '</marquee>' >>/workspace/survey.html")
					os.system("echo 'FROM centos' > /workspace/Dockerfile")
					os.system("echo 'RUN yum install httpd -y' >> /workspace/Dockerfile")
					os.system("echo 'COPY survey.html /var/www/html'>> /workspace/Dockerfile")
					os.system("echo 'CMD [\"/usr/sbin/httpd\",\"-D\",\"FOREGROUND\"]' >> /workspace/Dockerfile")
					os.system("echo 'EXPOSE 80' >> /workspace/Dockerfile")
					os.system("docker build -t webserver:v1 /workspace/")
					os.system("docker run -dit -p 1234:80 webserver:v1")
					os.system("firefox {}:1234/survey.html &  ".format(ip))

				elif int (ch)==7:
					break
				elif int (ch)==8:
					os.system("tput setaf 1")
					print(r)
					exit()		
				else:
					print("Enter a valid number")
				os.system("tput setaf 9")
				input("Enter to continue...")
				os.system("tput setaf 7")
				os.system("clear")
		elif int (choice) ==4 :
			os.system("tput setaf 9")
			a=input("Are u sure that AWS-CLI is installed [yes/no] : " )
			os.system("clear")
			os.system("tput setaf 7")
			b='yes'
			if a != b:
				os.system("tput setaf 9")
				print("First installed  AWS-CLI !!")
				os.system("tput setaf 7")
				exit()
				
			while True: 
					
					os.system("tput setaf 6")		
					print("""
							------------------------------------------------------------------
									"WELCOME TO THE AWS MENU...."
			
								Press 1:  Configure AWS-CLI
								Press 2:  Create key pair!!
								Press 3:  Detail of keypair!!
								Press 4:  Create security group!!
								Press 5:  Detail of security group!!
								Press 6:  Launch instance !!
								Press 7:  Detail of Instances!!
								Press 8:  Create S3 Bucket!!
								Press 9:  Create EBS Volume!!
								Press 10: Attach EBS Volume!!
								Press 11: Detail of EBS Volume!!
								Press 12: Detach EBS Volume!!
								Press 13: Start / Stop  the instance !!
								Press 14: Create cloudfront Distribution!!
								Press 15: Back To Main Menu
								Press 16: To Exit !!

							------------------------------------------------------------------		
		""")
					os.system("tput setaf 7")
					os.system("tput setaf 2")
					print(l)
					ch = input("Enter your option : ")
					os.system("tput setaf 7")
					if int(ch)==1:
						os.system("aws configure")

					elif int (ch)==2:
						key_name=input("Please enter key pair name of which you want to create : ")
						os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
						print("SUCCESSFULLY KEY PAIR CREATED !!")
					elif int (ch) == 3:
						print("DETAIL OF KEY_PAIRS ...")
						os.system("aws ec2 describe-key-pairs")
						

					elif int (ch)== 4 :
						security_grp=input("Please enter the security group name of which you want to create : ")
						description=input("Please enter the description of your security group : ")
						os.system('aws ec2 create-security-group --group-name {} --description "{}"'.format(security_grp,description))
						print("SECURITY GROUP IS SUCCESFULLY CREATED")
		
					elif int(ch)==5:
						print("DETAIL OF SECURITY_GROUP...")
						os.system("aws ec2 describe-security-groups") 
			
					elif int (ch)==6:
						image_id=input("Please enter the image id : ")
						instance_type=input("Please enter the instance-type : ")
						key=input("Please enter the key pair : ")
						security=input("Please enter the security group id : ")
						os.system("aws ec2 run-instances --image-id {} --count 1 --instance-type {} --key-name {} --security-group-ids {}".format(image_id,instance_type,key,security))
						print("SUCCESSFULLY LAUNCHED YOUR INSTANCE !! ")
			

					elif int (ch)==7:
						print("DETAIL OF INSTANCES...")
						os.system("aws ec2 describe-instances")
			
					elif int (ch)==8:
						bucket_name=input("Enter your bucket name : ")
						region_name=input("Enter your region name : ")
						os.system("aws s3api create-bucket --bucket {}  --region {}  --acl public-read --create-bucket-configuration LocationConstraint={} ".format(bucket_name,region_name,region_name))
						print("SUCCESSFULLY LAUNCHED YOUR S3 BUCKET ")





					elif int (ch)==9:
						zone=input("Please enter the zone : ")
						size=input("Please enter the size : ")
						volume_type=input("Please enter the volme type : ")
						os.system("aws ec2 create-volume  --availability-zone {} --size {} --volume-type {}".format(zone,size,volume_type))
						print("SUCCESSFULLY CREATED EBS VOLUME !!")


					elif int (ch)==10:
						state=input("Are u sure that your instance is in running  state [yes/no] : ")
						if state == "yes":
							volume_id=input("Please enter volume id : ")
							instance_id=input("Please enter instance id : ")
							device_name=input("Please enter device name : ")
							os.system("aws ec2 attach-volume  --volume-id {} --instance-id {} --device {} ".format(volume_id,instance_id,device_name))
							print("SUCCESSFULLY ATTACHED EBS VOLUME !!")
						elif state == "no" :
							print("First start your instance ")
		
					elif int (ch)==11:
						print("DETAIL OF EBS_VOLUMES...")
						os.system("aws ec2 describe-volumes")
					elif int (ch)==12:
						volume_id=input("Enter the id of the volume that you want to detach:  ")
						os.system("aws ec2 detach-volume --volume-id {}".format(volume_id))
			
					elif int (ch)==13:
						print("""
							 Press 1 : To stop 
				 			Press 2 : To start
							""")
						x=int(input("Enter your option"))
						if x == 1:
							instance_id=input("Please enter instance id : ")
							os.system("aws ec2 stop-instances  --instance-ids {}".format(instance_id))
						elif x== 2:
							instance_id=input("Please enter instance id : ")
							os.system("aws ec2 start-instances  --instance-ids {}".format(instance_id))
						else:
							print("INVALID OPTION")
			
			
					elif int (ch)==14:
						bucket=input("Please enter bucket name [Please don't enter space after bucket name] : ")
						os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucket))
						print("SUCCESSFULLY CREATED CLOUD FRONT DISTRIBUTION !!")
					elif int (ch)==15:
						break
					elif int (ch)==16:
						os.system("tput setaf 1")
						print(r)
						exit()

					else:
						print("Enter a valid number")
					os.system("tput setaf 9")
					input("Enter to continue...")
					os.system('espaek-ng"Enter to continue" ')
					os.system("tput setaf 7")
					os.system("clear")

		elif int(choice) ==5:
			os.system("tput setaf 6")
			os.system("clear")
			print(r)
			os.system("tput setaf 3")
			print(l)
			exit()
		else:
			print("Enter a valid number")
		os.system("tput setaf 9")
		input("Enter to continue...")
		os.system("tput setaf 7")
		os.system("clear")
		
