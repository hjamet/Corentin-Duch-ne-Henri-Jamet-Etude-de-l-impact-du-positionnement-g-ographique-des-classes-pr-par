import pandas as pd
import dash

import tab_grandes_ecoles.graph_map as graph_map
import tab_grandes_ecoles.graph_bar as graph_bar
import tab_grandes_ecoles.graph_pie as graph_pie


class Tab_grandes_ecoles:
    def __init__(self, dash_app):

        self.app = dash_app
        # ---------------------------------------------------------------------------- #
        #                               TAB ARCHITECTURE                               #
        # ---------------------------------------------------------------------------- #

        self.layout = (
            dash.html.Div(
                children=[
                    # ---------------------------------------------------------------------------- #
                    #                                  FIRST PART                                  #
                    # ---------------------------------------------------------------------------- #
                    dash.html.H2(
                        children="Géographie des Grandes Ecoles",
                        id="grandes_ecoles_map_1_title",
                        style={"text-align": "left"},
                    ),
                    dash.html.Center(
                        dash.dcc.Loading(
                            type="default",
                            children=dash.html.Iframe(
                                id="grandes_ecoles_map_1",
                                width="50%",
                                height="500px",
                                srcDoc=graph_map.display_graph_map_1(),
                            ),
                        )
                    ),
                    dash.html.Div(
                        [
                            dash.html.Button(
                                "Afficher les commentaires",
                                id="grandes_ecoles_button_comment_1",
                                style={
                                    "box-shadow": "0px 10px 14px -7px #3e7327",
                                    "background-color": "#77b55a",
                                    "border-radius": "4px",
                                    "border": "1px solid #4b8f29",
                                    "display": "inline-block",
                                    "color": "#ffffff",
                                    "font-family": "Arial",
                                    "font-size": "13px",
                                    "font-weight": "bold",
                                    "text-shadow": "0px 1px 0px #5b8a3c",
                                },
                            ),
                            dash.html.Div(
                                children=[
                                    dash.html.Br(),
                                    dash.dcc.Markdown(
                                        "* On remarque qu'à l'instar des Classes Préparatoires, les Grandes Ecoles sont majoritairement regroupées dans Paris et ses alentours. Cependant, leur localisation est davantage dispersée et on observe nombre d'entre elles dans d'autres pays, notamment la côte est des Etats-Unis."
                                    ),
                                ],
                                id="grandes_ecoles_collapse_comment_1",
                                style={
                                    "display": "none",
                                    "background-color": "#B6DDA6 ",
                                    "border": "1px solid #4b8f29",
                                    "border-radius": "4px",
                                },
                            ),
                            dash.html.Br(),
                        ],
                        className="d-grid gap-2 col-6 mx-auto",
                    ),
                    # ---------------------------------------------------------------------------- #
                    #                                  SECOND PART                                 #
                    # ---------------------------------------------------------------------------- #
                    dash.html.H2(
                        children="Offre et demande de l'éducation supérieure",
                        style={"text-align": "left"},
                    ),
                    dash.html.Div(
                        children=[
                            dash.html.Div(
                                dash.dcc.Loading(
                                    dash.dcc.Graph(
                                        id="grandes_ecoles_map_2",
                                        figure=graph_map.animate_graph_map_2(
                                            time_col="year"
                                        ),
                                    ),
                                ),
                                style={
                                    "width": "49%",
                                    "display": "inline-block",
                                },
                            ),
                            dash.html.Div(
                                dash.dcc.Loading(
                                    dash.dcc.Graph(
                                        id="grandes_ecoles_map_3",
                                        figure=graph_map.animate_graph_map_3(
                                            time_col="year"
                                        ),
                                    ),
                                ),
                                style={
                                    "width": "49%",
                                    "display": "inline-block",
                                },
                            ),
                        ]
                    ),
                    dash.html.Div(
                        dash.dcc.Loading(
                            type="default",
                            children=dash.dcc.Graph(
                                id="grandes_ecoles_graph_1",
                                figure=graph_bar.plot_inscrit_per_place(),
                            ),
                        )
                    ),
                    dash.html.Br(),
                    dash.html.Div(
                        [
                            dash.html.Button(
                                "Afficher les commentaires",
                                id="grandes_ecoles_button_comment_2",
                                style={
                                    "box-shadow": "0px 10px 14px -7px #3e7327",
                                    "background-color": "#77b55a",
                                    "border-radius": "4px",
                                    "border": "1px solid #4b8f29",
                                    "display": "inline-block",
                                    "color": "#ffffff",
                                    "font-family": "Arial",
                                    "font-size": "13px",
                                    "font-weight": "bold",
                                    "text-shadow": "0px 1px 0px #5b8a3c",
                                },
                            ),
                            dash.html.Div(
                                children=[
                                    dash.html.Br(),
                                    dash.dcc.Markdown(
                                        "* Les disparitions soudaines *(Notamment 2015-2016)* et les variations imprévisibles de la taille des points *(Notamment 2018-2019)* d'une année à l'autre sur les deux premiers graphes nous laisse supposer **des données collectées de manière non homogène**."
                                    ),
                                    dash.dcc.Markdown(
                                        "* Malgré la piètre qualité des données, on peut observer que le nombre d'étudiants inscrits a eu tendance à augmenter tandis que le nombre d'étudiants ayant intégré semble être resté stable, ce qui laisse deviner une croissance de la difficulté des concours au cours des 18 dernières années."
                                    ),
                                    dash.dcc.Markdown(
                                        "* Il est intéressant de constater que si une quantité considérable de Classes Préparatoires se trouve à Paris, les inscriptions aux concours semblent géographiquement mieux réparties d'après la première carte. On peut ainsi supposer que certains étudiants formés dans la capitale ont préféré passer les concours sur une autre partie du territoire, éventuellement pour augmenter leurs chances. Cette constatation pourra être prises en compte lors de l'analyse des résultats aux concours par département."
                                    ),
                                    dash.dcc.Markdown(
                                        "* On peut noter que ce quotient (***Nombre d'Inscriptions / Nombre de Places disponibles***) classe les Concours Communs Polytechniques en tête des concours les plus difficiles. Ce classement ne prend cependant pas en compte les intégrations excédentaires des écoles qui sont, après étude du jeu de donnée, monnaie courante."
                                    ),
                                    dash.dcc.Markdown(
                                        "* Un graphique similaire mettant en relation le rang du dernier integré et le nombre d'étudiants inscrits aurait également pu être intéressant mais le trop grand nombre de données manquantes nous l'a hélas rendu impossible."
                                    ),
                                ],
                                id="grandes_ecoles_collapse_comment_2",
                                style={
                                    "display": "none",
                                    "background-color": "#B6DDA6 ",
                                    "border": "1px solid #4b8f29",
                                    "border-radius": "4px",
                                },
                            ),
                            dash.html.Br(),
                        ],
                        className="d-grid gap-2 col-6 mx-auto",
                    ),
                    # ---------------------------------------------------------------------------- #
                    #                                  THIRD PART                                  #
                    # ---------------------------------------------------------------------------- #
                    dash.html.H2(
                        children="Résultats aux Concours en fonction du lieu d'apprentissage",
                        style={"text-align": "left"},
                    ),
                    dash.dcc.Dropdown(
                        id="grandes_ecoles_dropdown_pie_1",
                        options=[
                            {"label": str(concours), "value": concours}
                            for concours in pd.unique(
                                graph_pie.stats_lycees["concours"]
                            )
                        ],
                        multi=False,
                        value=graph_pie.stats_lycees["concours"].iloc[0],
                        style={"width": "40%"},
                    ),
                    dash.dcc.Loading(
                        type="default",
                        children=dash.dcc.Graph(
                            id="grandes_ecoles_graph_pie_1",
                            figure=graph_pie.update_pie(
                                graph_pie.stats_lycees["concours"].iloc[0],
                                min(graph_pie.stats_lycees["year"]),
                            )[0],
                        ),
                    ),
                    dash.html.Div(
                        "Aucune donnée n'est disponible pour ce coucours sur la période sélectionnée.",
                        id="grandes_ecoles_alert_pie_1",
                        style={
                            "background-color": "#FF6240",
                            "box-shadow": "3px 3px 3px grey",
                            "border": "1px solid red",
                            "display": "none",
                        },
                    ),
                    dash.html.Br(),
                    dash.dcc.Slider(
                        min(graph_pie.stats_lycees["year"]),
                        max(graph_pie.stats_lycees["year"]),
                        1,
                        marks={
                            i: str(i)
                            for i in range(
                                min(graph_pie.stats_lycees["year"]),
                                max(graph_pie.stats_lycees["year"]),
                            )
                        },
                        value=min(graph_pie.stats_lycees["year"]),
                        id="grandes_ecoles_slide_pie_1",
                    ),
                    dash.html.Br(),
                    dash.html.Div(
                        [
                            dash.html.Button(
                                "Afficher les commentaires",
                                id="grandes_ecoles_button_comment_3",
                                style={
                                    "box-shadow": "0px 10px 14px -7px #3e7327",
                                    "background-color": "#77b55a",
                                    "border-radius": "4px",
                                    "border": "1px solid #4b8f29",
                                    "display": "inline-block",
                                    "color": "#ffffff",
                                    "font-family": "Arial",
                                    "font-size": "13px",
                                    "font-weight": "bold",
                                    "text-shadow": "0px 1px 0px #5b8a3c",
                                },
                            ),
                            dash.html.Div(
                                children=[
                                    dash.html.Br(),
                                    dash.dcc.Markdown(
                                        "* La catégorie *Autres régions dont la proportion est inférieure à la moyenne* correspond à la somme des scores de ces autres régions et a vocation à éviter que les graphes ne soient surchargés"
                                    ),
                                ],
                                id="grandes_ecoles_collapse_comment_3",
                                style={
                                    "display": "none",
                                    "background-color": "#B6DDA6 ",
                                    "border": "1px solid #4b8f29",
                                    "border-radius": "4px",
                                },
                            ),
                            dash.html.Br(),
                        ],
                        className="d-grid gap-2 col-6 mx-auto",
                    ),
                ],
                title="Offre et demande de l'éducation supérieure",
            ),
        )

        # ---------------------------------------------------------------------------- #
        #                               CALLBACK SECTION                               #
        # ---------------------------------------------------------------------------- #

        @self.app.callback(
            dash.Output("grandes_ecoles_graph_pie_1", "figure"),
            dash.Output("grandes_ecoles_alert_pie_1", "style"),
            dash.Input("grandes_ecoles_dropdown_pie_1", "value"),
            dash.Input("grandes_ecoles_slide_pie_1", "value"),
        )
        def update_pie(concours, year):
            return graph_pie.update_pie(concours, year)

        @self.app.callback(
            dash.Output("grandes_ecoles_collapse_comment_1", "style"),
            [dash.Input("grandes_ecoles_button_comment_1", "n_clicks")],
            [dash.State("grandes_ecoles_collapse_comment_1", "style")],
        )
        def show_comment_3(n, is_open):
            if n:
                if is_open["display"] == "none":
                    is_open["display"] = "block"
                else:
                    is_open["display"] = "none"
            return is_open

        @self.app.callback(
            dash.Output("grandes_ecoles_collapse_comment_2", "style"),
            [dash.Input("grandes_ecoles_button_comment_2", "n_clicks")],
            [dash.State("grandes_ecoles_collapse_comment_2", "style")],
        )
        def show_comment_3(n, is_open):
            if n:
                if is_open["display"] == "none":
                    is_open["display"] = "block"
                else:
                    is_open["display"] = "none"
            return is_open

        @self.app.callback(
            dash.Output("grandes_ecoles_collapse_comment_3", "style"),
            [dash.Input("grandes_ecoles_button_comment_3", "n_clicks")],
            [dash.State("grandes_ecoles_collapse_comment_3", "style")],
        )
        def show_comment_3(n, is_open):
            if n:
                if is_open["display"] == "none":
                    is_open["display"] = "block"
                else:
                    is_open["display"] = "none"
            return is_open
