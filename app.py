import streamlit as st   
import matplotlib.pyplot as plt   
import seaborn as sns   
import plotly.graph_objects as go   
import plotly.express as px   
import pandas as pd   
import io
import plotly.io as pio
from plotly.tools import mpl_to_plotly
from PIL import Image

# Load the dataset   
df = pd.read_csv('cars.csv', sep = ';')

# Set the app title   
st.title('Cars Dataset Visualisation')   

st.write('### Dataframe Head')
st.dataframe(df.head())

# Define the sidebar  
logo = Image.open("2.png")
st.sidebar.image(logo)
st.sidebar.markdown('### ')
analysis_type1 = st.sidebar.selectbox('Select the type of analysis - PLOTLY' , ('Univariate' , 'Bivariate' , 'Multivariate'))   
analysis_type2 = st.sidebar.selectbox('Select the type of analysis - Seaborn' , ('Univariate' , 'Bivariate' , 'Multivariate'))

st.sidebar.markdown('### ')
st.sidebar.markdown('### Follow me on social media')
st.sidebar.markdown('### ')
st.sidebar.markdown('''
                    
    <a href="https://twitter.com/Azzammed19Azzam">
        <img src="https://cdn3.iconfinder.com/data/icons/popular-services-brands/512/twitter-512.png" alt="Twitter" width="50"/>
    </a>
    <a> &nbsp &nbsp </a>
    <a> &nbsp &nbsp </a>
    <a href="https://github.com/MedAzzam">
        <img src="https://cdn3.iconfinder.com/data/icons/social-media-2169/24/social_media_social_media_logo_github-512.png" alt="GitHub" width="50"/>
    </a>
    <a> &nbsp &nbsp </a>
    <a> &nbsp &nbsp </a>
    <a href="https://www.linkedin.com/in/azzam-mohamed1/">
        <img src="https://img.icons8.com/color/48/null/linkedin-2--v1.png" alt="LinkedIn" width="50"/>
    </a>
''', unsafe_allow_html=True)

# Define the main section   
if analysis_type1 == 'Univariate':   
    # Display the univariate visualizations   
    with st.container():   
        st.subheader('Univariate Analysis : PYPOLT')   
        with st.expander('Quantitative Variables'):   
            # Histogram   
            fig = px.histogram(df, x= 'MPG', nbins=10)   
            st.plotly_chart(fig)   
               
            # Box plot   
            fig = px.box(df , y='Horsepower')   
            st.plotly_chart(fig)   
               
        with st.expander('Qualitative Variables'):   
            # Bar plot   
            fig = px.bar(df , x='Origin')   
            st.plotly_chart(fig)   
               
            # Histogram   
            fig = px.histogram(df , x='Car')   
            st.plotly_chart(fig)   
               
            # Pie chart   
            fig = px.pie(df , names='Origin')   
            st.plotly_chart(fig)   
                    
elif analysis_type1 == 'Bivariate':   
    # Display the bivariate visualizations   
    with st.container():   
        st.subheader('Bivariate Analysis : PYPLOT')   
        with st.expander('Scatter plot'):   
            # Scatter plot   
            fig = px.scatter(df, x ='Horsepower' , color='Car')   
            st.plotly_chart(fig)   
               
        with st.expander('Box plot'):   
            # Box plot   
            fig = px.box(df , x= 'Origin', y='MPG' , orientation='v')   
            st.plotly_chart(fig)   
               
        with st.expander('Grouped bar plot'):   
            # Histogram   
            fig = px.histogram(df, x ='Displacement' , color='Origin')   
            st.plotly_chart(fig)   
               
            # Bar plot   
            fig = px.bar(df,  x='Origin', y='Displacement', orientation='v')   
            st.plotly_chart(fig)   
               
        with st.expander('Pie chart'):   
            # Pie chart   
            fig = px.pie(df, values='Displacement', names='Origin')   
            st.plotly_chart(fig)   
                    
elif analysis_type1 == 'Multivariate':   
    # Display the multivariate visualizations   
    with st.container():   
        st.subheader('Multivariate Analysis : PYPLOT')   
           
        # Heatmap  
        st.markdown('**Correlation matrix:**') 
        sns_plot = sns.heatmap(df.corr() , annot=True , cmap='coolwarm')   
        st.pyplot()   
        st.set_option('deprecation.showPyplotGlobalUse', False)
        
        # 3D Scatter plot
        st.markdown('**3D Scatter Plot of Horsepower, Weight, and MPG by Origin**')  
        fig = px.scatter_3d(df,  x='Horsepower',  y='Weight',  z='MPG',  color='Origin')   
        st.plotly_chart(fig)   
           
        # Facet Grid   
        st.markdown('**Distribution of Horsepower by Origin :**') 
        # Set the default style   
        sns.set_style('whitegrid')   

        # Create a FacetGrid with Origin as the column   
        g = sns.FacetGrid(df,  col='Origin')   

        # Map a histogram of Horsepower to each column   
        g.map(sns.histplot  ,'Horsepower')   
        
        # Convert the plot to a PNG image   
        buf = io.BytesIO()   
        plt.savefig(buf , format='png')   
           
        # Display the plot in Streamlit   
        st.image(buf.getvalue())   
        
        # create matplotlib figure
        fig, ax = plt.subplots(figsize=(9, 3))
        sns.barplot(x='Cylinders', y='MPG', hue='Origin', data=df, ax=ax)

        # convert matplotlib figure to plotly figure
        fig = mpl_to_plotly(fig)

        # modify the layout of the plotly figure
        fig.update_traces(
            hovertemplate='MPG: %{y:.2f}<br>Cylinders: %{x}<br>Origin: %{trace.name}',
            marker={'line': {'width': 1, 'color': 'white'}}
        )
        fig.update_layout(
            title='MPG by Origin and Cylinder Count',
            xaxis_title='Cylinders',
            yaxis_title='MPG',
            legend_title='Origin',
            font=dict(family='Arial, sans-serif', size=14, color='black')
        )

        # pass plotly figure to st.plotly_chart()
        st.plotly_chart(fig)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        


