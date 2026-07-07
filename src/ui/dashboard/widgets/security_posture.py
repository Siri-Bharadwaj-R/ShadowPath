from rich.columns import Columns
from rich.console import Group

from ...framework.metric_card import MetricCard
from ...framework.progress_metric import ProgressMetric


def build_security_posture(data):

    summary = data.summary

    score = ProgressMetric(
        "Overall Security Score",
        summary["overall_score"],
    ).render()

    total_findings = (
        summary["critical"]
        + summary["high"]
        + summary["medium"]
        + summary["low"]
    )

    # Determine overall posture
    if summary["critical"] > 0:
        posture = "CRITICAL"
        posture_color = "bright_red"

    elif summary["high"] > 0:
        posture = "HIGH"
        posture_color = "yellow"

    elif summary["medium"] > 0:
        posture = "MODERATE"
        posture_color = "cyan"

    else:
        posture = "LOW"
        posture_color = "green"

    top_metrics = Columns(
        [

            MetricCard(
                "Overall Risk",
                posture,
                color=posture_color,
            ).render(),

            MetricCard(
                "Total Findings",
                str(total_findings),
                color="bright_white",
            ).render(),

        ],
        equal=True,
        expand=True,
    )

    severity_metrics = Columns(
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

        top_metrics,

        severity_metrics,

    )