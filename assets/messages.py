# All messages structure:
# <step_name>_<step_id>_ ... _<step_id>

# This is /start message
start_message = """
<b>Hi, I am your personalized DNA search engine</b>
Search your DNA, anything you’d like to explore: muscles, vitamins, minerals, exercises….

To explore your DNA, you need a raw DNA file, which is produced by your Personal Genome Service.
Let’s determine the next step for you. Please choose one of the options below:
"""

# User have a DNA test. Ask him for DNA raw file.
start_1_message = """Great! Have you <b>raw DNA file</b>?"""

# User do not have DNA test.
start_2_message = """
No problem!

You have to be genotyped first.

Bellow is a link to our preferred Personal Genome Service provider. Please proceed to their website and follow the instructions.
<a href="https://www.23andme.com/">Personal Genome Service Provider</a>
"""

# User have DNA test and have a DNA raw file
start_1_1_message = """
Fantastic!
You can get a personalized wellness advisory!

Login?
"""

# When user choose log in
login_message = """
Send to bot your raw DNA file
"""

# User have a DNA test and do not have DNA raw file
start_1_2_message = """
Great!
You are very close to start exploring your DNA! Below are different links to instructions of Personal Genome Services to obtain a raw DNA file. Proceed to your Personal Genome Service, follow the instructions and download the raw DNA file.

Ancestry - <a href="https://support.ancestry.com/s/">Instructions</a>
DecodeMe - <a href="https://www.myheritage.ro/help-center/en">Instructions</a>
Geno2 - <a href="https://www.wegene.com/">Instructions</a>
PLink - <a href="https://learn.familytreedna.com/autosomal-ancestry/universal-dna-matching/may-download-family-finder-raw-data/">Instructions</a>
23andMe - <a href="https://auth.23andme.com/login/?next=https%3A//auth.23andme.com/authorize/%3Fredirect_uri%3Dhttps%253A%252F%252Fyou.23andme.com%252Fauth_callback%252F%26response_type%3Dcode%26client_id%3Dyou%26scope%3Dopenid%2Bancestry%2Bbasic%2Bhaplogroups%2Bnames%2Bphenotypes%253Aread%253Aall%26state%3D%257B%2522origin_uri%2522%253A%2B%2522%252Ftools%252Fdata%252Fdownload%252F%2522%257D">Instructions</a>
"""

# User send valid file in "log in" step
correct_file_message = """
Now you can use search. Just send to bot any query. 
"""

# User upload a wrong file
wrong_file_message = """Hmm, it looks like something wrong with your file. 
Please contact us at:"""