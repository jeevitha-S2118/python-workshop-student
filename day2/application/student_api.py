import requests
def get_user_details(user_id):
 """Fetch user details from the external API."""
 try:
 response = requests.get(
 f"https://jsonplaceholder.typicode.com/users/{user_id}"
 )
 response.raise_for_status()
 return response.json()
 except requests.exceptions.RequestException as error:
 print("Request failed:", error)
 return None