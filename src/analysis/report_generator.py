from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(findings, summary):

    document = SimpleDocTemplate(
        "../reports/shadowpath_report.pdf"
    )

    styles = getSampleStyleSheet()

    content = []

    # =========================
    # TITLE
    # =========================

    title = Paragraph(
        "ShadowPath Security Assessment Report",
        styles["Title"]
    )

    content.append(title)
    content.append(Spacer(1, 20))

    # =========================
    # EXECUTIVE SUMMARY
    # =========================

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    summary_data = [
        ["Metric", "Value"],
        ["Overall Security Score",
         str(summary["overall_score"]) + "/100"],
        ["Critical Findings",
         str(summary["critical"])],
        ["High Findings",
         str(summary["high"])],
        ["Medium Findings",
         str(summary["medium"])],
        ["Low Findings",
         str(summary["low"])]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[220, 120]
    )

    summary_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0),
             colors.lightgrey),

            ("GRID", (0, 0), (-1, -1),
             1, colors.black),

            ("FONTNAME", (0, 0), (-1, 0),
             "Helvetica-Bold")
        ])
    )

    content.append(summary_table)

    content.append(Spacer(1, 20))

    # =========================
    # GRAPH IMAGE
    # =========================

    content.append(
        Paragraph(
            "Attack Graph",
            styles["Heading1"]
        )
    )

    try:

        graph_image = Image(
            "attack_graph.png",
            width=400,
            height=300
        )

        content.append(graph_image)

    except:
        content.append(
            Paragraph(
                "Attack graph image not found.",
                styles["BodyText"]
            )
        )

    content.append(Spacer(1, 20))

    # =========================
    # ATTACK FINDINGS
    # =========================

    content.append(
        Paragraph(
            "Attack Findings",
            styles["Heading1"]
        )
    )

    for finding in findings:

        if finding.severity == "Critical":
            severity_color = "red"

        elif finding.severity == "High":
            severity_color = "orange"

        else:
            severity_color = "green"

        content.append(
            Paragraph(
                "<b>Attack Path:</b><br/>"
                + " → ".join(finding.path),
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Risk Score:</b> "
                f"{finding.score}",
                styles["BodyText"]
            )
        )

        content.append(
            Paragraph(
                f"<b>Severity:</b> "
                f"<font color='{severity_color}'>"
                f"{finding.severity}"
                f"</font>",
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

    # =========================
    # MITRE SECTION
    # =========================

    content.append(
        PageBreak()
    )

    content.append(
        Paragraph(
            "MITRE ATT&CK Mapping",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            "Relevant ATT&CK techniques identified "
            "during attack-path analysis.",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "• T1021 - Remote Services",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "• T1078 - Valid Accounts",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "• T1068 - Privilege Escalation",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    # =========================
    # RECOMMENDATIONS
    # =========================

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = [
        "Review Domain Admin membership.",
        "Implement least privilege access.",
        "Monitor privileged accounts.",
        "Restrict unnecessary administrative rights.",
        "Perform regular Active Directory audits."
    ]

    for recommendation in recommendations:

        content.append(
            Paragraph(
                "• " + recommendation,
                styles["BodyText"]
            )
        )

    document.build(content)

    print(
        "\nProfessional PDF report generated successfully."
    )