# Define the main section   
if analysis_type2 == 'Univariate':   
    # Display the univariate visualizations   
    with st.container():
        st.subheader('Univariate Analysis : SEABORN')  
        with st.expander('Quantitative Variables'):   
        # Analyse univariee
            
            # Quantitative variables
            st.markdown("#### Distribution plot for 'Acceleration'")
            sns.displot(df, x='Acceleration')
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)

            st.write("#### Kernel Density Estimate plot for 'MPG'")
            sns.kdeplot(df['MPG'])
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)

            st.write("#### Histogram for 'Horsepower'")
            sns.histplot(df, x='Horsepower')
            st.pyplot()
            st.set_option('deprecation.showPyplotGlobalUse', False)
        with st.expander('Qualitative Variables'):
            
            # Qualitative variables
            st.write("#### Countplot for 'Origin'")
            sns.countplot(data=df, x='Origin')
            st.pyplot()

            # Visualisation des boites a moustaches
            st.write("#### Boxplot for 'MPG' and 'Horsepower'")
            sns.boxplot(x='MPG', y='Horsepower', data=df)         
            st.pyplot()
            
            st.write("#### Violinplot for 'MPG' and 'Horsepower'")
            sns.violinplot(x='MPG', y='Horsepower', data=df)
            st.pyplot()
            
            
elif analysis_type2 == 'Bivariate':   
        # Display the bivariate visualizations 
    with st.container():   
        st.subheader('Bivariate Analysis : SEABORN') 
        with st.expander('Quantitative Variables'):  
            # 3. ANALYSE BIVARIEE

            ### 3.1 Nuage de points :

            #### les variables quantitatives
            st.write("### Scatterplot for 'Weight' vs 'MPG'")
            sns.scatterplot(x='Weight', y='MPG', data=df)
            st.pyplot()

            st.write("### Relplot for 'Cylinders' vs 'Horsepower'")
            sns.relplot(x='Cylinders', y='Horsepower', data=df)
            st.pyplot()

            st.write("### Distribution plot for 'Displacement'")
            sns.displot(df['Displacement'])
            st.pyplot()

        #### les variables Qualitatives
        with st.expander('Qualitative Variables'):
            st.write("### Stripplot for 'Origin' and 'Car'")
            sns.stripplot(x='Origin', y='Car', data=df)
            st.pyplot()
            
            st.write("### Swarmplot for 'Origin' and 'Car'")
            sns.swarmplot(x='Origin', y='Car', data=df)
            st.pyplot()

            # Box plot
            st.write("### Boxplot for 'Origin' and 'Weight'")
            sns.boxplot(x='Origin', y='Weight', data=df)
            st.pyplot()

            # Boxen plot
            st.write("### Boxenplot for 'Origin' and 'Weight'")
            sns.boxenplot(x='Origin', y='Weight', data=df)
            st.pyplot()

            # Cat plot with kind='box'
            st.write("### Boxplot for 'Origin' and 'Weight' using catplot")
            sns.catplot(x='Origin', y='Weight', kind='box', data=df)
            st.pyplot()

            # Violin plot
            st.write("### Violinplot for 'Origin' and 'Weight'")
            sns.violinplot(x='Origin', y='Weight', data=df)
            st.pyplot()
            
            # Bar plot
            st.write("### barplot for 'Origin' and 'Weight'")
            sns.barplot(x='Origin', y='Weight', data=df)
            st.pyplot()

            # Relation de régression : Implot
            st.write("### Relation de régression : Implot")
            sns.lmplot(x='Weight', y='MPG', hue='Origin', data=df)
            st.pyplot()
elif analysis_type2 == 'Multivariate':   
    # Display the multivariate visualizations   
    with st.container():   
        st.subheader('Multivariate Analysis : SEABORN') 
        # 4. ANALYSE MULTIVARIE
            
        # Plot MPG distribution
        st.header('MPG Distribution')
        sns.histplot(df['MPG'], kde=True)
        st.pyplot()

        # Pair plot
        st.header('Pair Plot')
        sns.pairplot(df, vars=['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight'], hue='Origin')
        st.pyplot()

        # Joint plot
        st.header('Joint Plot')
        sns.jointplot(x='Horsepower', y='MPG', data=df, kind='reg')
        st.pyplot()

        # Pair grid
        st.header('Pair Grid')
        g = sns.PairGrid(df, vars=['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight'], hue='Origin')
        g.map_diag(sns.histplot)
        g.map_offdiag(sns.scatterplot)
        g.add_legend()
        st.pyplot()

        # Facet grid
        st.header('Facet Grid')
        g = sns.FacetGrid(df, col='Origin')
        g.map(sns.scatterplot, 'Horsepower', 'MPG')
        st.pyplot()

        # Correlation matrix
        st.header('Correlation Matrix')
        corr_matrix = df[['MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight']].corr()
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
        st.pyplot()

        # Set the plot style
        sns.set_style('whitegrid')

        # Scatter plot
        st.header('Scatter Plot')
        sns.scatterplot(x='MPG', y='Horsepower', data=df)
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', False)
