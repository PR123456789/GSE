# Backend for GSE Class WS23/24

## Testing locally

### Start API
In CLI:\
  python Predict.py
### Test API
In CLI:\
  curl -d @API_Test_Data.json -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/predict 
