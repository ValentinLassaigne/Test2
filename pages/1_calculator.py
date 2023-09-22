import streamlit as st
import pandas as pd
import plotly.express as px
from utils import *
pd.options.plotting.backend = "plotly"

st.set_page_config(page_title="Information System Calculator ",
                   layout="wide",
                   initial_sidebar_state="collapsed")

st.title('Carbon calculator')
 
# Tab creation
titres_onglets = ['Hypotheses', 'BAT IS', 'HEMS IS', 'SYSTEM']
onglet1, onglet2, onglet3, onglet4 = st.tabs(titres_onglets)
 
# Tab adding content
with onglet1:
    st.header("General hypotheses")

    cols = st.columns(6)

    with cols[1]:
        Duree_vie_systeme = st.number_input(
            "System lifetime [years]",
            step = 1, 
            value = 30,
            help = "System lifetime in years",
            )
    
    with cols[2]:
 
        pays_mix_elec = st.selectbox('Household location',
        (
            "France",
            "Europe",
            "Germany",
            "World",
            "Poland",
        )
        )

        st.markdown("[kg CO2 eq/Kwh]",
                    help="Electric mix carbon intensity in kg CO2 eq/Kwh",
                    )
        
        Intensite_mix_elec_pays ={
                "France" : 0.058,
                "Europe" : 0.238,
                "Germany" : 0.348,
                "World" : 0.436,
                "Poland" : 0.721,
            }

        Intensite_mix_elec = Intensite_mix_elec_pays[pays_mix_elec]

        #source : https://www.eea.europa.eu/data-and-maps/daviz/co2-emission-intensity-13/#tab-googlechartid_chart_11

        st.code(Intensite_mix_elec)


    st.markdown("## Information System ")

    cols = st.columns(6)
    with cols[1]:
        Duree_vie_serveur = st.number_input(
            "Server lifetime [years]",
            step = 1, 
            value = 4,
            help = "Server lifetime in years",
            )

    with cols[2]:
        st_data_p = st.number_input(
            "Datapoint storage use [bytes]",
            step = 1.0, 
            value = 8.5,
            help = "Datapoint storage use in bytes",
            )

    with cols[3]:
        replication = st.number_input(
            "Data replication number []",
            step = 1, 
            value = 5,
            help = "Data replication number",
            )

    with cols[4]:
        conservation_data = st.number_input(
            "Years of data storage [years]",
            step = 1, 
            value = 30,
            help = "Years of data storage we want to retain",
            )
        
    with cols[5]:
        facteur_asset_facet = st.number_input(
            "Asset impact vs Facet impact on kafka and aks []",
            step = 0.1, 
            value = 0.5,
            help = "Asset impact vs Facet impact on kafka and aks",
            )
    
    st.markdown("## Server manufacture ")

    cols = st.columns(6)
    

    with cols[1]:
        intensite_cpu = st.number_input(
            "CPU carbon intensity [kg CO2 eq/CPU]",
            step = 0.1, 
            value = 19.7,
            help = "CPU carbon intensity in kg CO2 eq/CPU",
            )
    
    with cols[2]:
        intensite_ram = st.number_input(
            "RAM carbon intensity [kg CO2 eq/Go RAM]",
            step = 0.01, 
            value = 3.75,
            help = "CPU carbon intensity in kg CO2 eq/Go RAM",
            )
    
    with cols[3]:
        intensite_ssd = st.number_input(
            "SSD carbon intensity [kg CO2 eq/To SSD]",
            step = 1, 
            value = 51,
            help = "CPU carbon intensity in kg CO2 eq/To SSD",
            )
    
    intensite = Application(intensite_cpu,intensite_ram,intensite_ssd)

    cols = st.columns(6)

    with cols[1]:

        server_power = st.number_input(
            "Average server power [W/CPU]",
            step = 1, 
            value = 75,
            help = "Average server power [W/CPU]",
            )
    
    with cols[2]:

        server_loc = st.selectbox('Datacenter location',
        (
            "France",
            "Europe",
            "Germany",
            "World",
            "Poland",
        )
        )

        st.markdown("[kg CO2 eq/Kwh]",
                    help="Electric mix carbon intensity in kg CO2 eq/Kwh",
                    )
        
        server_loc_pays = Intensite_mix_elec_pays[server_loc]


        st.code(server_loc_pays)

    st.markdown("## Home devices ")
    
    cols = st.columns(6)

    with cols[1]:
        Pv_emissions = st.number_input(
            "PV carbon footprint [kg CO2 eq/kW]",
            step = 1, 
            value = 1000,
            help = "PV carbon footprint during all his lifetime in kg CO2 eq/kW",
            )
        
    with cols[2]:
        Pv_ddv = st.number_input(
            "PV lifetime [years]",
            step = 1, 
            value = 30,
            help = "PV lifetime in years",
            )
        
    cols = st.columns(6)

    with cols[1]:
        Bat_emissions = st.number_input(
            "Battery carbon footprint [kg CO2 eq/kWh]",
            step = 1, 
            value = 175,
            help = "Battery carbon footprint during all his lifetime in kg CO2 eq/kWh",
            )
        
    with cols[2]:
        Bat_ddv = st.number_input(
            "Battery lifetime [cycles]",
            step = 1, 
            value = 6000,
            help = "Battery lifetime in cycle",
            )
         
    cols = st.columns(6)

    with cols[1]:
        Inv_emission = st.number_input(
            "Micro-inverter carbon footprint [kg CO2 eq/kW]",
            step = 1, 
            value = 200,
            help = "Micro-inverter carbon footprint during all his lifetime in kg CO2 eq/kW",
            )
        
    with cols[2]:
        Inv_ddv = st.number_input(
            "Micro-inverter lifetime [years]",
            step = 1, 
            value = 25,
            help = "Micro-inverter lifetime in years",
            )
    
    cols = st.columns(6)

    with cols[1]:
        Gw_emission = st.number_input(
            "Gateway carbon footprint [kg CO2 eq]",
            step = 1, 
            value = 17,
            help = "Gateway carbon footprint in kg CO2 eq",
            )
        
    with cols[2]:
        Gw_ddv = st.number_input(
            "Gateway lifetime [years]",
            step = 1, 
            value = 5,
            help = "Gateway lifetime in years",
            )
        
    with cols[3]:
        Gw_use = st.number_input(
            "Gateway power [W]",
            step = 1, 
            value = 5,
            help = "Gateway power in Watt",
            ) * 1e-3


