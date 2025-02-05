import dash

import tab_classes_preparatoires.graph_map as graph_map
import tab_classes_preparatoires.graph_line as graph_line


class Tab_classes_preparatoires:
    def __init__(self, dash_app):
        # ---------------------------------------------------------------------------- #
        #                           TAB ARCHITECTURE SECTION                           #
        # ---------------------------------------------------------------------------- #

        self.app = dash_app

        self.layout = dash.html.Div(
            dash.html.Div(
                [
                    # ---------------------------------------------------------------------------- #
                    #                                  FIRST PART                                  #
                    # ---------------------------------------------------------------------------- #
                    dash.html.H2(
                        children="Géographie des classes préparatoires en {}".format(
                            graph_map.stats_lycees.year.min()
                        ),
                        id="classes_preparatoires_map_1_title",
                        style={"text-align": "left"},
                    ),
                    dash.html.Center(
                        dash.dcc.Loading(
                            type="default",
                            children=dash.html.Iframe(
                                id="classes_preparatoires_map_1",
                                width="50%",
                                height="500px",
                            ),
                        ),
                    ),
                    dash.dcc.Dropdown(
                        id="classes_preparatoires_dropdown_map_1",
                        options=[
                            {"label": str(year), "value": year}
                            for year in range(
                                graph_map.stats_lycees.year.min(),
                                graph_map.stats_lycees.year.max() + 1,
                            )
                        ],
                        multi=False,
                        value=graph_map.stats_lycees.year.min(),
                        style={"width": "40%"},
                    ),
                    dash.html.Br(),
                    dash.html.Div(
                        "Sur la carte ci-dessus, les Classes Préparatoires ayant pour la première fois cette année formé des élèves participant aux concours sont indiquées en rouge.",
                        style={
                            "background-color": "#FF6240",
                            "box-shadow": "3px 3px 3px grey",
                            "border": "1px solid red",
                        },
                    ),
                    dash.html.Br(),
                    dash.html.Div(
                        [
                            dash.html.Button(
                                "Afficher les commentaires",
                                id="classes_preparatoires_button_comment_1",
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
                                        "* On remarque que le nombre de Classes Préparatoires n'a cessé de croitre au cours des 18 dernières années."
                                    ),
                                    dash.dcc.Markdown(
                                        "* On peut noter que Paris profite d'une impressionnante densité de Classes Préparatoires tandis que les autres grandes villes n'en disposent que de peu."
                                    ),
                                    dash.dcc.Markdown(
                                        "* On identifie sans peine la *diagonale du vide*, zone géographique qui découpe la France du sud-ouest au nord-est et dont les Classes Préparatoires semblent singulièrement absentes."
                                    ),
                                ],
                                id="classes_preparatoires_collapse_comment_1",
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
                        children="Accès à la formation en fonction du lieu",
                        style={"text-align": "left"},
                    ),
                    dash.html.Div(
                        [
                            dash.html.Div(
                                dash.dcc.Loading(
                                    type="default",
                                    children=dash.dcc.Graph(
                                        id="classes_preparatoires_graph_1",
                                        figure={},
                                    ),
                                ),
                                style={"width": "49%", "display": "inline-block"},
                            ),
                            dash.html.Div(
                                dash.dcc.Loading(
                                    type="default",
                                    children=dash.dcc.Graph(
                                        id="classes_preparatoires_graph_2",
                                        figure={},
                                    ),
                                ),
                                style={"width": "49%", "display": "inline-block"},
                            ),
                        ]
                    ),
                    dash.html.Div(
                        [
                            dash.html.Button(
                                "Afficher les commentaires",
                                id="classes_preparatoires_button_comment_2",
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
                                        "* Paris se trouvant à environ 700km de sa plus lointaine frontière terrestre, la décroissance du nombre de Classes Préparatoires au km² que l'on observe à partir de cette distance de la capitale semble cohérente."
                                    ),
                                    dash.dcc.Markdown(
                                        "* On remarque que quelle que soit l'année, Paris profite du plus grand nombre de Classes Préparatoires au km², mais aussi du plus grand nombre d'élèves par établissement, ce qui peut nuire à la qualité de l'apprentissage."
                                    ),
                                    dash.dcc.Markdown(
                                        "* On note une décroissance générale du nombre d'élève par établissement à mesure que l'on s'éloigne de la capitale."
                                    ),
                                ],
                                id="classes_preparatoires_collapse_comment_2",
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
                        children="L'accès à la formation en fontion du sexe",
                        style={"text-align": "left"},
                    ),
                    dash.html.Center(
                        dash.html.Div(
                            dash.dcc.Loading(
                                type="default",
                                children=dash.dcc.Graph(
                                    id="classes_preparatoires_map_2", figure={}
                                ),
                            )
                        ),
                    ),
                    dash.html.Div(
                        "Sur la carte ci-dessus, la taille des points et leur impact sur la densité de coloration correspond à la proportion de filles inscrites par Classe Préparatoire. La couleur neutre (*blanc*) correspond a des Classes Préparatoires dont la proportion de filles inscrites est dans la moyenne.",
                        style={
                            "background-color": "#FF6240",
                            "box-shadow": "3px 3px 3px grey",
                            "border": "1px solid red",
                        },
                    ),
                    dash.html.Br(),
                    dash.html.Div(
                        [
                            dash.html.Button(
                                "Afficher les commentaires",
                                id="classes_preparatoires_button_comment_3",
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
                                        "* La couleur blanche correspondant à des Classes Préparatoires dont la proportion de filles inscrites est dans la moyenne, on peut constater que cette proportion n'a que modérément évolué au cours des 18 dernières années, passant d'environ **19% en 2004** à **23% en 2019**."
                                    ),
                                    dash.dcc.Markdown(
                                        "* Cette carte confirme également nos premières observations quant à la répartition des Classes Préparatoires sur le territoire : En réinitialisant le niveau de zoom, on observe une densité nettement supérieure au niveau de **Paris** tandis qu'on distingue à peine les plus grandes villes, **Marseille, Lyon, Nancy ou Lille.**"
                                    ),
                                ],
                                id="classes_preparatoires_collapse_comment_3",
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
                ]
            ),
        )

        # ---------------------------------------------------------------------------- #
        #                               CALLBACK SECTION                               #
        # ---------------------------------------------------------------------------- #

        @self.app.callback(
            [
                dash.Output(
                    component_id="classes_preparatoires_map_1",
                    component_property="srcDoc",
                ),
                dash.Output(
                    component_id="classes_preparatoires_map_1_title",
                    component_property="children",
                ),
            ],
            [
                dash.Input(
                    component_id="classes_preparatoires_dropdown_map_1",
                    component_property="value",
                )
            ],
        )
        def update_map(year):
            return graph_map.update_graph_map_1(year)

        @self.app.callback(
            [
                dash.Output(
                    component_id="classes_preparatoires_graph_1",
                    component_property="figure",
                ),
            ],
            [
                dash.Input(
                    component_id="classes_preparatoires_dropdown_map_1",
                    component_property="value",
                )
            ],
        )
        def update_graph_distance_to_paris(year):
            return graph_line.update_graph_distance_to_paris(year)

        @self.app.callback(
            [
                dash.Output(
                    component_id="classes_preparatoires_graph_2",
                    component_property="figure",
                ),
            ],
            [
                dash.Input(
                    component_id="classes_preparatoires_dropdown_map_1",
                    component_property="value",
                )
            ],
        )
        def update_graph_distance_to_paris_2(year):
            return graph_line.update_graph_student_distance_to_paris(year)

        @self.app.callback(
            [
                dash.Output(
                    component_id="classes_preparatoires_map_2",
                    component_property="figure",
                ),
            ],
            [
                dash.Input(
                    component_id="classes_preparatoires_dropdown_map_1",
                    component_property="value",
                )
            ],
        )
        def update_graph_distance_to_paris_2(year):
            return graph_map.update_graph_map_2(year)

        @self.app.callback(
            dash.Output("classes_preparatoires_collapse_comment_1", "style"),
            [dash.Input("classes_preparatoires_button_comment_1", "n_clicks")],
            [dash.State("classes_preparatoires_collapse_comment_1", "style")],
        )
        def show_comment_3(n, is_open):
            if n:
                if is_open["display"] == "none":
                    is_open["display"] = "block"
                else:
                    is_open["display"] = "none"
            return is_open

        @self.app.callback(
            dash.Output("classes_preparatoires_collapse_comment_2", "style"),
            [dash.Input("classes_preparatoires_button_comment_2", "n_clicks")],
            [dash.State("classes_preparatoires_collapse_comment_2", "style")],
        )
        def show_comment_3(n, is_open):
            if n:
                if is_open["display"] == "none":
                    is_open["display"] = "block"
                else:
                    is_open["display"] = "none"
            return is_open

        @self.app.callback(
            dash.Output("classes_preparatoires_collapse_comment_3", "style"),
            [dash.Input("classes_preparatoires_button_comment_3", "n_clicks")],
            [dash.State("classes_preparatoires_collapse_comment_3", "style")],
        )
        def show_comment_3(n, is_open):
            if n:
                if is_open["display"] == "none":
                    is_open["display"] = "block"
                else:
                    is_open["display"] = "none"
            return is_open
