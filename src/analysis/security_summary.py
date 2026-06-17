def generate_security_summary(findings):
    """
    Generate overall security statistics.
    """

    critical = 0
    high = 0
    medium = 0
    low = 0

    for finding in findings:

        if finding.severity == "Critical":
            critical += 1

        elif finding.severity == "High":
            high += 1

        elif finding.severity == "Medium":
            medium += 1

        elif finding.severity == "Low":
            low += 1

    overall_score = 100

    overall_score -= critical * 20
    overall_score -= high * 10
    overall_score -= medium * 5
    overall_score -= low * 2

    overall_score = max(overall_score, 0)

    return {
        "critical": critical,
        "high": high,
        "medium": medium,
        "low": low,
        "overall_score": overall_score
    }