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

class NodesTests(APITestCase):
	def __init__(self, *args, **kwargs):
		APITestCase.__init__(self, *args, **kwargs)
		# User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
	def test_createNode(self):
		"""
		Ensure we can create a new account object.
		"""
		User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
		user = User.objects.get(id=1)
		self.client.force_authenticate(user=user)
		url = reverse('node-list')
		data = {
			"app_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
			"app_key":"test1",
			"dev_addr":"test111",
			"dev_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
			"last_seen":"2017-12-1T11:22",
			"name":"test_name1",
			"type":"tepm"
		}
		response = self.client.post(url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Node.objects.count(), 1)
		self.assertEqual(Node.objects.get().name, 'test_name1')

# class GatewayTests(APITestCase):
# 	def __init__(self, *args, **kwargs):
# 		APITestCase.__init__(self, *args, **kwargs)
# 		# User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
# 	def test_createNode(self):
# 		"""
# 		Ensure we can create a new account object.
# 		"""
# 		User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
# 		user = User.objects.get(id=1)
# 		self.client.force_authenticate(user=user)
# 		url = reverse('node-list')
# 		data = {
# 			"app_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
# 			"app_key":"test1",
# 			"dev_addr":"test111",
# 			"dev_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
# 			"last_seen":"2017-12-1T11:22",
# 			"name":"test_name1",
# 			"type":"tepm"
# 		}
# 		response = self.client.post(url, data, format='json')
# 		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 		self.assertEqual(Node.objects.count(), 1)
# 		self.assertEqual(Node.objects.get().name, 'test_name1')

# class SwarmTests(APITestCase):
# 	def __init__(self, *args, **kwargs):
# 		APITestCase.__init__(self, *args, **kwargs)
# 		# User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
# 	def test_createNode(self):
# 		"""
# 		Ensure we can create a new account object.
# 		"""
# 		User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
# 		user = User.objects.get(id=1)
# 		self.client.force_authenticate(user=user)
# 		url = reverse('node-list')
# 		data = {
# 			"app_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
# 			"app_key":"test1",
# 			"dev_addr":"test111",
# 			"dev_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
# 			"last_seen":"2017-12-1T11:22",
# 			"name":"test_name1",
# 			"type":"tepm"
# 		}
# 		response = self.client.post(url, data, format='json')
# 		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 		self.assertEqual(Node.objects.count(), 1)
# 		self.assertEqual(Node.objects.get().name, 'test_name1')

# class MessagesTests(APITestCase):
# 	def __init__(self, *args, **kwargs):
# 		APITestCase.__init__(self, *args, **kwargs)
# 		# User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
# 	def test_createNode(self):
# 		"""
# 		Ensure we can create a new account object.
# 		"""
# 		User.objects.create(username="test", email="test@test.sk", password="test12345", company="test s.r.o")
# 		user = User.objects.get(id=1)
# 		self.client.force_authenticate(user=user)
# 		url = reverse('node-list')
# 		data = {
# 			"app_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
# 			"app_key":"test1",
# 			"dev_addr":"test111",
# 			"dev_eui":"a0cf4274-4b8b-11e7-a919-92ebcb67fe33",
# 			"last_seen":"2017-12-1T11:22",
# 			"name":"test_name1",
# 			"type":"tepm"
# 		}
# 		response = self.client.post(url, data, format='json')
# 		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
# 		self.assertEqual(Node.objects.count(), 1)
# 		self.assertEqual(Node.objects.get().name, 'test_name1')

