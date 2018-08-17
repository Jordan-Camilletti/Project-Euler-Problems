"""Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text."""
#CORRECT KEY:[103,111,100]
key=[0]

ciphered=[]
cipher=open("cipher.txt", "r")
ciphered=(cipher.read().split(","))
cipher.close()

for n1 in range(97,123):#Finding the correct key
	for n2 in range(97,123):
		for n3 in range(97,123):
			key=[n1,n2,n3]
			normal=[]
			for n in range(len(ciphered)):
				#print(chr(int(ciphered[n])^key[0]))
				normal.append(chr(int(ciphered[n])^key[n%len(key)]))

			joined="".join(normal).lower()
			if("the" in joined and "and" in joined and "that" in joined and "have" in joined):#Attempting to detect the most common 3+ letter english words
				print(key)
				print(joined)
				sum=0#Using the correct key to find the sum
				for n in range(len(ciphered)):
					sum+=int(int(ciphered[n])^key[n%3])
				print(sum)
