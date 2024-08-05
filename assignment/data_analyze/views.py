from django.shortcuts import render
from . import forms
from django.contrib import messages
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64

# Create your views here.


def generate_histograms(df):
    plots = {}
    numerical_cols = df.select_dtypes(include=['number']).columns

    for col in numerical_cols:
        plt.figure(figsize=(10, 5))  
        plt.hist(df[col].dropna(), bins=30, edgecolor='k')  
        plt.title(f'Histogram for {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        plots[col] = f'data:image/png;base64,{plot_url}'
        plt.close()
    
    return plots



def analyze_data(file):
   
    df = pd.read_csv(file)
    df_head = df.head()
    summary_stats = df.describe(include='all')
    missing_values = df.isnull().sum()
    missing_values_df = missing_values.to_frame(name='Missing Values') 
    
    plots = generate_histograms(df)
    return df_head.to_html(), summary_stats.to_html(), missing_values_df.to_html(), plots

def index(request):
    if request.method == 'POST':
        form = forms.UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request,"File Uploaded Successfully!")
            df_head, summary_stats, missing_values, plots = analyze_data(request.FILES['file'])
            return render(request, 'data_analyze/result.html', {
                'df_head': df_head,
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'plots':plots
                
            })
            
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = forms.UploadCSVForm()
        
    context={'form':form}
    return render(request, 'data_analyze/index.html', context)