with onglet2:
    st.header("BAT platform manufacturing carbon footprint ")
    st.markdown("## BAT datas")
    cols = st.columns(6)
    with cols[1]:
        nb_client = st.number_input(
            "Client number []",
            step = 1, 
            value = 27000,
            help = "Client number",
            )
        
    with cols[2]:
        facets = st.number_input(
            "Facets number []",
            step = 1, 
            value = 14,
            help = "Facets number",
            )

    with cols[3]:
        assets = st.number_input(
            "Assets number []",
            step = 1, 
            value = 0,
            help = "Assets number",
            )

    with cols[4]:
        collect = st.number_input(
            "Data collection period [second]",
            step = 1, 
            value = 120,
            help = "Data collection period in second",
            )
    
    cols = st.columns(5)

    st.markdown("## BAT server provision")

    cols = st.columns(5)

    with cols[1]:

        with st.expander("Cassandra"):
                
            CPU_C = st.number_input(
            "CPU number []",
            step = 1,
            value = 170,
            help = "Number of CPU provisioned for Cassandra",
            )
            RAM_C = st.number_input(
            "RAM storage [GB]",
            step = 1,
            value = 960,
            help = "RAM size provisioned for Cassandra in Gigabytes",
            )
            SSD_C = st.number_input(
            "SSD storage [TB]",
            step = 1,
            value = 66,
            help = "SSD size provisioned for Cassandra in Terabytes",
            )

    with cols[2]:

        with st.expander("Kafka"):
                
            CPU_K = st.number_input(
            "CPU Number []",
            step = 1,
            value = 15,
            help = "Number of CPU provisioned for Kafka",
            )
            RAM_K = st.number_input(
            "RAM storage [GB]",
            step = 1,
            value = 96,
            help = "RAM size provisioned for Kafka in Gigabytes",
            )
            SSD_K = st.number_input(
            "SSD storage [TB]",
            step = 1,
            value = 26,
            help = "SSD size provisioned for Kafka in Terabytes",
            )

    with cols[3]:

        with st.expander("Aks"):
                
            CPU_A = st.number_input(
            "CPU Number []",
            step = 1,
            value = 35,
            help = "Number of CPU provisioned for Aks",
            )
            RAM_A = st.number_input(
            "RAM storage [GB]",
            step = 1,
            value = 960,
            help = "RAM size provisioned for Aks in Gigabytes",
            )
            SSD_A = st.number_input(
            "SSD storage [TB]",
            step = 1,
            value = 2,
            help = "SSD size provisioned for Aks in Terabytes",
            )

    varta = {
        "data" : Environnement(nb_client,facets,assets,collect),
        "cassandra" : Application(CPU_C,RAM_C,SSD_C),
        "kafka" : Application(CPU_K,RAM_K,SSD_K),
        "aks" : Application(CPU_A,RAM_A,SSD_A)
    }
    ##Varta platform manufacturing carbon footprint
    #Calcul des emissions induites par le stockage long terme des données sur toute la durée du système (Hypothèse : impact sur la dimension du disque SSD)
    def Stock_annuel(Env):
        return (st_data_p * 365 * 24 * 60 * Env["data"].données_par_min * 1e-12) * intensite.SSD * replication *  Duree_vie_serveur * Env["data"].nb_client * sum(i  for i in range(0,int(conservation_data / Duree_vie_serveur)+1))

    #Création d'une dataframe pour la construction de l'impact carbone
    df=pd.DataFrame(
        {
            "Application" : pd.Categorical(["Cassandra", "Cassandra", "Cassandra", "Kafka", "Kafka", "Kafka", "Aks", "Aks", "Aks"]),
            "Infra" : pd.Categorical(["CPU", "RAM", "SSD", "CPU", "RAM", "SSD", "CPU", "RAM", "SSD"]),
            "Provision" : [varta["cassandra"].CPU, varta["cassandra"].RAM, varta["cassandra"].SSD, varta["kafka"].CPU, varta["kafka"].RAM, varta["kafka"].SSD, varta["aks"].CPU, varta["aks"].RAM, varta["aks"].SSD],
            "Intensite_par_infra" : [intensite.CPU, intensite.RAM, intensite.SSD, intensite.CPU, intensite.RAM, intensite.SSD, intensite.CPU, intensite.RAM, intensite.SSD]
        }
    )
    
    #Calcul de l'impact carbone de chaque partie d'un serveur sur sa durée de vie
    df=df.assign(Intensite_serv=df["Provision"]*df["Intensite_par_infra"])
    
    #Prise en compte de la durée de vie totale du système
    df=df.assign(Intensite_syst=df["Intensite_serv"] * Duree_vie_systeme  / Duree_vie_serveur)

    #Ajout des émissions du stockage annuel pour la partie SSD de Cassandra
    df.loc[(df["Application"]=="Cassandra") & (df["Infra"]=="SSD"), "Intensite_syst"] = df['Intensite_syst'] + Stock_annuel(varta)
    
    #Calcul de l'impact unitaire
    df=df.assign(Intensite_syst_unit=df["Intensite_syst"] / varta["data"].nb_client)
    df=round(df,2)

    #Graph
    fig = px.sunburst(df,
                    path=['Application', 'Infra'],
                    values='Intensite_syst_unit'

    )
    fig.update_traces(textinfo="label+percent entry+value")

    cols = st.columns(2)

    with cols[0]:
        st.markdown("## Data system carbon footprint sharing for BAT")
        st.plotly_chart(fig,use_container_width=True)

    df_use_manuf = pd.DataFrame(
    {
        'post' : pd.Index(['manufacture', 'use'])
    }
    )
    
    df_use_manuf["Varta"] = [df['Intensite_syst_unit'].sum(), df.loc[(df["Infra"]=="CPU"), 'Provision'].sum() * server_power * 1e-3 * 24 * 365  * server_loc_pays * Duree_vie_systeme / varta["data"].nb_client]
    df_use_manuf = round(df_use_manuf,2)
    
    fig2 = px.pie(df_use_manuf,values='Varta', names='post')
    fig2.update_traces(textposition='inside', textinfo='percent+label+value',marker=dict(line=dict(color='#000000', width=2)))
    

    with cols[1]:
        st.markdown("## Data system life cycle carbon footprint sharing for BAT")
        st.plotly_chart(fig2,use_container_width=True)

    cols = st.columns(2)

    with cols[0]:
        #Affichage d'indicateurs

        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"BAT IS life cycle carbon footprint", round(df_use_manuf["Varta"].sum() * varta["data"].nb_client * 1e-3,2), " tons CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"BAT IS manufacture carbon footprin", round(df['Intensite_syst'].sum() * 1e-3,2), " tons CO<sub>2 eq", col2)
        
        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"BAT IS life cycle carbon footprint per battery", df_use_manuf["Varta"].sum(), " kg CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"BAT IS manufacture carbon footprint per battery ", round(df["Intensite_syst_unit"].sum(),2), " kg CO<sub>2 eq", col2)


    with cols[1]:
        #Affichage d'indicateurs

        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"BAT IS use carbon footprint", round(df_use_manuf["Varta"][1] * varta["data"].nb_client * 1e-3,2), " tons CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"Additional storage each year per battery ", round(replication * st_data_p * 365 * 24 * 60 * varta["data"].données_par_min * 1e-6, 2), " MB per year", col2)
        
        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"BAT IS use carbon footprint per battery", df_use_manuf["Varta"][1]," kg CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"Metrics collection per battery", varta["data"].données_par_min," metrics/min",col2)
        



