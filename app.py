from dash import html
from datetime import datetime
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

from server import app, server

app.layout = html.Div(
    [
        fac.AntdTitle("网站测试", level=2),
        fac.AntdFormItem(
            fac.AntdDateRangePicker(
                id="date-range-picker", placement="topLeft", style={"width": 256}
            ),
            id="date-range-picker-container",
            hasFeedback=True,
            help="时间间隔不能超过31天",
        ),
        html.Div("请完成合法选值的选择", id="show-result"),
    ],
    style={"paddingTop": 350, "paddingLeft": 100},
)


@app.callback(
    [
        Output("date-range-picker-container", "validateStatus"),
        Output("date-range-picker-container", "help"),
    ],
    Input("date-range-picker", "value"),
    prevent_initial_call=True,
)
def validate_date_range(value):
    if value:
        start_datetime, end_datetime = (
            datetime.strptime(value[0], "%Y-%m-%d"),
            datetime.strptime(value[1], "%Y-%m-%d"),
        )

        # 计算范围间隔天数
        range_days = (end_datetime - start_datetime).days

        # 以超出31天为例
        if range_days > 31:
            return ["error", "所选日期范围超过31天限制，请重新选择"]

    return None, "时间间隔不能超过31天"


@app.callback(
    Output("show-result", "children"),
    Input("date-range-picker-container", "validateStatus"),
    State("date-range-picker", "value"),
    prevent_initial_call=True,
)
def update_result(validateStatus, value):
    if validateStatus != "error" and value:
        return f"合法的选值：{value}"

    return "请完成合法选值的选择"


if __name__ == "__main__":
    app.run_server(debug=True)
