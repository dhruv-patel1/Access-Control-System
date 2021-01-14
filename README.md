Name: Dhruv Patel

Written in Python 3

Design:
Stored the information related to access in local json files that are generated in the same directory that portal.py is in and used the data collected to validate the checks we make depending on the command.

Setup:
No setup is really necessary as portal.py will generate the json files holding the data in the same directory the python file is in.

How to run the program:
python portal.py COMMAND ARGUMENTS....

Usage for every command:
python portal.py AddUser user password
python portal.py Authenticate user password
python portal.py SetDomain user domain_name
python portal.py DomainInfo domain_name
python portal.py SetType object type_name
python portal.py TypeInfo type_name
python portal.py AddAccess operation domain_name type_name
python portal.py CanAccess operation user object

Testing:
After I wrote the code for each command, I did a good amount of manual testing to ensure that the code worked correctly and to see if the errors were getting caught during execution. Additionally, I ensured that the reading and writing of files was successful after each command inputted. Furthermore, this was tested on the iLab machines and works completely fine.


Test Script Example:
python portal.py AddUser a 123
-Outputs: Success
python portal.py AddUser b 123
-Outputs: Success
python portal.py AddUser a 456
-Outputs: Error: User already exists
python portal.py AddUser "" 123
-Outputs: Error: Username is missing

python portal.py Authenticate a 123
-Outputs: Success
python portal.py Authenticate b 123
-Outputs: Error: Invalid Password
python portal.py Authenticate b 123 34
-Outputs: Error: Invalid Arguments


python portal.py SetDomain a anime
-Outputs: Success
python portal.py SetDomain b ""
-Outputs: Error: Missing domain name

python portal.py DomainInfo anime
-Outputs: a
python portal.py DomainInfo clown
-Outputs: Error: Domain does not exist

python portal.py SetType video.mp4 videos
-Outputs:Success
python portal.py SetType lush.mp3 music stuff
-Outputs:Error: Invalid arguments

python portal.py TypeInfo videos
-Outputs: video.mp4
python portal.py TypeInfo food
-Outputs: Nothing because the type doesn't exist

python portal.py AddAccess download anime videos
Outputs: Success

python portal.py CanAccess download a video.mp4
Outputs: Success

