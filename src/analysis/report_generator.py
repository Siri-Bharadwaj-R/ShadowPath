from datetime import datetime

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

    # ==================================================
    # COVER PAGE
    # ==================================================

    content.append(Spacer(1, 150))

    content.append(
        Paragraph(
            "SHADOWPATH",
            styles["Title"]
        )
    )

    content.append(
        Paragraph(
            "Active Directory Attack Path Assessment Report",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            f"Generated: {datetime.now().strftime('%d %B %Y %H:%M')}",
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 20))

    content.append(
        Paragraph(
            """
            ShadowPath is an Active Directory attack path
            analysis platform designed to identify privilege
            escalation opportunities, evaluate security risk,
            and assist defenders in securing critical assets.
            """,
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            """
            The assessment identified attack paths that may
            enable privilege escalation toward highly
            privileged Active Directory groups. Findings
            were analyzed and assigned risk scores based
            on severity and potential impact.
            """,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    summary_data = [
        ["Metric", "Value"],
        [
            "Overall Security Score",
            f"{summary['overall_score']}/100"
        ],
        [
            "Critical Findings",
            str(summary["critical"])
        ],
        [
            "High Findings",
            str(summary["high"])
        ],
        [
            "Medium Findings",
            str(summary["medium"])
        ],
        [
            "Low Findings",
            str(summary["low"])
        ]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[250, 150]
    )

    summary_table.setStyle(
        TableStyle([
            ("BACKGROUND",
             (0, 0),
             (-1, 0),
             colors.darkblue),

            ("TEXTCOLOR",
             (0, 0),
             (-1, 0),
             colors.white),

            ("FONTNAME",
             (0, 0),
             (-1, 0),
             "Helvetica-Bold"),

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black),

            ("BACKGROUND",
             (0, 1),
             (-1, -1),
             colors.whitesmoke)
        ])
    )

    content.append(summary_table)

    content.append(Spacer(1, 25))

    # ==================================================
    # ATTACK GRAPH
    # ==================================================

    content.append(
        Paragraph(
            "Attack Graph",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            """
            The graph below visualizes privilege
            relationships and potential attack paths
            discovered during analysis.
            """,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 10))

    try:

        graph_image = Image(
            "attack_graph.png",
            width=450,
            height=320
        )

        content.append(graph_image)

    except Exception:

        content.append(
            Paragraph(
                "Attack graph image not found.",
                styles["BodyText"]
            )
        )

    content.append(PageBreak())

    # ==================================================
    # ATTACK FINDINGS
    # ==================================================

    content.append(
        Paragraph(
            "Attack Findings",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            """
            The following findings represent identified
            attack paths capable of leading to privileged
            access within the Active Directory environment.
            """,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 15))

    for index, finding in enumerate(findings, start=1):

        finding_id = f"SP-{index:03d}"

        if finding.severity == "Critical":
            severity_color = colors.red

        elif finding.severity == "High":
            severity_color = colors.orange

        elif finding.severity == "Medium":
            severity_color = colors.gold

        else:
            severity_color = colors.green

        finding_data = [
            ["Finding ID", finding_id],
            ["Attack Path",
             " → ".join(finding.path)],
            ["Risk Score",
             str(finding.score)],
            ["Severity",
             finding.severity]
        ]

        finding_table = Table(
            finding_data,
            colWidths=[120, 350]
        )

        finding_table.setStyle(
            TableStyle([

                ("GRID",
                 (0, 0),
                 (-1, -1),
                 1,
                 colors.black),

                ("BACKGROUND",
                 (0, 0),
                 (0, -1),
                 colors.lightgrey),

                ("FONTNAME",
                 (0, 0),
                 (0, -1),
                 "Helvetica-Bold"),

                ("BACKGROUND",
                 (1, 3),
                 (1, 3),
                 severity_color),

                ("TEXTCOLOR",
                 (1, 3),
                 (1, 3),
                 colors.white)
            ])
        )

        content.append(finding_table)
        content.append(Spacer(1, 15))

    # ==================================================
    # MITRE ATT&CK
    # ==================================================

    content.append(PageBreak())

    content.append(
        Paragraph(
            "MITRE ATT&CK Mapping",
            styles["Heading1"]
        )
    )

    mitre_data = [
        ["Technique ID", "Technique"],
        ["T1021", "Remote Services"],
        ["T1078", "Valid Accounts"],
        ["T1068", "Privilege Escalation"]
    ]

    mitre_table = Table(
        mitre_data,
        colWidths=[120, 300]
    )

    mitre_table.setStyle(
        TableStyle([
            ("BACKGROUND",
             (0, 0),
             (-1, 0),
             colors.darkblue),

            ("TEXTCOLOR",
             (0, 0),
             (-1, 0),
             colors.white),

            ("FONTNAME",
             (0, 0),
             (-1, 0),
             "Helvetica-Bold"),

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black)
        ])
    )

    content.append(mitre_table)

    content.append(Spacer(1, 20))

    # ==================================================
    # RECOMMENDATIONS
    # ==================================================

    content.append(
        Paragraph(
            "Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = [
        [
            "Critical",
            "Review Domain Admin membership and remove unnecessary accounts."
        ],
        [
            "High",
            "Implement least-privilege access controls."
        ],
        [
            "High",
            "Restrict administrative privileges."
        ],
        [
            "Medium",
            "Monitor privileged account activity."
        ],
        [
            "Medium",
            "Perform regular Active Directory security audits."
        ]
    ]

    recommendation_table = Table(
        [["Priority", "Recommendation"]] + recommendations,
        colWidths=[100, 350]
    )

    recommendation_table.setStyle(
        TableStyle([
            ("BACKGROUND",
             (0, 0),
             (-1, 0),
             colors.darkblue),

            ("TEXTCOLOR",
             (0, 0),
             (-1, 0),
             colors.white),

            ("FONTNAME",
             (0, 0),
             (-1, 0),
             "Helvetica-Bold"),

            ("GRID",
             (0, 0),
             (-1, -1),
             1,
             colors.black)
        ])
    )

    content.append(recommendation_table)

    content.append(Spacer(1, 25))

    # ==================================================
    # CONCLUSION
    # ==================================================

    content.append(
        Paragraph(
            "Conclusion",
            styles["Heading1"]
        )
    )

    content.append(
        Paragraph(
            """
            ShadowPath successfully identified attack paths
            capable of facilitating privilege escalation
            within the analyzed Active Directory
            environment. Critical and High severity
            findings should be prioritized to reduce
            organizational risk and strengthen the
            overall security posture.
            """,
            styles["BodyText"]
        )
    )

    document.build(content)

    print(
        "\nProfessional PDF report generated successfully."
    )

