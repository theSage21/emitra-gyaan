import json
import random
from copy import deepcopy


sample_response = {
    "FetchDetails": {
            "TransactionDetails": {
                "ServiceName" : "Airtel Mobile",
                "officeID":"DDD1",
                "BillAmount": "941.00",
                "ConsumerName": "Chetan Kumar Yadav",
                "consumerKeysValues": "9352423664",
                "partPaymentAllow": "1",
                "partPaymentType": "Both",
                "lookUpId": "6163298"
                },
            "BillDateils": [
                {"LableName": "Consumer Name", "LableValue": "Chetan Kumar Yadav" },
                { "LableName": "Account Number", "LableValue": "1116231291" },
                { "LableName": "Mobile Number", "LableValue": "9352423664" },
                { "LableName": "Amount Before Due Date", "LableValue": "931.00" },
                { "LableName": "Amount After Due Date", "LableValue": "941.00" },
                { "LableName": "Due Date", "LableValue": "NA" },
                { "LableName": "Bill Date", "LableValue": "NA" },
                { "LableName": "Bill Cycle", "LableValue": "NA" },
                { "LableName": "Bill Number", "LableValue": "NA" }
            ]
        }
}

first = 'Aaditya,Abhinav,Abhishek,Aditya,Aishwarya,Amit,Anjali,Ankit,Anusha,Arjun,Aryan,Ashish,Aswini,Deepak,Gayatri,Ira,Isha,Ishita,Karan,Manoj,Mayank,Naveen,Neeraj,Neha,Niharika,Nikita,Parth,Pavithra,Pranav,Priyanka,ROHIT,Raj,Rohan,Sakshi,Sam,Shreya,Sneha,Soham,Suhani,Tanya,Vinay,ajith,akash,ananya,ankur,divya,kumar,leah,mahesh,natasha,priya,rahul,rakesh,ramya,riya,sanjana,seema,shivangi,shivani,shyam,simran,tanvi,vani,varsha,vivek,yash'.split(',')
last = 'Rathod,Chouhan,Thakur,Gehlot,Sharma,Jain,Mehta,Soni,Parikh,Saxena,Paliwal,Gupta,Jhala,Solanki,Parmar,Sisodia'.split(',')
def get_random_name():
    return random.choice(first).title() + ' ' + random.choice(last).title()

def get_response(ssoid, srvid, searchKey):
    """Until I figure out how to make the API work. dummy responses"""
    new_dict = deepcopy(sample_response)
    new_dict['FetchDetails']['TransactionDetails']['consumerKeysValues'] = searchKey
    new_dict['FetchDetails']['TransactionDetails']['ConsumerName'] = get_random_name()
    new_dict['FetchDetails']['TransactionDetails']['BillAmount'] = str(random.random() * 1000)
    return new_dict

get_response(1234, 1234, 9899155975)
