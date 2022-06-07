# Libraries that we need:
import requests # This library can help us to send request and recieve response

# Start main part, create class
class APIPuller:
    def __init__(self, API_version): # this receive one argument: version of API
        # URLs that we need
        self.users_api_url = f'http://127.0.0.1:8000/api/v{API_version}/user-api/'
        self.posts_api_url = f'http://127.0.0.1:8000/api/v{API_version}/post-api/'
        self.register_api_url = f'http://127.0.0.1:8000/api/v{API_version}/dj-rest-auth/registration/'
        self.login_api_url = f'http://127.0.0.1:8000/api/v{API_version}/dj-rest-auth/login/'
        self.logout_api_url = f'http://127.0.0.1:8000/api/v{API_version}/dj-rest-auth/logout/'
        self.ok_status_codes = list(range(200, 300))

    # For generate responses that returned from functions 
    def response_generator(self, message, status, data=''):
        return {'message': message, 'status': status, 'data': data}

    # Function for login
    def login(self, parameters_as_json): # Recieve parameters(username, password) of user as a json format for login
        r = requests.post(self.login_api_url, parameters_as_json) # Trying to login
        # Check if there is no problem
        if r.status_code in self.ok_status_codes: 
            return self.response_generator(f'Logged in to({r.status_code}) ' +parameters_as_json['username'], True)
        else:
            return self.response_generator(f'Error({r.status_code}): {r.reason}', False)
    
    # Function for register
    def register(self, parameters_as_json): # Recieve parameters(username, password1, password2) of user as a json for register
        r = requests.post(self.register_api_url, parameters_as_json) # Trying to register
        # Ceck if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Created new user({r.status_code}): '+parameters_as_json['username'], True, parameters_as_json)
        else:
            return self.response_generator(f'Error({r.status_code}): {r.reason}', False)

    # Function for logout
    def logout(self): 
        r = requests.post(self.logout_api_url) # Trying to logout
        # Ceck if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Logged out({r.status_code})', True)
        else:
            return self.respone_generator(f'Error({r.status_code}): {r.response}', False)

    # Function that returns list of users 
    def users_list(self):
        r = requests.get(self.users_api_url) # Trying to get list of users
        # Check if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Success({r.status_code})', True, r.json())
        else:
            return self.response_generator(f'Error({r.status_code}): {r.reason}', False)

    # Function that returns parameters of exact user
    def user_detail(self, user_id): # Recieve id of user
        r = requests.get(self.users_api_url+str(user_id)) # Trying to get exact user
        # Check if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Success({r.status_code})',True, r.json())
        else:
            return self.respone_generator(f'Error({r.status_code}): {r.reason}', False)

    # Function that returns list of posts 
    def posts_list(self):
        r = requests.get(self.posts_api_url) # Trying to get list of users
        # Check if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Success({r.status_code})', True, r.json())
        else:
            return self.response_generator(f'Error({r.status_code}): {r.reason}', False)

    # Function that returns parameters of exact post
    def post_detail(self, post_id):
        r = requests.get(self.posts_api_url+str(post_id)) # Trying to get exact post
        # Check if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Success({r.status_code})', True, r.json())
        else:
            return self.response_generator(f'Error({r.status_code})', False)

    # Function for create post
    def create_post(self, parameters_as_json): # Recieve parameters() of post as json format 
        r = requests.post(self.posts_api_url, parameters_as_json) # Trying to create new post
        # Check if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Created post({r.status_code})', True, parameters_as_json)
        else:
            return self.response_generator(f'Error({status_code}): {r.reason}', False)
    
    # Function for update post
    def update_post(self, post_id, parameters_as_json): # Recieve id of post that updating and parameters of that post as a json format for update
        r = requests.put(self.posts_api_url+str(post_id), parameters_as_json) # Trying to update post
        # Check if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Updated post({r.status_code})', True, parameters_as_json)
        else:
            return self.response_generator(f'Error({r.status_code}): {r.reason}', False)
    
    # Function for delete post
    def delete_post(self, post_id): # Recieve id of post that deleting
        r = requests.delete(self.posts_api_url+str(post_id)) # Trying to delete post
        # Check if there is no problem
        if r.status_code in self.ok_status_codes:
            return self.response_generator(f'Deleted post({r.status_code})', True)
        else:
            return self.response_generator(f'Error({r.status_code}): {r.reason}', False)

# Create object
object = APIPuller(1) # Giving version of API. Its 1 for now

#Testing functions:

# Register
print(object.register({'username': 'daniel', 'password1': 'xwsw1xa4x', 'password2': 'xwsw1xa4x'})) 

# Login
print(object.login({'username': 'daniel', 'password': 'xwsw1xa4x'}))

# Logout
print(object.logout())

# Users list
print(object.users_list())

# User detail
print(object.user_detail(1))

# Posts list
print(object.posts_list())

# Post detail
print(object.post_detail(6))

# Create post
print(object.create_post({'title': 'New Post', 'body': 'Its new post for test.', 'author': 1}))

# Update post
print(object.update_post(6, {'title': 'This post updated', 'body': 'This post updated for test', 'author': 1}))

# Delete post
print(object.delete_post(6))



#################### You can see more using documentation ###############################