with onglet3:
    st.header("HEMS platform manufacturing carbon footprint")

    st.markdown("## HEMS datas")
    cols = st.columns(6)
    with cols[1]:
        nb_client = st.number_input(
            "HEMS client number []",
            step = 1, 
            value = 50,
            help = "HEMS client number",
            )
        
    with cols[2]:
        facets = st.number_input(
            "HEMS facet number []",
            step = 1, 
            value = 19,
            help = "HEMS facet number",
            )

    with cols[3]:
        assets = st.number_input(
            "HEMS asset number []",
            step = 1, 
            value = 59,
            help = "HEMS asset number",
            )

    with cols[4]:
        collect = st.number_input(
            "HEMS data collection period [second]",
            step = 1, 
            value = 15,
            help = "HEMS data collection period in second",
            )


    HEMS = {
        "data" : Environnement(nb_client,facets,assets,collect),
    }

    #Calcul des émissions de CO2 du matériel informatique rapporté à la métrique
    df=df.assign(infra_metrique=df["Provision"] / (varta["data"].données_par_min * varta["data"].nb_client ))

    ##Infra serveur HEMS

    #Le cas des facets (Hypothèse : une facet Varta = une facet HEMS)
    df=df.assign(Infra_HEMS = HEMS["data"].facets_par_min * HEMS["data"].nb_client * df["infra_metrique"])

    #Le cas des métriques "assets" (Hypothèse : une "asset" HEMS a un impact inférieur à une "facet" Varta )

    #asset = facet pour cassandra
    df.loc[df["Application"]=="Cassandra", "Infra_HEMS"] = df["Infra_HEMS"] + HEMS["data"].assets_par_min * HEMS["data"].nb_client * df["infra_metrique"]

    #asset <= facet pour le reste
    df.loc[df["Application"]!="Cassandra", "Infra_HEMS"] = df["Infra_HEMS"] + HEMS["data"].assets_par_min * facteur_asset_facet * HEMS["data"].nb_client * df["infra_metrique"]

    #Calcul des émissions par infrastructure HEMS
    df=df.assign(Intensite_HEMS_serv= df["Infra_HEMS"] * df["Intensite_par_infra"])

    
    #prise en compte de toute la durée de vie du système
    df=df.assign(Intensite_HEMS_syst=df["Intensite_HEMS_serv"] * Duree_vie_systeme  / Duree_vie_serveur)

    #Ajout des émissions induites par le stockage long terme
    df.loc[(df["Application"]=="Cassandra") & (df["Infra"]=="SSD"), "Intensite_HEMS_syst"] = df['Intensite_HEMS_syst'] + Stock_annuel(HEMS)

    #Impact individuel
    df=df.assign(Intensite_HEMS_syst_unit=df["Intensite_HEMS_syst"] / HEMS["data"].nb_client)
    df=round(df,2)

    st.markdown("## HEMS server provision per gateway")

    cols = st.columns(5)

    with cols[1]:
        st.markdown("CPU quantity []",
                    help="Number of CPU provision estimate for a HEMS gateway",
                    )
        st.code(round(df.loc[df["Infra"]=="CPU", "Infra_HEMS"].sum(),2))

    with cols[2]:
        st.markdown("RAM storage [GB]",
                    help="RAM size provision estimate for a HEMS gateway in Gigabyte",
                    )
        st.code(round(df.loc[df["Infra"]=="RAM", "Infra_HEMS"].sum(),2))

    with cols[3]:
        st.markdown("SSD storage [TB]",
                    help="SSD size provision estimate for a HEMS gateway in Terabyte",
                    )
        st.code(round(df.loc[df["Infra"]=="SSD", "Infra_HEMS"].sum(),2))

    #Graph
    fig = px.sunburst(df,
                    path=['Application', 'Infra'],
                    values='Intensite_HEMS_syst_unit'

    )
    fig.update_traces(textinfo="label+percent entry+value")


    cols = st.columns(2)

    with cols[0]:
        st.markdown("## Data system carbon footprint sharing for HEMS")
        st.plotly_chart(fig,use_container_width=True)

    Server_fab = acv(df['Intensite_HEMS_syst'].sum(),30,30,1) 
    Server_fab_unit = acv(df['Intensite_HEMS_syst_unit'].sum(),30,30,1) 
    Server_use = df.loc[(df["Infra"]=="CPU"), "Infra_HEMS"].sum() * (server_power * 1e-3) * 24 * 365 * Duree_vie_systeme * server_loc_pays
    Server_use_unit = df.loc[(df["Infra"]=="CPU"), "Infra_HEMS"].sum() * (server_power * 1e-3) * 24 * 365 * Duree_vie_systeme * server_loc_pays / HEMS["data"].nb_client

    df_use_manuf["HEMS"] = [Server_fab_unit.emissions_ddv, Server_use_unit]
    df_use_manuf = round(df_use_manuf,2)
    
    fig3 = px.pie(df_use_manuf,values='HEMS', names='post')
    fig3.update_traces(textposition='inside', textinfo='percent+label+value',marker=dict(line=dict(color='#000000', width=2)))

    with cols[1]:
        st.markdown("## Data system life cycle carbon footprint sharing for HEMS")
        st.plotly_chart(fig3,use_container_width=True)

    cols = st.columns(2)

    #Boite d'indicateurs
    with cols[0]:

        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"HEMS IS life cycle carbon footprint", round(df_use_manuf["HEMS"].sum() * 1e-3 * HEMS["data"].nb_client,2), " tons CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"HEMS IS manufacturing carbon footprint", round(df['Intensite_HEMS_syst'].sum() * 1e-3,2), " tons CO<sub>2 eq", col2)

        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"HEMS IS life cycle carbon footprint per gateway", round(df_use_manuf["HEMS"].sum(),2)," kg CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"HEMS IS manufacturing carbon footprint per gateway ", round(df["Intensite_HEMS_syst_unit"].sum(),2), " kg CO<sub>2 eq", col2)

    with cols[1]:
        #Affichage d'indicateurs
        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"HEMS IS use carbon footprint", round(df_use_manuf["HEMS"][1] * HEMS["data"].nb_client * 1e-3,2), " tons CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"Metrics collection per gateway", HEMS["data"].données_par_min," métrics/min",col2)
        
        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"HEMS IS use carbon footprint per gataway", df_use_manuf["HEMS"][1]," kg CO<sub>2 eq",col1)
        boite((0,0,0),(250,250,250),"Additional storage each year per gateway", round(st_data_p * 365 * 24 * 60 * HEMS["data"].données_par_min * 1e-9, 2), " GB per year", col2)

        

