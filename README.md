To test the code locally

##Start API
python Predict.py
##Test API
curl -d @API_Test_Data.json -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predict 
