import requests

get_url = "https://jsonplaceholder.typicode.com/todos/15"

#get_response= requests.get(get_url)
#print(get_response.json())


#PUT
todoitem15={"userId" : 2, "title" : "put title", "completed" : False }
#put_response = requests.put(get_url,json=todoitem15)
#print(put_response.json())

#PATCH
todoitempatch15= {"title":"Patch test"}
#patch_response = requests.patch (get_url, json=todoitempatch15)
#print(patch_response.json())


#DELETE
delete_response = requests.delete(get_url)
print(delete_response.json())
print(delete_response.status_code)
