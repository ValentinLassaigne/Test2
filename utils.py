import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
pd.options.plotting.backend = "plotly"

class Environnement:
    def __init__(self,nb_client,facets,assets,periode_collecte):
        self.nb_client = nb_client
        self.facets = facets
        self.assets = assets
        self.periode_collecte = periode_collecte
        self.facets_par_min = facets * 60 / periode_collecte
        self.assets_par_min = assets * 60 / periode_collecte
        self.données_par_min = self.facets_par_min + self.assets_par_min     


class Application:
    def __init__(self,CPU,RAM,SSD ):
        self.CPU = CPU
        self.RAM = RAM
        self.SSD = SSD
        
        
intensite = Application(19.7,3.75,51)
 
class acv:
    def __init__(self,emissions,ddv,ddv_syst, site ):
        self.emissions = emissions
        self.ddv = ddv
        self.nb_ddv_syst = ddv_syst / ddv
        self.site = site
        self.emissions_ddv = emissions * self.nb_ddv_syst * site

def boite(c_texte, c_fond, phrase, res, unite, place):
    wch_colour_box = c_fond
    wch_colour_font = c_texte
    fontsize = 25
    valign = "left"
    iconname = "fas fa-asterisk"
    sline = phrase
    i = res

    htmlstr = f"""<p style='background-color: rgb({wch_colour_box[0]}, 
                                                {wch_colour_box[1]}, 
                                                {wch_colour_box[2]}, 0.75); 
                            color: rgb({wch_colour_font[0]}, 
                                    {wch_colour_font[1]}, 
                                    {wch_colour_font[2]}, 0.75); 
                            font-size: {fontsize}px; 
                            border-radius: 7px; 
                            padding-left: 12px; 
                            padding-top: 18px; 
                            padding-bottom: 18px; 
                            line-height:25px;'>
                            <i class='{iconname} fa-xs'></i> {i}{unite}    
                            </style><BR><span style='font-size: 14px;
                            margin-top: 0;'>{sline}</style></span></p>"""
    place.markdown( htmlstr, unsafe_allow_html=True)
    