import dash
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from feffery_dash_utils.style_utils import style
from dash.dependencies import Input, Output, State, ClientsideFunction

from server import app, server

app.layout = fac.AntdCenter(
    [
        # 功德统计
        dcc.Store(id="gongde-data", data={"gongde": 0, "gold": 0}),
        fac.AntdSpace(
            [
                fac.AntdText(
                    "孙家琪已攒功德数：0",
                    id="gongde-count",
                    style=style(color="white", fontSize=36, fontFamily="KaiTi"),
                ),
                fac.AntdText(
                    "已出金次数：0",
                    id="gold-count",
                    style=style(color="#ffec3d", fontSize=36, fontFamily="KaiTi"),
                ),
            ],
            direction="vertical",
            align="center",
            size=0,
            style=style(
                position="fixed",
                top=100,
                left="50%",
                transform="translateX(-50%)",
            ),
        ),
        html.Div(
            [
                # 木鱼主体
                fuc.FefferyMotion(
                    html.Img(id="muyu-img", src="/assets/木鱼.svg", width="100%"),
                    whileTap={"scale": 1.2, "originX": "center", "originY": "center"},
                    initial={
                        "left": "50%",
                        "top": "50%",
                        "translateX": "-50%",
                        "translateY": "-50%",
                    },
                    style=style(
                        position="absolute",
                        width="100%",
                        cursor="url(/assets/木鱼锤鼠标指针.cur), pointer",
                        zIndex=2,
                        userSelect="none",
                    ),
                ),
                # 敲击响应动态文字
                fac.Fragment([], id="muyu-animate-texts"),
            ],
            style=style(
                position="relative",
                width="calc(max(15vw, 15vh))",
                height="calc(max(15vw, 15vh))",
            ),
        ),
        # 普通音频播放回调更新目标
        fac.Fragment(id="audio-target"),
        # “金色传说”音频播放回调更新目标
        fac.Fragment(id="gold-audio-target"),
    ],
    style=style(background="#000", height="100vh"),
)


app.clientside_callback(
    # 控制敲击木鱼触发的动效及数据更新
    ClientsideFunction(namespace="clientside", function_name="newEffect"),
    [
        Output("muyu-animate-texts", "children"),
        Output("audio-target", "children"),
        Output("gold-audio-target", "children"),
        Output("gongde-data", "data"),
    ],
    Input("muyu-img", "n_clicks"),
    [State("muyu-animate-texts", "children"), State("gongde-data", "data")],
    prevent_initial_call=True,
)


@app.callback(
    [
        Output("gongde-count", "children"),
        Output("gold-count", "children"),
    ],
    Input("gongde-data", "data"),
    prevent_initial_call=True,
)
def update_gongde_count(gongde_data):
    """控制功德统计"""
    return [
        "孙家琪已攒功德数：{}".format(gongde_data["gongde"]),
        "已出金次数：{}".format(gongde_data["gold"]),
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
