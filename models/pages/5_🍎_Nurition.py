import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
# from pydataset import data
from streamlit_extras.no_default_selectbox import selectbox
import matplotlib.pyplot as plt

st.set_page_config(page_title='Nutrition Calorie Tracker', layout='wide')

# ---- HEADER SECTION ----
css_styles = """
    <style>
    .header-container {
        background-color: #9C0000;
        padding: 20px;
        text-align: center;
        border-radius: 10px;
        animation: fadeIn 2s ease-in-out;
    }
    .header-container h1 {
        color: #FFFFFF;
        font-size: 48px;
        margin: 0;
        animation: slideInFromLeft 1.5s ease-in-out;
    }
    .header-container p {
        color: #FFFFFF;
        font-size: 24px;
        animation: slideInFromRight 1.5s ease-in-out;
    }

    /* Adjust margin between header and content */
    .content-container {
        margin-top: 50px;
    }
    
    /* Animation Keyframes */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideInFromLeft {
        from { transform: translateX(-100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    @keyframes slideInFromRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    </style>
"""

# Apply the CSS styles
st.markdown(css_styles, unsafe_allow_html=True)

# Header for the Nutrition page
header_html = """
    <div class="header-container">
        <h1>Nutrition</h1>
        <p>Nourish your body and fuel your goals with our expert nutrition guidance</p>
    </div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# ---- SPACE ADJUSTMENT FOR CONTENT ----
st.markdown('<div class="content-container"></div>', unsafe_allow_html=True)
st.write("")

# Load dataset
df = pd.read_csv("./food1.csv", encoding='mac_roman')

ye = st.number_input('Enter Number of dishes', min_value=1, max_value=10)
i = 0
j = 0
calories = 0
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list7 = []
list8 = []

try:
    while i < ye:
        st.write("--------------------")
        sel = selectbox('Select the food', df['Shrt_Desc'].unique(), no_selection_label=" ", key=i)
        list1.append(sel)
        sel_serving = st.number_input('Select the number of servings', min_value=1, max_value=10, value=1, step=1, key=j+100)
        
        i += 1
        j += 1
        
        st.write(f"Food: {sel}")
        st.write(f"Serving: {sel_serving}")
        
        # Check if the selection exists
        selected_food = df[df['Shrt_Desc'] == sel]
        
        if not selected_food.empty:
            calorie_per_serving = selected_food['Energ_Kcal'].values[0]
            cal = calorie_per_serving * sel_serving
            list2.append(cal)
            st.write(f"Calories per serving: {calorie_per_serving}")
            st.write(f"Total calories for {sel_serving} servings of {sel} = {cal} Energ_Kcal")
            
            # Calculate other nutrients
            protine = selected_food['Protein_(g)'].values[0] * sel_serving
            list3.append(protine)

            carbs = selected_food['Carbohydrt_(g)'].values[0] * sel_serving
            list4.append(carbs)

            fat = selected_food['Lipid_Tot_(g)'].values[0] * sel_serving
            list5.append(fat)

            sugar = selected_food['Sugar_Tot_(g)'].values[0] * sel_serving
            list7.append(sugar)

            calcium = selected_food['Calcium_(mg)'].values[0] * sel_serving
            list8.append(calcium)

            # Add to total calories
            calories += cal
        else:
            st.write(f"Food item '{sel}' not found in the dataset.")
        
        # Comparison with daily recommended values (RDV)
        rdv_calories = 2000  # Modify these values based on the user's needs
        # rdv_protein = 50  # grams
        # rdv_carbs = 300  # grams
        # rdv_fat = 70  # grams

        # Stylish Gauge Chart for RDV comparison
        fig_rdv = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=calories,
            delta={'reference': rdv_calories, 'increasing': {'color': "#9C0000"}},
            title={'text': "Total Calories vs RDV", 'font': {'size': 24}},
            gauge={
                'axis': {'range': [0, rdv_calories]},
                'bar': {'color': "#FF6347"},
                'steps': [{'range': [0, 1500], 'color': "#90EE90"}, {'range': [1500, rdv_calories], 'color': "#FFD700"}],
            }
        ))
        st.plotly_chart(fig_rdv)
        

    st.write(f"Total calories for all dishes = {calories} Energ_Kcal")
    st.write("Total Calories:", calories)
    
    # Display feedback based on total calorie intake
    if calories < 1500:
        st.write("You may need to eat more to reach your daily caloric needs.")
    elif calories > 2500:
        st.write("You've consumed a lot of calories today! Consider eating lighter meals for the rest of the day.")
    else:
        st.write("Your calorie intake is balanced for the day.")

    col1, col2, col3 = st.columns(3)

    # Stacked bar chart for macronutrient distribution
    macronutrient_data = pd.DataFrame({
        'Food': list1,
        'Proteins': list3,
        'Carbs': list4,
        'Fats': list5
    })

    fig_macronutrient = go.Figure(data=[
        go.Bar(name='Proteins', x=macronutrient_data['Food'], y=macronutrient_data['Proteins']),
        go.Bar(name='Carbs', x=macronutrient_data['Food'], y=macronutrient_data['Carbs']),
        go.Bar(name='Fats', x=macronutrient_data['Food'], y=macronutrient_data['Fats'])
    ])
    fig_macronutrient.update_layout(barmode='stack', title="Macronutrient Distribution per Food")
    st.plotly_chart(fig_macronutrient)
    
    # Radar chart data preparation
    categories = ['Proteins', 'Carbs', 'Fats', 'Sugar']
    values = [np.sum(list3), np.sum(list4), np.sum(list5), np.sum(list7)]

    # Add zero values for categories that may not be selected
    if len(values) < len(categories):
        values += [0] * (len(categories) - len(values))
        
    fig_radar = go.Figure()

    fig_radar.add_trace(go.Scatterpolar(
        r=values + [values[0]],  # Close the loop
        theta=categories + [categories[0]],  # Close the loop
        fill='toself',
        name='Nutritional Breakdown',
        marker=dict(color='#9C0000')
    ))

    fig_radar.update_layout(
        title='Nutritional Breakdown Radar Chart',
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) + 10]  # Adjust based on your values
            )
        ),
        showlegend=True
    )

    st.plotly_chart(fig_radar)

    # Macronutrient data (Example)
    macronutrient_data = pd.DataFrame({
        'Food': list1,
        'Proteins': list3,
        'Carbs': list4,
        'Fats': list5,
        'Sugar': list7,
        'Calcium': list8
    })

    # Create the heatmap
    fig_heatmap = go.Figure(
        data=go.Heatmap(
            z=macronutrient_data[['Proteins', 'Carbs', 'Fats', 'Sugar', 'Calcium']].T,
            x=macronutrient_data['Food'],
            y=['Proteins', 'Carbs', 'Fats', 'Sugar', 'Calcium'],
            colorscale='Viridis'
        )
    )

    # Customize the layout
    fig_heatmap.update_layout(
        title="Macronutrient Concentration Heatmap",
        xaxis_title="Food Items",
        yaxis_title="Nutrient Types"
    )

    # Display the heatmap
    st.plotly_chart(fig_heatmap)
    # Pie charts for nutrient breakdown
    with col1:
        fig = go.Figure(data=[go.Pie(labels=list1, values=list2, textinfo='percent', insidetextorientation='radial')])
        fig.update_layout(title="Calorie Breakdown")
        st.plotly_chart(fig)
    
    with col2:
        fig1 = go.Figure(data=[go.Pie(labels=list1, values=list3, textinfo='percent', insidetextorientation='radial')])
        fig1.update_layout(title="Protein Breakdown")
        st.plotly_chart(fig1)
    
    with col3:
        fig2 = go.Figure(data=[go.Pie(labels=list1, values=list4, textinfo='percent', insidetextorientation='radial')])
        fig2.update_layout(title="Carbs Breakdown")
        st.plotly_chart(fig2)
    
    with col1:
        fig3 = go.Figure(data=[go.Pie(labels=list1, values=list5, textinfo='percent', insidetextorientation='radial')])
        fig3.update_layout(title="Fat Breakdown")
        st.plotly_chart(fig3)
    
    with col3:
        fig5 = go.Figure(data=[go.Pie(labels=list1, values=list7, textinfo='percent', insidetextorientation='radial')])
        fig5.update_layout(title="Sugar Breakdown")
        st.plotly_chart(fig5)

except Exception as e:
    st.write(f"An error occurred: {e}")