with onglet4:
    st.header('Home Energy Management System carbon footprint')
    
    st.markdown("## Home configuration")

    cols = st.columns(6)
    with cols[1]:
        Pv_site = st.number_input(
            "PV install power [kW]",
            step = 1, 
            value = 3,
            help = "Solar panel install power in kW",
            )
        
    with cols[2]:
        Bat_site = st.number_input(
            "Battery capacity [kWh]",
            step = 1, 
            value = 3,
            help = "Battery capacity in kWh",
            )


    with cols[1]:
        st.markdown("Number of heat pump []",
                    help="Number of heat pump",
                    )
        nb_hp=1
        st.code(nb_hp,language= 'markdown')
        #nb_hp= st.number_input(
        #    "Pompes à chaleur",
        #    step = 1, 
        #    value = 1,
        #    help = "Nombre de pompes à chaleur",
        #    )

    with cols[2]:
        st.markdown("Number of EVSE []",
                    help="Number of EVSE",
                    )
        nb_evse=1
        st.code(nb_evse,language= 'markdown')
        #nb_evse = st.number_input(
        #    "Borne de recharge de VE",
        #    step = 1, 
        #    value = 1,
        #    help = "Nombre de borne de recharge de véhicule électrique",
        #    )
        
    Pv = acv(Pv_emissions,Pv_ddv,Duree_vie_systeme,Pv_site)
    Bat= acv(Bat_emissions,Bat_ddv,Duree_vie_systeme * 365,Bat_site)
    Inverter_Pv =  acv(Inv_emission ,Inv_ddv,Duree_vie_systeme,Pv_site)
    Inverter_Bat =  acv(Inv_emission ,Inv_ddv,Duree_vie_systeme,Bat_site / 3)
    Gateway_fab = acv(Gw_emission,Gw_ddv,Duree_vie_systeme,1)
    Gateway_use = acv(Intensite_mix_elec,1,Duree_vie_systeme*365*24,Gw_use)
    
    st.markdown("## Life cycle assesment of HEMS")


    cols = st.columns(2)


    #Création d'un dataframe pour les émissions global de GES(Gaz à effet de serre)
    df_CO2 = pd.DataFrame(
        {
            'Device' : pd.Categorical(['Pv', 'Bat', 'Inverter', 'Inverter', 'Gateway', 'Gateway', 'Server', 'Server','Instal']),
            'Family_device' : pd.Categorical(['Pv','Bat','Pv','Bat','Gateway','Gateway','Server','Server','Instal']),
            'Post_emission' : pd.Categorical(['Fab','Fab','Fab','Fab','Fab','Use','Fab','Use','Instal'])
        }
        
    )
    #Emissions de chaque partie du système sur toute la durée du système
    df_CO2['Emissions'] = [Pv.emissions_ddv, Bat.emissions_ddv, Inverter_Pv.emissions_ddv, Inverter_Bat.emissions_ddv, Gateway_fab.emissions_ddv,Gateway_use.emissions_ddv,Server_fab_unit.emissions_ddv,Server_use_unit,0]
    #La partie installation est fixé ici à 10% des émissions de
    df_CO2.loc[(df_CO2["Device"]=="Instal") , "Emissions"] = df_CO2.loc[(df_CO2["Post_emission"]=="Fab") , "Emissions"].sum() * 0.1
    df_CO2=round(df_CO2,2)

    #Graph
    fig = px.sunburst(df_CO2, path=['Family_device', 'Device', 'Post_emission'], values='Emissions',  color='Family_device')
    fig.update_traces(textinfo="label+percent entry")

    cols = st.columns(2)

    data = df_CO2.loc[(df_CO2["Device"]=="Server") , "Emissions"].sum()
    data_part = data * 100 / df_CO2['Emissions'].sum()

    with cols[0]:
        st.plotly_chart(fig,use_container_width=True)



    with cols[1]:
 
        col1, col2= st.columns(2)
        boite((14,17,23),(14,17,23),"","","", col1)
        boite((14,17,23),(14,17,23),"","","", col2)

        col1, col2 = st.columns(2)
        boite((0,0,0),(250,250,250),"HEMS life cycle carbon footprint", round(df_CO2["Emissions"].sum() * 1e-3,2), " tons CO<sub>2 eq", col1)
        boite((0,0,0),(250,250,250),"HEMS life cycle IS carbon footprint", round(data * 1e-3,2), " tons CO<sub>2 eq", col2)

        boite((0,0,0),(250,250,250),"Carbon footprint share of IS", round(data_part, 2)," %",col1)
        boite((0,0,0),(250,250,250),"Carbon footprint share of non IS", round(100 - data_part,2)," %", col2)
        
        boite((0,0,0),(250,250,250),"Daily emissions to avoid", round(data/(Duree_vie_systeme * 365), 2)," kg CO<sub>2 eq </sub> /days",col1)
        boite((0,0,0),(250,250,250),"System life time", Duree_vie_systeme," years",col2)


