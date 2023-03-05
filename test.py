import requests


# Making a GET request
print("Model Information")
r = requests.get('http://172.17.0.2:5000/info')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)


# Making a GET request
print("Health Service")
r = requests.get('http://172.17.0.2:5000/health')

# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

print('\n\n')
print("Model Prediction")
json = \
[
   {
      "radius_mean":15,
      "texture_mean":10.38,
      "perimeter_mean":122.8,
      "area_mean":1001.0,
      "smoothness_mean":0.1184,
      "compactness_mean":0.2776,
      "concavity_mean":0.9001,
      "concave points_mean":0.2471,
      "symmetry_mean":0.789,
      "fractal_dimension_mean":0.07871,
      "radius_se":1.095,
      "texture_se":1,
      "perimeter_se":5.54757,
      "area_se":153.4,
      "smoothness_se":0.6456,
      "compactness_se":0.0490664,
      "concavity_se":0.05373,
      "concave points_se":0.01587,
      "symmetry_se":0.03003,
      "fractal_dimension_se":0.006193,
      "radius_worst":25.38,
      "texture_worst":6.33,
      "perimeter_worst":100.6,
      "area_worst":2019.0,
      "smoothness_worst":0.66,
      "compactness_worst":0.7925,
      "concavity_worst":0.7119,
      "concave points_worst":0.2654,
      "symmetry_worst":0.46464,
      "fractal_dimension_worst":0.565
   }
]
headers = {'Content-Type': 'application/json'} 
detail = requests.post('http://172.17.0.2:5000/predict', json=json, 
headers=headers)

# success code - 200
print(detail)

# print content of request
print(detail.json())
