from apiServices import constant
from helper.helper_methods import HelperMethods
from requests import request, post, put, delete, get
from json import loads, dumps


class PetApi():
    def __init__(self):
        self.helper = HelperMethods()

    def pet_api_post(self) -> request:
        url = constant.BASE_URL + constant.PET_ENDPOINT

        # Additional headers.

        # Body
        body = {
            'id': self.helper.getRandomInt(),
            'category':
                {
                    'id': self.helper.getRandomInt(),
                    'name': self.helper.getRandomPetCategory()
                },
            'name': self.helper.getRandomPetName(),
            'photoUrls':
                [
                    "www.url.com"
                ],
            'tags': [
                {
                    'id': self.helper.getRandomInt(),
                    'name': self.helper.getRandomTag()
                }
            ],
            'status': 'available'
        }

        # convert dict to json by json.dumps() for body data.
        return post(url, headers=constant.HEADERS, data=dumps(body, indent=4))

    def pet_api_get(self, id: int) -> request:
        url = constant.BASE_URL + constant.PET_ENDPOINT + "/" + str(id)
        return get(url, headers=constant.HEADERS)

    def pet_api_update(
            self,
            id: int,
            name: str = None,
            category: dict = None,
            tag: dict = None,
            status: str = None
    ) -> request:
        body = {"id": id, }
        url = constant.BASE_URL + constant.PET_ENDPOINT
        isAllNone = all(v is None for v in [name, category, tag, status])
        if not isAllNone:
            if name is not None:
                body['name'] = name
                pass
            if category is not None:
                body['category'] = category
                pass
            if tag is not None:
                body['tag'] = tag
                pass
            if status is not None:
                body['status'] = status
                pass
            pass
        else:
            raise ("name, category, tag, status is none")

        return post(url, headers=constant.HEADERS, data=dumps(body, indent=4))

    def pet_api_delete(self, id: int) -> request:
        url = constant.BASE_URL + constant.PET_ENDPOINT + "/" + str(id)
        return delete(url, headers=constant.HEADERS)
