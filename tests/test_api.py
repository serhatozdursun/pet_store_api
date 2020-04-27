from unittest import TestCase
import json

from apiServices.pet_api import PetApi


class apitest(TestCase):
    def test_post_headers_body_json(self):
        pet_api = PetApi()
        postRequestResp = pet_api.pet_api_post()
        self.assertEqual(postRequestResp.status_code, 200)
        postReqRespBody = json.loads(postRequestResp.text)
        pet_id = postReqRespBody["id"]

        getRequestResp = pet_api.pet_api_get(pet_id)
        getReqRespBody = json.loads(getRequestResp.text)

        self.assertEqual(getRequestResp.status_code, 200)
        self.assertDictEqual(postReqRespBody, getReqRespBody)
        name = "Duman"
        status = "pending";
        pet_api.pet_api_update(pet_id, name=name, status=status)
        getRequestResp = pet_api.pet_api_get(pet_id)
        getReqRespBody = json.loads(getRequestResp.text)

        self.assertNotEqual(postReqRespBody['name'], getReqRespBody['name'])
        self.assertEqual(name, getReqRespBody['name'])
        self.assertEqual(status, getReqRespBody['status'])

        pet_api.pet_api_delete(pet_id)

        getRequestResp = pet_api.pet_api_get(pet_id)

        self.assertEqual(getRequestResp.status_code, 404)
