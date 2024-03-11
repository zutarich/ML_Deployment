from flask import Flask,render_template,request
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
application=Flask(__name__)

app=application

#  route for a home page

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_data_points():
    if request.method=='GET':
        return render_template('home.html')
    # elif request.method=='POST':
        #  the case when the method is POST
        #  here i need to create my custom folder
        #--> here we will connect it to the pipelines-->predict_pipeline.py
    else:
        data=CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        #  converting as df
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        print(results[0])
        return render_template('home.html',results=results[0])
    
    # else :
       
    #     # prolly if not available we need to wirte we can make a alternative things rn i am just pasing 
    #     # else i can make a seperate 404 error page though!!!
    #     pass
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        

    



