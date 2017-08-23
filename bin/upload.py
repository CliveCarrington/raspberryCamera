def add_to_clipboard(the_text):
	from Tkinter import Tk
	clip=Tk()
	clip.withdraw()
	clip.clipboard_clear()
	clip.clipboard_append(the_text)
	clip.destroy

def auth_dropbox():
	from dropbox import client, rest, session
	import pickle,os
	APP_KEY = 'vj1wj79q76d25fe' #replace the key and secret with those of your own app
	APP_SECRET = '9xa061pw6x3zqgt'
	#ACCESS_TYPE = 'app_folder'
	ACCESS_TYPE = 'dropbox'
	sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

	#has an access token been saved already?
	if os.path.exists('config.dat')==False:
		request_token = sess.obtain_request_token()
		url = sess.build_authorize_url(request_token)
		add_to_clipboard(url)
		# Make the user sign in and authorize this token
		print "", url
		print "Please visit this website (it's in the clipboard) and press the 'Allow' button, then hit 'Enter' here."
		raw_input()

		# This will fail if the user didn't visit the above URL and hit 'Allow'
		access_token = sess.obtain_access_token(request_token)
		if access_token:
			save_data={'access_token':access_token.key,'secret_token':access_token.secret}
			save_file=open('config.dat','wb')
			pickle.dump(save_data,save_file)
			print "success"
		

def save_to_dropbox(thefile):
	from dropbox import client, rest, session
	import pickle,os,sys

	APP_KEY = 'vj1wj79q76d25fe'
	APP_SECRET = '9xa061pw6x3zqgt'
	# ACCESS_TYPE = 'app_folder'
	ACCESS_TYPE = 'dropbox'
	try:
		sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
		token_file=open('config.dat')
		token_data=pickle.load(token_file)
		access_token=token_data['access_token']
		access_secret=token_data['secret_token']
		sess.set_token(access_token,access_secret)
		print "about to open client sesion"
		client = client.DropboxClient(sess)
		print "About to open the file"
		f=open(thefile,'rb')
		print "About to put the file"
		response=client.put_file('/'+thefile,f,True)
		print "about to print the response"
		print response['client_mtime']
	except IOError as e:
		print "I/O error"
	except:
		print "Unexpected error:",sys.exc_info()[0]
		print sys.exc_info()[1]
		print sys.exc_info()[2]

	
	
