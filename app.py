import streamlit as st
import pandas as pd


st.title('GWC - Global Wage Calculator')
df=pd.read_excel("v1-data.xlsx",sheet_name="Sheet3")
# st.write(df)
def main():
    selected_country = st.selectbox("Select Country",df["Country"].unique())
    selected_categories=st.multiselect("Select Category of Labour",df["Labour Type New"].unique())
    for category in selected_categories:
        num_people=st.number_input(f"Number of {category} units:",min_value=0,step=1,key=category)
        # st.write(f"{category} : {num_people} units")
    # st.write("Selected Categories and their Units")
    
    if not selected_categories:
        st.warning("Please select Labour Types to see the monthly costs.")
    else:
        data_list=[]
        grand_total=0
        for category in selected_categories:
            num_people=st.session_state.get(category,0)
            monthly_wage = df[(df['Country'] == selected_country) & (df['Labour Type New'] == category)]['Wage'].values[0]
            latest_year=df[(df['Country'] == selected_country) & (df['Labour Type New'] == category)]['Year'].values[0]
            # st.write(monthly_wage)
            monthly_cost = num_people * monthly_wage 
            grand_total += monthly_cost
            # st.write(f"{category}: {monthly_cost}")
            data_list.append({"Labour Type":category,"Year": latest_year,"Monthly Wage":monthly_wage,"Number of Units":num_people,"Montly Cost":monthly_cost})
        result_df=pd.DataFrame(data_list)
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        # st.write("Monthly Cost for Selected Labour Types")
        st.subheader('Monthly Cost for Selected Labour Types', divider='blue')
        st.write(result_df)
        grand_total=round(grand_total,2)
        st.metric(label="Grand Total", value=grand_total)
        # st.write(f"Grand Total: {grand_total}")


    
        
if __name__ == "__main__": 
    main()





