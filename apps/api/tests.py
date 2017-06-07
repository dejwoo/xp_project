from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.api.models import User, Gateway, Node, Swarm, RxInfo, TxInfo, Message

class NodesTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
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