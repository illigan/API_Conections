import time
import os 
import requests
import json
import pandas as pd
from API import Core, Data


base_url = "https://au-api.basiq.io/"

API_KEY = 'MTQ2YWFhOTYtNzU5Yi00ZjgxLTg0ZmYtMjg0YzQzNzM3YWQ2OjUyZTZjMGMxLTQ0OTItNDRiZC1iOTA3LTMxMTEyYTViMmM2Yw=='
user_id = 'bca4b9cc-b7e2-4458-83bc-4855c147bd70'

# Call the function to get the access token
api_key = API_KEY
core_instance = Core(api_key)
data_instance = Data()

# Call the method to get the access token
access_token = core_instance.get_auth_token()
print(access_token)

user = core_instance.get_user(user_id, access_token)
print(user)

retrieved_user = core_instance.retreive_user(user_id, access_token)
print(user)

#### test data calls #####

#list all accounts
all_accounts = data_instance.all_accounts(user_id, access_token)
print(all_accounts)

account_id = '594d1aa0-73d2-4ce2-8a0a-9ae6a28985c6'

#return one account
an_account = data_instance.get_account(user_id, account_id, access_token)
print(an_account)

#return transactions
transactions = data_instance.get_transactions(user_id, access_token)
print(transactions)

#get details on one transaction
transaction_id = '8e7ecaa7-66f4-4cbd-ab47-ab5265bcf0b7'
transaction = data_instance.get_transaction(user_id, transaction_id, access_token)
print(transaction)

#get affordability report
afford_report = data_instance.get_affordability_report(user_id, access_token)
print(afford_report)

#get expenses statement
expenses = data_instance.get_expenses(user_id, access_token)
print(expenses)

#get income statement
income = data_instance.get_income(user_id, access_token)
print(income)