import streamlit as st

st.set_page_config(page_title="Hello",
                   layout="centered",
                   initial_sidebar_state="collapsed")

st.header("Welcome on the carbon calculator")

st.markdown("### App Overview")

st.markdown("The objective of this application is to be able to easily estimate the carbon impact of an Home Energy Management System. Thanks to this application, it is possible to see the impact of devices installed directly at the customer's premises, but also the impact generated by the processing and storage of data.")

st.markdown("### Manual")

st.markdown("You are currently on the home page of the application, clicked on the navigation button at the top left to change pages and access the calculator.")

st.markdown("### Hypotheses")

st.markdown("The results of this carbon calculator are based on hypotheses that can be more or less strong and more or less obvious.")

st.markdown("Regarding the numerical hypotheses, they are all detailed in the 'hypothesis' tab of the application and can be modified if necessary.")

st.markdown("List of hidden hypotheses: ")

st.markdown("- BAT and HEMS data management systems work similarly. It is therefore possible to make an analogy between the two systems. ")

st.markdown("- The carbon impact of manufacturing a server is represented by the sum of the impacts of manufacturing the number of CPUs, the size of RAM memory and disk memory.")

st.markdown("- The complete calculation depends on the hardware provisioned for the BAT system. We do not count the provisioned hardware to anticipate the increase in load of the system because we assume that it is in a stationary regime.")

st.markdown("- All stored metrics are the same size and are characterized by a datapoint. This assumption minimizes the final result.")

st.markdown("- The “asset” metrics influence the sizing of Cassandra because they are reported and then stored, however they have less influence on the sizing of Kafka and AKS because they are used less subsequently. “Facet” metrics, unlike “asset” metrics, influence the sizing of the complete system because they are essential throughout the process.")

st.markdown("- The carbon footprint of a server is represented by the sum of its footprint during its manufacture and during its use. We calculate the manufacturing footprint and deduce the usage footprint by taking a percentage which depends on the energy mix of the country concerned.")
