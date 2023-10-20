import json;
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('IBM API KEY')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator)
visual_recognition.set_service_url('IBM URL') 
with open('./test.jpg', 'rb') as images_file: 
    classes = visual_recognition.classify(images_file=images_file,threshold='0.6',classifier_ids='food').get_result()
print(json.dumps(classes, indent=2))
{
  "images": [
    {
      "classifiers": [
        {
          "classifier_id": "food",
          "name": "food",
          "classes": [
            {
              "class": "pepperoni pizza",
              "score": 0.809,
              "type_hierarchy": "/pizza/pepperoni pizza"
            },
            {
              "class": "pizza",
              "score": 0.918
            }
          ]
        }
      ],
      "image": "test.jpg"
    }
  ],
  "images_processed": 1,
  "custom_classes": 0
}
