import streamlit as st
import pandas as pd


st.title('GWC - Global Wage Calculator')
df=pd.read_excel("test-1.xlsx")
# st.write(df)
def main():
    selected_country = st.selectbox("Select Country",df["Country"].unique())
    selected_categories=st.multiselect("Select Category of Labour",df["Job Title"].unique())
    wage_type=st.selectbox("Select the Type of Wage",["Min","Max","Average"])
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
            wage_type_df=df[wage_type]
            wage = df[(df['Country'] == selected_country) & (df['Job Title'] == category) ][wage_type].values[0]
            # latest_year=df[(df['Country'] == selected_country) & (df['Labour Type New'] == category)]['Year'].values[0]
            # st.write(monthly_wage)
            annual_cost = num_people * wage 
            grand_total += annual_cost
            # st.write(f"{category}: {monthly_cost}")
            data_list.append({"Labour Type":category,"Year":2024,"Annual Wage":round(wage,0),"Number of Units":num_people,"Annual Cost":annual_cost})
        result_df=pd.DataFrame(data_list)
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        # st.write("Monthly Cost for Selected Labour Types")
        st.subheader('Monthly Cost for Selected Labour Types', divider='blue')
        st.write(result_df)
        grand_total=round(grand_total,0)
        st.metric(label="Grand Total", value=grand_total)
        # st.write(f"Grand Total: {grand_total}")


    
        
if __name__ == "__main__": 
    main()





