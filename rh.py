#  libraries
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.set_option('deprecation.showPyplotGlobalUse', False)

############################################################


#Title
st.title('Reporte de Empleados Activos RH 2022')

# read data

df = pd.read_excel("C:\\Users\\User\\OneDrive\\Documentos\\PowerBI\\Curso Yutube\\RH data.xlsx")

#Filter to active employee
data= df[df['Estatus']=='Activo']
data = data.drop('Fecha Baja', axis =1)

st.write(data.head())


#EDA
col1, col2, col3 = st.columns(3)

with col1:
	with st.expander('Total de empleados', False):
		st.write(data.shape[0])

	data['Género'].value_counts().plot(kind = 'pie', autopct= '%1.f%%')
	st.pyplot()

	data['Función'].value_counts().plot(kind = 'pie', autopct= '%1.f%%').set_title('Cantidad de empleados por Función')
	st.pyplot()

with col2:
		st.info('Grafico de  Barras por:' )
		sns.countplot(x = 'Unidad', data = data, color ='b').set_title('Unidad')
		st.pyplot()

		sns.countplot(y = 'Departamento', data = data, color = 'b').set_title('Departamento')
		st.pyplot()

with col3:

	st.info('empleados activos por:')

	data['Tipo de Trabajo'].value_counts().plot(kind = 'pie', autopct= '%1.f%%').set_title('Cantidad de empleados por Tipo de Trabajo')
	st.pyplot()

	data['Modalidad'].value_counts().plot(kind = 'pie', autopct= '%1.f%%').set_title('Cantidad de empleados por Tipo de Modalidad')
	st.pyplot()

	data['Educación'].value_counts().plot(kind = 'pie', autopct= '%1.f%%').set_title('Cantidad de empleados por Tipo de Educacion')
	st.pyplot()