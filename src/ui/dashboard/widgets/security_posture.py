from rich.columns import Columns
from rich.console import Group

from ui.framework.metric_card import MetricCard
from ui.framework.progress_metric import ProgressMetric


def build_security_posture(data):

    summary = data.summary

    score = ProgressMetric(
        "Overall Security Score",
        summary["overall_score"],
    ).render()

    metrics = Columns(
        [

            MetricCard(
                "Critical",
                str(summary["critical"]),
                color="bright_red",
            ).render(),

            MetricCard(
                "High",
                str(summary["high"]),
                color="yellow",
            ).render(),

            MetricCard(
                "Medium",
                str(summary["medium"]),
                color="cyan",
            ).render(),

            MetricCard(
                "Low",
                str(summary["low"]),
                color="green",
            ).render(),

        ],
        equal=True,
        expand=True,
    )

    return Group(

        score,

        metrics

    )