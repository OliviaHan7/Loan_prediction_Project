# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)
api=Api(app)


def log_transform(x):
    return np.log(x+1)
model = pickle.load( open( "model.p", "rb" ) )
    
    
class Scoring(Resource):
    def post(self):
        json_data=request.get_json()
        print(json_data)
        df=pd.DataFrame(json_data.values(),index=json_data.keys()).transpose()
        res=model.predict(df)
        print(df)
        return res.tolist()
    
    
# class Predict(Resource):
#     def post(self):
#         json.data=request.get_json()
#         df=pd.DataFrame(json_data.values(),
#                         index=json_data.keys()).transpose()
#         result=model.predict(df)
#         return result.tolist()
    
    
    
api.add_resource(Scoring, '/scoring')
# api.add_resource(Predict, '/predict')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



                        
                        
                        
                           
                           
                         