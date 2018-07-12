from cryptography.fernet import Fernet
import os
import datetime

blog_name = "blog.md"
def crypt(strs):
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(str.encode(strs))
	return key, cipher_text


def dcrypt(key, e_strs):
	import pdb; pdb.set_trace
	cipher_suite = Fernet(key)
	plain_text = cipher_suite.decrypt(e_strs)
	return plain_text.decode("utf-8")

def read_all(f_name):
	f_read = open(f_name, "r+")
	return '\n'.join(f_read.readlines())

def push():

	_header = "\n__\n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M") + "\n___\n"
	import pdb; pdb.set_trace()
	prev_strs = get()

	f_read = open("enter_blog","r+")
	strs = prev_strs + _header  + ''.join(f_read.readlines())
	key, e_strs = crypt(strs)

	f_write = open(blog_name, "w")
	f_write.writelines(e_strs.decode("utf-8"))
	print("crypt with key = {}".format(key))
	f_key = open("key","w")
	f_key.write(key.decode("utf-8"))

def get():
	#def get():
	strs = str.encode(read_all(blog_name))
	f_read_key = open("key", "r+")
	key = str.encode(''.join(f_read_key.readlines()))
	f_read_key.close()

	if len(key)==0 or len(strs)==0:
		return ""

	return dcrypt(key,strs)

if __name__ == "__main__":
    # push()
    print(get())