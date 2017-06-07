from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.api.models import User, Gateway, Node, Swarm, RxInfo, TxInfo, Message


class UsersTest(APITestCase):
	def __init__(self, *args, **kwargs):
		APITestCase.__init__(self, *args, **kwargs)
		# User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
	def test_create_user(self):
		"""
		Ensure we can create a new account object.
		"""
		url = reverse('signup')
		response = self.client.get(url)
		assert response.status_code == 200
		csrftoken = response.cookies['csrftoken']
		data = {
			"username":"username_testovacieho_usera",
			"email":"test@test.sk",
			"password1":"test12345",
			"password2":"test12345",
			"company":"test s.r.o"
		}
		response = self.client.post(url, data, headers={'X-CSRFToken': csrftoken}, format='multipart')
		print(response.content)
		self.assertEqual(response.status_code, status.HTTP_302_FOUND)
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(User.objects.get().username, 'username_testovacieho_usera')

	def test_get_user_list(self):

		user =User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
		self.client.force_authenticate(user=user)
		valid_response = {
		  "url": "http://testserver/api/users/"+str(user.id)+"/",
		  "username": "test",
		  "email": "test@test.sk",
		  "date_joined": "2017-06-07T14:11:02.220673Z",
		  "company": "test s.r.o",
		}
		url = reverse('user-list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		result_to_compare = dict(response.data['results'][0])
		self.assertEqual(result_to_compare['url'], valid_response['url'])
		self.assertEqual(result_to_compare['username'], valid_response['username'])
		self.assertEqual(result_to_compare['email'], valid_response['email'])
		self.assertEqual(result_to_compare['company'], valid_response['company'])

	def test_get_user_detail(self):

		user =User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
		self.client.force_authenticate(user=user)
		valid_response = {
		  "url": "http://testserver/api/users/"+str(user.id)+"/",
		  "username": "test",
		  "email": "test@test.sk",
		  "date_joined": "2017-06-07T14:11:02.220673Z",
		  "company": "test s.r.o",
		}
		url = reverse('user-detail',args=[user.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['url'], valid_response['url'])
		self.assertEqual(response.data['username'], valid_response['username'])
		self.assertEqual(response.data['email'], valid_response['email'])
		self.assertEqual(response.data['company'], valid_response['company'])

	def test_delete_user_detail(self):
		user =User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
		self.client.force_authenticate(user=user)
		valid_response = {
		  "url": "http://testserver/api/users/"+str(user.id)+"/",
		  "username": "test",
		  "email": "test@test.sk",
		  "date_joined": "2017-06-07T14:11:02.220673Z",
		  "company": "test s.r.o",
		}
		url = reverse('user-detail',args=[user.id])
		response = self.client.delete(url)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
		self.assertEqual(response.data, None)

	def test_patch_user_detail(self):
		user =User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
		self.client.force_authenticate(user=user)
		valid_response = {
		  "url": "http://testserver/api/users/"+str(user.id)+"/",
		  "username": "test_patched",
		  "email": "test@test.sk",
		  "date_joined": "2017-06-07T14:11:02.220673Z",
		  "company": "test s.r.o",
		}
		url = reverse('user-detail',args=[user.id])
		response = self.client.patch(url, valid_response)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data['url'], valid_response['url'])
		self.assertEqual(User.objects.get().username, 'test_patched')
		self.assertEqual(response.data['username'], valid_response['username'])
		self.assertEqual(response.data['email'], valid_response['email'])
		self.assertEqual(response.data['company'], valid_response['company'])
		self.assertEqual(User.objects.count(), 1)


class NodesTests(APITestCase):
    def __init__(self, *args, **kwargs):
        APITestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        self.user = User.objects.create(username="test", email="test@test.sk", password="asdasdasd",
                                        company="test s.r.o")
        self.client.force_authenticate(user=self.user)
        self.data = {
            "app_eui": "a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
            "app_key": "test1",
            "dev_addr": "test111",
            "dev_eui": "a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
            "last_seen": "2017-12-1T11:22",
            "name": "test_name1",
            "type": "tepm"
        }

    def tearDown(self):
        self.user.delete()

    def test_createNode(self):
        self.url = reverse('node-list')
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Node.objects.count(), 1)
        self.assertEqual(Node.objects.get().name, 'test_name1')

    def create_node(self):
        self.client.post(reverse('node-list'), self.data, format='json')

    def test_deleteNode(self):
        self.create_node()
        self.url = reverse('node-detail', args=[Node.objects.get().id])
        response = self.client.delete(self.url, {'id': Node.objects.get().id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_updateNode(self):
        self.create_node()
        response = self.client.patch(reverse('node-detail', args=[Node.objects.get().id]), {'name': 'modified_name'},
                                     format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Node.objects.get().name, 'modified_name')
