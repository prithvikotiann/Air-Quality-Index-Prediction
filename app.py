from flask import Flask, render_template,request
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pickle
df = pd.read_csv("AQI.csv")

app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    result_str = ""
    category=""
    result_cat=""
    bg_color=""
    if request.method == "POST":
        dt = pickle.load(open('dt.pkl', 'rb'))
        co = request.form["co"]
        ozone = request.form["ozone"]
        no2 = request.form["no2"]
        pm = request.form["pm"]
        input_df = [[co, ozone, no2, pm]]
        result = round(float(dt.predict(input_df)), 3)

        result_str = f"Air Quality Index = {result:.3f}"
        if 0 < result <= 50:
            category = 'Good'
            bg_color = '#00cc00'  # Green
        elif 50 < result <= 99:
            category = 'Moderate'
            bg_color = '#33cc33'  # Light green
        elif 99 < result <= 149:
            category = 'Unhealthy for Sensitive Groups'
            bg_color = '#ff9933'  # Orange
        elif 149 < result <= 200:
            category = 'Unhealthy'
            bg_color = '#ff3300'  # Red
        elif 200 < result <= 300:
            category = 'Very Unhealthy'
            bg_color = '#990000'  # Dark red
        else:
            category = 'Hazardous'
            bg_color = '#660066'  # Purple

        result_cat = f"Category = {category:}"
        return render_template("home.html", active='home', m=result_str, p=result_cat, bg_color=bg_color)
    else:
        return render_template("home.html")

def generate_plots():
    plt.figure(figsize=(11, 5))
    sns.scatterplot(data=df, x="lng", y="lat", hue=df["AQI Category"])
    plt.title("AQI Category distribution over longitude and latitude.", size=20)
    plt.xlabel("Longitude", size=15)
    plt.ylabel("Latitude", size=15)
    plt.savefig('static/plot2.png')

    plt.figure(figsize=(11, 5))
    sns.scatterplot(data=df, x="lng", y="lat", hue=df["CO AQI Category"])
    plt.title("CO AQI Category distribution over longitude and latitude.", size=20)
    plt.xlabel("Longitude", size=15)
    plt.ylabel("Latitude", size=15)
    plt.savefig('static/plot3.png')

    plt.figure(figsize=(11, 5))
    sns.scatterplot(data=df, x="lng", y="lat", hue=df["Ozone AQI Category"])
    plt.title("Ozone AQI Category distribution over longitude and latitude.", size=20)
    plt.xlabel("Longitude", size=15)
    plt.ylabel("Latitude", size=15)
    plt.savefig('static/plot4.png')

    plt.figure(figsize=(11, 5))
    sns.scatterplot(data=df, x="lng", y="lat", hue=df["NO2 AQI Category"])
    plt.title("NO2 AQI Category distribution over longitude and latitude.", size=20)
    plt.xlabel("Longitude", size=15)
    plt.ylabel("Latitude", size=15)
    plt.savefig('static/plot5.png')

    plt.figure(figsize=(11, 5))
    sns.scatterplot(data=df, x="lng", y="lat", hue=df["PM2.5 AQI Category"])
    plt.title("PM2.5 AQI Category distribution over longitude and latitude.", size=20)
    plt.xlabel("Longitude", size=15)
    plt.ylabel("Latitude", size=15)
    plt.savefig('static/plot6.png')

    df1 = df['Country'].value_counts().sort_values(ascending=False)[:25].reset_index()
    plt.figure(figsize=(12, 7))
    sns.barplot(data=df1, y='index', x='Country')
    plt.title("Number of times the Countries name, that had occurred in the pollution list", size=18)
    plt.xlabel('Country', size=14)
    plt.ylabel('Count', size=14)
    plt.xticks(rotation=45, ha='right', size=12)
    plt.savefig('static/plot1.png')

@app.route('/graphs', methods=["GET", "POST"])
def mygraphs():
    if request.method == "POST":
        generate_plots()
        return render_template('graphs.html', active='mygraphs',
                               plot1="static/plot1.png", plot2="static/plot2.png",
                               plot3="static/plot3.png", plot4="static/plot4.png",
                               plot5="static/plot5.png", plot6="static/plot6.png",
                               plot7="static/plot7.png", plot8="static/plot8.png",
                               plot9="static/plot9.png")
    else:
        return render_template('graphs.html', active='mygraphs',
                               plot1="static/plot1.png", plot2="static/plot2.png",
                               plot3="static/plot3.png", plot4="static/plot4.png",
                               plot5="static/plot5.png", plot6="static/plot6.png",
                               plot7="static/plot7.png", plot8="static/plot8.png",
                               plot9="static/plot9.png")

@app.route('/aboutus',methods=["GET","POST"])
def myaboutus():
    return render_template('aboutus.html', active='aboutus')

@app.route('/tableau',methods=["GET","POST"])
def mypowerbi():
    return render_template('tableau.html', active='tableau')


if __name__=="__main__":
    app.run(debug=True, use_reloader=True)
